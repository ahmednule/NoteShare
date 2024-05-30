<template>
  <div>
    <v-app>
      <v-navigation-drawer v-model="drawer" app color="purple">
        <v-list>
          <v-list-item v-for="link in links" :key="link.text" :to="link.route">
            <v-list-item-icon>
              <v-icon>{{ link.icon }}</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>{{ link.text }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>

      <v-app-bar app dark prominent>
        <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
        <v-toolbar-title>NoteShare</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn icon>
          <v-icon>mdi-export</v-icon>
        </v-btn>
      </v-app-bar>
    </v-app>
  </div>
</template>

<script>
export default {
  data() {
    return {
      drawer: false,
      links: [
        { icon: 'mdi-view-dashboard', text: 'Dashboard', route: '/dashboard' },
        { icon: 'mdi-account', text: 'Profile', route: '/profile' },
        { icon: 'mdi-book-search', text: 'Settings', route: '/settings' },
        { icon: 'mdi-logout', text: 'Logout', route: '/logout' }
      ]
    }
  }
}
</script>

<style>
</style>
