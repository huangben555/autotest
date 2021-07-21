<template>
  <div>
    <div v-for="(item, index) in arrayData" :key="index">
      <el-input v-model="item.data" style="margin-left: 20px; width: 200px"></el-input>
      <el-button style="margin-left: 20px; margin-top: 1px" type="danger" v-on:click="del(index)">-</el-button>
    </div>
    <el-button style="margin-left: 400px; margin-top: 5px" type="primary" v-on:click="add">+</el-button>
  </div>
</template>

<script lang="js">
import {defineComponent, reactive, toRefs} from "vue";

export default defineComponent({
  name: "Home",
  setup() {
    const requestData = reactive(
        {
				arrayData:[
					{
						data:""
					}
				],
				dataNum:0
			}
    );

    const add = () => {
      requestData.arrayData.push({
        data: "",
      });
    };

    const del = (index) => {
      if (requestData.arrayData.length <= 1){
        return false
      }
      else {
        requestData.arrayData.splice(index, 1)
      }
    };

    return {
      ...toRefs(requestData),
      add,
      del,
    };
  },
})
</script>

<style>

</style>