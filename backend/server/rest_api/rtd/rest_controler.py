""" REST controller for RTD ressource """
import logging
from flask.views import MethodView
from flask_smorest import Blueprint
from server.managers.mongo_db_manager import mongo_db_manager_service
from .rest_model import RtdSchema


logger = logging.getLogger(__name__)

bp = Blueprint("rtd", __name__, url_prefix="/api-sln/rtd")
""" The api blueprint. Should be registered in app main api object """


@bp.route("/")
class InferenceResultsApi(MethodView):
    """API to retrieve inference results list"""

    @bp.doc(security=[{"tokenAuth": []}], responses={400: "BAD_REQUEST", 401: "UNAUTHORIZED"})
    @bp.response(status_code=200, schema=RtdSchema(many=True))
    def get(self):
        """Get rtd list"""

        logger.info(f"GET rtd/")

        rtd_list = mongo_db_manager_service.get_stations_rtd_list()
        return rtd_list
    


@bp.route("/<string:station>")
class InferenceResultsApi(MethodView):
    """API to retrieve the rtd list for a specific station"""

    @bp.doc(security=[{"tokenAuth": []}], responses={400: "BAD_REQUEST", 401: "UNAUTHORIZED"})
    @bp.response(status_code=200, schema=RtdSchema(many=True))
    def get(self, station):
        """Get single station rtd list"""

        logger.info(f"GET rtd/{station}")

        rtd_list = mongo_db_manager_service.get_rtd_list_for_station(station=station)
        return rtd_list
    