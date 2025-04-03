<script setup>
import Header from '@/components/Header.vue';
</script>

<template>
  <Header></Header>
</template>

<script>
export default {
  name: 'App',
  
  data() {
    return {
        running: true
    };
  },
  mounted() {
    this.running = false; 
    this.$router.push({name: "home"})  
  },
  components: {
    Header
  },
  methods:{
    setServiceStatus(newStatus) {
      this.running = newStatus;        
    }
  },
}

</script>