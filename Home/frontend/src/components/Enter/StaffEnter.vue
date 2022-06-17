<template>
    <div>

        <el-container class="customContainer">
          <el-header class="customPageHeader" style="height:90px !important;color:white;" >
            <!-- <div style="margin-top:15px;"></div>  -->
            <div>
              <img src="../../assets/logo2.png" class="logoStyle">
            <p class="titleText2">{{title}}</p>

          <!-- <div class="perNote"> -->
            <!-- welcome -->
            <p class="perWelcome">欢迎回来！</p>
            <!-- 个人信息 -->
              <el-avatar icon="el-icon-user-solid" @click.native="showper()" class="perInfo"></el-avatar>
              <!-- 退出到登陆界面 -->
              <el-button class="butexit" @click="exit()">退出</el-button>
          </div>
            <!-- </div> -->
            
          
          </el-header>

          <el-divider class="eld1"></el-divider>

        <el-container>
          <el-aside width="200px">
             <el-menu
              router
      default-active="/AllManagement"
      class="el-menu-vertical-demo"
      @open="handleOpen"
      @close="handleClose"
      background-color="#394f69"
      text-color="#fff"
      >
      
      <!-- active-text-color="#ffd04b" -->

      <!-- <el-submenu index="00">
        <template slot="title">
          <span>个人信息</span>
        </template>
          <el-menu-item index="/Calendar">员工日历</el-menu-item>
          <el-menu-item index="/test_p">测试</el-menu-item>
          <el-menu-item index="/test_p2">测试2</el-menu-item>
      </el-submenu> -->

      <!-- <el-submenu index="01"> -->
        <!-- <template slot="title"> -->
          <!-- <i class="el-icon-location"></i> -->
          <!-- <span>订单管理</span> -->
        <!-- </template> -->
          <!-- <el-menu-item index="/Ongoing">订单修改</el-menu-item> -->
          <el-menu-item index="/History"><i class="el-icon-s-order"></i>查看订单</el-menu-item>
      <!-- </el-submenu> -->

      <!-- <el-submenu index="02"> -->
        <!-- <template slot="title"> -->
          <!-- <i class="el-icon-location"></i> -->
          <!-- <span>预约管理</span> -->
        <!-- </template> -->
          <el-menu-item index='/Reservation/AllReservationPage'><i class="el-icon-bell"></i>预约管理</el-menu-item>
          <!-- <el-menu-item index="/History">查看订单</el-menu-item> -->
      <!-- </el-submenu> -->


        <!-- <el-submenu index="03">
        <template slot="title">
          <span>餐桌管理</span>
        </template> -->
          <el-menu-item index="/NewTable1"><i class="el-icon-eleme"></i>餐桌管理</el-menu-item>
          <!-- <el-menu-item index="/Table2">查看指定餐桌使用情况</el-menu-item>
          <el-menu-item index="/Table3">查找可用餐桌</el-menu-item>
          <el-menu-item index="/Table4">修改餐桌使用状态</el-menu-item> -->
        <!-- </el-submenu> -->

        <!-- <el-submenu index="04">
        <template slot="title">
          <span>菜单管理</span>
        </template> -->
          <el-menu-item index="/NewDish1"><i class="el-icon-menu"></i>菜品管理</el-menu-item>
          <!-- <el-menu-item index="/Dish2">查询指定菜品的信息</el-menu-item>
          <el-menu-item index="/Dish3">添加菜品</el-menu-item> -->
        <!-- </el-submenu> -->

        <!-- <el-submenu index="05" >
        <template slot="title">
          <span>会员管理</span>
        </template> -->
          <el-menu-item index="/VIP200"><i class="el-icon-s-custom"></i>会员管理</el-menu-item>
        <!-- </el-submenu> -->

        <!-- <el-submenu index="06"> -->
        <!-- <template slot="title"> -->
          <!-- <i class="el-icon-location"></i> -->
          <!-- <span>员工管理</span> -->
        <!-- </template> -->
          <el-menu-item index="/AllManagement"><i class="el-icon-info"></i>员工管理</el-menu-item>
          <!-- <el-menu-item index="/StaffSearch">员工信息查找</el-menu-item> -->
          <!-- <el-menu-item index="/StaffRewrite">员工信息修改</el-menu-item> -->
          <!-- <el-menu-item index="/StaffManagement">员工信息管理</el-menu-item> -->
        <!-- </el-submenu> -->

        <el-menu-item index="/StatementManage"><i class="el-icon-s-data"></i>流水管理</el-menu-item>
        <el-menu-item index="/CRUD_Ingredient"><i class="el-icon-s-data"></i>食材管理</el-menu-item>
        <el-menu-item index="/CRUD_Utensil"><i class="el-icon-s-data"></i>器材管理</el-menu-item>

    </el-menu>
          </el-aside>
            
            <el-main>
                <router-view :requester_ID='requester_ID'></router-view>
            </el-main>
          </el-container>
        </el-container>

    <!-- 个人信息弹窗 -->
    <el-dialog
        title="员工个人信息"
        :visible.sync="dialogVisible"
        width="40%"
        :before-close="handleClosePer"
        custom-class="customeclassstaffPer">
        <!-- <span>这是一段信息</span> -->

        <div style="height:320px;" :data="descData">
        <!-- <el-descriptions title="用户信息" > -->
        <div><el-descriptions-item label="员工编号" class="perStaffID" prop="staff_id">员工编号：{{per_staff_id}}</el-descriptions-item></div>
        <div><el-descriptions-item label="工作" class="perJob"  prop="job">工作：<el-tag size="medium">{{per_job}}</el-tag></el-descriptions-item></div>
        <div><el-descriptions-item label="姓名" class="perName"  prop="name">姓名：{{per_name}}</el-descriptions-item></div>
        <div><el-descriptions-item label="联系方式" class="perPhone" prop="phone">联系方式：{{per_phone}}</el-descriptions-item></div>
        <div><el-descriptions-item label="身份证号" class="perIDNum" prop="iD_num">身份证号：{{per_iD_num}}</el-descriptions-item></div>
        <div><el-descriptions-item label="入职日期" class="perDate" prop="entry_date">入职日期：{{per_date}}</el-descriptions-item></div>
        <div><el-image  class="perPic" :src="'data:image/jpeg;base64,'+per_pic"></el-image></div>
        </div>

        <span slot="footer" class="dialog-footer">
          <!-- <el-button @click="dialogVisible = false, callOff()" class="per_but2">上传图片</el-button> -->
          <el-button type="primary" @click="perPwd()" class="per_but1">修改密码</el-button>
        </span>
      </el-dialog>
    
    <!-- 修改密码 -->
    <el-dialog
        title="修改密码"
        :visible.sync="dialogVisiblePwd"
        width="32%"
        :before-close="handleClosePwd">

         <div style="height:250px;">
        <el-form ref="form" :model="form" label-width="120px">
        
        <!-- <div style="width:380px;background-color:green"> -->
        <el-form-item label="您的原密码：" label-width="150px" style="width:360px;" :rules="[{ required: true, message: '初始密码不能为空'},]">
            <el-input v-model="form.oldPwd" type="password"></el-input>
        </el-form-item>
        <!-- </div> -->
        <el-form-item label="您的新密码：" label-width="150px" style="width:360px;" :rules="[{ required: true, message: '新密码不能为空'},]">
            <el-input v-model="form.newPwd" type="password" @input="equalN()" show-password></el-input>
        </el-form-item>
        <el-form-item label="请再次输入：" label-width="150px" style="width:360px;" show-password :rules="[{ required: true, message: '新密码不能为空'},]">
            <el-input v-model="form.againPwd" type="password" @input="equalNA()" show-password></el-input>
            <p class="hintText">{{hint}}</p>
        </el-form-item>
        </el-form>
    </div>

        <span slot="footer">
          <el-button @click="cancelCP(),dialogVisiblePwd=false" class="perCP_but2">取消</el-button>
          <el-button type="primary" @click="findOld()" class="perCP_but1">确定</el-button>
        </span>
    </el-dialog>
    
    </div>
    
