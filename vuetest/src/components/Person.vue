<template>
  <div style="margin-top: 25px">
    <label style="margin-left: 50px;">单号：</label>
    <el-input style="width: 200px" placeholder="输入申请号" v-model="applyNo" v-on:keypress="changeApplyInfo"></el-input>
    <br>
    <el-button style="margin-left: 165px; margin-top: 50px" type="primary" v-on:click="submit()">提交</el-button>
  </div>
</template>

<script lang="js">
import {defineComponent, reactive, toRefs} from "vue";
import {useStore} from "vuex";
import {getTaskNo} from "../intergration/getNowTime";

export default defineComponent({
  name: "Person",

  setup() {
    const applyInfo = useStore();

    const requestData = reactive({
      applyNo: applyInfo.state.applyNo,
    });

    const submit = () => {
      requestData.taskNo = getTaskNo();
      console.log(requestData.applyNo);
      applyInfo.commit("setData", requestData.applyNo);
    };

    const changeApplyInfo = () => {

    }

    return {
      ...toRefs(requestData),
      submit,
      changeApplyInfo,
    };
  }
})
</script>

<style>

</style>