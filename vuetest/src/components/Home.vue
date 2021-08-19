<template>
  <div style="margin-top: 25px">
    <div v-for="(item, index) in arrayData" :key="index">
      <el-input v-model="item.table" style="margin-left: 20px; width: 200px"></el-input>
      <el-select v-model="item.menu" placeholder="请选择" style="margin-left: 20px">
        <el-option v-for="(item, index) in menus" :key="index" :label="item.label" :value="item.value"></el-option>
      </el-select>
      <el-button style="margin-left: 20px; margin-top: 1px" type="danger" v-on:click="del(index)">-</el-button>
    </div>
    <el-button style="margin-left: 400px; margin-top: 5px" type="primary" v-on:click="add">+</el-button>
    <br>
    <el-button style="margin-left: 200px; margin-top: 10px" type="primary" v-on:click="submit()">提交</el-button>
  </div>
</template>

<script lang="js">
import {defineComponent, reactive, toRefs} from "vue";
import {getTaskNo} from "../intergration/getTaksNo"

export default defineComponent({
  name: "Home",

  setup() {
    const requestData = reactive(
        {
          taskNo: "",
          arrayData: [
            {
              table: "",
              menu: "",
            }
          ],
          dataNum: 0
        }
    );

    const options = reactive({
      menus: [{
          value: '选项1',
          label: '黄金糕'
        }, {
          value: '选项2',
          label: '双皮奶'
        }, {
          value: '选项3',
          label: '蚵仔煎'
        }, {
          value: '选项4',
          label: '龙须面'
        }, {
          value: '选项5',
          label: '北京烤鸭'
        }]
    });

    const add = () => {
      requestData.arrayData.push({
        table: "",
      });
    };

    const del = (index) => {
      if (requestData.arrayData.length <= 1) {
        return false
      } else {
        requestData.arrayData.splice(index, 1)
      }
    };

    const submit = () => {
      requestData.taskNo = getTaskNo();
      console.log(requestData);
    };

    return {
      ...toRefs(requestData),
      ...toRefs(options),
      add,
      del,
      submit,
    };
  },
})
</script>

<style>

</style>