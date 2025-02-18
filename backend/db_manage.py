from flask.cli import FlaskGroup
from datetime import datetime, timedelta
from server.app import create_app
from server.managers.mongo_db_manager import mongo_db_manager_service

app = create_app()
cli = FlaskGroup(create_app=create_app)

BAND_STATUS_SAMPLES = [
    {
        "timestamp": datetime.now(),
        "status": True,
    },
    {
        "timestamp": datetime.now() - timedelta(seconds=5),
        "status": True,
    },
    {
        "timestamp": datetime.now() - timedelta(seconds=10),
        "status": True,
    },
    {
        "timestamp": datetime.now() - timedelta(seconds=15),
        "status": True,
    },
    {
        "timestamp": datetime.now() - timedelta(seconds=20),
        "status": True,
    },
    {
        "timestamp": datetime.now() - timedelta(seconds=25),
        "status": True,
    },

]

BOX_TRAFFIC_SAMPLES = [
    {
        "band": "5GHz",
        "rx_Mbps": 1,
        "tx_Mbps": 1,
        "timestamp": datetime.now(),
        
    },
    {
        "band": "2.4GHz",
        "rx_Mbps": 1,
        "tx_Mbps": 1,
        "timestamp": datetime.now(),
        
    },
    {
        "band": "5GHz",
        "rx_Mbps": 2,
        "tx_Mbps": 2,
        "timestamp": datetime.now(),
        
    },
    {
        "band": "2.4GHz",
        "rx_Mbps": 2,
        "tx_Mbps": 2,
        "timestamp": datetime.now(),
        
    },
    {
        "band": "5GHz",
        "rx_Mbps": 3,
        "tx_Mbps": 3,
        "timestamp": datetime.now(),
        
    },
    {
        "band": "2.4GHz",
        "rx_Mbps": 3,
        "tx_Mbps": 3,
        "timestamp": datetime.now(),
        
    },
    {
        "band": "5GHz",
        "rx_Mbps": 4,
        "tx_Mbps": 4,
        "timestamp": datetime.now(),
        
    },
    {
        "band": "2.4GHz",
        "rx_Mbps": 4,
        "tx_Mbps": 4,
        "timestamp": datetime.now(),
        
    },
    {
        "band": "5GHz",
        "rx_Mbps": 5,
        "tx_Mbps": 5,
        "timestamp": datetime.now(),
        
    },
    {
        "band": "2.4GHz",
        "rx_Mbps": 5,
        "tx_Mbps": 5,
        "timestamp": datetime.now(),
        
    },
]

STATIONS_TRAFFIC_SAMPLES = [
    {
        "station": "AA:BB:CC:DD:EE:FF",
        "rx_Mbps": 1,
        "tx_Mbps": 1,
        "timestamp": datetime.now(),
        
    },
    {
        "station": "11:22:33:44:55:66",
        "rx_Mbps": 1,
        "tx_Mbps": 1,
        "timestamp": datetime.now(),
        
    },
    {
        "station": "AA:BB:CC:DD:EE:FF",
        "rx_Mbps": 2,
        "tx_Mbps": 2,
        "timestamp": datetime.now(),
        
    },
    {
        "station": "11:22:33:44:55:66",
        "rx_Mbps": 2,
        "tx_Mbps": 2,
        "timestamp": datetime.now(),
        
    },
    {
        "station": "AA:BB:CC:DD:EE:FF",
        "rx_Mbps": 3,
        "tx_Mbps": 3,
        "timestamp": datetime.now(),
        
    },
    {
        "station": "11:22:33:44:55:66",
        "rx_Mbps": 3,
        "tx_Mbps": 3,
        "timestamp": datetime.now(),
        
    },
]

