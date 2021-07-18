<template>
  <div class="Login_class" style="margin-top: 50px">
    <label>请输入账号：</label>
    <el-input class="input_account" style="width: 200px;" v-model="requestData.account"></el-input>
    <label style="margin-left: 200px;">请输入密码：</label>
    <el-input class="input_account" style="width: 200px;" v-model="requestData.password"></el-input>
    <br>
    <el-button style="margin-left: 240px; margin-top: 50px;" v-on:click="submit">提交</el-button>
  </div>
</template>

<script lang="js">
import {defineComponent, reactive} from "vue";
import requestPost from "../requests";

export default defineComponent({
  name: "Login",
  setup() {
    return {
      requestData: reactive(
          {account: "", password: ""}
      ),
    };
  },
  methods: {
    submit() {
      requestPost("http://www.mockbin.com/har", this.requestData);
    }
  }
})
</script>

<style>

</style>