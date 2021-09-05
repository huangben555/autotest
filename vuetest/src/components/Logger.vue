<template>
  <el-form style="margin-top: 25px" :rules="dataRules" :model="requestData" ref="personFormRef" label-width="75px">
    <el-form-item label="单号" prop="applyNo">
      <el-input style="width: 500px" placeholder="输入申请号" v-model="requestData.applyNo"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" v-on:click="submit('requestData')" :loading="Status.buttonLoading">提交</el-button>
      <el-button type="warning" v-on:click="resetForm(requestData)">重置</el-button>
      <el-tag style="margin-left: 330px" type="">{{Status.requestStatus}}</el-tag>
    </el-form-item>
  </el-form>
  <ul class="infinite-list" v-infinite-scroll="load" style="overflow: auto">
    <li v-for="item in responseData" v-bind:key="item" class="infinite-list-item">{{item}}</li>
  </ul>
</template>

<script lang="js">
import {defineComponent, reactive, ref} from "vue";
import {useStore} from "vuex";
import axios from "axios";
import {postHeaders} from "../intergration/requestHeaders";

export default defineComponent({
  name: "Logger",

  setup() {
    const doApplyInfo = useStore();

    const personFormRef = ref();

    const requestData = reactive({
      applyNo: doApplyInfo.state.applyNo,
    });

    const responseData = reactive({
      logData: "",
    })

    const dataRules = reactive({
      applyNo: [
        {required: true, message: "请输入活动名称", trigger: 'blur'},
        {max: 10, min: 5, message: "请输入5-10个字符", trigger: 'blur'},
      ],
    });

    const requestConfig = {
      url: "http://127.0.0.1:9999/login/",
      method: "post",
      headers: postHeaders,
      data: requestData,
    };

    const Status = reactive({
      buttonLoading: false,
      requestStatus: "未进行",
    });

    const submit = () => {
      personFormRef.value.validate((valid) => {
        if (valid) {
          console.log("Validation Success!");
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
        } else {
          console.log("Validation Error!");
        }
      })
    };

    const resetForm = () => {
      personFormRef.value.resetFields();
    };

    const changeApplyInfo = () => {
      doApplyInfo.commit("setData", requestData.applyNo);
    };

    const load = () => {

    }

    return {
      requestData,
      submit,
      changeApplyInfo,
      dataRules,
      personFormRef,
      resetForm,
      Status,
      responseData,
      load,
    };
  }
})
</script>

<style>

</style>