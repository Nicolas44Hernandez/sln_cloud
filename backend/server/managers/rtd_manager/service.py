import logging
import ping3
import time
from datetime import datetime, timedelta
from flask import Flask
from typing import List
import threading
from server.managers.mongo_db_manager import mongo_db_manager_service

logger = logging.getLogger(__name__)


class RtdManager:
    """Manager for RTD management service"""

    stations : List[str]
    rtd_period: float

    def __init__(self, app: Flask = None) -> None:
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        """Initialize RtdManager"""
        if app is not None:
            logger.info("initializing the MRTD manager")
            self.stations = app.config["RTD_STATIONS"]
            self.rtd_period = app.config["RTD_PERIOD_IN_SECS"]

            self.run_service_in_dedicated_thread()

    def ping_station(self, station_ip: str, station_mac: str, timestamp: datetime, nb_pings: int=10):
        """Ping a single station and log the response time in milliseconds"""
        start = datetime.now()
        results = []
        for i in range(nb_pings):
            rtd_ms = ping3.ping(station_ip, timeout=1, unit="ms")
            if rtd_ms is not None:
                results.append(rtd_ms)
            else:
                logger.warning(f"Ping to {station_ip} failed")
                return 
        delta = datetime.now() - start
        logger.debug(f"{nb_pings} pings executed in {delta}")
        
        if len(results) > 1:
            sorted_results = sorted(results)
            station_rtd = sum(sorted_results[:4]) / len(sorted_results[:4])

            logger.debug(f"RTD to {station_ip}: {station_rtd:.2f} ms")
            rtd_obj = {
                "station": station_mac,
                "rtd": station_rtd,
                "timestamp": timestamp - timedelta(hours=2),
            }
            # Store response in mongo DB
            try: 
                mongo_db_manager_service.create_stations_rtd_obj(rtd_obj)
            except: 
                logger.error("Error writting RTD object to DB")


    def run_service_in_dedicated_thread(self):
        """Run RTD manager service in dedicated thread"""
        thread = threading.Thread(target=self.run_service)
        thread.daemon = True
        thread.start()

    def run_service(self):
        """Run RTD service"""
        while True:            
            threads = []
            start = datetime.now()
            for station in self.stations:
                # Create a new thread for each ping
                thread = threading.Thread(target=self.ping_station, args=(station["ip"],station["mac"],start,10,))
                threads.append(thread)
                thread.start()    

            # Wait for all threads to complete
            for thread in threads:
                thread.join()
            # Get remaining time to wait
            end = datetime.now()
            elapsed_time = (end - start).total_seconds()
            remaining_time = self.rtd_period - elapsed_time

            remaining_time = self.rtd_period if remaining_time <= 0 else remaining_time
            
            # Wait sample period
            time.sleep(remaining_time)

rtd_manager_service: RtdManager = RtdManager()
""" RTD manager service singleton"""
