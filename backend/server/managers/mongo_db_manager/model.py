"""Model for mongo objects"""

from dataclasses import dataclass
from datetime import datetime

@dataclass
class BandStatus:
    status: str
    timestamp: datetime = None

    def __init__(self, status: bool, timestamp: datetime):
        self.status = status
        self.timestamp = timestamp

    def to_dict(self):
        """Convert the dataclass instance to a dictionary."""
        return {
            "status": self.status,
            "timestamp": self.timestamp
        }

@dataclass
class BoxTraffic:
    band: str
    tx_Mbps: float
    rx_Mbps: float
    timestamp: datetime = None

    def __init__(self, band: str, rx_Mbps: float, tx_Mbps: float, timestamp: datetime):
        self.band = band
        self.rx_Mbps = rx_Mbps
        self.tx_Mbps = tx_Mbps
        self.timestamp = timestamp

    def to_dict(self):
        """Convert the dataclass instance to a dictionary."""
        return {
            "band": self.band,
            "tx_Mbps": self.tx_Mbps,
            "rx_Mbps": self.rx_Mbps,
            "timestamp": self.timestamp
        }

@dataclass
class StationsTraffic:
    station: str
    tx_Mbps: float
    rx_Mbps: float
    timestamp: datetime = None

    def __init__(self, station: str, rx_Mbps: float, tx_Mbps: float, timestamp: datetime):
        self.station = station
        self.rx_Mbps = rx_Mbps
        self.tx_Mbps = tx_Mbps
        self.timestamp = timestamp

    def to_dict(self):
        """Convert the dataclass instance to a dictionary."""
        return {
            "station": self.station,
            "tx_Mbps": self.tx_Mbps,
            "rx_Mbps": self.rx_Mbps,
            "timestamp": self.timestamp
        }

@dataclass
class BoxCounters:   
    band: str
    bytesReceived: int
    bytesSent: int
    noise: int
    load: int
    freeTime: int
    rxTime: int
    vendorStats_glitch: int
    obssTime: int
    txTime: int
    intTime: int
    noise_air: int  
    packetsReceived: int
    packetsSent: int
    errorsReceived: int
    errorsSent: int
    timestamp: datetime

    def __init__(
        self, 
        band: str,
        bytesReceived: int,
        bytesSent: int,
        noise: int,
        load: int,
        freeTime: int,
        rxTime: int,
        vendorStats_glitch: int,
        obssTime: int,
        txTime: int,
        intTime: int,
        noise_air: int  ,
        packetsReceived: int,
        packetsSent: int,
        errorsReceived: int,
        errorsSent: int,
        timestamp: datetime,
    ):
        self.band = band
        self.bytesReceived = bytesReceived
        self.bytesSent = bytesSent
        self.noise = noise
        self.load = load
        self.freeTime = freeTime
        self.rxTime = rxTime
        self.vendorStats_glitch = vendorStats_glitch
        self.obssTime = obssTime
        self.txTime = txTime
        self.intTime = intTime
        self.noise_air = noise_air
        self.packetsReceived = packetsReceived
        self.packetsSent = packetsSent
        self.errorsReceived = errorsReceived
        self.errorsSent = errorsSent
        self.timestamp = timestamp

    def to_dict(self):
        """Convert the dataclass instance to a dictionary."""
        return {
            "band": self.band,
            "bytesReceived": self.bytesReceived,
            "bytesSent": self.bytesSent,
            "noise": self.noise,
            "load": self.load,
            "freeTime": self.freeTime,
            "rxTime": self.rxTime,
            "vendorStats_glitch": self.vendorStats_glitch,
            "obssTime": self.obssTime,
            "txTime": self.txTime,
            "intTime": self.intTime,
            "noise_air": self.noise_air,
            "packetsReceived": self.packetsReceived,
            "packetsSent": self.packetsSent,
            "errorsReceived": self.errorsReceived,
            "errorsSent": self.errorsSent,
            "timestamp": self.timestamp,
        }
    
