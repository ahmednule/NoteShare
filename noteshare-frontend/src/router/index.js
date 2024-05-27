import { createRouter, createWebHistory } from 'vue-router'
import LogoutView from '../views/LogoutView.vue'
import DashboardView from '../views/DashboardView.vue'
import SearchView from '../views/SearchView.vue'
import SettingView from '../views/SettingView.vue'
import ProfileView from '../views/ProfileView.vue'



const routes = [
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: DashboardView
  },
  {
    path: '/search',
    name: 'search',
    component: SearchView
  },
  {
path: '/settings',
name: 'settings',
component: SettingView
  },
  {
  path: '/profile',
name: 'profile',
component: ProfileView
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
