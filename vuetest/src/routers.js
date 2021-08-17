import {createRouter, createWebHashHistory} from "vue-router";
import Home from "./components/Home";
import Login from "./components/Login";
import Person from "./components/Person";

const routers = createRouter({
    history: createWebHashHistory(),
    routes:[
        {path: '/dist/',  redirect: '/Home'},
        {path: '/Login', component: Login},
        {path: '/Home',  component: Home},
        {path: '/Person',  component: Person},
    ]
});

export default routers;