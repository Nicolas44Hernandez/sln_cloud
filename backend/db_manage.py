import os
from flask.cli import FlaskGroup
from datetime import datetime, timedelta
from server.app import create_app
from server.managers.mongo_db_manager import mongo_db_manager_service
from random import random

app = create_app()
cli = FlaskGroup(create_app=create_app)

DEVELOPMENT = os.getenv("DB_ENV") == "DEVELOPMENT"
if DEVELOPMENT:
    NB_OF_SAMPLES = 40
else:
    NB_OF_SAMPLES = 1
if DEVELOPMENT:
    TIMESTAMPS = [datetime.now() + timedelta(seconds=(i*5)) for i in range(NB_OF_SAMPLES)]
else:
    TIMESTAMPS = [datetime.now() + timedelta(hours=1, seconds=(i*1)) for i in range(NB_OF_SAMPLES)]

if DEVELOPMENT:
    BAND_STATUS_SAMPLES = [
        {"timestamp": TIMESTAMPS[n],"status": random() > 0.5}
        for n in range(NB_OF_SAMPLES)
    ]
else:
    BAND_STATUS_SAMPLES = [
        {"timestamp": TIMESTAMPS[n],"status": False}
        for n in range(NB_OF_SAMPLES)
    ]

if DEVELOPMENT:
    BOX_TRAFFIC_SAMPLES = [
        {
            "timestamp": TIMESTAMPS[int(n/2)],
            "band": "5GHz" if n%2 == 0 else "2.4GHz",
            "rx_Mbps": random()*10,
            "tx_Mbps": random()*10,
        }
        for n in range(NB_OF_SAMPLES*2)
    ]
else:
    BOX_TRAFFIC_SAMPLES = [
        {
            "timestamp": TIMESTAMPS[int(n/2)],
            "band": "5GHz" if n%2 == 0 else "2.4GHz",
            "rx_Mbps": 0,
            "tx_Mbps": 0,
        }
        for n in range(NB_OF_SAMPLES*2)
    ]

if DEVELOPMENT:
    STATIONS_TRAFFIC_SAMPLES = [
        {
            "timestamp": TIMESTAMPS[n],
            "station": "6E:F0:60:14:53:B9" if random() < 0.5 else "66:55:44:33:22:11",
            "rx_Mbps": random()*10,
            "tx_Mbps": random()*10,
        }
        for n in range(NB_OF_SAMPLES)
    ]
else:
    STATIONS_TRAFFIC_SAMPLES = [
        {
            "timestamp": TIMESTAMPS[n],
            "station": "6E:F0:60:14:53:B9",
            "rx_Mbps": 0,
            "tx_Mbps": 0,
        }
        for n in range(NB_OF_SAMPLES)
    ]

BOX_COUNTERS_SAMPLES = [
    {
        "band": "2.4GHz" if n%2 == 0 else "5GHz",
        "bytesReceived": 0,
        "bytesSent": 0,
        "noise": 0,
        "load": 0,
        "freeTime": 0,
        "rxTime": 0,
        "vendorStats_glitch": 0,
        "obssTime": 0,
        "txTime": 0,
        "intTime": 0,
        "noise_air": 0,
        "packetsReceived": 0,
        "packetsSent": 0,
        "errorsReceived": 0,
        "errorsSent": 0,
        "timestamp": TIMESTAMPS[n],
    }
    for n in range(NB_OF_SAMPLES)
]
if DEVELOPMENT:
    STATIONS_COUNTERS_SAMPLES = [
        {   
            "station": "AA:BB:CC:DD:EE:FF" if random() < 0.5 else "11:22:33:44:55:66",
            "txBytes": 10,
            "rxBytes": 10,
            "uplinkMCS": 10,
            "lastDataUplinkRate": 10,
            "lastDataDownlinkRate": 10,
            "signalStrength": 10,
            "avgSignalStrengthByChain": 10,
            "uplinkShortGuard": 10,
            "downlinkMCS": 10,
            "inactive": 10,
            "signalNoiseRatio": 10,
            "rxPacketCount": 10,
            "txPacketCount": 10,
            "txErrors": 10,
            "band": "2.4GHz" if random() < 0.5 else "5GHz",
            "timestamp": TIMESTAMPS[n],  
        }
        for n in range(NB_OF_SAMPLES)
    ]
