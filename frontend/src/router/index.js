import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from '../views/LandingPage.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
<<<<<<< Updated upstream
      path: '/approach',
      name: 'approach',
      component: () => import('../views/ApproachPage.vue'),
    },
    {
      path: '/timeline',
      name: 'timeline',
      component: () => import('../views/TimelinePage.vue'),
    },
    {
      path: '/application',
      name: 'application',
      component: () => import('../views/ApplicationPage.vue'),
    },
    {
      path: '/faqs',
      name: 'faqs',
      component: () => import('../views/faqsPage.vue'),
=======
      path: "",
      name: "LandingPage",
      component: LandingPage
>>>>>>> Stashed changes
    }
  ],
})

export default router
