"""REST API models for inference management package"""

from marshmallow import Schema
from marshmallow.fields import Str, DateTime, Float

class RtdSchema(Schema):
    """REST ressource for Rtd schema"""
    
    station = Str(required=True)
    rtd  = Float(required=True)
    timestamp = DateTime(required=True)  