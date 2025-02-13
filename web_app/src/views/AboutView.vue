<template>
  <div>
   <br>
   <h2>{{ appName }}</h2>
   <h3>v{{ appVersion }}</h3>
   <p>Designed and developed by {{ developer }}</p>
   <p>{{ email }}</p>
 </div>
</template>
<script>
export default {
 data() {
   return {
     appName: 'Smart Local Networks Web Server',
     appVersion: '1.0.0',
     developer: 'Nicolas Hernandez',
     email: 'nicolas.hernandezpaez@orange.com',
   }
 },
}
</script>

