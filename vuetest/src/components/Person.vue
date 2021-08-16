<template>
  <div>
    <label style="margin-left: 50px;">请输入姓名：</label>
    <el-input style="width: 200px" placeholder="请输入姓名" v-model="name"></el-input>
  </div>
</template>

<script lang="js">
import {defineComponent, ref} from "vue";

export default defineComponent({
  name: "Person",

  emits: ["aa"],
  setup(props, content){
    const name = ref("");

    const sendChild = () =>{
      content.emit("aa", name)
    }

    return {
      name,
      sendChild,
    };
  }
})
</script>

<style>

</style>