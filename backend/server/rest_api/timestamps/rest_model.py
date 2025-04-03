"""REST API models for Timestamps management package"""

from marshmallow import Schema
from marshmallow.fields import List, DateTime


class DateTimeListSchema(Schema):
    timestamps = List(DateTime(required=True), required=True)

    

