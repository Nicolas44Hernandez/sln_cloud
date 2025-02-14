"""Model for mongo objects"""

from dataclasses import dataclass
from datetime import datetime
from typing import Iterable

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
class InferenceResults:
    station: str
    status: bool
    probability: float
    timestamp: datetime = None

    def __init__(self, station: str, status: bool, probability: float, timestamp: datetime):
        self.station = station
        self.status = status
        self.probability = probability
        self.timestamp = timestamp

    def to_dict(self):
        """Convert the dataclass instance to a dictionary."""
        return {
            "station": self.station,
            "status": self.status,
            "probability": self.probability,
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
    rx_Mbps : float
    rx_Mbps_lag1 : float
    rx_Mbps_lag2 : float
    rx_Mbps_lag3 : float
    rx_Mbps_avg3 : float
    rx_Mbps_avg5 : float
    rx_Mbps_avg7 : float
    tx_Mbps : float
    tx_Mbps_lag1 : float
    tx_Mbps_lag2 : float
    tx_Mbps_lag3 : float
    tx_Mbps_avg3 : float
    tx_Mbps_avg5 : float
    tx_Mbps_avg7 : float
    noise: int
    noise_lag3: int
    noise_avg3: int
    noise_avg5: int
    noise_avg7: int
    rx_pps : float
    tx_pps : float
    load: int
    freeTime: int
    rxTime: int
    vendorStats_glitch: int
    obssTime: int
    txTime: int
    intTime: int
    noise_air: int
    tx_err_ps : float
    tx_ber : float
    timestamp : datetime

    def __init__(
            self, 
            rx_Mbps : float,
            rx_Mbps_lag1 : float,
            rx_Mbps_lag2 : float,
            rx_Mbps_lag3 : float,
            rx_Mbps_avg3 : float,
            rx_Mbps_avg5 : float,
            rx_Mbps_avg7 : float,
            tx_Mbps : float,
            tx_Mbps_lag1 : float,
            tx_Mbps_lag2 : float,
            tx_Mbps_lag3 : float,
            tx_Mbps_avg3 : float,
            tx_Mbps_avg5 : float,
            tx_Mbps_avg7 : float,
            noise: int,
            noise_lag3: int,
            noise_avg3: int,
            noise_avg5: int,
            noise_avg7: int,
            rx_pps : float,
            tx_pps : float,
            load: int,
            freeTime: int,
            rxTime: int,
            vendorStats_glitch: int,
            obssTime: int,
            txTime: int,
            intTime: int,
            noise_air: int,
            tx_err_ps : float,
            tx_ber : float,
            timestamp : datetime,
    ):
        self.rx_Mbps = rx_Mbps
        self.rx_Mbps_lag1 = rx_Mbps_lag1
        self.rx_Mbps_lag2 = rx_Mbps_lag2
        self.rx_Mbps_lag3 = rx_Mbps_lag3
        self.rx_Mbps_avg3 = rx_Mbps_avg3
        self.rx_Mbps_avg5 = rx_Mbps_avg5
        self.rx_Mbps_avg7 = rx_Mbps_avg7
        self.tx_Mbps = tx_Mbps
        self.tx_Mbps_lag1 = tx_Mbps_lag1
        self.tx_Mbps_lag2 = tx_Mbps_lag2
        self.tx_Mbps_lag3 = tx_Mbps_lag3
        self.tx_Mbps_avg3 = tx_Mbps_avg3
        self.tx_Mbps_avg5 = tx_Mbps_avg5
        self.tx_Mbps_avg7 = tx_Mbps_avg7
        self.noise = noise
        self.noise_lag3 = noise_lag3
        self.noise_avg3 = noise_avg3
        self.noise_avg5 = noise_avg5
        self.noise_avg7 = noise_avg7
        self.rx_pps = rx_pps
        self.tx_pps = tx_pps
        self.load = load
        self.freeTime = freeTime
        self.rxTime = rxTime
        self.vendorStats_glitch = vendorStats_glitch
        self.obssTime = obssTime
        self.txTime = txTime
        self.intTime = intTime
        self.noise_air = noise_air
        self.tx_err_ps = tx_err_ps
        self.tx_ber = tx_ber
        self.timestamp = timestamp

    def to_dict(self):
        """Convert the dataclass instance to a dictionary."""
        return {
            "rx_Mbps" : self.rx_Mbps,
            "rx_Mbps_lag1" : self.rx_Mbps_lag1,
            "rx_Mbps_lag2" : self.rx_Mbps_lag2,
            "rx_Mbps_lag3" : self.rx_Mbps_lag3,
            "rx_Mbps_avg3" : self.rx_Mbps_avg3,
            "rx_Mbps_avg5" : self.rx_Mbps_avg5,
            "rx_Mbps_avg7" : self.rx_Mbps_avg7,
            "tx_Mbps" : self.tx_Mbps,
            "tx_Mbps_lag1" : self.tx_Mbps_lag1,
            "tx_Mbps_lag2" : self.tx_Mbps_lag2,
            "tx_Mbps_lag3" : self.tx_Mbps_lag3,
            "tx_Mbps_avg3" : self.tx_Mbps_avg3,
            "tx_Mbps_avg5" : self.tx_Mbps_avg5,
            "tx_Mbps_avg7" : self.tx_Mbps_avg7,
            "noise" : self.noise,
            "noise_lag3" : self.noise_lag3,
            "noise_avg3" : self.noise_avg3,
            "noise_avg5" : self.noise_avg5,
            "noise_avg7" : self.noise_avg7,
            "rx_pps" : self.rx_pps,
            "tx_pps" : self.tx_pps,
            "load" : self.load,
            "freeTime" : self.freeTime,
            "rxTime" : self.rxTime,
            "vendorStats_glitch" : self.vendorStats_glitch,
            "obssTime" : self.obssTime,
            "txTime" : self.txTime,
            "intTime" : self.intTime,
            "noise_air" : self.noise_air,
            "tx_err_ps" : self.tx_err_ps,
            "tx_ber" : self.tx_ber,
            "timestamp" : self.timestamp, 
        }
    
@dataclass
class StationsCounters:
    station: str
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
    tx_Mbps: float
    tx_Mbps_lag1: float
    tx_Mbps_avg3: float
    tx_Mbps_avg5: float
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
    rx_pps: float
    tx_pps: float
    uplinkMCS: float
    lastDataUplinkRate: float
    lastDataDownlinkRate: float
    uplinkShortGuard: float
    downlinkMCS: float
    avgSignalStrengthByChain: float
    signalNoiseRatio: float
    timestamp: datetime = None

    def __init__(
        self, 
        station: str,
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
        tx_Mbps: float,
        tx_Mbps_lag1: float,
        tx_Mbps_avg3: float,
        tx_Mbps_avg5: float,
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
        rx_pps: float,
        tx_pps: float,
        uplinkMCS: float,
        lastDataUplinkRate: float,
        lastDataDownlinkRate: float,
        uplinkShortGuard: float,
        downlinkMCS: float,
        avgSignalStrengthByChain: float,
        signalNoiseRatio: float,
        timestamp: datetime,
        ):
        self.station = station
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
        self.tx_Mbps = tx_Mbps
        self.tx_Mbps_lag1 = tx_Mbps_lag1
        self.tx_Mbps_avg3 = tx_Mbps_avg3
        self.tx_Mbps_avg5 = tx_Mbps_avg5
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
        self.rx_pps = rx_pps
        self.tx_pps = tx_pps
        self.uplinkMCS = uplinkMCS
        self.lastDataUplinkRate = lastDataUplinkRate
        self.lastDataDownlinkRate = lastDataDownlinkRate
        self.uplinkShortGuard = uplinkShortGuard
        self.downlinkMCS = downlinkMCS
        self.avgSignalStrengthByChain = avgSignalStrengthByChain
        self.signalNoiseRatio = signalNoiseRatio
        self.timestamp = timestamp

    def to_dict(self):
        """Convert the dataclass instance to a dictionary."""
        return {

            "station" : self.station,
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
            "tx_Mbps" : self.tx_Mbps,
            "tx_Mbps_lag1" : self.tx_Mbps_lag1,
            "tx_Mbps_avg3" : self.tx_Mbps_avg3,
            "tx_Mbps_avg5" : self.tx_Mbps_avg5,
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
            "rx_pps" : self.rx_pps,
            "tx_pps" : self.tx_pps,
            "uplinkMCS" : self.uplinkMCS,
            "lastDataUplinkRate" : self.lastDataUplinkRate,
            "lastDataDownlinkRate" : self.lastDataDownlinkRate,
            "uplinkShortGuard" : self.uplinkShortGuard,
            "downlinkMCS" : self.downlinkMCS,
            "avgSignalStrengthByChain" : self.avgSignalStrengthByChain,
            "signalNoiseRatio" : self.signalNoiseRatio,
            "timestamp" : self.timestamp,
        }
  