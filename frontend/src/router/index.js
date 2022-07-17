import { createRouter, createWebHashHistory } from 'vue-router'


const routes = [
  {
    path:'/',
    component:()=>{return import('../views/Main.vue')}
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
