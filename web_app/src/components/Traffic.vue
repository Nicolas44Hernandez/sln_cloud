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
  <div class="rtd-container">
    <StationsRtdChart :stations_rtd="stations_rtd" :stations_colors="stations_colors" :timestamps="timestamps" />
  </div>
  <div class="band-status-container">
    <BandStatusChart :band_status="band_status" :timestamps="timestamps" />
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
      this.getStationsRtd();
      
      this.getTimestamps();
    },
    getBoxTraffic() {
      // Geting box traffic list of points from backend
      const url ='http://localhost:3000/api-sln/traffic/box'
      //const url ='/api-eip/traffic/box'
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
      const url ='http://localhost:3000/api-sln/traffic/stations'
      //const url ='/api-eip/traffic/stations'
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
      const url ='http://localhost:3000/api-sln/band_status'
      //const url ='/api-eip/band_status'
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
      const url ='http://localhost:3000/api-sln/counters/box'
      //const url ='/api-eip/counters/box'
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
      const url ='http://localhost:3000/api-sln/counters/stations'
      //const url ='/api-eip/counters/stations'
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
      const url ='http://localhost:3000/api-sln/inference'
      //const url ='/api-eip/inference'
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
    getStationsRtd() {
      // Geting stations traffic list of points from backend
      const url ='http://localhost:3000/api-sln/rtd'
      //const url ='/api-eip/traffic/rtd'
      axios.get(url)
        .then(response => {
          let new_stations_rtd_dict = {};
        
          console.log("When retreiving stations RTD");

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
      const url ='http://localhost:3000/api-sln/timestamps'
      //const url ='/api-eip/timestamps'
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
 
</style>