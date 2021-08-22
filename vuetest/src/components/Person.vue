<template>
  <el-form style="margin-top: 25px" :rules="dataRules" :model="requestData" ref="loginFormRef" label-width="75px">
    <el-form-item label="单号" prop="applyNo">
      <el-input style="width: 500px" placeholder="输入申请号" v-model="requestData.applyNo"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" v-on:click="submit('requestData')">提交</el-button>
      <el-button v-on:click="resetForm(requestData)">重置</el-button>
    </el-form-item>
  </el-form>
</template>

<script lang="js">
import {defineComponent, reactive, ref} from "vue";
import {useStore} from "vuex";
import {getTaskNo} from "../intergration/getTaksNo";

export default defineComponent({
  name: "Person",

  setup() {
    const doApplyInfo = useStore();

    const loginFormRef = ref();

    const requestData = reactive({
      applyNo: doApplyInfo.state.applyNo,
    });

    const dataRules = reactive({
      applyNo: [
        {required: true, message: "请输入活动名称", trigger: 'blur'},
        {max: 10, min: 5, message: "请输入5-10个字符", trigger: 'blur'},
      ],
    });

    const submit = async() => {
      requestData.taskNo = getTaskNo();
      if (!dataRules.value) return;
      await dataRules.value.validate((valid) => {
        console.log(valid)
      })
      // $this.ref.requestData.validate((valid) => {
      //   if (valid) {
      //     console.log(formName);
      //   } else {
      //     console.log("error");
      //   }
      // });
    };

    const changeApplyInfo = () => {
      doApplyInfo.commit("setData", requestData.applyNo);
    }

    return {
      requestData,
      submit,
      changeApplyInfo,
      dataRules,
      loginFormRef,
    };
  }
})
</script>

<style>

</style>