<template>
    <v-app>
      <!-- Navbar -->
      <v-app-bar app color="brown" dark>

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
              <v-btn color="primary" class="ma-2 custom-button" >University</v-btn>
              <v-btn color="primary" class="ma-2 custom-button">College</v-btn>
              <v-btn color="primary" class="ma-2 custom-button">High School</v-btn>
            </v-col>
          </v-row>
          <v-row>
            <v-col class="text-center">
              <h1 class="font-weight-bold heading" >Sharing notes and knowledge</h1>
              <p>Find top related study notes from students sharing the same course</p>
            </v-col>
          </v-row>
          <v-row>
            <v-col class="text-center">
              <v-text-field
                class="mt-8 search"
                label="Search for documents Books or Quizes"
                outlined
                dense
              ></v-text-field>
              <p>Only the best</p>
            </v-col>
          </v-row>
        </v-container>
      </v-main>
 
      <!-- Bottom Bar -->
      <v-footer app color="grey"  position="relative" class="text-center"> 
        <v-col>
          <v-icon>mdi-youtube</v-icon>
          <v-icon>mdi-twitter</v-icon>
          <v-icon>mdi-facebook</v-icon>
          <v-icon>mdi-instagram</v-icon>
          <v-icon>mdi-linkedin</v-icon>
          <v-icon>mdi-github</v-icon>
          <v-icon>mdi-tiktok</v-icon>
        </v-col>
      </v-footer>
    </v-app>
  </template>
 
  <script>
 
  </script>
 
  <style scoped>
  .v-application {
    background-color: rgb(138, 90, 90);
  }
  .search {
    border:3px rounded rgb(42, 36, 122);
    width:100%;
    height:90px;
    margin:0;
    padding:0;
    font-size:25px;
    border-style: rounded;
  }
  p{
    font-size:30px;
  }
  .heading{
  color:rgb(204, 179, 179);
  font-size:50px;
  }
  .custom-button{
    font-size:15px;
    font-family: 'Times New Roman', Times, serif;
    display: inline-block;
    justify-content: flex-start;
    align-items: space-around;
  }

  </style>