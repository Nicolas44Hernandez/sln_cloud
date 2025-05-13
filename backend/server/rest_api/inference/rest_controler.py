""" REST controller for Inference results ressource """
import logging
from flask.views import MethodView
from flask_smorest import Blueprint
from server.managers.mongo_db_manager import mongo_db_manager_service
from .rest_model import InferenceSchema


logger = logging.getLogger(__name__)

bp = Blueprint("inferences", __name__, url_prefix="/api/inference")
""" The api blueprint. Should be registered in app main api object """


@bp.route("/")
class InferenceResultsApi(MethodView):
    """API to retrieve inference results list"""

    @bp.doc(security=[{"tokenAuth": []}], responses={400: "BAD_REQUEST", 401: "UNAUTHORIZED"})
    @bp.response(status_code=200, schema=InferenceSchema(many=True))
    def get(self):
        """Get inferneces list"""

        logger.info(f"GET inference/")

        inference_resuts_list = mongo_db_manager_service.get_inferences_list()
        return inference_resuts_list
    

    @bp.doc(security=[{"tokenAuth": []}], responses={201: "CREATED", 400: "BAD_REQUEST", 401: "UNAUTHORIZED"})
    @bp.response(status_code=201, schema=InferenceSchema(many=True))
    @bp.arguments(InferenceSchema(many=True)) 
    def post(self, new_inference):
        """receive inference results  sample """

        logger.info(f"POST inference/ sample: {new_inference}")

        created_inferences = []
        for inference in new_inference:
            created_inference = mongo_db_manager_service.create_inference_obj(inference)
            created_inferences.append(created_inference)

        return created_inferences, 201


@bp.route("/<string:station>")
class InferenceResultsApi(MethodView):
    """API to retrieve the inference list for a specific station"""

    @bp.doc(security=[{"tokenAuth": []}], responses={400: "BAD_REQUEST", 401: "UNAUTHORIZED"})
    @bp.response(status_code=200, schema=InferenceSchema(many=True))
    def get(self, station):
        """Get single station inference results list"""

        logger.info(f"GET inference/{station}")

        inference_list = mongo_db_manager_service.get_inferences_list_for_station(station=station)
        return inference_list
    