<template>
    <nav>
        <v-toolbar flat app>
            <v-toolbar-side-icon @click="drawer = !drawer">
                <v-icon>mdi-menu</v-icon>
            </v-toolbar-side-icon>
            <v-toolbar-title class="text-uppercase grey--text">
                <span>Note</span>
                <span class="font-weight-light">Share</span>
            </v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn class="ma-2" color="orange darken-2" @click="drawer = !drawer">
                <v-icon start>mdi-arrow-left</v-icon> Back
            </v-btn>
        </v-toolbar>
        <v-navigation-drawer v-model="drawer" app color="purple">
            <v-list>
                <v-list-item v-for="link in links" :key="link.text" :to="link.route">
                    <v-list-item-action>
                        <v-icon>{{ link.icon }}</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title>{{ link.text }}</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-navigation-drawer>
    </nav>
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
