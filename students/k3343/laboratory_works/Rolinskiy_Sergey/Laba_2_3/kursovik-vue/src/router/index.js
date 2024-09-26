import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/components/Main'
import Home from '@/components/Home'
import Rooms from '@/components/Rooms'
import Clients from '@/components/Clients'
import Workers from '@/components/Workers'
import Worktable from '@/components/Worktable'
import Journal from '@/components/Journal'
import Report from '@/components/Report'
import Request1 from '@/components/Request1'
import Request2 from '@/components/Request2'
import Request3 from '@/components/Request3'
import Request4 from '@/components/Request4'
import Request5 from '@/components/Request5'
import Login from '@/components/Login'
import MuseUI from 'muse-ui';
import 'muse-ui/dist/muse-ui.css';

Vue.use(Router)
Vue.use(MuseUI);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/main',
      name: 'main',
      component: Main
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/rooms',
      name: 'rooms',
      component: Rooms
    },
    {
      path: '/clients',
      name: 'clients',
      component: Clients
    },
    {
      path: '/workers',
      name: 'workers',
      component: Workers
    },
    {
      path: '/worktable',
      name: 'worktable',
      component: Worktable
    },
    {
      path: '/journal',
      name: 'journal',
      component: Journal
    },
    {
      path: '/report',
      name: 'report',
      component: Report
    },
    {
      path: '/request1',
      name: 'request1',
      component: Request1
    },
    {
      path: '/request2',
      name: 'request2',
      component: Request2
    },
    {
      path: '/request3',
      name: 'request3',
      component: Request3
    },
    {
      path: '/request4',
      name: 'request4',
      component: Request4
    },
    {
      path: '/request5',
      name: 'request5',
      component: Request5
    },

  ]
})
