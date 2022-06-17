<template>
    <div>
    
        <el-table
    :data="tableData"
    border
    style="width: 100%;line-height: 20px"
    class="ep1"
    >
    <div :class="{table1:isShowT1}">
    <el-table-column
      prop="staff_id"
      label="员工编号"
      width="210%"
      align="center"
      
      >
    </el-table-column>
    </div>
    <el-table-column
      prop="job"
      label="工作"
      width="215%"
      align="center">
    </el-table-column>
    <el-table-column
      prop="name"
      label="姓名"
      width="215%"
      align="center">
    </el-table-column>
    <el-table-column
      prop="phone"
      label="联系方式"
      width="215%"
      align="center">
    </el-table-column>
    <el-table-column
      prop="iD_num"
      label="身份证号"
      width="215%"
      align="center">
    </el-table-column>
    <el-table-column
      prop="entry_date"
      label="入职日期"
      width="215%"
      align="center">
    </el-table-column>
  </el-table>
 
    </div>
</template>

<script>
  export default {
  
  props:['requester_ID'],
    
    mounted(){
      this.$axios.get("/api/Employee/getEmployeeInfobyAttr", {
        params: {
        attribute:"staff_id",
        value:this.requester_ID,
        }
        })
        .then(response=> {
            // console.log(response.data);
            this.tableData=response.data;  
          })
          .catch((error) => {
          console.log(error);
          alert("请求失败!");
        });
    },

    data () {
      return {
          msg:'',
          tableData: [],
          isShowT1:true
      }
    },

    methods:{
    }
  }
</script>

<style>
.ep1{
  position:absolute;
  top:300px;
}
</style>