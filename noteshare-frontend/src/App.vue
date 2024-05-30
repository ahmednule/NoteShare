<template>
  <v-app color="grey">
    <HeaderView/>
    <v-content>
      <router-view/>
    </v-content>
    <FooterView />
  </v-app>
</template>

<script>
import HeaderView from '@/components/HeaderView'
import FooterView from '@/components/FooterView'
export default {
  name: 'App',
  components: {
   HeaderView, FooterView
  },
  data: () => ({
    //
  }),
}
</script>
<style>

</style>
