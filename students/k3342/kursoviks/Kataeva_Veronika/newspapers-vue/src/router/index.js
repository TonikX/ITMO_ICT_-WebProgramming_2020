import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Login from '@/components/Login'
import SignUp from '@/components/SignUp'
import MainPage from '@/components/MainPage'
import Request1 from '@/components/Request1'
import Request2 from '@/components/Request2'
import Request3 from '@/components/Request3'
import Request4 from '@/components/Request4'
import Request5 from '@/components/Request5'
import Report from '@/components/Report'
import Certificate from '@/components/Certificate'
import Offices from '@/components/Offices'
import Newspapers from '@/components/Newspapers'
import Editors from '@/components/Editors'
import PrintingHouses from '@/components/PrintingHouses'
import InStocks from '@/components/InStocks'
import MuseUI from 'muse-ui';
import 'muse-ui/dist/muse-ui.css';

Vue.use(MuseUI);
Vue.use(Router)

export default new Router({
  routes: [
      {
      path: '/',
      name: 'mainpage',
      component: MainPage
    },
    {
      path: '/home',
      name: 'home',
      component: Home
    },
    {
      path: '/login',
      name: 'login',
      component: Login
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
    {
      path: '/report',
      name: 'report',
      component: Report
    },
    {
      path: '/certificate',
      name: 'certificate',
      component: Certificate
    },
    {
      path: '/offices',
      name: 'offices',
      component: Offices
    },
    {
      path: '/newspapers',
      name: 'newspapers',
      component: Newspapers
    },
    {
      path: '/editors',
      name: 'editors',
      component: Editors
    },
    {
      path: '/printinghouses',
      name: 'printinghouses',
      component: PrintingHouses
    },
    {
      path: '/instocks',
      name: 'instocks',
      component: InStocks
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUp
    },
  ]
})
