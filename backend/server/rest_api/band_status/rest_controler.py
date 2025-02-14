""" REST controller for band status ressource """
import logging
from flask.views import MethodView
from flask_smorest import Blueprint
from server.managers.mongo_db_manager import mongo_db_manager_service
from .rest_model import BandStatusSchema


logger = logging.getLogger(__name__)

bp = Blueprint("band_status", __name__, url_prefix="/api-sln/band_status")
""" The api blueprint. Should be registered in app main api object """


@bp.route("/")
class BandStatusApi(MethodView):
    """API to retrieve band status list"""

    @bp.doc(security=[{"tokenAuth": []}], responses={400: "BAD_REQUEST", 401: "UNAUTHORIZED"})
    @bp.response(status_code=200, schema=BandStatusSchema(many=True))
    def get(self):
        """Get band status list"""

        logger.info(f"GET band_status/")

        band_status_list = mongo_db_manager_service.get_band_status_list()
        return band_status_list
    

    @bp.doc(security=[{"tokenAuth": []}], responses={201: "CREATED", 400: "BAD_REQUEST", 401: "UNAUTHORIZED"})
    @bp.response(status_code=201, schema=BandStatusSchema)
    @bp.arguments(BandStatusSchema) 
    def post(self, new_band_status):
        """receive band status sample """

        logger.info(f"POST band_status/ sample: {new_band_status}")

        created_band_status = mongo_db_manager_service.create_band_status_obj(new_band_status)

        return created_band_status, 201
