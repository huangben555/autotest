<template>
  <ul class="header">
    <li>
      <router-link to="/Home">Home</router-link>
    </li>
    <li>
      <router-link to="/Login">Login</router-link>
    </li>
    <li>
      <router-link to="/Logger">Logger</router-link>
    </li>
  </ul>
  <router-view></router-view>
  <!--  <router-view v-slot="{ Component }">-->
  <!--    <keep-alive>-->
  <!--      <component :is="Component"></component>-->
  <!--    </keep-alive>-->
  <!--  </router-view>-->
</template>

<script lang="js">
import {defineComponent} from "vue";

export default defineComponent({
  name: "App",
  setup() {

  },
})
</script>

<style>
* {
  margin: 0px;
  padding: 0px;
}

.header {
  width: 100%;
  height: 50px;
  background: black;
  list-style: None;
}

.header li {
  text-align: center;
  float: left;
  margin-top: 5px;
  width: 100px;
  font-size: 25px;
}

.header li a {
  color: white;
}

.header li a:hover{
    color: lightslategray;
  }
</style>
