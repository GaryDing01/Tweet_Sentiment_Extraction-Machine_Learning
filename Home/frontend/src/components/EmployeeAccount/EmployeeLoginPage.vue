<template>

  <div>

    <div class="background" :style="backgroundIm">
    </div>

    <div class="loginList">
      <form>
        <p class="titleText">员工登录</p>
        <input placeholder="用户名"  v-model="username"/>
        <input placeholder="密码" type="password" v-model="password"/>
        <p class="hintText">{{hint}}</p>
      </form>
    </div>

    <div>
      <button class="loginButton" @click="login()">登录</button>
      <button class="butallexitel" @click="exitall()">返回主页面</button>
    </div>

  </div>

</template>

<script>
import crypto from 'crypto'

export default {

  name: 'EmployeeLoginPage',

  data () {
    return {
      backgroundIm:{
        backgroundImage: "url(" + require("../../assets/mainBackground.png") + ")",
        backgroundRepeat: "no-repeat",
        backgroundSize: "cover",
      },
      hint:'',
      username:'',
      password:'',
    }
  },

  methods:{

    login(){

        // //加密
        // let md5 = crypto.createHash('md5');
        // md5.update(this.password+this.username);
        // // P=md5.digest('hex')+'';
        // // console.log(md5.digest('hex'));
        // this.$axios
        //   .get('/api/Employee/checkEmployeeAndPwd',{
        //     params:{
        //       staff_id: this.username ,
        //       // pwd: this.password
        //       pwd:md5.digest('hex')
        //     }
        //   })
        //   .then(response=> {
        //     console.log('看这里');
        //     this.test = response.data;
        //     switch(response.data){
        //       case 0:
        //         this.hint = "*用户名不存在";
        //         break;
        //       case 1:
        //       	alert("登录成功！");
        //         this.$router.push({
        //           path:'/StaffEnter',
        //           name:'StaffEnter',
        //           // params:{
        //           //   employeeID: this.username,
        //           // },
        //         });
        //         sessionStorage.setItem("employeeID",this.username);
        //       	break;
        //       case 2:
        //       	this.hint = "*密码错误，请重新输入";
        //       	break;
        //     }
        //   })

        // 测试
        alert("登录成功！");
                this.$router.push({
                  path:'/StaffEnter',
                  name:'StaffEnter',
                  params:{
                    employeeID: this.username,
                  },
                });
    }, 
    exitall(){
      this.$router.push({
        path:'/',
      });
    },

  }
}
</script>

<style scoped>

  .background{
    width:100%;
    height:100%;
    z-index:-1;
    position: absolute;
  }

  .loginList{
    z-index:1;
    position: absolute;
    width: 400px;
    height: 430px;
    top: 50%;
    margin-top: -200px;
    left: 50%;
    margin-left: -200px;
    background-color: aliceblue;
    border-radius: 25px;
    text-align: center;
    padding: 5px 40px;
    box-sizing: border-box;
    
  }

  .titleText{
    /* background-color:green; */
    font-size: 42px;
    font-weight: 600;
    text-align: left;
    margin-left: 80px;
  }

  .hintText{
    text-align: left;
    margin-top: 10px;
    margin-bottom: -60px;
    color: red;
  }

  input{
    background-color: aliceblue;
    width: 100%;
    height: 48px;
    margin-bottom: 10px;
    border: none;
    border-bottom: 2px solid silver;
    outline: none;
    font-size: 22px;
  }

  .loginButton{
    z-index: 3;
    position:absolute;
    left: 50%;
    margin-left: -55px;
    top: 50%;
    margin-top: 110px;
    background-color: aquamarine;
    width: 110px;
    height: 48px;
    border-radius: 8px;
    font-size: 28px;
    font-weight: 600;
    color: white;
  }

  .loginButton:hover{
    background-color:aqua ;
  }

  .butallexitel{
    z-index:3;
    position: absolute;
    width:100px;
    height:45px;
    top:20px;
    right:20px
  }

</style>
