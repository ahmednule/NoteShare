// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import LandingPage from '../views/LandingPage.vue';
import Login from '../components/LoginPage.vue';
import SignUp from '../components/SignUpPage.vue';
import Homepage from '../components/Homepage.vue';
import ProfilePage from '../views/Profilepage.vue';

const routes = [
  {
    path: '/',
    name: 'LandingPage',
    component: LandingPage
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/home',
    name: 'Home',
    component: Homepage,
    meta: { requiresAuth: true},
  },
  {
    path: '/profile',
    name: 'Profile',
    component: ProfilePage,
    meta: { requiresAuth: true },
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

//Navigation to check for authentication
//router.beforeEach((to, from, next)=> {
// const loggedin = !!localstorage.getitem('user');

// if (to.matched.some(record => record.mata.requiresAuth) && !loggedIn) {
// next({name: 'Login'});
// }else {
// next();
//}
router.beforeEach((to, from, next) => {
  if (typeof window !== 'undefined') {
    const loggedIn = !!localStorage.getItem('user'); // Ensure localStorage is defined
    if (to.matched.some(record => record.meta.requiresAuth) && !loggedIn) {
      next({ name: 'Login' });
    } else {
      next();
    }
  } else {
    next();
  }

});


export default router;