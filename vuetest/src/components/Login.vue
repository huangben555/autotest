<template>
  <div class="Login_class" style="margin-top: 50px">
    <label style="margin-left: 50px;">请输入账号：</label>
    <el-input style="width: 200px;" v-model="requestData.account"></el-input>
    <label style="margin-left: 200px;">请输入密码：</label>
    <el-input style="width: 200px;" v-model="requestData.password"></el-input>
    <br>
    <el-button style="margin-left: 290px; margin-top: 50px;" v-on:click="submit()" :loading="requestData.buttonLoading">
      提交
    </el-button>
  </div>
</template>

<script lang="js">
import {defineComponent, reactive} from "vue";

export default defineComponent({
  name: "Login",
  setup() {
    const requestData = reactive(
        {
          account: "",
          password: "",
          buttonLoading: false,
        }
    );

    const submit = () => {
      requestData.buttonLoading = true;
      this.request({
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
            }
            setTimeout(function () {
              requestData.buttonLoading = false;
            }, 6000)
          });
    };

    return {
      requestData,
      submit,
    };
  },
  methods: {}
})
</script>

<style>

</style>