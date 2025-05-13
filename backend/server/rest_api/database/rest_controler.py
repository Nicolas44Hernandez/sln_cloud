""" REST controller for database ressource """
import logging
import json
import io
import zipfile
from flask import send_file
from bson import ObjectId
from datetime import datetime
from flask.views import MethodView
from flask_smorest import Blueprint
from flask import current_app
from server.managers.mongo_db_manager import mongo_db_manager_service


logger = logging.getLogger(__name__)

bp = Blueprint("database", __name__, url_prefix="/api/database")
""" The api blueprint. Should be registered in app main api object """

def json_serializable(obj):
    """Convert ObjectId and datetime to string for JSON serialization."""
    if isinstance(obj, ObjectId):
        return str(obj)
    elif isinstance(obj, datetime):
        return f"ISODate('{obj.isoformat()}Z')"
    raise TypeError(f"Type {type(obj)} not serializable")


@bp.route("/reset")
class ResetDatabaseApi(MethodView):
    """API to reset database"""

    @bp.doc(security=[{"tokenAuth": []}], responses={201: "CREATED", 400: "BAD_REQUEST", 401: "UNAUTHORIZED"})
    @bp.response(status_code=201)
    def post(self):
        """delete database """

        logger.info(f"POST database/reset")

        mongo_db_manager_service.delete_database() 

        return 201


@bp.route("/export/<string:foldername>", methods=['GET'])
class ResetDatabaseApi(MethodView):
    """API to export database"""

    @bp.doc(security=[{"tokenAuth": []}], responses={201: "CREATED", 400: "BAD_REQUEST", 401: "UNAUTHORIZED"})
    @bp.response(status_code=201)
    def get(self, foldername):
        """delete database """

        logger.info(f"GET database/export/{foldername}")

        # Get collection names
        band_status_collection_name=current_app.config.get("MONGO_BAND_STATUS_COLLECTION_NAME")
        box_traffic_collection_name=current_app.config.get("MONGO_BOX_TRAFFIC_COLLECTION_NAME")
        stations_traffic_collection_name=current_app.config.get("MONGO_STATIONS_TRAFFIC_COLLECTION_NAME")
        box_counters_collection_name=current_app.config.get("MONGO_BOX_COUNTERS_COLLECTION_NAME")
        stations_counters_collection_name=current_app.config.get("MONGO_STATIONS_COUNTERS_COLLECTION_NAME")
        inferences_collection_name=current_app.config.get("MONGO_INFERENCES_COLLECTION_NAME")

        # Get data from database
        logger.info(f"Exporting data from database")               
        band_status_list = mongo_db_manager_service.get_band_status_list()
        box_traffic_list = mongo_db_manager_service.get_box_traffic_list()
        stations_traffic_list = mongo_db_manager_service.get_stations_traffic_list()
        box_counters_list = mongo_db_manager_service.get_box_counters_list()
        stations_counters_list = mongo_db_manager_service.get_stations_counters_list()
        inferences_list = mongo_db_manager_service.get_inferences_list()

        logger.info(f"Preparing data for export...")
        # Create a ZIP file in memory
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
            # Prepare each file and add it to the ZIP
            for collection_name, data in [
                (band_status_collection_name, band_status_list),
                (box_traffic_collection_name, box_traffic_list),
                (stations_traffic_collection_name, stations_traffic_list),
                (box_counters_collection_name, box_counters_list),
                (stations_counters_collection_name, stations_counters_list),
                (inferences_collection_name, inferences_list),
            ]:
                # Create a JSON file in memory
                json_data = json.dumps(data, default=json_serializable, indent=4)
                zip_file.writestr(f"{foldername}/{collection_name}.json", json_data)

        # Seek to the beginning of the BytesIO buffer
        zip_buffer.seek(0)

        logger.info(f"Database data successfully prepared for export")

        # Return the ZIP file as a downloadable response
        return send_file(zip_buffer, as_attachment=True, download_name=f"{foldername}.zip", mimetype='application/zip'), 200