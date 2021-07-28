import {createRouter, createWebHashHistory} from "vue-router";
import Home from "./components/Home";
import Login from "./components/Login";

const routers = createRouter({
    history: createWebHashHistory(),
    routes:[
        {path: '/',  redirect: '/Home'},
        {path: '/dist',  redirect: '/Home'},
        {path: '/Login', component: Login},
        {path: '/Home',  component: Home},
    ]
});

export default routers;