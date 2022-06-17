<template>
    <el-row>
  <!-- <el-button round>圆角按钮</el-button> -->
  <!-- <el-button type="primary" round>主要按钮</el-button> -->
  <el-button type="success" round @click="toAddVIP()">添加会员</el-button>
  <!-- <el-button type="info" round @click="toDeleteVIP()">删除会员</el-button> -->
  <!-- <el-button type="warning" round>警告按钮</el-button> -->
  <!-- <el-button type="danger" round>危险按钮</el-button> -->
</el-row>
    

</template>

<script>
  export default {

    data () {
      return {
          msg:'更新会员名单！',
          input:''
      }
    },

    methods:{
      toAddVIP(){
        this.$router.push({path:'/VIP2_add'})
      },
      toDeleteVIP(){
        this.$router.push({path:'/VIP2_delete'})
      },
    }
  }
</script>

<style>
</style>