</template>

<script>
  // 加密
  import crypto from 'crypto'

  export default {
  
  created(){
      this.requester_ID = sessionStorage.getItem("employeeID");
      console.log(requester_ID);
      
  },

    mounted(){

       this.$router.push({
        path:'/AllManagement',
      });

  },

    data () {
      return {
        title: "欢迎来到和平饭店",
        requester_ID:'',
        dialogVisible:false,
        dialogVisiblePwd:false,
        //个人信息
        descData: [],
        per_staff_id:" ",
        per_job:" ",
        per_name:" ",
        per_phone:" ",
        per_iD_num:" ",
        per_date:" ",
        //修改密码
        hint:'',
        form:{
          oldPwd:'',
          newPwd:'',
          againPwd:'',
        },
        temp1:'',
        temp2:'',
        per_pic:null,
      }
    },

    rules:{
      oldPwd:[
        { required: true, message: '请输入初始密码', trigger: 'blur' },
      ],
      newPwd:[
        { required: true, message: '请输入新密码', trigger: 'blur' },
      ],
      againPwd:[
        { required: true, message: '请输入新密码', trigger: 'blur' },
      ],
    },

    methods:{
      return_to_login(){
       
      if(sessionStorage.getItem('employeeID') == null)
      {
        alert("请先登录!");
        console.log("用户未登录,跳转回登录界面");
                this.$router.push({
                path: '/',
                name: 'MainPage',
              });
              return false;
      }
      return true;
    },
      exit(){
      this.$router.push({
        path:'/EmployeeAccount/EmployeeLoginPage',
      });
    },
    
    //按下按钮显示个人信息
    handleClosePer(done) {
        this.$confirm('确认关闭？')
          .then(_ => {
            done();
          })
          .catch(_ => {});
      },

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
        this.perPicture();
      }).catch((error) => {
          console.log(error);
          alert("请求失败!");
        });
    },

    // 显示个人图片
    perPicture(){
      //  console.log('perPicture');
       this.$axios.get("/api/Employee/getEmployeePict",{
         params: {
           staff_id:this.requester_ID,
        }
      }).then(response=>{
        // console.log('response.data:');
        // console.log(response.data);
        // console.log('this.imgpic:');
        // console.log(this.imgpic);
        this.per_pic=response.data;
      }).catch((error) => {
          console.log(error);
          alert("请求失败!");
        });
    },

    //按下按钮修改密码
    handleClosePwd(done) {
        this.$confirm('确认关闭？')
          .then(_ => {
            this.cancelCP();
            done();
          })
          .catch(_ => {});
      },

    perPwd(){
      this.dialogVisible=false;
      this.dialogVisiblePwd=true;
    },

    equalN(){
        if(this.form.newPwd!=this.form.againPwd&&this.form.againPwd!='')
        {
          this.hint="*密码不匹配！";
        }
        // else if(this.form.againPwd==''){
        //   this.hint="密码不能为空！";
        // }
        else{
          this.hint="";
        }
      },
    
    equalNA(){
        if(this.form.newPwd!=this.form.againPwd)
        {
          this.hint="*密码不匹配！";
        }
        else if(this.form.againPwd==''){
          this.hint="*新密码不能为空！";
        }
        else{
          this.hint="";
        }
      },

    findOld(){

      if(this.form.oldPwd==='')
      {
        this.hint="*原密码不能为空！";
        return ;
      }
      else if(this.form.newPwd===''||this.form.againPwd==='')
      {
        this.hint="*新密码不能为空！";
        return ;
      }
      else if(/^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,16}$/.test(this.form.newPwd)===false||/^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,16}$/.test(this.form.againPwd)===false)
      {
        this.hint="*密码必须由数字或字母组成。"
        return;
      }
        //加密
        let md5 = crypto.createHash('md5');
        md5.update(this.form.oldPwd+this.requester_ID);

        console.log('findOld');

        this.$axios.get("/api/Employee/checkEmployeeAndPwd", {
      params: {
      "staff_id":this.requester_ID,
      "pwd":md5.digest('hex')
      }
      })
      .then(response=> {
        // console.log(response.data);
            switch(response.data){
              case 2:
                alert('初始密码错误，请重新输入！');
                this.cancelCP();
                break;
              case 3:
                alert('数据库连接失败！'); 
                this.cancelCP();
                break;
              default:
                this.changePwd();
                break;
            }
      })
      .catch((error) => {
          console.log(error);
          alert("请求失败!");
        });
      },

    changePwd(){
        if(this.form.againPwd==''){
         this.hint="*新密码不能为空！";
         return;
        }

        if(this.hint==="")
        {
          // this.temp1=md5.digest('hex');
        let md5 = crypto.createHash('md5');
        md5.update(this.form.againPwd+this.requester_ID);
        this.temp2=md5.digest('hex');

        this.$axios.post('/api/Employee/updateEmployee', {
          "staff_id":this.requester_ID+"",
          "attribute":'password',
          "newvalue":this.temp2,
        })

        .then(response=> {

        console.log(response);
        console.log(response.data);
        console.log(response.status);
            switch(response.data){
              case 0:
              	alert("没有该员工！");
                // this.msg="没有该员工！";
              	break;
                // case -1:
              	// alert("您没有权限更改！");
                // // this.msg="您没有权限更改！";
              	// break;
              default:
                alert("更新成功！");
                this.cancelCP();
                this.dialogVisiblePwd=false;
                // this.msg=response.data;
                break;
            }
            // console.log(response.data);
          })
          .catch((error) => {
          console.log(error);
          alert("请求失败!");
        });
        }
        else 
        {
          alert('您两次输入的密码不一样！');
          this.cancelCP();
        }
        
      },

    //取消修改密码
    cancelCP(){
       this.form.oldPwd='';
       this.form.newPwd='';
       this.form.againPwd='';
       this.hint="";
    }

    }
  }
