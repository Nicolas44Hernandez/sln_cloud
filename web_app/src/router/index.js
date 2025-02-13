import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/sln',
      name: 'home',
      component: () => import('../views/TrafficView.vue') 
    },
    {
      path: '/sln/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/sln/traffic',
      name: 'traffic',
      component: () => import('../views/TrafficView.vue')
    },
    {
      path: '/sln/noise',
      name: 'login',
      component: () => import('../views/NoiseView.vue')
    }
    // {
    //   path: '/sln/air-stats',
    //   name: 'login',
    //   component: () => import('../views/AirStatsView.vue')
    // }
  ]
})

export default router
