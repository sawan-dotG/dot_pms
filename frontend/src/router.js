import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('./pages/Home.vue'),
  },
  {
    path: '/okr',
    name: 'OKR',
    component: () => import('./pages/OKR.vue'),
  },
  {
    path: '/feedback',
    name: 'Feedback',
    component: () => import('./pages/Feedback.vue'),
  },
  {
    path: '/1on1',
    name: 'OneOnOne',
    component: () => import('./pages/OneOnOne.vue'),
  },
]

let router = createRouter({
  history: createWebHistory('/pms_space'),
  routes,
})

export default router
