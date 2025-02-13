<template>
    TRAFFIC CHARTS COMPONENT
  </template>
  
  <script>
  export default {
    props: {
      tx_Mbps_2GHz: {
        type: Array,
        required: true,
        //     validator: function(value) {
        //       // Check if each item in the array is a string
        //       return value.every(item => typeof item === 'string')
        //     }
      },
      rx_Mbps_2GHz: {
        type: Array,
        required: true,
        //     validator: function(value) {
        //       // Check if each item in the array is a string
        //       return value.every(item => typeof item === 'string')
        //     }
      },
      tx_Mbps_5GHz: {
        type: Array,
        required: true,
        //     validator: function(value) {
        //       // Check if each item in the array is a string
        //       return value.every(item => typeof item === 'string')
        //     }
      },
      rx_Mbps_5GHz: {
        type: Array,
        required: true,
        //     validator: function(value) {
        //       // Check if each item in the array is a string
        //       return value.every(item => typeof item === 'string')
        //     }
      },
    },
  }
  </script>

<style scoped>
</style> 
  