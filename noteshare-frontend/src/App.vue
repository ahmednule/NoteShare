<template>
  <v-app color="grey">
    <HeaderView app/>
    <v-content>
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
