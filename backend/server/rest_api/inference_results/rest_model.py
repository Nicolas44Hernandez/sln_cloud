"""REST API models for inference results management package"""

from marshmallow import Schema
from marshmallow.fields import Str, DateTime, Boolean, Float


class InferenceResultSchema(Schema):
    """REST ressource for Inference results schema"""
    
    station = Str(required=True)
    status = Boolean(required=True)
    probability = Float(required=True)  
    timestamp = DateTime(required=True)  

