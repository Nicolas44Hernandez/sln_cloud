import os
import logging
import pymongo
from flask import Flask
from server.common import ServerException, ErrorCode
from .model import BandStatus, BoxTraffic, StationsTraffic, BoxCounters, StationsCounters, InferenceResults, InferenceInput, Inferences, StationRtd

logger = logging.getLogger(__name__)


class MongoDbManager:
    """Manager for mongo management service"""

    mongodb_client: pymongo.MongoClient
    db_name: pymongo
    mongodb_str: str
    band_status_collection_name: str
    band_status_collection: str
    box_traffic_collection_name: str
    box_traffic_collection: str
    stations_traffic_collection_name: str
    stations_traffic_collection: str
    box_counters_collection_name: str
    box_counters_collection: str
    stations_counters_collection_name: str
    stations_counters_collection: str
    inferences_collection_name: str
    inferences_collection: str
    stations_rtd_collection_name: str
    stations_rtd_collection: str
    connected: bool

    def __init__(self, app: Flask = None) -> None:
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        """Initialize MongoDbManager"""
        if app is not None:
            logger.info("initializing the Mongo DB manager")
            if os.getenv("FLASK_ENV") != "DEVELOPMENT":
                self.mongodb_str=app.config["MONGO_STR"]
            else:                
                self.mongodb_str=app.config["MONGO_STR_DEV"]   

            self.db_name=app.config["MONGO_DB_NAME"]
            self.band_status_collection_name=app.config["MONGO_BAND_STATUS_COLLECTION_NAME"]
            self.box_traffic_collection_name=app.config["MONGO_BOX_TRAFFIC_COLLECTION_NAME"]
            self.stations_traffic_collection_name=app.config["MONGO_STATIONS_TRAFFIC_COLLECTION_NAME"]
            self.box_counters_collection_name=app.config["MONGO_BOX_COUNTERS_COLLECTION_NAME"]
            self.stations_counters_collection_name=app.config["MONGO_STATIONS_COUNTERS_COLLECTION_NAME"]
            self.inferences_collection_name=app.config["MONGO_INFERENCES_COLLECTION_NAME"]
            self.stations_rtd_collection_name=app.config["MONGO_STATIONS_RTD_COLLECTION_NAME"]
            self.connected=False

            self.connect_to_mongo_db()

    def connect_to_mongo_db(self, reconnection=False):
        """Connect to database"""

        self.connected=False
        self.mongodb_client = pymongo.MongoClient(self.mongodb_str)

        logger.info("Connecting to mongodb service")

        # Check if the database exists
        try:
            dblist = self.mongodb_client.list_database_names()
            new_db_cols = []
            if self.db_name not in dblist:     
                new_db = self.create_database()
                new_db_cols = list(new_db.keys())

            # Check if the collection exists
            mydb = self.mongodb_client[self.db_name]
            collist = mydb.list_collection_names()
            db_collumns = collist if len(collist) > 0 else new_db_cols
            expected_cols = [
                self.band_status_collection_name, 
                self.box_traffic_collection_name,
                self.stations_traffic_collection_name,
                self.box_counters_collection_name,
                self.stations_counters_collection_name,
                self.inferences_collection_name,
                #self.stations_rtd_collection_name,
            ]
            if not all(item in db_collumns for item in expected_cols):
                raise ServerException(ErrorCode.MONGO_ERROR)
            
            self.band_status_collection = self.mongodb_client[self.db_name][self.band_status_collection_name]
            self.box_traffic_collection = self.mongodb_client[self.db_name][self.box_traffic_collection_name]
            self.stations_traffic_collection = self.mongodb_client[self.db_name][self.stations_traffic_collection_name]
            self.box_counters_collection = self.mongodb_client[self.db_name][self.box_counters_collection_name]
            self.stations_counters_collection = self.mongodb_client[self.db_name][self.stations_counters_collection_name]
            self.inferences_collection = self.mongodb_client[self.db_name][self.inferences_collection_name]
            self.stations_rtd_collection = self.mongodb_client[self.db_name][self.stations_rtd_collection_name]
            self.connected=True
            logger.info("Succefully connected")
        except:
            logger.error("Error in mongodb connection")
            self.connected=False
            if reconnection:
                raise ServerException(ErrorCode.MONGO_ERROR)

    def reconnect_to_mongodb(self):
        """Try to reconnect to database"""
        logger.info("Trying to reconect to mongo service")
        self.connect_to_mongo_db(reconnection=True)

    def get_band_status_list(self):
        """Retreive band_status list from mongo"""
        if not self.connected:
            self.reconnect_to_mongodb()
        # Find all samples
        try:
            band_status_db = self.band_status_collection.find()
            samples = []
            for status in band_status_db:
                samples.append(status)
            return samples
        except:
            self.connected=False
            raise ServerException(ErrorCode.MONGO_ERROR)

    def get_timestamps_list(self):
        """Retreive timestamps list from mongo"""
        if not self.connected:
            self.reconnect_to_mongodb()
        
        try:
            # Find all samples from all the DBs
            band_status_samples = self.get_band_status_list()
            box_traffic_samples = self.get_box_traffic_list()
            stations_traffic_samples = self.get_stations_traffic_list()
            box_counters_samples = self.get_box_counters_list()
            stations_counters_samples = self.get_stations_counters_list()
            inferences_samples = self.get_inferences_list()
            stations_rtd_samples = self.get_stations_rtd_list()

            # Set a single samples list
            samples = band_status_samples + box_traffic_samples + stations_traffic_samples + box_counters_samples +  stations_counters_samples + inferences_samples + stations_rtd_samples
            # Extract the timestamps
            timestamps = []
            for sample in samples:
                timestamps.append(sample["timestamp"])
            # Filter and sort the timestamps
            unique_timestamps = list(set(timestamps))
            sorted_timestamps = sorted(unique_timestamps)
            # Return the sorted timestamps array
            return sorted_timestamps
        except:
            self.connected=False
            raise ServerException(ErrorCode.MONGO_ERROR)


    def create_band_status_obj(self, band_status: dict):
        """Create band status entry in collection"""
        try:
            sample = BandStatus(**band_status)
            sample_dict = sample.to_dict()
        except:
            raise ServerException(ErrorCode.ARGS_ERROR)
        try:
            self.band_status_collection.insert_one(sample_dict)
        except:
            self.connected=False
            raise ServerException(ErrorCode.MONGO_ERROR)
        return sample

    def get_box_traffic_list(self):
        """Retreive box traffic list from mongo"""
        if not self.connected:
            self.reconnect_to_mongodb()
        # Find all samples
        try:
            box_traffic_db = self.box_traffic_collection.find()
            samples = []
            for box_traffic_sample in box_traffic_db:
                samples.append(box_traffic_sample)
            return samples
        except:
            self.connected=False
            raise ServerException(ErrorCode.MONGO_ERROR)

    def get_traffic_list_for_band(self, band: str):
        """Retreive specific band traffic list from mongo"""
        if not self.connected:
            self.reconnect_to_mongodb()
        # Find all samples
        try:
            query = {"band": band} 
            filtered_samples = self.box_traffic_collection.find(query)
            samples = list(filtered_samples)
            return samples
        except:
            self.connected=False
            raise ServerException(ErrorCode.MONGO_ERROR)

    def create_box_traffic_obj(self, box_traffic: dict):
        """Create box_traffic entry in collection"""
        try:
            sample = BoxTraffic(**box_traffic)
            sample_dict = sample.to_dict()
        except:
            raise ServerException(ErrorCode.ARGS_ERROR)
        try:
            self.box_traffic_collection.insert_one(sample_dict)
        except:
            self.connected=False
            raise ServerException(ErrorCode.MONGO_ERROR)
        return sample

    def get_stations_traffic_list(self):
        """Retreive stations traffic list from mongo"""
        if not self.connected:
            self.reconnect_to_mongodb()
        # Find all samples
        try:
            stations_traffic_db = self.stations_traffic_collection.find()
            samples = []
            for stations_traffic_sample in stations_traffic_db:
                samples.append(stations_traffic_sample)
            return samples
        except:
            self.connected=False
            raise ServerException(ErrorCode.MONGO_ERROR)

    def create_stations_traffic_obj(self, stations_traffic: dict):
        """Create stations_traffic entry in collection"""
        try:
            sample = StationsTraffic(**stations_traffic)
            sample_dict = sample.to_dict()
        except:
            raise ServerException(ErrorCode.ARGS_ERROR)
        try:
            self.stations_traffic_collection.insert_one(sample_dict)
        except:
            self.connected=False
            raise ServerException(ErrorCode.MONGO_ERROR)
        return sample

    def get_traffic_list_for_station(self, station: str):
        """Get traffic list for a specific station from mongo"""
        if not self.connected:
            self.reconnect_to_mongodb()
        # Find all samples
        try:
            query = {"station": station} 
            filtered_samples = self.stations_traffic_collection.find(query)
            samples = list(filtered_samples)
            return samples
        except:
            self.connected=False
            raise ServerException(ErrorCode.MONGO_ERROR)

    def get_box_counters_list(self):
        """Retreive box counters list from mongo"""
        if not self.connected:
            self.reconnect_to_mongodb()
        # Find all samples
        try:
            box_counters_db = self.box_counters_collection.find()
            samples = []
            for box_counters_sample in box_counters_db:
                samples.append(box_counters_sample)
            return samples
        except:
            self.connected=False
            raise ServerException(ErrorCode.MONGO_ERROR)

    def create_box_counters_obj(self, box_counters: dict):
        """Create box_counters entry in collection"""
        try:
            sample = BoxCounters(**box_counters)
            sample_dict = sample.to_dict()
        except:
            raise ServerException(ErrorCode.ARGS_ERROR)
        try:
            self.box_counters_collection.insert_one(sample_dict)
        except:
            self.connected=False
            raise ServerException(ErrorCode.MONGO_ERROR)
        return sample
    
    def get_stations_counters_list(self):
        """Retreive stations counters list from mongo"""
        if not self.connected:
            self.reconnect_to_mongodb()
        # Find all samples
        try:
            stations_counters_db = self.stations_counters_collection.find()
            samples = []
            for stations_counters_sample in stations_counters_db:
                samples.append(stations_counters_sample)
            return samples
        except:
            self.connected=False
            raise ServerException(ErrorCode.MONGO_ERROR)

    def get_counters_list_for_station(self, station: str):
        """Get counters list for a specific station from mongo"""
        if not self.connected:
            self.reconnect_to_mongodb()
        # Find all samples
        try:
            query = {"station": station} 
            filtered_samples = self.stations_counters_collection.find(query)
            samples = list(filtered_samples)
            return samples
        except:
            self.connected=False
            raise ServerException(ErrorCode.MONGO_ERROR)
        
    def create_stations_counters_obj(self, stations_counters: dict):
        """Create stations_counters entry in collection"""
        try:
            sample = StationsCounters(**stations_counters)
            sample_dict = sample.to_dict()
        except:
            raise ServerException(ErrorCode.ARGS_ERROR)
        try:
            self.stations_counters_collection.insert_one(sample_dict)
        except:
            self.connected=False
            raise ServerException(ErrorCode.MONGO_ERROR)
        return sample

    def get_inferences_list(self):
        """Retreive inferences list from mongo"""
        if not self.connected:
            self.reconnect_to_mongodb()
        # Find all samples
        try:
            inferences_db = self.inferences_collection.find()
            samples = []
            for inferences_sample in inferences_db:
                samples.append(inferences_sample)
            return samples
        except:
            self.connected=False
            raise ServerException(ErrorCode.MONGO_ERROR)

    def get_inferences_list_for_station(self, station: str):
        """Get inferences list for a specific station from mongo"""
        if not self.connected:
            self.reconnect_to_mongodb()
        # Find all samples
        try:
            query = {"station": station} 
            filtered_samples = self.inferences_collection.find(query)
            samples = list(filtered_samples)
            return samples
        except:
            self.connected=False
            raise ServerException(ErrorCode.MONGO_ERROR)

    def get_stations_rtd_list(self):
        """Retreive stations rtd list from mongo"""
        if not self.connected:
            self.reconnect_to_mongodb()
        # Find all samples
        try:
            stations_rtd_db = self.stations_rtd_collection.find()
            samples = []
            for stations_rtd_sample in stations_rtd_db:
                samples.append(stations_rtd_sample)
            return samples
        except:
            self.connected=False
            raise ServerException(ErrorCode.MONGO_ERROR)

    def create_stations_rtd_obj(self, stations_rtd: dict):
        """Create stations_rtd entry in collection"""
        try:
            sample = StationRtd(**stations_rtd)
            sample_dict = sample.to_dict()
        except:
            raise ServerException(ErrorCode.ARGS_ERROR)
        try:
            self.stations_rtd_collection.insert_one(sample_dict)
        except:
            self.connected=False
            raise ServerException(ErrorCode.MONGO_ERROR)
        return sample

    def get_rtd_list_for_station(self, station: str):
        """Get rtd list for a specific station from mongo"""
        if not self.connected:
            self.reconnect_to_mongodb()
        # Find all samples
        try:
            query = {"station": station} 
            filtered_samples = self.stations_rtd_collection.find(query)
            samples = list(filtered_samples)
            return samples
        except:
            self.connected=False
            raise ServerException(ErrorCode.MONGO_ERROR)

     
    def create_inference_obj(self, inference: dict):
        """Create infernece entry in collection"""
        try:
            input = InferenceInput(**inference["input"])
            result = InferenceResults(**inference["result"])
            sample = Inferences(
                station=inference["station"],
                input=input,
                result=result,
                timestamp=inference["timestamp"],
            )
            sample_dict = sample.to_dict()
        except:
            raise ServerException(ErrorCode.ARGS_ERROR)
        try:
            self.inferences_collection.insert_one(sample_dict)
        except:
            self.connected=False
            raise ServerException(ErrorCode.MONGO_ERROR)
        return sample   

    def create_database(self):
        """Create database if doesnt exists"""

        dblist = self.mongodb_client.list_database_names()
        if self.db_name not in dblist:   
            logger.info(f"Creatting database {self.db_name}")         
            #Create database            
        else:
            logger.info(f"Database {self.db_name} already created") 
        mydb = self.mongodb_client[self.db_name]  
        
                
        collist = mydb.list_collection_names()
        # Band status collection
        if self.band_status_collection_name not in collist:
            logger.info(f"Creatting collection {self.band_status_collection_name}")
            self.band_status_collection = self.mongodb_client[self.db_name][self.band_status_collection_name]
        
        # Box traffic collection
        if self.box_traffic_collection_name not in collist:
            logger.info(f"Creatting collection {self.box_traffic_collection_name}")
            self.box_traffic_collection = self.mongodb_client[self.db_name][self.box_traffic_collection_name]
        
        # Stations traffic collection
        if self.stations_traffic_collection_name not in collist:
            logger.info(f"Creatting collection {self.stations_traffic_collection_name}")
            self.stations_traffic_collection = self.mongodb_client[self.db_name][self.stations_traffic_collection_name]

        # Box counters collection
        if self.box_counters_collection_name not in collist:
            logger.info(f"Creatting collection {self.box_counters_collection_name}")
            self.box_counters_collection = self.mongodb_client[self.db_name][self.box_counters_collection_name]
        
        # Station counters collection
        if self.stations_counters_collection_name not in collist:
            logger.info(f"Creatting collection {self.stations_counters_collection_name}")
            self.stations_counters_collection = self.mongodb_client[self.db_name][self.stations_counters_collection_name]
        
        # Inferences collection
        if self.inferences_collection_name not in collist:
            logger.info(f"Creatting collection {self.inferences_collection_name}")
            self.inferences_collection = self.mongodb_client[self.db_name][self.inferences_collection_name]

        # Stations rtd collection
        if self.stations_rtd_collection_name not in collist:
            logger.info(f"Creatting collection {self.stations_rtd_collection_name}")
            self.stations_rtd_collection = self.mongodb_client[self.db_name][self.stations_rtd_collection_name]


        # Return the number of samples in the colections
        collections_elements= {
            self.band_status_collection_name: self.band_status_collection.count_documents({}),
            self.box_traffic_collection_name: self.box_traffic_collection.count_documents({}),
            self.stations_traffic_collection_name: self.stations_traffic_collection.count_documents({}),
            self.box_counters_collection_name: self.box_counters_collection.count_documents({}),
            self.stations_counters_collection_name: self.stations_counters_collection.count_documents({}),
            self.inferences_collection_name: self.inferences_collection.count_documents({}),
            self.stations_rtd_collection_name: self.stations_rtd_collection.count_documents({}),
        }
        return collections_elements

    def insert_band_status_samples(self, samples):
        """Create multiple band status samples in database"""
        self.band_status_collection.insert_many(samples)
    
    def insert_box_traffic_samples(self, samples):
        """Create multiple box_traffic samples in database"""
        self.box_traffic_collection.insert_many(samples)
    
    def insert_stations_traffic_samples(self, samples):
        """Create multiple stations_traffic samples in database"""
        self.stations_traffic_collection.insert_many(samples)
    
    def insert_box_counters_samples(self, samples):
        """Create multiple box_counters samples in database"""
        self.box_counters_collection.insert_many(samples)
    
    def insert_stations_counters_samples(self, samples):
        """Create multiple stations_counters samples in database"""
        self.stations_counters_collection.insert_many(samples)

    def insert_inferences_samples(self, samples):
        """Create multiple inference samples in database"""
        self.inferences_collection.insert_many(samples)

    def insert_stations_rtd_samples(self, samples):
        """Create multiple stations_rtd samples in database"""
        self.stations_rtd_collection.insert_many(samples)
    
    def delete_database(self):
        """Drop collection and database"""
        self.band_status_collection.drop()
        self.box_traffic_collection.drop()
        self.stations_traffic_collection.drop()
        self.box_counters_collection.drop()
        self.stations_counters_collection.drop()
        self.inferences_collection.drop()
        self.stations_rtd_collection.drop()

mongo_db_manager_service: MongoDbManager = MongoDbManager()
""" Mongo DB manager service singleton"""
