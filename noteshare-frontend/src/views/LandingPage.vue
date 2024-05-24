<template>
    <v-app>
      <!-- Navbar -->
      <v-app-bar app color="white" dark>

        <v-icon color="Yellow" left class = "mr-2">fas fa-signature</v-icon>NOTESHARE
        <v-spacer></v-spacer>
        <v-btn text @click="goToProfile"><v-icon>mdi-account</v-icon></v-btn>
        <v-btn text @click="goToSignUp">Sign Up</v-btn>
        <v-btn text @click="goToLogin">Login</v-btn>
      </v-app-bar>
      
      <!-- Body -->
      <v-main>
        <v-container class="grey lighten-3 py-16">
          <v-row>
            <v-col class="text-center">
              <v-btn color="grey" class="ma-2">University</v-btn>
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
      <v-footer app color="grey" class="text-center">
        <v-col>
          <v-icon>mdi-youtube</v-icon>
          <v-icon>mdi-twitter</v-icon>
        </v-col>
      </v-footer>
    </v-app>
  </template>
 
  <script>
 
  </script>
 
  <style scoped>
  .v-application {
    background-color: #584e4e;
  }
  </style>