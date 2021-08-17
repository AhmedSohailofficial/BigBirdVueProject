import Vue from 'vue'
import VueRouter from 'vue-router'
// import Home from '../views/Home.vue'

import LandingPage from '../components/LandingPage.vue'
import SecondPage from '../components/SecondPage.vue'
import ThirdPage from '../components/ThirdPage.vue'
import FourPage from '../components/FourPage.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'LandingPage',
    component: LandingPage
  },
  {
    path: '/products',
    name: 'Products',
    component: SecondPage
  },
  {
    path: '/oneproduct/:id',
    name: 'OneProduct',
    component: ThirdPage
  },
  {
    path: '/contact',
    name: 'Contact',
    component: FourPage
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
