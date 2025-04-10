import os
import json
from bson import ObjectId
from flask.cli import FlaskGroup
import click
from datetime import datetime
from server.app import create_app
from server.managers.mongo_db_manager import mongo_db_manager_service

app = create_app()
cli = FlaskGroup(create_app=create_app)


def json_serializable(obj):
    """Convert ObjectId and datetime to string for JSON serialization."""
    if isinstance(obj, ObjectId):
        return str(obj)
    elif isinstance(obj, datetime):
        return f"ISODate('{obj.isoformat()}Z')"
    raise TypeError(f"Type {type(obj)} not serializable")


def json_deserializable(data):
    """Convert JSON data back to appropriate types."""
    for item in data:
        # Convert ObjectId strings back to ObjectId
        if 'id' in item:  # Assuming your JSON has an 'id' field
            item['id'] = ObjectId(item['id'])
        # Convert ISO format strings back to datetime
        if 'timestamp' in item:  # Replace 'date_field' with your actual date field name
            date_str = item['timestamp']
            if date_str.startswith("ISODate('") and date_str.endswith("')"):
                date_str = date_str[9:-2]  # Extract the date string
                item['timestamp'] = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
    return data


@cli.command('export')
@click.argument('foldername')
def export_db(foldername):
    """Export database collections """
    # Create folder 
    if not os.path.exists(foldername):
        os.makedirs(foldername)  
    
    # Get collection names from config
    band_status_collection_name=app.config["MONGO_BAND_STATUS_COLLECTION_NAME"]
    box_traffic_collection_name=app.config["MONGO_BOX_TRAFFIC_COLLECTION_NAME"]
    stations_traffic_collection_name=app.config["MONGO_STATIONS_TRAFFIC_COLLECTION_NAME"]
    box_counters_collection_name=app.config["MONGO_BOX_COUNTERS_COLLECTION_NAME"]
    stations_counters_collection_name=app.config["MONGO_STATIONS_COUNTERS_COLLECTION_NAME"]
    inferences_collection_name=app.config["MONGO_INFERENCES_COLLECTION_NAME"]

    # Build backup file names
    band_status_file =f"{foldername}/{band_status_collection_name}.json"
    box_traffic_file =f"{foldername}/{box_traffic_collection_name}.json"
    stations_traffic_file =f"{foldername}/{stations_traffic_collection_name}.json"
    box_counters_file =f"{foldername}/{box_counters_collection_name}.json"
    stations_counters_file =f"{foldername}/{stations_counters_collection_name}.json"
    inferences_file =f"{foldername}/{inferences_collection_name}.json"

    print(f"Exporting data from database")
    # Get data from database
    band_status_list = mongo_db_manager_service.get_band_status_list()
    box_trafic_list = mongo_db_manager_service.get_box_traffic_list()
    stations_traffic_list = mongo_db_manager_service.get_stations_traffic_list()
    box_counters_list = mongo_db_manager_service.get_box_counters_list()
    stations_counters_list = mongo_db_manager_service.get_stations_counters_list()
    inferences_list = mongo_db_manager_service.get_inferences_list()

    print(f"Creating bacup files...")
    # Create backup files
    with open(band_status_file, 'w') as json_file:
        json.dump(band_status_list, json_file, default=json_serializable, indent=4)

    with open(box_traffic_file, 'w') as json_file:
        json.dump(box_trafic_list, json_file, default=json_serializable, indent=4)

    with open(stations_traffic_file, 'w') as json_file:
        json.dump(stations_traffic_list, json_file, default=json_serializable, indent=4)

    with open(box_counters_file, 'w') as json_file:
        json.dump(box_counters_list, json_file, default=json_serializable, indent=4)

    with open(stations_counters_file, 'w') as json_file:
        json.dump(stations_counters_list, json_file, default=json_serializable, indent=4)
    
    with open(inferences_file, 'w') as json_file:
        json.dump(inferences_list, json_file, default=json_serializable, indent=4)        

    print(f"Database successfully exported")

