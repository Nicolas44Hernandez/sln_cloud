from flask.cli import FlaskGroup
from datetime import datetime, timedelta
from server.app import create_app
from server.managers.band_status_manager import band_status_manager_service

app = create_app()
cli = FlaskGroup(create_app=create_app)

TEST_SAMPLES = [
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

@cli.command('create')
def create_db():
    """Create database and collection if doesnt exists"""

    # Create database if needed
    nb_samples = band_status_manager_service.create_database()

    # Create samples
    if nb_samples != 0:
        print("Database exists, run delete command before re create it")
        return   
     
    print("Database created")
    print("Seeding database")
    
    # Insert clients to DB
    band_status_manager_service.insert_samples(TEST_SAMPLES)
    
    print("Database successfully created!")

@cli.command('delete')
def delete_db():
    """Delete database and collection if exists"""

    # Delete database and collection
    band_status_manager_service.delete_database()    
    print("Database successfully deleted!")


if __name__ == '__main__':
    cli()
