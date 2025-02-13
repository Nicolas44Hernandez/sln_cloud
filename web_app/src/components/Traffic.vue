<script setup>
import TrafficCharts from './TrafficCharts.vue'
</script>
<template>  
<h2>Traffic Charts WIP</h2>
</template>
<script>
import axios from 'axios';

export default {
  data() {
    return {
      box_txMbps_2GHz: [],
      box_rxMbps_2GHz: [],
      box_txMbps_5GHz: [],
      box_rxMbps_5GHz: [],
    };
  },
  mounted() {
    // in startup
    console.log("in mounted TrafficCharts Vue");
  },
  methods: {
    getCallToUse() {
      //const url ='http://localhost:5000/api-sln/path/'
      const url ='/api-sln/path/'
      axios.get(url)
        .then(response => {
          console.log(response.data);
        })
        .catch(error => {
          console.log(error);  
          //TODO: Handle errors in API calls
        });
    },       
  }
}
</script>

<style scoped>

h2{
  text-align: center;
}
</style>