<template>
    <v-app>
      <NavBar />
 
      <!-- Body -->
      <v-main>
        <v-container class="grey lighten-3 py-16">
          <v-row>
            <v-col class="text-center">
              <v-btn color="blue" class="ma-2">University</v-btn>
              <v-btn color="blue" class="ma-2">College</v-btn>
              <v-btn color="blue" class="ma-2">High School</v-btn>
            </v-col>
          </v-row>
          <v-row>
            <v-col class="text-center">
              <h1 class="font-weight-bold">Sharing notes and knowledge</h1>
              <p>Find top related study notes from students sharing the same course</p>
            </v-col>
          </v-row>
          <v-row>
            <v-col class="text-center">
              <v-text-field
                class="mt-8"
                label="Search for documents"
                outlined
                dense
              ></v-text-field>
              <p>Only the best</p>
            </v-col>
          </v-row>
        </v-container>
      </v-main>
 
      <!-- Bottom Bar -->
      <v-footer app color="white" class="text-center">
        <v-col>
          <v-icon>mdi-youtube</v-icon>
          <v-icon>mdi-twitter</v-icon>
        </v-col>
      </v-footer>
    </v-app>
  </template>
 
  <script>
  import NavBar from '@/components/NavBar.vue';
 
  export default {
    components: {
      NavBar,
    },
  };
  </script>
 
  <style scoped>
  .v-application {
    background-color: #666161;
  }
  </style>