<script setup>
import axios from 'axios';
import BoxTrafficChart from './BoxTrafficChart.vue'
import BoxCountersChart from './BoxCountersChart.vue'
import StationsCountersChart from './StationsCountersChart.vue'
import InferenceProbabilitiesChart from './InferenceProbabilitiesChart.vue'
import InferenceResultsChart from './InferenceResultsChart.vue'
import BandStatusChart from './BandStatusChart.vue'
import StationsRtdChart from './StationsRtdChart.vue'

</script>
<template>  
<div class="charts-container">
  <div class="toggle-container">
    SLN 
    <div class="toggle-switch" :class="{ 'active': serviceRunning }" @click="toggleService">
      <div class="toggle-thumb" :class="{ 'active': serviceRunning }"></div>
    </div>
  
  </div>
  <div class="box-counters-container">
    <BoxCountersChart :counters_2GHz="box_counters_2GHz" :counters_5GHz="box_counters_5GHz" :timestamps="timestamps"/>
  </div>
  <div class="stations-counters-container">
    <StationsCountersChart :stations_counters="stations_counters" :stations_colors="stations_colors" :timestamps="timestamps"/>
  </div>
  <div class="traffic-container">
    <BoxTrafficChart :traffic_2GHz="box_traffic_2GHz" :traffic_5GHz="box_traffic_5GHz" :connected_stations="connected_stations" :stationsTraffic="stations_traffic" :stations_colors="stations_colors" :timestamps="timestamps" />
  </div> 
  <div class="inferences-probabilities-container">
    <InferenceProbabilitiesChart :inferences="inferences" :stations_colors="stations_colors" :timestamps="timestamps"/>
  </div>
  <div class="inferences-results-container">
    <InferenceResultsChart :inferences="inferences" :stations_colors="stations_colors" :timestamps="timestamps" />
  </div>
  <!-- <div class="rtd-container">
    <StationsRtdChart :stations_rtd="stations_rtd" :stations_colors="stations_colors" :timestamps="timestamps" />
  </div> -->
  <div class="band-status-container">
    <BandStatusChart :band_status="band_status" :timestamps="timestamps" />
  </div>
  <div class="button-container">
    <button @click="confirmDataBaseDelete" class="restart-database-button">Restart Database</button>
    <button @click="confirmDataBaseExport" class="export-database-button">Export Database</button>
  </div>
</div>


</template>
<script>
import axios from 'axios';