</script>

<style scoped>
.el-header, .el-footer {
    background-color: #394f69;
    color: #333;
    text-align: center;
    font-style:normal;
    font-size:40px;
    line-height: 60px;
  }
  
  .el-aside {
    background-color: #394f69;
    color: #333;
    text-align: center;
    line-height: 200px;
    /* height:225px; */
  }
  
  .el-main {
    background-color: #E9EEF3;
    color: #333;
    text-align: center;
    /* line-height: 160px; */
  }
  
  .eld1{
    z-index:5;
    /* margin-left:-800px; */
    /* width:3000px; */
    background-color: white;
    position:absolute;
    top:73px;
  }
  .customContainer{
    height:740px;
    width:100%
  }
  .customPageHeader{
    height:90px !important;
  }

   .logoStyle{
    position:absolute;
    width:80px;
    height:80px;
    left:30px;
    top:11px;
  }

  .titleText2{
    position:absolute;
    font-size: 25px;
    font-weight: 600;
    top: 0px;
    margin-left: 100px;
    color:white
  }
  
  /* 个人信息 */
  /* Welcome */
 .perWelcome{
   font-size: 20px;
   font-weight: 300;
   position: absolute;
    /* width:80px; */
    top:8px;
    right:210px;
 }
  
  /* 个人信息 */
  .perInfo{
     position:absolute;
     width:40px;
     /* height:80px; */
     right:150px;
     top:36px;
     /* padding-top: 20px; */
  }

  /* 个人信息弹窗整体 */
  .customeclassstaffPer{
    /* width:30px; */
    height:900px
  }

  /* 个人信息弹窗中内容 */
  .perStaffID{
    position:absolute;
    font-size: 17px;
    left: 300px;
    top:80px;
  }

  .perJob{
    position:absolute;
    font-size: 17px;
    left: 300px;
    top:120px;
  }

  .perName{
    position:absolute;
    font-size: 17px;
    left: 300px;
    top:160px;
  }

  .perPhone{
    position:absolute;
    font-size: 17px;
    left: 300px;
    top:200px;
  }

  .perIDNum{
    position:absolute;
    font-size: 17px;
    left: 300px;
    top:240px;
  }

  .perDate{
    position:absolute;
    font-size: 17px;
    left: 300px;
    top:280px;
  }

  .perPic{
    background-color: grey;
    height:220px;
    width:200px;
  }

  /* 个人信息两个按钮 */
  .per_but1{
    position:absolute;
    left: 295px;
    top:350px;
  }

  .per_but2{
    position:absolute;
    left: 75px;
    top:350px;
  }

  /* 修改密码两个按钮 */
  .perCP_but1{
    position:absolute;
    left: 230px;
    top:306px;
  }

  .perCP_but2{
    position:absolute;
    left: 140px;
    top:306px;
  }

  /* 修改密码校验 */
  .hintText{
    text-align: left;
    margin-top: 10px;
    margin-bottom: -60px;
    color: red;
  }

  /* 退出 */
  .butexit{
    position: absolute;
    width:80px;
    top:36px;
    /* right:20px */
    right:30px;
  }

</style>