@dataclass
class StationsCounters:  

    station: str
    txBytes: int
    rxBytes: int
    uplinkMCS: int
    lastDataUplinkRate: int
    lastDataDownlinkRate: int
    signalStrength: int
    avgSignalStrengthByChain: int
    uplinkShortGuard: int
    downlinkMCS: int
    inactive: int
    signalNoiseRatio: int
    rxPacketCount: int
    txPacketCount: int
    txErrors: int
    band: str
    timestamp: datetime
    
    def __init__(
        self, 
        station: str,        
        txBytes: int,
        rxBytes: int,
        uplinkMCS: int,
        lastDataUplinkRate: int,
        lastDataDownlinkRate: int,
        signalStrength: int,
        avgSignalStrengthByChain: int,
        uplinkShortGuard: int,
        downlinkMCS: int,
        inactive: int,
        signalNoiseRatio: int,
        rxPacketCount: int ,
        txPacketCount: int,
        txErrors: int,
        band: str,
        timestamp: datetime,
    ):
        self.station = station        
        self.txBytes = txBytes
        self.rxBytes = rxBytes
        self.uplinkMCS = uplinkMCS
        self.lastDataUplinkRate = lastDataUplinkRate
        self.lastDataDownlinkRate = lastDataDownlinkRate
        self.signalStrength = signalStrength
        self.avgSignalStrengthByChain = avgSignalStrengthByChain
        self.uplinkShortGuard = uplinkShortGuard
        self.downlinkMCS = downlinkMCS
        self.inactive = inactive
        self.signalNoiseRatio = signalNoiseRatio
        self.rxPacketCount = rxPacketCount
        self.txPacketCount = txPacketCount
        self.txErrors = txErrors
        self.band = band
        self.timestamp = timestamp

    def to_dict(self):
        """Convert the dataclass instance to a dictionary."""
        return {
            "station": self.station,
            "txBytes": self.txBytes,
            "rxBytes": self.rxBytes,
            "uplinkMCS": self.uplinkMCS,
            "lastDataUplinkRate": self.lastDataUplinkRate,
            "lastDataDownlinkRate": self.lastDataDownlinkRate,
            "signalStrength": self.signalStrength,
            "avgSignalStrengthByChain": self.avgSignalStrengthByChain,
            "uplinkShortGuard": self.uplinkShortGuard,
            "downlinkMCS": self.downlinkMCS,
            "inactive": self.inactive,
            "signalNoiseRatio": self.signalNoiseRatio,
            "rxPacketCount": self.rxPacketCount,
            "txPacketCount": self.txPacketCount,
            "txErrors": self.txErrors,
            "band": self.band,
            "timestamp": self.timestamp,
        }

