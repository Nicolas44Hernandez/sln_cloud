""" REST controller for box traffic ressource """
import logging
from flask.views import MethodView
from flask_smorest import Blueprint
from server.managers.mongo_db_manager import mongo_db_manager_service
from .rest_model import BoxTrafficSchema, StationTrafficSchema


logger = logging.getLogger(__name__)

bp = Blueprint("traffic", __name__, url_prefix="/api-sln/traffic")
""" The api blueprint. Should be registered in app main api object """


@bp.route("/box")
class BoxTrafficApi(MethodView):
    """API to retrieve box traffic list"""

    @bp.doc(security=[{"tokenAuth": []}], responses={400: "BAD_REQUEST", 401: "UNAUTHORIZED"})
    @bp.response(status_code=200, schema=BoxTrafficSchema(many=True))
    def get(self):
        """Get box traffic list"""

        logger.info(f"GET traffic/box")

        box_traffic_list = mongo_db_manager_service.get_box_traffic_list()
        return box_traffic_list
    

    @bp.doc(security=[{"tokenAuth": []}], responses={201: "CREATED", 400: "BAD_REQUEST", 401: "UNAUTHORIZED"})
    @bp.response(status_code=201, schema=BoxTrafficSchema)
    @bp.arguments(BoxTrafficSchema) 
    def post(self, new_box_traffic):
        """receive box traffic sample """

        logger.info(f"POST traffic/box sample: {new_box_traffic}")

        created_box_traffic = mongo_db_manager_service.create_box_traffic_obj(new_box_traffic)

        return created_box_traffic, 201


@bp.route("/box/<string:band>")
class BandTrafficApi(MethodView):
    """API to retrieve specific band traffic list"""

    @bp.doc(security=[{"tokenAuth": []}], responses={400: "BAD_REQUEST", 401: "UNAUTHORIZED"})
    @bp.response(status_code=200, schema=BoxTrafficSchema(many=True))
    def get(self, band):
        """Get traffic list for a band"""

        logger.info(f"GET traffic/box/{band}")

        box_traffic_list = mongo_db_manager_service.get_traffic_list_for_band(band=band)
        return box_traffic_list


@bp.route("/stations")
class StationsTrafficApi(MethodView):
    """API to retrieve stations traffic list"""

    @bp.doc(security=[{"tokenAuth": []}], responses={400: "BAD_REQUEST", 401: "UNAUTHORIZED"})
    @bp.response(status_code=200, schema=StationTrafficSchema(many=True))
    def get(self):
        """Get stations traffic list"""

        logger.info(f"GET traffic/stations")

        stations_traffic_list = mongo_db_manager_service.get_stations_traffic_list()
        return stations_traffic_list


    @bp.doc(security=[{"tokenAuth": []}], responses={201: "CREATED", 400: "BAD_REQUEST", 401: "UNAUTHORIZED"})
    @bp.response(status_code=201, schema=StationTrafficSchema)
    @bp.arguments(StationTrafficSchema(many=True)) 
    def post(self, stations_traffic_sample):
        """receive station traffic sample """

        logger.info(f"POST traffic/stations sample: {stations_traffic_sample}")

        created_stations_traffic = []
        for station_traffic in stations_traffic_sample:
            created_station_traffic = mongo_db_manager_service.create_stations_traffic_obj(station_traffic)
            created_stations_traffic.append(created_station_traffic)

        return created_stations_traffic, 201

@bp.route("/stations/<string:mac>")
class SingleStationTrafficApi(MethodView):
    """API to retrieve the traffic list for a specific station"""

    @bp.doc(security=[{"tokenAuth": []}], responses={400: "BAD_REQUEST", 401: "UNAUTHORIZED"})
    @bp.response(status_code=200, schema=StationTrafficSchema(many=True))
    def get(self, mac):
        """Get station traffic list"""

        logger.info(f"GET traffic/stations/{mac}")

        stations_traffic_list = mongo_db_manager_service.get_traffic_list_for_station(station=mac)
        return stations_traffic_list
    