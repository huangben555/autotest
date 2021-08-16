<template>
  <div class="Login_class" style="margin-top: 50px">
    <v-person></v-person>
  </div>
  <div class="Login_class" style="margin-top: 50px">
    <label style="margin-top: 100px; margin-left: 50px;">请输入账号：</label>
    <el-input style="width: 200px;" v-model="account"></el-input>
    <label style="margin-left: 200px;">请输入密码：</label>
    <el-input style="width: 200px;" v-model="password"></el-input>
    <p style="margin-left: 780px; margin-top: 50px;">{{ requestStatus }}</p>
    <br>
    <el-button style="margin-left: 400px; margin-top: 20px;" v-on:click="submit()" :loading="buttonLoading">
      提交
    </el-button>
  </div>
</template>

<script lang="js">
import {defineComponent, reactive, toRefs} from "vue";
import axios from "axios";
import {postHeaders} from "../intergration/requestHeaders";
import Person from "./Person";

export default defineComponent({
  name: "Login",

  components:{
  "v-person": Person
},

  setup() {
    const requestData = reactive({
      name: "",
      account: "",
      password: "",
    });

    const Status = reactive({
      buttonLoading: false,
      requestStatus: "未进行",
    });

    const requestConfig = {
      url: "http://127.0.0.1:9999/login/",
      method: "post",
      headers: postHeaders,
      data: requestData,
    };

    const submit = () => {
      Status.buttonLoading = true;
      Status.requestStatus = "请求中";
      axios.request(requestConfig)
          .then(function (response) {
            if (response.status == 200 && response.data != null) {
              Status.requestStatus = "请求成功";
            } else {
              Status.requestStatus = "请求失败";
            }
          })
          .catch(function (error) {
            console.log(error)
          })
          .finally(function (){
            Status.buttonLoading = false;
          })
    };

    return {
      ...toRefs(requestData),
      ...toRefs(Status),
      submit,
    };
  },
})
</script>

<style>

</style>