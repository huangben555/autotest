import {createRouter, createWebHashHistory} from "vue-router";
import Home from "./components/Home";
import Login from "./components/Login";
import Logger from "./components/Logger";

const routers = createRouter({
    history: createWebHashHistory(),
    routes:[
        {path: '',  redirect: '/Home'},
        {path: '/Login', component: Login},
        {path: '/Home',  component: Home},
        {path: '/Logger',  component: Logger},
    ]
});

export default routers;