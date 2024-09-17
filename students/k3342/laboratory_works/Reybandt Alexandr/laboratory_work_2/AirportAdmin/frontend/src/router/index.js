import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../components/Login.vue'
import Single from '../views/Single.vue'
import Profile from '../views/Profile.vue'
import Registration from '../components/Registration.vue'
Vue.use(VueRouter)

const routes = [
    {
        path: '/accounts/login',
        name: 'Login',
        component: Login,
        exact: true,
    },
    {
        path: '/profile',
        name: 'Profile',
        component: Profile,
        exact: true,
    },
    {
        path: '/accounts/register',
        name: 'Registration',
        component: Registration,
        exact: true,
    },
    {
        path: '/about',
        name: 'About',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
        exact: true,
    },
    {
        path: '/:id',
        name: 'Single',
        component: Single,
        props: true,
        exact: true,
    },
    {
        path: '/',
        name: 'Home',
        component: Home,
        exact: true,
    },
]

const router = new VueRouter({
    mode: 'history',
    routes
})

export default router
