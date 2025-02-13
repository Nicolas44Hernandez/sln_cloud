<script setup>
import NoiseCharts from './NoiseCharts.vue'
</script>
<template>  
<h2>
  Noise Charts 
  WIP
  </h2>
</template>
<script>
import axios from 'axios';

export default {
  data() {
    return {
      box_noise_2GHz: [],
      box_noise_5GHz: [],
    };
  },
  mounted() {
    // in startup
    console.log("in mounted NoiseCharts Vue");
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