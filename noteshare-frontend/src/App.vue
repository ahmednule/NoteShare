<template>
  <v-app color="grey">
    <HeaderView app/>
    <v-content class="mx-5 mb-5y" color="red">
      <router-view/>
    </v-content>
  </v-app>
</template>

<script>
import HeaderView from '@/components/HeaderView'
export default {
  name: 'App',
  components: {
   HeaderView
  },
  data: () => ({
    //
  }),
}
</script>
<style>

</style>
