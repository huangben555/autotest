<template>
  <div style="margin-top: 25px">
    <label style="margin-left: 50px;">单号：</label>
    <el-input style="width: 200px;" placeholder="输入申请号" v-model="applyNo"></el-input>
    <br>
    <br>
    <label style="margin-left: 50px;">账号：</label>
    <el-input style="width: 200px;" v-model="account"></el-input>
    <label style="margin-left: 200px;">密码：</label>
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
import {useStore} from "vuex";
import {postHeaders} from "../intergration/requestHeaders";

export default defineComponent({
  name: "Login",

  setup() {
    const applyInfo = useStore();

    const requestData = reactive({
      applyNo: applyInfo.state.applyNo,
      account: "",
      password: "",
    });

    const Status = reactive({
      buttonLoading: false,
      requestStatus: "未进行",
    });

    const requestConfig = {
      url: "http://192.168.43.187:9999/login/",
      method: "post",
      headers: postHeaders,
      data: requestData,
    };

    const submit = () => {
      console.log(requestData)
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
          .finally(function () {
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