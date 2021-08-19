<template>
  <div style="margin-top: 25px">
    <label style="margin-left: 50px;">单号：</label>
    <el-input style="width: 200px" placeholder="输入申请号" v-model="applyNo"></el-input>
    <br>
    <el-button style="margin-left: 165px; margin-top: 50px" type="primary" v-on:click="submit()">提交</el-button>
  </div>
</template>

<script lang="js">
import {defineComponent, reactive, toRefs} from "vue";
import {useStore} from "vuex";
import {getTaskNo} from "../intergration/getTaksNo";

export default defineComponent({
  name: "Person",

  setup() {
    const doApplyInfo = useStore();

    const requestData = reactive({
      applyNo: doApplyInfo.state.applyNo,
    });

    const submit = () => {
      changeApplyInfo();
      requestData.taskNo = getTaskNo();
      console.log(requestData.applyNo);
    };

    const changeApplyInfo = () => {
      doApplyInfo.commit("setData", requestData.applyNo);
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