else:
    STATIONS_COUNTERS_SAMPLES = [
        {   
            "station": "6E:F0:60:14:53:B9",
            "txBytes": 0,
            "rxBytes": 0,
            "uplinkMCS": 0,
            "lastDataUplinkRate": 0,
            "lastDataDownlinkRate": 0,
            "signalStrength": 0,
            "avgSignalStrengthByChain": 0,
            "uplinkShortGuard": 0,
            "downlinkMCS": 0,
            "inactive": 0,
            "signalNoiseRatio": 0,
            "rxPacketCount": 0,
            "txPacketCount": 0,
            "txErrors": 0,
            "band": "2.4GHz" if random() < 0.5 else "5GHz",
            "timestamp": TIMESTAMPS[n],  
        }
        for n in range(NB_OF_SAMPLES)
    ]

INFERENCE_INPUT_SAMPLES = [
    {
        "box_obssTime" : 5,
        "box_rxTime" : 5,
        "box_txTime" : 5,
        "box_tx_Mbps" : 5,
        "box_rx_Mbps" : 5,        
        "box_rx_pps" : 5,
        "box_tx_pps" : 5,
        "signalStrength" : 5,
        "downlinkMCS" : 5,
        "uplinkMCS" : 5,
        "uplinkShortGuard" : 5,        
        "tx_Mbps" : 5,
        "rx_Mbps" : 5,
        "rx_pps" : 5,
        "tx_pps" : 5,
        "tx_err_pps" : 5,
    }
    for counter in STATIONS_COUNTERS_SAMPLES
]

if DEVELOPMENT:
    INFERENCE_RESULTS_SAMPLES = [
    {
        "status": random() < 0.5,
        "probability": random(),
    }
    for counter in STATIONS_COUNTERS_SAMPLES
]
else:
    INFERENCE_RESULTS_SAMPLES = [
    {
        "status": False,
        "probability": 0,
    }
    for counter in STATIONS_COUNTERS_SAMPLES
]


if DEVELOPMENT:
    INFERENCES_SAMPLES = [
        {
            "station": "AA:BB:CC:DD:EE:FF" if random() < 0.5 else "11:22:33:44:55:66",
            "input": input,
            "result": result,
            "timestamp": TIMESTAMPS[n],
        }
        for n, (input, result) in enumerate(zip(INFERENCE_INPUT_SAMPLES, INFERENCE_RESULTS_SAMPLES))
    ]
else:
    INFERENCES_SAMPLES = [
        {
            "station": "6E:F0:60:14:53:B9",
            "input": input,
            "result": result,
            "timestamp": TIMESTAMPS[n],
        }
        for n, (input, result) in enumerate(zip(INFERENCE_INPUT_SAMPLES, INFERENCE_RESULTS_SAMPLES))
    ]


@cli.command('create')
def create_db():
    """Create database and collection if doesnt exists"""

    # Create database if needed and samples
    nb_samples = mongo_db_manager_service.create_database()

    band_status_samples_nb = nb_samples[mongo_db_manager_service.band_status_collection_name]
    box_traffic_samples_nb = nb_samples[mongo_db_manager_service.box_traffic_collection_name]
    stations_traffic_samples_nb = nb_samples[mongo_db_manager_service.stations_traffic_collection_name]
    box_counters_samples_nb = nb_samples[mongo_db_manager_service.box_counters_collection_name]
    stations_counters_samples_nb = nb_samples[mongo_db_manager_service.stations_counters_collection_name]
    inferences_samples_nb = nb_samples[mongo_db_manager_service.inferences_collection_name]

    if band_status_samples_nb != 0 or box_traffic_samples_nb  != 0 or stations_traffic_samples_nb  != 0 or box_counters_samples_nb  != 0 or stations_counters_samples_nb  != 0 or inferences_samples_nb  != 0:
        print("Database exists, run delete command before re create it")
        return   
     
    print("Database created")
    print("Seeding database")
    
    # Insert band status samples to DB
    mongo_db_manager_service.insert_band_status_samples(BAND_STATUS_SAMPLES)

    # Insert box traffic samples to DB
    mongo_db_manager_service.insert_box_traffic_samples(BOX_TRAFFIC_SAMPLES)

    # Insert stations traffic samples to DB
    mongo_db_manager_service.insert_stations_traffic_samples(STATIONS_TRAFFIC_SAMPLES)

    # Insert box counters samples to DB
    mongo_db_manager_service.insert_box_counters_samples(BOX_COUNTERS_SAMPLES)

    # Insert stations counters samples to DB
    mongo_db_manager_service.insert_stations_counters_samples(STATIONS_COUNTERS_SAMPLES)

    # Insert inference samples to DB
    mongo_db_manager_service.insert_inferences_samples(INFERENCES_SAMPLES)
    
    print("Database successfully created!")

@cli.command('delete')
def delete_db():
    """Delete database and collection if exists"""

    # Delete database and collection
    mongo_db_manager_service.delete_database()    
    print("Database successfully deleted!")


if __name__ == '__main__':
    cli()
