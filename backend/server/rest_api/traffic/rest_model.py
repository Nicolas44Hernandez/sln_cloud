"""REST API models for Band status management package"""

from marshmallow import Schema
from marshmallow.fields import Str, DateTime, Float


class BoxTrafficSchema(Schema):
    """REST ressource for BoxTraffic schema"""

    band = Str(required=True)
    rx_Mbps = Float(required=True)
    tx_Mbps = Float(required=True)
    timestamp = DateTime(required=True)

class StationTrafficSchema(Schema):
    """REST ressource for StationTraffic schema"""

    station = Str(required=True)
    rx_Mbps = Float(required=True)
    tx_Mbps = Float(required=True)
    timestamp = DateTime(required=True)

    