export default {
  data() {
    return {
      timestamps: [],
      box_traffic_2GHz: [],
      box_traffic_5GHz: [],
      band_status: [],
      connected_stations: [],
      stations_traffic: {},
      stations_rtd: {},
      box_counters_2GHz: [],
      box_counters_5GHz: [],
      stations_counters: {},
      inferences: {},
      stations_colors: [],
      serviceRunning: false,
    };
  },
  mounted() {
    // in startup
    console.log("in mounted TrafficCharts Vue");
    this.generateStationsColors();
    this.getDataFromBackend();
    
    setInterval(this.getDataFromBackend, 5000); // Call every 5 seconds    
  },
  methods: {
    getDataFromBackend(){
      this.getBandStatusList();
      this.getBoxTraffic();      
      this.getInferences();
      this.getStationsTraffic();
      this.getBoxCounters();
      this.geStationsCounters();
      //this.getStationsRtd();
      this.getServiceStatus();
      
      this.getTimestamps();
    },
    getBoxTraffic() {
      // Geting box traffic list of points from backend
      //const url ='http://localhost:3000/api/traffic/box'
      const url ='/api/traffic/box'
      axios.get(url)
        .then(response => {
          let new_box_2GHz_array = [];
          let new_box_5GHz_array = [];

          response.data.forEach((point) => {
            if(point.band == "5GHz"){
              new_box_5GHz_array.push(point);
            }
            else if(point.band == "2.4GHz"){
              new_box_2GHz_array.push(point);
            }
          });

        // update arrays
        if(!this.arraysAreSimilar(new_box_2GHz_array, this.box_traffic_2GHz)){
          console.log("Array 2.4GHz changed");
          this.box_traffic_2GHz = new_box_2GHz_array;
          //console.log(this.box_traffic_2GHz);
        }
        if(!this.arraysAreSimilar(new_box_5GHz_array, this.box_traffic_5GHz)){
          console.log("Array 5GHz changed");
          this.box_traffic_5GHz = new_box_5GHz_array;
          //console.log(this.box_traffic_5GHz);
        }
        })
        .catch(error => {
          console.log(error);  
        });
    },
    getStationsTraffic() {
      // Geting stations traffic list of points from backend
      //const url ='http://localhost:3000/api/traffic/stations'
      const url ='/api/traffic/stations'
      axios.get(url)
        .then(response => {
          let new_stations_traffic_dict = {};

          response.data.forEach((sample) => {
            const newSample = {
                "timestamp": sample.timestamp,
                "rx_Mbps": sample.rx_Mbps,
                "tx_Mbps": sample.tx_Mbps,                
              }
            if (sample.station in new_stations_traffic_dict) {              
              new_stations_traffic_dict[sample.station].push(newSample);
            } else {
              new_stations_traffic_dict[sample.station] = [newSample];
            }                
          });
          
          // Get stations list
          const stations_list = Object.keys(new_stations_traffic_dict)
          const stations_in_new_data = [...new Set(stations_list)];
          
          // update stations traffic arrays    
          for (const station of stations_in_new_data) {            
            if(station in this.stations_traffic) {           
              if(!this.arraysAreSimilar(new_stations_traffic_dict[station], this.stations_traffic[station])){
                console.log("Stations Array changed");
                this.stations_traffic = new_stations_traffic_dict;
                this.connected_stations=stations_in_new_data;
                break;
              }  
            }
            else {
              console.log("Stations Array changed");
              this.stations_traffic = new_stations_traffic_dict;
              this.connected_stations=stations_in_new_data;
              break;
            }
          }
        })
        .catch(error => {
          console.log(error);  
        });
    },
    getBandStatusList() {
      // Geting band status list of points from backend
      //const url ='http://localhost:3000/api/band_status'
      const url ='/api/band_status'
      axios.get(url)
        .then(response => {
          let new_band_status_array = [];
          response.data.forEach((point) => {
            new_band_status_array.push(point);            
          });

        // update arrays
        if(!this.arraysAreSimilar(new_band_status_array, this.band_status)){
          console.log("Band status array changed");
          this.band_status = new_band_status_array;
          console.log(this.band_status);
        }
        })
        .catch(error => {
          console.log(error);  
        });
    },
    getBoxCounters() {
      // Geting box traffic list of points from backend
      //const url ='http://localhost:3000/api/counters/box'
      const url ='/api/counters/box'
      axios.get(url)
        .then(response => {
          let new_box_counters_2GHz_array = [];
          let new_box_counters_5GHz_array = [];

          response.data.forEach((point) => {
            if(point.band == "5GHz"){
              new_box_counters_5GHz_array.push(point);
            }
            else if(point.band == "2.4GHz"){
              new_box_counters_2GHz_array.push(point);
            }
          });

          

          // update arrays
          if(!this.arraysAreSimilar(new_box_counters_2GHz_array, this.box_counters_2GHz)){
            console.log("Counters array 2.4GHz changed");
            this.box_counters_2GHz = new_box_counters_2GHz_array;
            console.log(this.box_counters_2GHz);
          }
          if(!this.arraysAreSimilar(new_box_counters_5GHz_array, this.box_counters_5GHz)){
            console.log("Counters array 5GHz changed");
            this.box_counters_5GHz = new_box_counters_5GHz_array;
            console.log(this.box_counters_5GHz);
          }
        })
        .catch(error => {
          console.log(error);  
        });
    }, 
    geStationsCounters() {
      // Geting stations counters list of points from backend
      //const url ='http://localhost:3000/api/counters/stations'
      const url ='/api/counters/stations'
      axios.get(url)
        .then(response => {
          let new_stations_counters_dict = {};

          response.data.forEach((sample) => {
            const newSample = {
                "station": sample.station,
                "timestamp": sample.timestamp,
                "txBytes" : sample.txBytes,
                "rxBytes" : sample.rxBytes,
                "uplinkMCS" : sample.uplinkMCS,
                "lastDataUplinkRate" : sample.lastDataUplinkRate,
                "lastDataDownlinkRate" : sample.lastDataDownlinkRate,
                "signalStrength" : sample.signalStrength,
                "avgSignalStrengthByChain" : sample.avgSignalStrengthByChain,
                "uplinkShortGuard" : sample.uplinkShortGuard,
                "downlinkMCS" : sample.downlinkMCS,
                "inactive" : sample.inactive,
                "signalNoiseRatio" : sample.signalNoiseRatio,
                "rxPacketCount" : sample.rxPacketCount,
                "txPacketCount" : sample.txPacketCount,  
                "txErrors" : sample.txErrors,   
                "band" : sample.band,             
              }
            if (sample.station in new_stations_counters_dict) {              
              new_stations_counters_dict[sample.station].push(newSample);
            } else {
              new_stations_counters_dict[sample.station] = [newSample];
            }                
          });
          
          // Get stations list
          const stations_list = Object.keys(new_stations_counters_dict)
          const stations_in_new_data = [...new Set(stations_list)];
          
          // update stations counters arrays    
          for (const station of stations_in_new_data) {            
            if(station in this.stations_counters) {           
              if(!this.arraysAreSimilar(new_stations_counters_dict[station], this.stations_counters[station])){
                console.log("Stations counters array changed");
                this.stations_counters = new_stations_counters_dict;
                break;
              }  
            }
            else {
              console.log("Stations counters array changed");
              this.stations_counters = new_stations_counters_dict;
              break;
            }
          }
        })
        .catch(error => {
          console.log(error);  
        });
    },
    getInferences() {
      // Geting inferences list of points from backend
      //const url ='http://localhost:3000/api/inference'
      const url ='/api/inference'
      axios.get(url)
        .then(response => {
          let new_inferences_dict = {};

          response.data.forEach((sample) => {
            const inferece_status = sample.result.status ? true : false;          
            const newSample = {
                "timestamp": sample.timestamp,
                "status": inferece_status,
                "probability": sample.result.probability,              
              }
            if (sample.station in new_inferences_dict) {
              new_inferences_dict[sample.station].push(newSample);
            } else {
              new_inferences_dict[sample.station] = [newSample];  
            }                
          });

          // update inferences arrays
          const stations_list = Object.keys(new_inferences_dict)
          const stations_in_new_data = [...new Set(stations_list)];
          for (const station of stations_in_new_data) {            
            if(station in this.inferences) {           
              if(!this.arraysAreSimilar(new_inferences_dict[station], this.inferences[station])){
                console.log(`Inferences array changed for station ${station}`);
                this.inferences = new_inferences_dict;
                break;
              }  
            }
            else {
              console.log(`Inferences samples received for station ${station}`);
              this.inferences = new_inferences_dict;
              break;
            }
          }
        })
        .catch(error => {
          console.log(error);  
        });
    },
    getServiceStatus() {
      // Geting inferences list of points from backend
      const url ='http://192.168.102.1:8000/api/wifi/sln/status'
      axios.get(url)
        .then(response => {
          this.serviceRunning = response.data.status;
        })
        .catch(error => {
          console.log(error);  
        });
    },
    getStationsRtd() {
      // Geting stations traffic list of points from backend
      //const url ='http://localhost:3000/api/rtd'
      const url ='/api/traffic/rtd'
      axios.get(url)
        .then(response => {
          let new_stations_rtd_dict = {};
          response.data.forEach((sample) => {
            const newSample = {
                "timestamp": sample.timestamp,
                "rtd": sample.rtd,
              }
            if (sample.station in new_stations_rtd_dict) {              
              new_stations_rtd_dict[sample.station].push(newSample);
            } else {
              new_stations_rtd_dict[sample.station] = [newSample];
            }                
          });
          
          // Get stations list
          const stations_list = Object.keys(new_stations_rtd_dict)
          const stations_in_new_data = [...new Set(stations_list)];
          
          // update stations rtd arrays    
          for (const station of stations_in_new_data) {            
            if(station in this.stations_rtd) {           
              if(!this.arraysAreSimilar(new_stations_rtd_dict[station], this.stations_rtd[station])){
                this.stations_rtd = new_stations_rtd_dict;
                break;
              }  
            }
            else {
              this.stations_rtd = new_stations_rtd_dict;
              break;
            }
          }
        })
        .catch(error => {
          console.log(error);  
        });
    },
    getTimestamps() {
      // Geting timestamps list from backend
      //const url ='http://localhost:3000/api/timestamps'
      const url ='/api/timestamps'
      axios.get(url)
        .then(response => {
          const new_timestamps_list = response.data.timestamps;
          // update timestamps array
          if(!this.arraysAreSimilar(new_timestamps_list, this.timestamps)){
            console.log("Timestamps array changed");
            this.timestamps = new_timestamps_list;
          }
        })
        .catch(error => {
          console.log(error);  
        });
    },
    generateStationsColors(){
      for (let i = 1; i <= 10; i++) {
        const colors =  this.getRandomColor();
        this.stations_colors.push(colors);
      }
    },
    getRandomColor() {
        // Generate random RGB values
        const r = Math.floor(Math.random() * 256);
        const g = Math.floor(Math.random() * 256);
        const b = Math.floor(Math.random() * 256);

        // Create the border color (opaque)
        const borderColor = `rgba(${r}, ${g}, ${b}, 1)`;

        // Create the background color (semi-transparent)
        const backgroundColor = `rgba(${r}, ${g}, ${b}, 0)`;

        return { borderColor, backgroundColor };
    },
    arraysAreSimilar(arr1, arr2) {
      if (arr1.length !== arr2.length) {
          return false; // Arrays are not the same length
      }
      return arr1.slice().sort().toString() === arr2.slice().sort().toString();
    }, 
    confirmDataBaseDelete() {
      const userConfirmed = confirm("Are you sure you want to restart database?");
      if (userConfirmed) {
        this.restartDatabase(); 
      } else {
        console.log("Database restart canceled.");
      }
    },
    async restartDatabase() {
      // Geting timestamps list from backend
      //const url ='http://localhost:3000/api/database/reset'
      const url ='/api/database/reset'

      axios.post(url)
        .then(response => {
          console.log('Response:', response.data);
        })
        .catch(error => {
          console.log('Error in database restart:', response.data);
          console.log(error);  
        });
    },
    confirmDataBaseExport(){
      const userInput = prompt("Please type database export file:");
      this.exportDatabase(userInput);       
    },
    async exportDatabase(file_name) {
      console.log('Exporting database to :', file_name);
      // Geting timestamps list from backend
      //const url =`http://localhost:3000/api/database/export/${file_name}`
      const url =`/api/database/export/${file_name}` 

      axios.get(url, { responseType: 'blob' })
        .then(response => {
          const url = window.URL.createObjectURL(new Blob([response.data]));
          const link = document.createElement('a');
          link.href = url;
          link.setAttribute('download', `${file_name}.zip` );
          document.body.appendChild(link);
          link.click();
          link.remove();
          console.log('Database exported');
        })
        .catch(error => {
          console.log('Error in database export:', error.response.data);
          console.log(error); 
        });
    },
    toggleService() {
      this.serviceRunning = !this.serviceRunning;
      const url =`http://192.168.102.1:8000/api/wifi/sln/status?new_status=${this.serviceRunning}`
      axios.post(url)
        .catch(error => {
          console.log('Error in service status toggle:', response.data);
          console.log(error);  
        });
    },
  }
}
</script>

