<template>
    <el-row>
  <!-- <el-button round>圆角按钮</el-button> -->
  <!-- <el-button type="primary" round>主要按钮</el-button> -->
  <el-button type="success" round @click="toAddEmployee()">添加</el-button>
  <el-button type="info" round @click="toDeleteEmployee()">删除</el-button>
  <el-button type="warning" round @click="toUpdateEmployee()">更新</el-button>
  <!-- <el-button type="danger" round>危险按钮</el-button> -->
</el-row>

</template>
<script>
export default {
  data() {
    return {
      input: ''
    }
  }
}
</script>
<script>
  export default {

    data () {
      return {
          msg:'欢迎来到Employee管理页面！'
      }
    },

    methods:{
      toAddEmployee(){
        this.$router.push({path:'/Employee2_add'})
      },
      toDeleteEmployee(){
        this.$router.push({path:'/Employee2_delete'})
      },
      toUpdateEmployee(){
        this.$router.push({path:'/Employee2_update'})
      },
    }
  }
</script>

<style>
</style>