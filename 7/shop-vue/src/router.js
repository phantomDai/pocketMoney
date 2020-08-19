import Vue from 'vue'
import Router from 'vue-router'
import Index from './views/index'
import Login from './views/login'
import User from './views/user'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/user',
      name: 'User',
      component: User
    },
  ]
})
