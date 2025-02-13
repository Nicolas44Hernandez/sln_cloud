"""REST API models for Clients management package"""

from marshmallow import Schema
from marshmallow.fields import Str, DateTime, Boolean


class BandStatusSchema(Schema):
    """REST ressource for Clients schema"""

    timestamp = DateTime(required=True)
    status = Boolean(required=True)

    

