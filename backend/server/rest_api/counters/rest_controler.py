""" REST controller for box and stations counters ressource """
import logging
from flask.views import MethodView
from flask_smorest import Blueprint
from server.managers.mongo_db_manager import mongo_db_manager_service
from .rest_model import BoxCountersSchema, StationCountersSchema


logger = logging.getLogger(__name__)

bp = Blueprint("counters", __name__, url_prefix="/api-sln/counters")
""" The api blueprint. Should be registered in app main api object """


@bp.route("/box")
class BoxCountesrApi(MethodView):
    """API to retrieve box counters list"""

    @bp.doc(security=[{"tokenAuth": []}], responses={400: "BAD_REQUEST", 401: "UNAUTHORIZED"})
    @bp.response(status_code=200, schema=BoxCountersSchema(many=True))
    def get(self):
        """Get box counters list"""

        logger.info(f"GET counters/box")

        box_counters_list = mongo_db_manager_service.get_box_counters_list()
        return box_counters_list
    

    @bp.doc(security=[{"tokenAuth": []}], responses={201: "CREATED", 400: "BAD_REQUEST", 401: "UNAUTHORIZED"})
    @bp.response(status_code=201, schema=BoxCountersSchema)
    @bp.arguments(BoxCountersSchema) 
    def post(self, new_box_counters):
        """receive box counters sample """

        logger.info(f"POST counters/box sample: {new_box_counters}")

        created_box_counters = mongo_db_manager_service.create_box_counters_obj(new_box_counters)

        return created_box_counters, 201


@bp.route("/stations")
class StationsCountersApi(MethodView):
    """API to retrieve stations counters list"""

    @bp.doc(security=[{"tokenAuth": []}], responses={400: "BAD_REQUEST", 401: "UNAUTHORIZED"})
    @bp.response(status_code=200, schema=StationCountersSchema(many=True))
    def get(self):
        """Get stations counters list"""

        logger.info(f"GET counters/stations")

        stations_counters_list = mongo_db_manager_service.get_stations_counters_list()
        return stations_counters_list


    @bp.doc(security=[{"tokenAuth": []}], responses={201: "CREATED", 400: "BAD_REQUEST", 401: "UNAUTHORIZED"})
    @bp.response(status_code=201, schema=StationCountersSchema(many=True))
    @bp.arguments(StationCountersSchema(many=True)) 
    def post(self, new_stations_counters):
        """receive station counters sample """

        logger.info(f"POST counters/stations sample: {new_stations_counters}")

        created_stations_counters = []
        for station_counters in new_stations_counters:
            created_station_counters = mongo_db_manager_service.create_stations_counters_obj(station_counters)
            created_stations_counters.append(created_station_counters)

        return created_stations_counters, 201

@bp.route("/stations/<string:mac>")
class SingleStationCountersApi(MethodView):
    """API to retrieve the counters list for a specific station"""

    @bp.doc(security=[{"tokenAuth": []}], responses={400: "BAD_REQUEST", 401: "UNAUTHORIZED"})
    @bp.response(status_code=200, schema=StationCountersSchema(many=True))
    def get(self, mac):
        """Get single station counters list"""

        logger.info(f"GET counters/stations/{mac}")

        station_counters_list = mongo_db_manager_service.get_counters_list_for_station(station=mac)
        return station_counters_list
    