<template>
<div>
    <!-- 个人信息右边 -->
    <!-- <el-dialog
        title="员工个人信息"
        :visible.sync="dialogVisible"
        width="40%"
        :before-close="handleClosePer"
        custom-class="customeclassstaffPer">
        <span>这是一段信息</span> -->

        <!-- <div style="height:320px;" :data="descData"> -->
        <!-- <el-descriptions title="用户信息" > -->
        <div><el-image  style="width:90px;height:90px;margin-top:20px;margin-left:20px;" :src="'data:image/jpeg;base64,'+imgpic"></el-image></div>
        <div><el-descriptions-item label="员工编号" class="perStaffID" prop="staff_id">员工编号：{{per_staff_id}}</el-descriptions-item></div>
        <div><el-descriptions-item label="工作" class="perJob"  prop="job">工作：<el-tag size="medium">{{per_job}}</el-tag></el-descriptions-item></div>
        <div><el-descriptions-item label="姓名" class="perName"  prop="name">姓名：{{per_name}}</el-descriptions-item></div>
        <div><el-descriptions-item label="联系方式" class="perPhone" prop="phone">联系方式：{{per_phone}}</el-descriptions-item></div>
        <div><el-descriptions-item label="身份证号" class="perIDNum" prop="iD_num">身份证号：{{per_iD_num}}</el-descriptions-item></div>
        <div><el-descriptions-item label="入职日期" class="perDate" prop="entry_date">入职日期：{{per_date}}</el-descriptions-item></div>
        
        <!-- </div> -->

        <!-- <span slot="footer" class="dialog-footer">
          <el-button @click="dialogVisible = false, callOff()" class="per_but2">上传图片</el-button>
          <el-button type="primary" @click="perPwd()" class="per_but1">修改密码</el-button>
        </span> -->
      <!-- </el-dialog> -->
</div>
</template>

<script>
// import Global from '@/components/Setting/Global'

  export default {
    props:['requester_ID'],

    data() {
      return {
        // requester_ID:Global.req_ID,
        per_staff_id:" ",
        per_job:" ",
        per_name:" ",
        per_phone:" ",
        per_iD_num:" ",
        per_date:" ",
        imgpic:null,
      };
    },

    mounted(){
        this.showper();
        this.perPicture();
    },

    methods: {
        showper(){
      this.dialogVisible=true;

      this.$axios.get("/api/Employee/getEmployeeInfobyAttr",{
         params: {
           attribute:"staff_id",
           value:this.requester_ID,
        }
      }).then(response=>{
        this.per_staff_id=response.data[0].staff_id;
        this.per_job=response.data[0].job;
        this.per_name=response.data[0].name;
        this.per_phone=response.data[0].phone;
        this.per_iD_num=response.data[0].iD_num;
        this.per_date=response.data[0].entry_date;
      }).catch((error) => {
          console.log(error);
          alert("请求失败!");
        });
    },

    perPicture(){
    //    console.log('perPicture');
       this.$axios.get("/api/Employee/getEmployeePict",{
         params: {
           staff_id:this.requester_ID,
        }
      }).then(response=>{
        console.log('response.data:');
        console.log(response.data);
        console.log('this.imgpic:');
        console.log(this.imgpic);
        this.imgpic=response.data;
      }).catch((error) => {
          console.log(error);
          alert("请求失败!");
        });
    },
  }
}
</script>

<style scoped>
  
</style>