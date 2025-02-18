"""REST API models for counters management package"""

from marshmallow import Schema
from marshmallow.fields import Str, DateTime, Float, List, Integer


class BoxCountersSchema(Schema):
    """REST ressource for BoxCounters schema"""
    
    rx_Mbps = Float(required=True)
    rx_Mbps_lag1 = Float(required=True)
    rx_Mbps_lag2 = Float(required=True)
    rx_Mbps_lag3 = Float(required=True)
    rx_Mbps_avg3 = Float(required=True)
    rx_Mbps_avg5 = Float(required=True)
    rx_Mbps_avg7 = Float(required=True)
    tx_Mbps = Float(required=True)
    tx_Mbps_lag1 = Float(required=True)
    tx_Mbps_lag2 = Float(required=True)
    tx_Mbps_lag3 = Float(required=True)
    tx_Mbps_avg3 = Float(required=True)
    tx_Mbps_avg5 = Float(required=True)
    tx_Mbps_avg7 = Float(required=True)
    noise = Integer(required=True)
    noise_lag3 = Integer(required=True)
    noise_avg3 = Integer(required=True)
    noise_avg5 = Integer(required=True)
    noise_avg7 = Integer(required=True)
    rx_pps = Float(required=True)
    tx_pps = Float(required=True)
    load = Integer(required=True)
    freeTime = Integer(required=True)
    rxTime = Integer(required=True)
    vendorStats_glitch = Integer(required=True)
    obssTime = Integer(required=True)
    txTime = Integer(required=True)
    intTime = Integer(required=True)
    noise_air = Integer(required=True)
    tx_err_ps = Float(required=True)
    tx_ber = Float(required=True)
    timestamp = DateTime(required=True)

  

class StationCountersSchema(Schema):
    """REST ressource for StationCounters schema"""

    station = Str(required=True)
    rx_Mbps = Float(required=True)
    rx_Mbps_lag1 = Float(required=True)
    rx_Mbps_lag2 = Float(required=True)
    rx_Mbps_lag3 = Float(required=True)
    rx_Mbps_lag5 = Float(required=True)
    rx_Mbps_lag7 = Float(required=True)
    rx_Mbps_avg3 = Float(required=True)
    rx_Mbps_avg5 = Float(required=True)
    rx_Mbps_avg7 = Float(required=True)
    rx_Mbps_avg10 = Float(required=True)
    tx_Mbps = Float(required=True)
    tx_Mbps_lag1 = Float(required=True)
    tx_Mbps_avg3 = Float(required=True)
    tx_Mbps_avg5 = Float(required=True)
    signalStrength = Integer(required=True)
    signalStrength_lag1 = Integer(required=True)
    signalStrength_lag2 = Integer(required=True)
    signalStrength_lag3 = Integer(required=True)
    signalStrength_lag5 = Integer(required=True)
    signalStrength_lag7 = Integer(required=True)
    signalStrength_avg3 = Integer(required=True)
    signalStrength_avg5 = Integer(required=True)
    signalStrength_avg7 = Integer(required=True)
    signalStrength_avg10 = Integer(required=True)
    rx_pps = Float(required=True)
    tx_pps = Float(required=True)
    uplinkMCS = Float(required=True)
    lastDataUplinkRate = Float(required=True)
    lastDataDownlinkRate = Float(required=True)
    uplinkShortGuard = Float(required=True)
    downlinkMCS = Float(required=True)
    avgSignalStrengthByChain = Float(required=True)
    signalNoiseRatio = Float(required=True)
    timestamp = DateTime(required=True)

