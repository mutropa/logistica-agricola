import { createRouter, createWebHistory } from 'vue-router'

import Home from '../components/Home.vue'
import Login from '../components/Login.vue'
import Registo from '../components/Registo.vue'

// Layouts
import ProdutorLayout from '../paginas/ProdutorLayout.vue'
import CompradorLayout from '../paginas/CompradorLayout.vue'
import TransportadorLayout from '../paginas/TransportadorLayout.vue'

// Dashboards
import ProdutorDashboard from '../components/produtor/Dashboard.vue'
import CompradorDashboard from '../components/comprador/Dashboard.vue'
import TransportadorDashboard from '../components/transportador/Dashboard.vue'

const requireAuth = (to, from, next) => {
  const token = localStorage.getItem('access')
  if (token) {
    next()
  } else {
    next('/login')
  }
}

const routes = [
  { path: '/', component: Home },
  { path: '/login', component: Login },
  { path: '/registar', component: Registo },

  {
    path: '/produtor',
    component: ProdutorLayout,
    beforeEnter: requireAuth,
    children: [
      { path: 'dashboard', name: 'ProdutorDashboard', component: ProdutorDashboard }
    ]
  },
  {
    path: '/comprador',
    component: CompradorLayout,
    beforeEnter: requireAuth,
    children: [
      { path: 'dashboard', name: 'CompradorDashboard', component: CompradorDashboard}
    ]
  },
  {
    path: '/transportador',
    component: TransportadorLayout,
    beforeEnter: requireAuth,
    children: [
      { path: 'dashboard', name: 'TransportadorDashboard', component:TransportadorDashboard }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router
