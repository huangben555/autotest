<template>
  <div class="Login_class" style="margin-top: 50px">
    <label>请输入账号：</label>
    <el-input class="input_account" style="width: 200px;" v-model="requestData.account"></el-input>
    <label style="margin-left: 200px;">请输入密码：</label>
    <el-input class="input_account" style="width: 200px;" v-model="requestData.password"></el-input>
    <br>
    <el-button style="margin-left: 240px; margin-top: 50px;" v-on:click="submit()">提交</el-button>
  </div>
</template>

<script lang="js">
import {defineComponent, reactive} from "vue";
import request from "request";


export default defineComponent({
  name: "Login",
  setup() {
    const requestData = reactive(
          {
            account: "",
            password: "",
          }
      );

    const submit = ()=> {
      request({
            url: "http://www.mockbin.com/hars",
            method: "POST",
            json: true,
            headers: {
                "content-type": "application/json",
            },
            body: JSON.stringify(requestData)
        },
        function (error, response) {
            if (!error && response.statusCode == 200) {
                console.log("response.statusCode: ", response.statusCode); // 请求成功的处理逻辑
                requestData.account = "graesegesgr";
            }
        });
    };

    return {
      requestData,
      submit,
    };
  },
  methods: {

  }
})
</script>

<style>

</style>