""" REST controller for timestamps ressource """
import logging
from flask.views import MethodView
from flask_smorest import Blueprint
from server.managers.mongo_db_manager import mongo_db_manager_service
from .rest_model import DateTimeListSchema


logger = logging.getLogger(__name__)

bp = Blueprint("timestamps", __name__, url_prefix="/api-sln/timestamps")
""" The api blueprint. Should be registered in app main api object """


@bp.route("/")
class TimestampsApi(MethodView):
    """API to retrieve timestamps list"""

    @bp.doc(security=[{"tokenAuth": []}], responses={400: "BAD_REQUEST", 401: "UNAUTHORIZED"})
    @bp.response(status_code=200, schema=DateTimeListSchema())
    def get(self):
        """Get timestamps list"""

        logger.info(f"GET timestamps/")

        timestamps_list = mongo_db_manager_service.get_timestamps_list()
        return {"timestamps" : timestamps_list}
    