<template>
  <v-footer class="d-flex flex-column m-0" style="position: relative; bottom: 0; left: 0; width: 100%;">
    <div class="bg-teal d-flex w-100 align-center px-4 ml-0">
      <strong>Get connected with us on social networks!</strong>

      <v-spacer></v-spacer>

      <v-btn
        v-for="icon in icons"
        :key="icon"
        :icon="icon"
        class="mx-4"
        size="small"
        variant="plain"
      ></v-btn>
    </div>

    <div class="px-4 py-2 bg-black text-center w-100">
      {{ new Date().getFullYear() }} — <strong>NoteShare</strong>
    </div>
  </v-footer>
</template>

<script>
export default {
    mounted() {
    // Set body margins and padding to 0
    document.body.style.margin = '0';
    document.body.style.padding = '0';
  },
  data: () => ({
    icons: [
      'mdi-facebook',
      'mdi-twitter',
      'mdi-linkedin',
      'mdi-instagram',
    ],
  }),
}
</script>
