<template>
    <v-container class="profile-container">
      <v-row>
        <v-col cols="12" md="4">
          <v-card>
            <v-card-title class="justify-center">
              <h2>Profile</h2>
            </v-card-title>
            <v-card-text>
              <div class="profile-details">
                <p><strong>Name:</strong> {{ user.name }}</p>
                <p><strong>Email:</strong> {{ user.email }}</p>
                <p><strong>Level:</strong> {{ user.level }}</p>
                <p><strong>Subjects:</strong></p>
                <v-chip-group
                  v-if="user.subjects && user.subjects.length"
                  column
                  mandatory
                  multiple
                >
                  <v-chip
                    v-for="(subject, index) in user.subjects"
                    :key="index"
                    class="ma-2"
                  >
                    {{ subject }}
                  </v-chip>
                </v-chip-group>
              </div>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col cols="12" md="8">
          <v-card>
            <v-tabs v-model="tab" grow>
              <v-tab>Upload Notes</v-tab>
              <v-tab>Access Notes</v-tab>
            </v-tabs>
            <v-tabs-items v-model="tab">
              <v-tab-item>
                <v-card-text>
                  <v-form @submit.prevent="uploadNotes">
                    <v-file-input
                      v-model="noteFile"
                      label="Upload Notes"
                      required
                    ></v-file-input>
                    <v-btn type="submit" color="primary">Upload</v-btn>
                  </v-form>
                </v-card-text>
              </v-tab-item>
              <v-tab-item>
                <v-card-text>
                  <!-- Replace with actual notes list rendering -->
                  <v-list>
                    <v-list-item
                      v-for="note in notes"
                      :key="note.id"
                    >
                      <v-list-item-content>
                        <v-list-item-title>{{ note.title }}</v-list-item-title>
                        <v-list-item-subtitle>{{ note.description }}</v-list-item-subtitle>
                      </v-list-item-content>
                    </v-list-item>
                  </v-list>
                </v-card-text>
              </v-tab-item>
            </v-tabs-items>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script>
  export default {
    name: 'ProfilePage',
    data() {
      return {
        tab: null,
        user: {
          name: 'John Doe',
          email: 'john.doe@example.com',
          level: 'University',
          subjects: ['Mathematics', 'Physics', 'Chemistry']
        },
        noteFile: null,
        notes: [
          { id: 1, title: 'Calculus Notes', description: 'Chapter 1 - Limits' },
          { id: 2, title: 'Physics Notes', description: 'Chapter 3 - Motion' },
          { id: 3, title: 'Chemistry Notes', description: 'Chapter 5 - Organic Chemistry' }
        ]
      };
    },
    methods: {
      uploadNotes() {
        // Mock upload logic, replace with actual API call
        alert('Notes uploaded successfully!');
      }
    }
  }
  </script>
  
  <style scoped>
  .profile-container {
    padding: 20px;
  }
  
  .profile-details {
    margin-bottom: 20px;
  }
  
  .v-card-title {
    justify-content: center;
  }
  
  .v-card-text {
    text-align: center;
  }
  
  .v-btn {
    margin-top: 10px;
  }
  </style>
  