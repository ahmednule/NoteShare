<template>
  <div id="app">
    <LandingPage />
  </div>
</template>

<script>
import LandingPage from './views/LandingPage.vue'

export default {
  name: 'App',
  components: {
    LandingPage
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
