""" REST controller for Inference results ressource """
import logging
from flask.views import MethodView
from flask_smorest import Blueprint
from server.managers.mongo_db_manager import mongo_db_manager_service
from .rest_model import InferenceResultSchema


logger = logging.getLogger(__name__)

bp = Blueprint("inference_results", __name__, url_prefix="/api-sln/inference_results")
""" The api blueprint. Should be registered in app main api object """


@bp.route("/")
class InferenceResultsApi(MethodView):
    """API to retrieve inference results list"""

    @bp.doc(security=[{"tokenAuth": []}], responses={400: "BAD_REQUEST", 401: "UNAUTHORIZED"})
    @bp.response(status_code=200, schema=InferenceResultSchema(many=True))
    def get(self):
        """Get infernece results list"""

        logger.info(f"GET inference_results/")

        inference_resuts_list = mongo_db_manager_service.get_inference_results_list()
        return inference_resuts_list
    

    @bp.doc(security=[{"tokenAuth": []}], responses={201: "CREATED", 400: "BAD_REQUEST", 401: "UNAUTHORIZED"})
    @bp.response(status_code=201, schema=InferenceResultSchema(many=True))
    @bp.arguments(InferenceResultSchema(many=True)) 
    def post(self, new_inference_results):
        """receive inference results  sample """

        logger.info(f"POST inference_results/ sample: {new_inference_results}")

        created_inferences_resullts = []
        for inference_result in new_inference_results:
            created_inference_result = mongo_db_manager_service.create_inference_results_obj(inference_result)
            created_inferences_resullts.append(created_inference_result)

        return created_inferences_resullts, 201


@bp.route("/<string:mac>")
class InferenceResultsApi(MethodView):
    """API to retrieve the inference results list for a specific station"""

    @bp.doc(security=[{"tokenAuth": []}], responses={400: "BAD_REQUEST", 401: "UNAUTHORIZED"})
    @bp.response(status_code=200, schema=InferenceResultSchema(many=True))
    def get(self, mac):
        """Get single station inference results list"""

        logger.info(f"GET inference_results/{mac}")

        inference_results_list = mongo_db_manager_service.get_inference_results_list_for_station(station=mac)
        return inference_results_list
    