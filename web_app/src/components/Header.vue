<script setup>
import { RouterLink, RouterView } from 'vue-router';
</script>

<template>
<header>
  <div>
    <img alt="SLN logo" class="logo" src="@/assets/sln-logo.png"/>
  </div>
  <div>
    <div class="wrapper">      
      <nav>
        <RouterLink to="/sln/traffic"  >Traffic</RouterLink>
        <RouterLink to="/sln/noise"  >Noise</RouterLink>
        <RouterLink to="/sln/about">About</RouterLink>                  
      </nav>
    </div>    
  </div>   
</header>
  <div>
    <RouterView />
  </div>  
</template>

<script>
export default {
  name: 'Header',
}

</script>

<style scoped>
header {
    line-height: 1.5;
    position: fixed;
    top: 0;
    left: 0;    
    width: 100%;
    background-color: #fff; /* Set background color if needed */
    z-index: 1000; /* Set a high z-index to make sure it stays above other elements */
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Optional: Add a box shadow for a subtle effect */
  }
.logo {
  /* display: block;
  margin: 0 auto 2rem; */
  width: 80px; /* Adjust as needed */
  height: auto; /* Maintain aspect ratio */
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 0;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: grid;
    place-items: center;
    top: 0;
    /* position: fixed; */
    width: 100%;
  }

  .logo {
    margin: 0 0 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: center;
    flex-wrap: wrap;
    top: 0;
    /* position: fixed; */
    width: 100%;
  }

  nav {
    /* text-align: left;
    margin-left: -1rem; */
    font-size: 1rem;

    padding: 0;
    /* margin-top: 1rem; */
  }
}
</style>
