<template>
  <div id="app">
    <LandingPage />
     </div>
  <router-view> </router-view>
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
/* Add global styles here */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}
</style>
