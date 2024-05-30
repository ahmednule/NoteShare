<template>
  <v-container class="fill-height d-flex flex-column justify-center align-center">
    <div class="search text-center">
      <h1 class="subheading grey--text">This is the SearchView page</h1>
      <v-container class="my-5">
        content
      </v-container>
    </div>
  </v-container>
</template>

<script>
export default {
  name: 'SearchView',
  data () {
    return {
      //
    }
  }
}
</script>

<style scoped>
.search {
  width: 100%;
  max-width: 600px; /* Adjust this as necessary */
}
.subheading {
  margin-bottom: 20px;
}
</style>
