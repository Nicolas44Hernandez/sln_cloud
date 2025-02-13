""" REST controller for clients ressource """
import logging
from flask.views import MethodView
from flask_smorest import Blueprint
from server.managers.band_status_manager import band_status_manager_service
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

        band_status_list = band_status_manager_service.get_band_status_list()
        return band_status_list
