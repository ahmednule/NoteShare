<<<<<<< HEAD
import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from '../views/LandingPage.vue'
=======
// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import LandingPage from '../views/LandingPage.vue';
import Login from '../components/LoginPage.vue';
import SignUp from '../components/SignUpPage.vue';

>>>>>>> Saisa
const routes = [
  {
    path: '/',
    name: 'LandingPage',
    component: LandingPage
  },
  {
<<<<<<< HEAD
    path: '/home',
    name: 'Home',
    component: () => import('../views/Home.vue'),
=======
    path: '/signup',
    name: 'SignUp',
    component: SignUp,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
>>>>>>> Saisa
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;