BOX_COUNTERS_SAMPLES = [
    {   
        "rx_Mbps": 1,
        "rx_Mbps_lag1": 1,
        "rx_Mbps_lag2": 1,
        "rx_Mbps_lag3": 1,
        "rx_Mbps_avg3" : 1,
        "rx_Mbps_avg5" : 1,
        "rx_Mbps_avg7" : 1,
        "tx_Mbps" : 1,
        "tx_Mbps_lag1" : 1,
        "tx_Mbps_lag2" : 1,
        "tx_Mbps_lag3" : 1,
        "tx_Mbps_avg3" : 1,
        "tx_Mbps_avg5" : 1,
        "tx_Mbps_avg7" : 1,
        "noise" : -90,
        "noise_lag3" : -90,
        "noise_avg3" : -90,
        "noise_avg5" : -90,
        "noise_avg7" : -90,
        "rx_pps": 15.6,
        "tx_pps": 16.8,
        "load": 10,
        "freeTime": 20,
        "rxTime": 30,
        "vendorStats_glitch": 40,
        "obssTime": 50,
        "txTime": 10,
        "intTime": 10,
        "noise_air": -20,
        "tx_err_ps": 1.56,
        "tx_ber": 12.66,
        "timestamp" : datetime.now(),          
    },
    {   
        "rx_Mbps": 2,
        "rx_Mbps_lag1": 2,
        "rx_Mbps_lag2": 2,
        "rx_Mbps_lag3": 2,
        "rx_Mbps_avg3" : 2,
        "rx_Mbps_avg5" : 2,
        "rx_Mbps_avg7" : 2,
        "tx_Mbps" : 2,
        "tx_Mbps_lag1" : 2,
        "tx_Mbps_lag2" : 2,
        "tx_Mbps_lag3" : 2,
        "tx_Mbps_avg3" : 2,
        "tx_Mbps_avg5" : 2,
        "tx_Mbps_avg7" : 2,
        "noise" : -80,
        "noise_lag3" : -80,
        "noise_avg3" : -80,
        "noise_avg5" : -80,
        "noise_avg7" : -80,
        "rx_pps": 15.6,
        "tx_pps": 16.8,
        "load": 10,
        "freeTime": 20,
        "rxTime": 30,
        "vendorStats_glitch": 40,
        "obssTime": 50,
        "txTime": 10,
        "intTime": 10,
        "noise_air": -20,
        "tx_err_ps": 1.56,
        "tx_ber": 12.66,
        "timestamp" : datetime.now(),          
    },    
]

STATIONS_COUNTERS_SAMPLES = [
    {
        "station": "AA:BB:CC:DD:EE:FF",
        "rx_Mbps" : 1,
        "rx_Mbps_lag1" : 1,
        "rx_Mbps_lag2" : 1,
        "rx_Mbps_lag3" : 1,
        "rx_Mbps_lag5" : 1,
        "rx_Mbps_lag7" : 1,
        "rx_Mbps_avg3" : 1,
        "rx_Mbps_avg5" : 1,
        "rx_Mbps_avg7" : 1,
        "rx_Mbps_avg10" : 1,
        "tx_Mbps" : 1,
        "tx_Mbps_lag1" : 1,
        "tx_Mbps_avg3" : 1,
        "tx_Mbps_avg5" : 1,
        "signalStrength" : 10,
        "signalStrength_lag1" : 10,
        "signalStrength_lag2" : 10,
        "signalStrength_lag3" : 10,
        "signalStrength_lag5" : 10,
        "signalStrength_lag7" : 10,
        "signalStrength_avg3" : 10,
        "signalStrength_avg5" : 10,
        "signalStrength_avg7" : 10,
        "signalStrength_avg10" : 10,
        "rx_pps" : 1.5,
        "tx_pps" : 1.5,
        "uplinkMCS" : 1,
        "lastDataUplinkRate" : 1,
        "lastDataDownlinkRate" : 1,
        "uplinkShortGuard" : 1,
        "downlinkMCS" : 1,
        "avgSignalStrengthByChain" : 1,
        "signalNoiseRatio" : 1,
        "timestamp": datetime.now(),  
    },
    {
        "station": "AA:BB:CC:DD:EE:FF",
        "rx_Mbps" : 2,
        "rx_Mbps_lag1" : 2,
        "rx_Mbps_lag2" : 2,
        "rx_Mbps_lag3" : 2,
        "rx_Mbps_lag5" : 2,
        "rx_Mbps_lag7" : 2,
        "rx_Mbps_avg3" : 2,
        "rx_Mbps_avg5" : 2,
        "rx_Mbps_avg7" : 2,
        "rx_Mbps_avg10" : 2,
        "tx_Mbps" : 2,
        "tx_Mbps_lag1" : 2,
        "tx_Mbps_avg3" : 2,
        "tx_Mbps_avg5" : 2,
        "signalStrength" : 20,
        "signalStrength_lag1" : 20,
        "signalStrength_lag2" : 20,
        "signalStrength_lag3" : 20,
        "signalStrength_lag5" : 20,
        "signalStrength_lag7" : 20,
        "signalStrength_avg3" : 20,
        "signalStrength_avg5" : 20,
        "signalStrength_avg7" : 20,
        "signalStrength_avg10" : 20,
        "rx_pps" : 2.5,
        "tx_pps" : 2.5,
        "uplinkMCS" : 2,
        "lastDataUplinkRate" : 2,
        "lastDataDownlinkRate" : 2,
        "uplinkShortGuard" : 2,
        "downlinkMCS" : 2,
        "avgSignalStrengthByChain" : 2,
        "signalNoiseRatio" : 2,
        "timestamp": datetime.now(),  
    },
    {
        "station": "11:22:33:44:55:66",
        "rx_Mbps" : 3,
        "rx_Mbps_lag1" : 3,
        "rx_Mbps_lag2" : 3,
        "rx_Mbps_lag3" : 3,
        "rx_Mbps_lag5" : 3,
        "rx_Mbps_lag7" : 3,
        "rx_Mbps_avg3" : 3,
        "rx_Mbps_avg5" : 3,
        "rx_Mbps_avg7" : 3,
        "rx_Mbps_avg10" : 3,
        "tx_Mbps" : 3,
        "tx_Mbps_lag1" : 3,
        "tx_Mbps_avg3" : 3,
        "tx_Mbps_avg5" : 3,
        "signalStrength" : 30,
        "signalStrength_lag1" : 30,
        "signalStrength_lag2" : 30,
        "signalStrength_lag3" : 30,
        "signalStrength_lag5" : 30,
        "signalStrength_lag7" : 30,
        "signalStrength_avg3" : 30,
        "signalStrength_avg5" : 30,
        "signalStrength_avg7" : 30,
        "signalStrength_avg10" : 30,
        "rx_pps" : 3.5,
        "tx_pps" : 3.5,
        "uplinkMCS" : 3,
        "lastDataUplinkRate" : 3,
        "lastDataDownlinkRate" : 3,
        "uplinkShortGuard" : 3,
        "downlinkMCS" : 3,
        "avgSignalStrengthByChain" : 3,
        "signalNoiseRatio" : 3,
        "timestamp": datetime.now(),   
    },
    {
        "station": "11:22:33:44:55:66",
        "rx_Mbps" : 4,
        "rx_Mbps_lag1" : 4,
        "rx_Mbps_lag2" : 4,
        "rx_Mbps_lag3" : 4,
        "rx_Mbps_lag5" : 4,
        "rx_Mbps_lag7" : 4,
        "rx_Mbps_avg3" : 4,
        "rx_Mbps_avg5" : 4,
        "rx_Mbps_avg7" : 4,
        "rx_Mbps_avg10" : 4,
        "tx_Mbps" : 4,
        "tx_Mbps_lag1" : 4,
        "tx_Mbps_avg3" : 4,
        "tx_Mbps_avg5" : 4,
        "signalStrength" : 40,
        "signalStrength_lag1" : 40,
        "signalStrength_lag2" : 40,
        "signalStrength_lag3" : 40,
        "signalStrength_lag5" : 40,
        "signalStrength_lag7" : 40,
        "signalStrength_avg3" : 40,
        "signalStrength_avg5" : 40,
        "signalStrength_avg7" : 40,
        "signalStrength_avg10" : 40,
        "rx_pps" : 4.5,
        "tx_pps" : 4.5,
        "uplinkMCS" : 4,
        "lastDataUplinkRate" : 4,
        "lastDataDownlinkRate" : 4,
        "uplinkShortGuard" : 4,
        "downlinkMCS" : 4,
        "avgSignalStrengthByChain" : 4,
        "signalNoiseRatio" : 4,
        "timestamp": datetime.now(),   
    },
]

