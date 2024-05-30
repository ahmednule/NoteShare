<template>
  <v-container class="dashboard app" style="position: fixed; top: 70px; left: 20px; right: 20px;">
    <h1 class="sub-heading grey--text text-left">Dashboard</h1>
    <v-btn class="mb-4" width=10000 color="grey" @click="searchDocuments">Search for your documents</v-btn>
  
    <v-row justify="center">
      <v-col cols="12" sm="6" md="4" lg="3" v-for="pdf in pdfs" :key="pdf.id" class="d-flex">
        <v-card class="mx-auto" max-width="344">
          <v-img :src="pdf.image" height="200px"></v-img>
          <v-card-title>{{ pdf.title }}</v-card-title>
          <v-card-subtitle>{{ pdf.subtitle }}</v-card-subtitle>
          <v-card-actions>
            <v-btn text>View</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      pdfs: [
        { id: 1, image: 'https://via.placeholder.com/150?text=PDF+1', title: 'PDF Title 1', subtitle: 'Subtitle 1' },
        { id: 2, image: 'https://via.placeholder.com/150?text=PDF+2', title: 'PDF Title 2', subtitle: 'Subtitle 2' },
        { id: 3, image: 'https://via.placeholder.com/150?text=PDF+3', title: 'PDF Title 3', subtitle: 'Subtitle 3' },
        { id: 4, image: 'https://via.placeholder.com/150?text=PDF+4', title: 'PDF Title 4', subtitle: 'Subtitle 4' }
      ]
    }
  },
  methods: {
    searchDocuments() {
      
    }
  }
}
</script>

<style scoped>
.dashboard {
  background-color: #f5f5f5;
  padding-top: 20px;
}
.sub-heading {
  font-size: 24px;
  font-weight: 400;
  margin-bottom: 20px;
}
</style>