@cli.command('import')
@click.argument('foldername')
def import_db(foldername):
    """Import database collections"""

    # Get collection names from config
    band_status_collection_name=app.config["MONGO_BAND_STATUS_COLLECTION_NAME"]
    box_traffic_collection_name=app.config["MONGO_BOX_TRAFFIC_COLLECTION_NAME"]
    stations_traffic_collection_name=app.config["MONGO_STATIONS_TRAFFIC_COLLECTION_NAME"]
    box_counters_collection_name=app.config["MONGO_BOX_COUNTERS_COLLECTION_NAME"]
    stations_counters_collection_name=app.config["MONGO_STATIONS_COUNTERS_COLLECTION_NAME"]
    inferences_collection_name=app.config["MONGO_INFERENCES_COLLECTION_NAME"]

    # Create database if needed and samples
    nb_samples = mongo_db_manager_service.create_database()

    band_status_samples_nb = nb_samples[band_status_collection_name]
    box_traffic_samples_nb = nb_samples[box_traffic_collection_name]
    stations_traffic_samples_nb = nb_samples[stations_traffic_collection_name]
    box_counters_samples_nb = nb_samples[box_counters_collection_name]
    stations_counters_samples_nb = nb_samples[stations_counters_collection_name]
    inferences_samples_nb = nb_samples[inferences_collection_name]

    if band_status_samples_nb != 0 or box_traffic_samples_nb  != 0 or stations_traffic_samples_nb  != 0 or box_counters_samples_nb  != 0 or stations_counters_samples_nb  != 0 or inferences_samples_nb  != 0:
        print("Database exists, run delete command before re create it")
        return   

    # Build backup file names
    band_status_file =f"{foldername}/{band_status_collection_name}.json"
    box_traffic_file =f"{foldername}/{box_traffic_collection_name}.json"
    stations_traffic_file =f"{foldername}/{stations_traffic_collection_name}.json"
    box_counters_file =f"{foldername}/{box_counters_collection_name}.json"
    stations_counters_file =f"{foldername}/{stations_counters_collection_name}.json"
    inferences_file =f"{foldername}/{inferences_collection_name}.json"

    # Check if backup files exist
    backup_files = [band_status_file, box_traffic_file, stations_traffic_file, box_counters_file, stations_counters_file, inferences_file]
    for file in backup_files:
        if not os.path.exists(file):
            print(f"File {file} does not exist.")
            return
        
    print(f"Reading data from files...")
    # Get data from files
    with open(band_status_file, 'r') as json_file:
        band_status_data = json.load(json_file)
    
    with open(box_traffic_file, 'r') as json_file:
        box_traffic_data = json.load(json_file)
        
    with open(stations_traffic_file, 'r') as json_file:
        stations_traffic_data = json.load(json_file)
    
    with open(box_counters_file, 'r') as json_file:
        box_counters_data = json.load(json_file)

    with open(stations_counters_file, 'r') as json_file:
        stations_counters_data = json.load(json_file)

    with open(inferences_file, 'r') as json_file:
        inferences_data = json.load(json_file)

    # Deserialize the data
    band_status_data = json_deserializable(band_status_data)   
    box_traffic_data = json_deserializable(box_traffic_data)   
    stations_traffic_data = json_deserializable(stations_traffic_data)   
    box_counters_data = json_deserializable(box_counters_data)   
    stations_counters_data = json_deserializable(stations_counters_data)   
    inferences_data = json_deserializable(inferences_data)     

    print(f"Creating database with retreived data...")

    # Insert backup data into the database
    mongo_db_manager_service.insert_band_status_samples(band_status_data)
    mongo_db_manager_service.insert_box_traffic_samples(box_traffic_data)
    mongo_db_manager_service.insert_stations_traffic_samples(stations_traffic_data)
    mongo_db_manager_service.insert_box_counters_samples(box_counters_data)
    mongo_db_manager_service.insert_stations_counters_samples(stations_counters_data)
    mongo_db_manager_service.insert_inferences_samples(inferences_data)

    print(f"Data successfully imported")

if __name__ == '__main__':
    cli()
