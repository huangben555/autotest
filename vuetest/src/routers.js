import {createRouter, createWebHistory} from "vue-router";
import Home from "./components/Home";
import Login from "./components/Login";

const routers = createRouter({
    history: createWebHistory(),
    routes:[
        {path: '/',  redirect: '/Home'},
        {path: '/Home',  component: Home},
        {path: '/Login', component: Login},
    ]
});

export default routers;