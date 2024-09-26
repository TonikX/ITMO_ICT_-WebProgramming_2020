import Vue from 'vue'
import Router from 'vue-router'
import Home from '../components/Home'
import login from '../components/login'
import Clients_view from '../components/rooms/Clients_view'
import Workers_view from '../components/rooms/Workers_view'
import Add_checkin from "../components/rooms/Add_checkin";
import ChangeTT from "../components/rooms/ChangeTT";
import AddClient from "../components/rooms/AddClient";
import Client_filter from "../components/rooms/Client_filter";
import Find_worker from "../components/rooms/Find_worker";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/login',
      name: 'login',
      component: login
    },
    {
      path: '/clients',
      name: 'Clients_view',
      component: Clients_view
    },
    {
      path: '/workers',
      name: 'Workers_view',
      component: Workers_view
    },
    {
      path: '/add_checkin',
      name: 'Add_checkin',
      component: Add_checkin
    },
    {
      path: '/add_client',
      name: 'AddClient',
      component: AddClient
    },
    {
      path: '/change_timetable',
      name: 'ChangeTT',
      component: ChangeTT
    },
    {
      path: '/find_worker',
      name: 'Find_worker',
      component: Find_worker
    },
    {
      path: '/client_filt',
      name: 'Client_filter',
      component: Client_filter
    }
  ]
})
