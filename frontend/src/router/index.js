import { createRouter, createWebHistory } from 'vue-router'
import UserTable from '../components/UserTable.vue'
import PageNavigation from '../components/PageNavigation.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [

    {
      path: '/',
      name: 'Users',
      component: UserTable
    },
    {
      path: '/',
      name: 'PageNavigation',
      component: PageNavigation
    }
  ]
})

export default router