@dataclass
class InferenceInput:
    # BOX
    box_obssTime: int
    box_rxTime: int
    box_txTime: int
    box_tx_Mbps: float
    box_tx_Mbps_lag1: float
    box_tx_Mbps_lag2: float
    box_tx_Mbps_lag3: float
    box_tx_Mbps_avg3: float
    box_tx_Mbps_avg5: float
    box_tx_Mbps_avg7: float
    box_rx_Mbps: float
    box_rx_Mbps_lag1: float
    box_rx_Mbps_lag2: float
    box_rx_Mbps_lag3: float
    box_rx_Mbps_avg3: float
    box_rx_Mbps_avg5: float
    box_rx_Mbps_avg7:float
    box_tx_err_pps: float
    box_tx_ber: float
    box_rx_pps: float
    box_tx_pps: float
    # STATION
    signalStrength: int
    signalStrength_lag1: int
    signalStrength_lag2: int
    signalStrength_lag3: int
    signalStrength_lag5: int
    signalStrength_lag7: int
    signalStrength_avg3: float
    signalStrength_avg5: float
    signalStrength_avg7: float
    signalStrength_avg10: float
    tx_Mbps: float
    tx_Mbps_lag1: float
    tx_Mbps_lag2: float
    tx_Mbps_lag3: float
    tx_Mbps_lag5: float
    tx_Mbps_lag7: float
    tx_Mbps_avg3: float
    tx_Mbps_avg5: float
    tx_Mbps_avg7: float
    tx_Mbps_avg10: float
    rx_Mbps: float
    rx_Mbps_lag1: float
    rx_Mbps_lag2: float
    rx_Mbps_lag3: float
    rx_Mbps_lag5: float
    rx_Mbps_lag7: float
    rx_Mbps_avg3: float
    rx_Mbps_avg5: float
    rx_Mbps_avg7: float
    rx_Mbps_avg10: float
    downlinkMCS: float
    inactive: float
    uplinkMCS: float
    uplinkShortGuard: float
    rx_pps: float
    tx_pps: float
    tx_err_pps: float
    tx_ber: float

    def __init__(
        self,
        box_obssTime: int,
        box_rxTime: int,
        box_txTime: int,
        box_tx_Mbps: float,
        box_tx_Mbps_lag1: float,
        box_tx_Mbps_lag2: float,
        box_tx_Mbps_lag3: float,
        box_tx_Mbps_avg3: float,
        box_tx_Mbps_avg5: float,
        box_tx_Mbps_avg7: float,
        box_rx_Mbps: float,
        box_rx_Mbps_lag1: float,
        box_rx_Mbps_lag2: float,
        box_rx_Mbps_lag3: float,
        box_rx_Mbps_avg3: float,
        box_rx_Mbps_avg5: float,
        box_rx_Mbps_avg7:float,
        box_tx_err_pps: float,
        box_tx_ber: float,
        box_rx_pps: float,
        box_tx_pps: float,
        signalStrength: int,
        signalStrength_lag1: int,
        signalStrength_lag2: int,
        signalStrength_lag3: int,
        signalStrength_lag5: int,
        signalStrength_lag7: int,
        signalStrength_avg3: float,
        signalStrength_avg5: float,
        signalStrength_avg7: float,
        signalStrength_avg10: float,
        tx_Mbps: float,
        tx_Mbps_lag1: float,
        tx_Mbps_lag2: float,
        tx_Mbps_lag3: float,
        tx_Mbps_lag5: float,
        tx_Mbps_lag7: float,
        tx_Mbps_avg3: float,
        tx_Mbps_avg5: float,
        tx_Mbps_avg7: float,
        tx_Mbps_avg10: float,
        rx_Mbps: float,
        rx_Mbps_lag1: float,
        rx_Mbps_lag2: float,
        rx_Mbps_lag3: float,
        rx_Mbps_lag5: float,
        rx_Mbps_lag7: float,
        rx_Mbps_avg3: float,
        rx_Mbps_avg5: float,
        rx_Mbps_avg7: float,
        rx_Mbps_avg10: float,
        downlinkMCS: float,
        inactive: float,
        uplinkMCS: float,
        uplinkShortGuard: float,
        rx_pps: float,
        tx_pps: float,
        tx_err_pps: float,
        tx_ber: float,
    ):
        self.box_obssTime = box_obssTime
        self.box_rxTime = box_rxTime
        self.box_txTime = box_txTime
        self.box_tx_Mbps = box_tx_Mbps
        self.box_tx_Mbps_lag1 = box_tx_Mbps_lag1
        self.box_tx_Mbps_lag2 = box_tx_Mbps_lag2
        self.box_tx_Mbps_lag3 = box_tx_Mbps_lag3
        self.box_tx_Mbps_avg3 = box_tx_Mbps_avg3
        self.box_tx_Mbps_avg5 = box_tx_Mbps_avg5
        self.box_tx_Mbps_avg7 = box_tx_Mbps_avg7
        self.box_rx_Mbps = box_rx_Mbps
        self.box_rx_Mbps_lag1 = box_rx_Mbps_lag1
        self.box_rx_Mbps_lag2 = box_rx_Mbps_lag2
        self.box_rx_Mbps_lag3 = box_rx_Mbps_lag3
        self.box_rx_Mbps_avg3 = box_rx_Mbps_avg3
        self.box_rx_Mbps_avg5 = box_rx_Mbps_avg5
        self.box_rx_Mbps_avg7 = box_rx_Mbps_avg7
        self.box_tx_err_pps = box_tx_err_pps
        self.box_tx_ber = box_tx_ber
        self.box_rx_pps = box_rx_pps
        self.box_tx_pps = box_tx_pps
        self.signalStrength = signalStrength
        self.signalStrength_lag1 = signalStrength_lag1
        self.signalStrength_lag2 = signalStrength_lag2
        self.signalStrength_lag3 = signalStrength_lag3
        self.signalStrength_lag5 = signalStrength_lag5
        self.signalStrength_lag7 = signalStrength_lag7
        self.signalStrength_avg3 = signalStrength_avg3
        self.signalStrength_avg5 = signalStrength_avg5
        self.signalStrength_avg7 = signalStrength_avg7
        self.signalStrength_avg10 = signalStrength_avg10
        self.tx_Mbps = tx_Mbps
        self.tx_Mbps_lag1 = tx_Mbps_lag1
        self.tx_Mbps_lag2 = tx_Mbps_lag2
        self.tx_Mbps_lag3 = tx_Mbps_lag3
        self.tx_Mbps_lag5 = tx_Mbps_lag5
        self.tx_Mbps_lag7 = tx_Mbps_lag7
        self.tx_Mbps_avg3 = tx_Mbps_avg3
        self.tx_Mbps_avg5 = tx_Mbps_avg5
        self.tx_Mbps_avg7 = tx_Mbps_avg7
        self.tx_Mbps_avg10 = tx_Mbps_avg10
        self.rx_Mbps = rx_Mbps
        self.rx_Mbps_lag1 = rx_Mbps_lag1
        self.rx_Mbps_lag2 = rx_Mbps_lag2
        self.rx_Mbps_lag3 = rx_Mbps_lag3
        self.rx_Mbps_lag5 = rx_Mbps_lag5
        self.rx_Mbps_lag7 = rx_Mbps_lag7
        self.rx_Mbps_avg3 = rx_Mbps_avg3
        self.rx_Mbps_avg5 = rx_Mbps_avg5
        self.rx_Mbps_avg7 = rx_Mbps_avg7
        self.rx_Mbps_avg10 = rx_Mbps_avg10
        self.downlinkMCS = downlinkMCS
        self.inactive = inactive
        self.uplinkMCS = uplinkMCS
        self.uplinkShortGuard = uplinkShortGuard
        self.rx_pps = rx_pps
        self.tx_pps = tx_pps
        self.tx_err_pps = tx_err_pps
        self.tx_ber = tx_ber

    def to_dict(self):
        """Convert the dataclass instance to a dictionary."""
        return {
            "box_obssTime" : self.box_obssTime,
            "box_rxTime" : self.box_rxTime,
            "box_txTime" : self.box_txTime,
            "box_tx_Mbps" : self.box_tx_Mbps,
            "box_tx_Mbps_lag1" : self.box_tx_Mbps_lag1,
            "box_tx_Mbps_lag2" : self.box_tx_Mbps_lag2,
            "box_tx_Mbps_lag3" : self.box_tx_Mbps_lag3,
            "box_tx_Mbps_avg3" : self.box_tx_Mbps_avg3,
            "box_tx_Mbps_avg5" : self.box_tx_Mbps_avg5,
            "box_tx_Mbps_avg7" : self.box_tx_Mbps_avg7,
            "box_rx_Mbps" : self.box_rx_Mbps,
            "box_rx_Mbps_lag1" : self.box_rx_Mbps_lag1,
            "box_rx_Mbps_lag2" : self.box_rx_Mbps_lag2,
            "box_rx_Mbps_lag3" : self.box_rx_Mbps_lag3,
            "box_rx_Mbps_avg3" : self.box_rx_Mbps_avg3,
            "box_rx_Mbps_avg5" : self.box_rx_Mbps_avg5,
            "box_rx_Mbps_avg7" : self.box_rx_Mbps_avg7,
            "box_tx_err_pps" : self.box_tx_err_pps,
            "box_tx_ber" : self.box_tx_ber,
            "box_rx_pps" : self.box_rx_pps,
            "box_tx_pps" : self.box_tx_pps,
            "signalStrength" : self.signalStrength,
            "signalStrength_lag1" : self.signalStrength_lag1,
            "signalStrength_lag2" : self.signalStrength_lag2,
            "signalStrength_lag3" : self.signalStrength_lag3,
            "signalStrength_lag5" : self.signalStrength_lag5,
            "signalStrength_lag7" : self.signalStrength_lag7,
            "signalStrength_avg3" : self.signalStrength_avg3,
            "signalStrength_avg5" : self.signalStrength_avg5,
            "signalStrength_avg7" : self.signalStrength_avg7,
            "signalStrength_avg10" : self.signalStrength_avg10,
            "tx_Mbps" : self.tx_Mbps,
            "tx_Mbps_lag1" : self.tx_Mbps_lag1,
            "tx_Mbps_lag2" : self.tx_Mbps_lag2,
            "tx_Mbps_lag3" : self.tx_Mbps_lag3,
            "tx_Mbps_lag5" : self.tx_Mbps_lag5,
            "tx_Mbps_lag7" : self.tx_Mbps_lag7,
            "tx_Mbps_avg3" : self.tx_Mbps_avg3,
            "tx_Mbps_avg5" : self.tx_Mbps_avg5,
            "tx_Mbps_avg7" : self.tx_Mbps_avg7,
            "tx_Mbps_avg10" : self.tx_Mbps_avg10,
            "rx_Mbps" : self.rx_Mbps,
            "rx_Mbps_lag1" : self.rx_Mbps_lag1,
            "rx_Mbps_lag2" : self.rx_Mbps_lag2,
            "rx_Mbps_lag3" : self.rx_Mbps_lag3,
            "rx_Mbps_lag5" : self.rx_Mbps_lag5,
            "rx_Mbps_lag7" : self.rx_Mbps_lag7,
            "rx_Mbps_avg3" : self.rx_Mbps_avg3,
            "rx_Mbps_avg5" : self.rx_Mbps_avg5,
            "rx_Mbps_avg7" : self.rx_Mbps_avg7,
            "rx_Mbps_avg10" : self.rx_Mbps_avg10,
            "downlinkMCS" : self.downlinkMCS,
            "inactive" : self.inactive,
            "uplinkMCS" : self.uplinkMCS,
            "uplinkShortGuard" : self.uplinkShortGuard,
            "rx_pps" : self.rx_pps,
            "tx_pps" : self.tx_pps,
            "tx_err_pps" : self.tx_err_pps,
            "tx_ber" : self.tx_ber,
        }

@dataclass
class InferenceResults:
    status: bool
    probability: float

    def __init__(self, status: bool, probability: float):
        self.status = status
        self.probability = probability

    def to_dict(self):
        """Convert the dataclass instance to a dictionary."""
        return {
            "status": self.status,
            "probability": self.probability,
        }

@dataclass
class Inferences:
    station: str
    input: InferenceInput
    result: InferenceResults
    timestamp: datetime = None

    def __init__(self, station: str, input: InferenceInput, result: InferenceResults, timestamp: datetime):
        self.station = station
        self.input = input
        self.result = result
        self.timestamp = timestamp

    def to_dict(self):
        """Convert the dataclass instance to a dictionary."""
        return {
            "station": self.station,
            "input": self.input.to_dict(),
            "result": self.result.to_dict(),
            "timestamp": self.timestamp
        }
