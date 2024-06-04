<template>
    <v-app>
      <v-container>
        <v-row class="text-center">
          <v-col>
            <h1>Welcome to NoteShare</h1>
          </v-col>
        </v-row>
  
        <v-row>
          <v-col>
            <v-card class="pa-5" outlined>
              <v-card-title>
                <v-icon left>mdi-account</v-icon>
                <span>User Profile</span>
              </v-card-title>
              <v-card-subtitle>
                <v-btn color="primary" @click="$router.push({name: 'profile'})">
                    Go to Profile
                </v-btn>
              </v-card-subtitle>
            </v-card>
          </v-col>
        </v-row>
  
        <v-row>
          <v-col>
            <v-card class="pa-5" outlined>
              <v-card-title>Education Levels</v-card-title>
              <v-card-subtitle>University, High School, College</v-card-subtitle>
              <v-list>
                <v-list-item v-for="(subject, index) in subjects" :key="index">
                  <v-list-item-content>
                    <v-list-item-title>{{ subject }}</v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-card>
          </v-col>
        </v-row>
  
        <v-row>
          <v-col>
            <v-card class="pa-5" outlined>
              <v-card-title>Upload Notes</v-card-title>
              <v-file-input
                v-model="noteFile"
                label="Upload your notes"
                prepend-icon="mdi-upload"
                outlined
                @change="uploadNotes"
              ></v-file-input>
            </v-card>
          </v-col>
  
          <v-col>
            <v-card class="pa-5" outlined>
              <v-card-title>Access Uploaded Notes</v-card-title>
              <v-btn color="primary" @click="accessNotes">View Notes</v-btn>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-app>
  </template>
  
  <script>
  export default {
    data() {
      return {
        subjects: ['Math', 'Science', 'History', 'Literature', 'Physics', 'Chemistry'],
        noteFile: null,
      };
    },
    methods: {
      goToProfile() {
        this.$router.push({ name: 'Profile' });
      },
      uploadNotes() {
        // Logic for uploading notes
        console.log('Uploading notes:', this.noteFile);
      },
      accessNotes() {
        // Logic for accessing uploaded notes
        this.$router.push({ name: 'Notes' });
      },
    },
  };
  </script>
  
  <style scoped>
  .v-container {
    max-width: 800px;
    margin: auto;
  }
  
  .v-card {
    margin-bottom: 20px;
  }
  
  .v-card-title {
    font-weight: bold;
    color: #1976D2;
  }
  
  .v-card-subtitle {
    color: #424242;
  }
  
  .v-btn {
    margin-top: 10px;
  }
  </style>
  