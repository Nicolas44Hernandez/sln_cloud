<template>
    NOISE CHARTS COMPONENT
  </template>
  
  <script>
  export default {
    props: {
      noise_2GHz: {
        type: Array,
        required: true,
        //     validator: function(value) {
        //       // Check if each item in the array is a string
        //       return value.every(item => typeof item === 'string')
        //     }
      },
      noise_5GHz: {
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
  