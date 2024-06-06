<template>
  <v-app class="gradient-container">
    <v-container class="gradient-container">
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
              <v-btn color="primary" @click="goToProfile">
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
            <v-card-subtitle>
              <v-btn text  class="ma-2">
                <router-link to="/University" color="primary" class="white--text">University</router-link>
              </v-btn>
              <v-btn text>
                <router-link to="/Highschool" color="primary" class="blue--text">High School</router-link>
              </v-btn>
              <v-btn text>
                <router-link to="/College" color="primary" class="white--text">College</router-link>
              </v-btn>
            </v-card-subtitle>
          </v-card>
        </v-col>
      </v-row>

      <v-row class="gradient-container">
        <v-col v-for="(subject, index) in subjects" :key="index" cols="12" sm="6" md="4">
          <v-card class="pa-5" outlined @click="viewNotes(subject)">
            <v-card-title>{{ subject }}</v-card-title>
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
      subjects: ['Math', 'Science', 'History', 'Literature', 'Physics', 'Chemistry', 'Philosophy'],
      noteFile: null,
    };
  },
  methods: {
    goToProfile() {
      this.$router.push({ name: 'Profile' });
    },
    selectLevel(level) {
      // Handle level selection
      console.log('Selected level:', level);
    },
    viewNotes(subject) {
      // Navigate to notes view for the selected subject
      console.log('Viewing notes for subject:', subject);
      this.$router.push({ name: 'Notes', params: { subject } });
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
.homepage-container {
  max-width: 1200px;
  margin: auto;
  background-color: #f5f5f5;
  padding: 20px;
  border-radius: 8px;
}

.v-card {
  margin-bottom: 20px;
  cursor: pointer;
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

.text-center {
  margin-bottom: 20px;
}

.pa-5 {
  padding: 20px;
}
.custom-container {
  background-color:#055e64;
  padding: 20px;
}
.custom-footer {
  background-color: linear-gradient( to right, #055e64, rgb(38, 70, 10));
  padding: 20px;
}
.gradient-container {
  background: linear-gradient(to right, #8ecece, rgb(37, 69, 78));
  padding: 20px;
}
</style>