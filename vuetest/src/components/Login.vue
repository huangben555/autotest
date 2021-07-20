<template>
  <div class="Login_class" style="margin-top: 50px">
    <label style="margin-left: 50px;">请输入账号：</label>
    <el-input style="width: 200px;" v-model="account"></el-input>
    <label style="margin-left: 200px;">请输入密码：</label>
    <el-input style="width: 200px;" v-model="password"></el-input>
    <br>
    <el-button style="margin-left: 290px; margin-top: 50px;" v-on:click="submit()" :loading="buttonLoading">
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

    const controlStatus = reactive({
      buttonLoading: false,
    });

    const submit = () => {
      controlStatus.buttonLoading = true;
      request({
        url: "http://10.0.0.7:9999/login/",
        method: "POST",
        json: true,
        headers: {
          "content-type": "application/json",
        },
        body: JSON.stringify(requestData)
      }, function (error, response, body) {
        if (!error && response.statusCode == 200) {
          console.log(body) // 请求成功的处理逻辑
        }
        setTimeout(function () {
          controlStatus.buttonLoading = false;
        }, 6000)
      });
    };

    return {
      ...toRefs(requestData),
      ...toRefs(controlStatus),
      submit,
    };
  },
  methods: {}
})
</script>

<style>

</style>