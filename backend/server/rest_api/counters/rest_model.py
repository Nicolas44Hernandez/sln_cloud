"""REST API models for counters management package"""

from marshmallow import Schema
from marshmallow.fields import Str, DateTime, Float, List, Integer


class BoxCountersSchema(Schema):
    """REST ressource for BoxCounters schema"""

    band = Str(required=True)
    bytesReceived = Integer(required=True)
    bytesSent= Integer(required=True)
    noise = Integer(required=True)
    load = Integer(required=True)
    freeTime = Integer(required=True)
    rxTime = Integer(required=True)
    vendorStats_glitch = Integer(required=True)
    obssTime = Integer(required=True)
    txTime = Integer(required=True)
    intTime = Integer(required=True)
    noise_air = Integer(required=True)  
    packetsReceived = Integer(required=True)
    packetsSent = Integer(required=True)
    errorsReceived = Integer(required=True)
    errorsSent = Integer(required=True)
    timestamp = DateTime(required=True)
  

class StationCountersSchema(Schema):
    """REST ressource for StationCounters schema"""

    station = Str(required=True)
    band = Str(required=True)    
    txBytes = Integer(required=True)
    rxBytes = Integer(required=True)
    uplinkMCS = Integer(required=True)
    lastDataUplinkRate = Integer(required=True)
    lastDataDownlinkRate = Integer(required=True)
    signalStrength = Integer(required=True)
    avgSignalStrengthByChain = Integer(required=True)
    uplinkShortGuard = Integer(required=True)
    downlinkMCS = Integer(required=True)
    inactive = Integer(required=True)
    signalNoiseRatio = Integer(required=True)
    rxPacketCount = Integer(required=True) 
    txPacketCount = Integer(required=True)
    txErrors = Integer(required=True)
    timestamp = DateTime(required=True)

