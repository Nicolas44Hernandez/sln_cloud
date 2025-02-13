import os
import logging
import pymongo
from flask import Flask
from server.common import ServerException, ErrorCode

logger = logging.getLogger(__name__)


class BandStatusManager:
    """Manager for Band status mongo management service"""

    mongodb_client: pymongo.MongoClient
    db_name: pymongo
    mongodb_str: str
    band_status_collection_name: str
    band_status_collection: str
    connected: bool

    def __init__(self, app: Flask = None) -> None:
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        """Initialize BandStatusManager"""
        if app is not None:
            logger.info("initializing the BandStatus manager")
            if os.getenv("FLASK_ENV") != "DEVELOPMENT":
                self.mongodb_str=app.config["MONGO_STR"]
            else:                
                self.mongodb_str=app.config["MONGO_STR_DEV"]       
            self.db_name=app.config["MONGO_DB_NAME"]
            self.band_status_collection_name=app.config["MONGO_BAND_STATUS_COLLECTION_NAME"]
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
            if self.db_name not in dblist:            
                raise ServerException(ErrorCode.MONGO_ERROR)                 

            # Check if the collection exists
            mydb = self.mongodb_client[self.db_name]
            collist = mydb.list_collection_names()
            if self.band_status_collection_name not in collist:
                raise ServerException(ErrorCode.MONGO_ERROR)
            
            self.band_status_collection = self.mongodb_client[self.db_name][self.band_status_collection_name]
            self.connected=True
            logger.info("Succefully connected")
        except:
            logger.error("Error in mongodb connection")
            self.connected=False
            if reconnection:
                raise ServerException(ErrorCode.MONGO_ERROR)

    def reconnect_to_mongodb(self):
        """Try to reconnect to database"""
        logger.info("Trying to recconect to mongo service")
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
        if self.band_status_collection_name not in collist:
            logger.info(f"Creatting collection {self.band_status_collection_name}")
            self.band_status_collection = self.mongodb_client[self.db_name][self.band_status_collection_name]
    
        # Return the number of samples in the colection
        return self.band_status_collection.count_documents({})

    def insert_samples(self, samples):
        """Create multiple band status samples in database"""
        self.band_status_collection.insert_many(samples)
    
    def delete_database(self):
        """Drop collection and database"""
        self.band_status_collection.drop()

band_status_manager_service: BandStatusManager = BandStatusManager()
""" Band status manager service singleton"""
