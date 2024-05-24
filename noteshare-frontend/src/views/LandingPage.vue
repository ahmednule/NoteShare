<!-- src/views/LandingPage.vue -->
<template>
  <v-app>
    <!-- Navbar -->
    <v-app-bar app color="black" dark>
      <v-icon color="yellow" left class="mr-2">fas fa-signature</v-icon>NOTESHARE
      <v-spacer></v-spacer>
      <v-btn text>
        <router-link to="/profile" class="white">Profile</router-link>
      </v-btn>
      <v-btn text>
        <router-link to="/about" class="white">About Us</router-link>
      </v-btn>
      <v-btn text>
        <router-link to="/signup" class="white">Sign Up</router-link>
      </v-btn>
      <v-btn text>
        <router-link to="/login" class="white">Login</router-link>
      </v-btn>
    </v-app-bar>
    
    <!-- Body -->
    <v-main>
      <v-container class="grey lighten-3 py-16">
        <v-row>
          <v-col class="text-center">
            <v-btn color="black" class="ma-2">University</v-btn>
            <v-btn color="black" class="ma-2">College</v-btn>
            <v-btn color="black" class="ma-2">High School</v-btn>
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
export default {
  name: 'LandingPage',
  methods: {
    goToProfile() {
      this.$router.push({ name: 'Profile' });
    },
    goToAboutUs() {
      this.$router.push({ name: 'AboutUs' });
    }
  }
};
</script>

<style scoped>
.v-application {
  background-color: #584e4e;
}
.v-btn .router-link-active {
  text-decoration: none;
  color: inherit;
}
</style>