<style scoped>

h2{
  text-align: center;
}
.box-counters-container{
  margin-top: 10px; 
}
.traffic-container {
    margin-top: 10px; 
}
.charts-container {
    margin-top: 150px; 
}
.inferences-probabilities-container{
  margin-top: 15px; 
}
.inferences-results-container{
  margin-top: 15px;
}
.band-status-container {
    margin-top: 15px; 
}
.button-container {
  margin: 30px; 
  text-align: center;
}
.restart-database-button {
  background-color: red; 
  color: rgb(0, 0, 0); 
  padding: 10px 20px; 
  cursor: pointer; 
  font-size: 14px;
  margin: 5px;
}
.export-database-button {
  background-color: rgb(31, 26, 92); 
  color: rgb(252, 252, 252); 
  padding: 10px 20px; 
  cursor: pointer; 
  font-size: 14px;
  margin: 5px;
}
.toggle-container {
  margin: 30px; 
  text-align: center;
}
.toggle-switch {
  width: 60px; /* Width of the toggle switch */
  height: 30px; /* Height of the toggle switch */
  background-color: red; /* Background color when off */
  border-radius: 15px; /* Rounded corners */
  position: relative; /* Positioning for the thumb */
  cursor: pointer; /* Change cursor on hover */
  display: inline-block; /* Inline block for alignment */
  transition: background-color 0.3s; /* Smooth transition for background color */
}
.toggle-switch.active {
  background-color: green; /* Background color when on */
}
.toggle-thumb {
  width: 28px; /* Width of the toggle thumb */
  height: 28px; /* Height of the toggle thumb */
  background-color: white; /* Thumb color */
  border-radius: 50%; /* Circular thumb */
  position: absolute; /* Positioning */
  top: 1px; /* Center the thumb vertically */
  left: 1px; /* Position the thumb on the left */
  transition: transform 0.3s; /* Smooth transition for movement */
}
.toggle-thumb.active {
  transform: translateX(30px); /* Move thumb to the right when active */
}

 
</style>