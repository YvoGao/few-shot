import Vue from 'vue'
import VueRouter from "vue-router";
// import Home from "../views/Main.vue";
//路由配置文件
Vue.use(VueRouter)

const routes =[
    // {
    //     path:'/login',
    //     name: 'login',
    //     component:()=>import('../views/login')
    // },
    {
        path:'/',
        name:'main',
        component:()=>import('../views/Main'),
        children:[
            {
                path:'/home',
                name:'home',
                component:()=>import('../views/home/index')
            },
            {
                path: '/text',
                name: '20news',
                component:()=>import('../views/text/20news')
            },
            {
                path: '/text',
                name: 'retuers',
                component:()=>import('../views/text/retuers')
            }
        ]
    },
    {
        path:'/l',
        name: 'test',
        component:()=>import('../views/test'),
    },
    {
        path:'/send',
        name: 'send',
        component:()=>import('../views/send')
    }



]

const router = new VueRouter({
    mode:'hash',
    routes
})

export default router