INFERENCE_RESULTS_SAMPLES = [
    {
        "station": "AA:BB:CC:DD:EE:FF",
        "status": True,
        "probability": 0.65,
        "timestamp": datetime.now(),        
    },
    {
        "station": "11:22:33:44:55:66",
        "status": True,
        "probability": 0.85,
        "timestamp": datetime.now(),        
    },
    {
        "station": "AA:BB:CC:DD:EE:FF",
        "status": False,
        "probability": 0.42,
        "timestamp": datetime.now(),        
    },
    {
        "station": "11:22:33:44:55:66",
        "status": False,
        "probability": 0.35,
        "timestamp": datetime.now(),        
    },
    {
        "station": "AA:BB:CC:DD:EE:FF",
        "status": False,
        "probability": 0.85,
        "timestamp": datetime.now(),        
    },
    {
        "station": "11:22:33:44:55:66",
        "status": False,
        "probability": 0.32,
        "timestamp": datetime.now(),        
    },
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
    inference_results_samples_nb = nb_samples[mongo_db_manager_service.inference_results_collection_name]

    if band_status_samples_nb != 0 or box_traffic_samples_nb  != 0 or stations_traffic_samples_nb  != 0 or box_counters_samples_nb  != 0 or stations_counters_samples_nb  != 0 or inference_results_samples_nb  != 0:
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

    # Insert inference results samples to DB
    mongo_db_manager_service.insert_inference_results_samples(INFERENCE_RESULTS_SAMPLES)
    
    print("Database successfully created!")

@cli.command('delete')
def delete_db():
    """Delete database and collection if exists"""

    # Delete database and collection
    mongo_db_manager_service.delete_database()    
    print("Database successfully deleted!")


if __name__ == '__main__':
    cli()
