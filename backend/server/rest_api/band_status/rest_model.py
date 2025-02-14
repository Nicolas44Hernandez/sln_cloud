"""REST API models for Band status management package"""

from marshmallow import Schema
from marshmallow.fields import Str, DateTime, Boolean


class BandStatusSchema(Schema):
    """REST ressource for BandStatus schema"""

    timestamp = DateTime(required=True)
    status = Boolean(required=True)

    

