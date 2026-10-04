import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
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
    }
  ],
})

export default router
