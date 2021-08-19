import { createApp } from 'vue'
import ElementPlus from 'element-plus';
import 'element-plus/lib/theme-chalk/index.css';
import App from './App.vue';
import routers from "./routers";
import {doApplyInfo} from "./intergration/doApplyInfo";

const app = createApp(App);

app.use(ElementPlus, {size: 'mini'});
app.use(routers);
app.use(doApplyInfo);
app.mount('#app');