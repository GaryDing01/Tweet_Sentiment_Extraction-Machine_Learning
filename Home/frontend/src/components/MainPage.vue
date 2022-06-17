<template>
  <div>

    <div class="mainBackground" :style="backgroundIm"></div>

    <div class="mainBox">
      <img class="titlePicture" src="../assets/title.png">
      <el-divider class="mainDivide"></el-divider>
      <button class="employeeEnterButton" @click="toEmployeeLoginPage()">员工登录</button>
      <!-- <button class="customEnterButton" @click="toCustomLoginPage()">用户登录</button> -->
    </div>

  </div>
</template>

<script>
  export default {
    name: 'MainPage',

    data () {
      return {
        backgroundIm:{
          backgroundImage: "url(" + require("../assets/mainBackground.png") + ")",
          backgroundRepeat: "no-repeat",
          backgroundSize: "cover",
        },
      }
    },

    methods:{

      toCustomLoginPage(){
        this.$router.push({
          path:'/CustomLoginPage',
          name:'CustomLoginPage',
        })
      },

      toEmployeeLoginPage(){
        this.$router.push({
          path:'/EmployeeLoginPage',
          name:'EmployeeLoginPage',
        })
      },

    }
  }
</script>

<style scoped>
  .mainBackground{
    width:100%;
    height:100%;
    z-index:-1;
    position: absolute;
  }

  .mainBox{
    position:absolute;
    top:50%;
    left:50%;
    transform:translate(-50%,-50%);
    width:566px;
    height: 350px;
    padding:50px;
    background: rgba(255,255,255,0.9);
    box-sizing:border-box;
    box-shadow: 0px 15px 25px rgba(0,0,0,0.5);
    border-radius:15px;
    }

  .titlePicture{
    width:100%
  }

  .mainDivide{
    position:absolute;
    left: 50%;
    margin-left:-270px;
    top:55%;
    background-color:rgba(117, 138, 119, 0.5);
    width:540px;
   }

  .employeeEnterButton{
    z-index: 3;
    position:absolute;
    left: 50%;
    margin-left: -80px;
    top: 50%;
    margin-top: 90px;
    background-color: rgba(255, 170, 0, 0.5);
    width: 160px;
    height: 48px;
    border-radius: 15px;
    font-size: 18px;
    font-weight: 400;
    color: rgba(0, 0, 0, 1);
  }

  .employeeEnterButton:hover{
    background-color:rgba(255, 170, 0, 0.7) ;
  }

  .customEnterButton{
    z-index: 3;
    position:absolute;
    left: 50%;
    /* margin-left: 200px; */
    top: 50%;
    margin-top: 90px;
    background-color: rgba(107, 196, 255, 0.5);
    width: 160px;
    height: 48px;
    border-radius: 15px;
    font-size: 18px;
    font-weight: 400;
    color: rgba(0, 0, 0, 1);
  }

  .customEnterButton:hover{
    background-color:rgba(107, 196, 255, 0.7) ;
  }

</style>
