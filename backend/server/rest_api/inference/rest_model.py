"""REST API models for inference management package"""

from marshmallow import Schema
from marshmallow.fields import Str, DateTime, Boolean, Float, Integer, Nested


class InferenceInputSchema(Schema):
    """REST ressource for Inference input schema"""
    # BOX
    box_obssTime = Integer(required=True)
    box_rxTime = Integer(required=True)
    box_txTime = Integer(required=True)
    box_tx_Mbps = Float(required=True)
    box_rx_Mbps = Float(required=True)  
    box_rx_pps = Float(required=True)
    box_tx_pps = Float(required=True)
    # STATION
    signalStrength = Integer(required=True)
    downlinkMCS = Float(required=True)
    uplinkMCS = Float(required=True)
    uplinkShortGuard = Float(required=True)
    tx_Mbps = Float(required=True)
    rx_Mbps = Float(required=True)
    rx_pps = Float(required=True)
    tx_pps = Float(required=True)
    tx_err_pps = Float(required=True)

    
class InferenceResultsSchema(Schema):
    """REST ressource for Inference results schema"""

    status = Boolean(required=True)
    probability = Float(required=True)


class InferenceSchema(Schema):
    """REST ressource for Inference schema"""
    
    station = Str(required=True)
    input  = Nested(InferenceInputSchema, required=True)
    result = Nested(InferenceResultsSchema, required=True)
    timestamp = DateTime(required=True)  