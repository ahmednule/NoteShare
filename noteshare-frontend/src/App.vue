<template>
  <div id="app">
<<<<<<< HEAD
    <LandingPage />
     </div>
  <router-view> </router-view>
=======
    <router-view></router-view>
  </div>
>>>>>>> Saisa
</template>

<script>
import LandingPage from './views/LandingPage.vue'
import Home from './views/Home.vue'
export default {
  name: 'App',
  components: {
    LandingPage,
    Home
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #584e4e;
  margin-top: 60px;
}
/* Add global styles here */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}
</style>

