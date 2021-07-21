<template>
  <div class="Login_class" style="margin-top: 50px">
    <label style="margin-left: 50px;">请输入账号：</label>
    <el-input style="width: 200px;" v-model="account"></el-input>
    <label style="margin-left: 200px;">请输入密码：</label>
    <el-input style="width: 200px;" v-model="password"></el-input>
    <p style="margin-left: 780px; margin-top: 50px;">{{ requestStatus }}</p>
    <br>
    <el-button style="margin-left: 400px; padding-top: 20px;" v-on:click="submit()" :loading="buttonLoading">
      提交
    </el-button>
  </div>
</template>

<script lang="js">
import {defineComponent, reactive, toRefs} from "vue";
import request from "request";

export default defineComponent({
  name: "Login",
  setup() {
    const requestData = reactive({
      account: "",
      password: "",
    });

    const Status = reactive({
      buttonLoading: false,
      requestStatus: "未进行",
    });

    const submit = () => {
      Status.buttonLoading = true;
      Status.requestStatus = "请求中";
      request({
        url: "http://192.168.43.187:9999/login/",
        method: "POST",
        json: true,
        headers: {
          "content-type": "application/json",
        },
        body: JSON.stringify(requestData)
      }, function (error, response) {
        if (!error && response.statusCode == 200) {
          setTimeout(function () {
            Status.buttonLoading = false;
            Status.requestStatus = "请求成功";
          }, 6000);
        }
        else {
          Status.requestStatus = "请求失败";
        }
      });
    };

    return {
      ...toRefs(requestData),
      ...toRefs(Status),
      submit,
    };
  },
  methods: {}
})
</script>

<style>

</style>