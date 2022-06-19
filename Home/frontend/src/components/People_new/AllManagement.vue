<template>
<div>
    <!-- <el-col :span="14" class="am_col1">
            <div v-if="show_am1" class="show_am1">
                <div><el-button icon="el-icon-user-solid" class="empInfo_but" @click="getData1()">员工信息</el-button></div>
                <div><el-button  icon="el-icon-star-off" class="empSal_but" @click="showAuth_Sal()">工资管理</el-button></div>
            </div>
        </el-col>

        <el-col :span="8" class="am_col2">
            <div v-if="show_am2" class="show_am2">
                <div><el-image  style="width:200px;height:210px;margin-top:70px;margin-left:20px;" :src="'data:image/jpeg;base64,'+imgpic"></el-image></div>
                <div><el-descriptions-item label="员工编号" class="all_pStaffID" prop="staff_id">员工编号：{{per_staff_id}}</el-descriptions-item></div>
                <div><el-descriptions-item label="工作" class="all_pJob"  prop="job">工作：{{per_job}}</el-descriptions-item></div>
                <div><el-descriptions-item label="姓名" class="all_pName"  prop="name">姓名：{{per_name}}</el-descriptions-item></div>
                <div><el-descriptions-item label="联系方式" class="all_pPhone" prop="phone">联系方式：{{per_phone}}</el-descriptions-item></div>
                <div><el-descriptions-item label="身份证号" class="all_pIDNum" prop="iD_num">身份证号：{{per_iD_num}}</el-descriptions-item></div>
                <div><el-descriptions-item label="入职日期" class="all_pDate" prop="entry_date">入职日期：{{per_date}}</el-descriptions-item></div>
            </div>
        </el-col> -->

        <!-- 机器学习上传文件 -->
        <!-- <div style="">
          <input style="color:#000FFF;" type="file" @change="getFile($event)">
          <el-button style="margin-left:10px;z-index:99999;" size="small" type="primary" @click="batchPredict($event)">开始预测</el-button>
        </div> -->

        <!-- <div style="margin: 10vh 25vh;"> -->

        <el-row style="margin-top:60px;margin-right:0px;">
          <el-col
              v-for="(item,index) in blogContent"
              :key="item"
              :span="4"
              :offset="index %4 !==0 ? 2 : 0"
              >
            <el-card shadow="hover" :body-style="{ padding: '0px' }"  style="width:125%;height:300px;">
              <img
                  :src="item.picPath"
                  class="image"
                  style="width:80%;"
              />
              <div style=" text-align: center">
                <h3>{{item.text}}</h3>
              </div>
              <div style="text-align: center;">
                <input style="color:#000FFF;margin-left:45px;" type="file" @change="getFile($event)">
                <el-button style="margin-top:10px;" size="small" type="primary" @click="batchFilter($event,item.text)">开始预测</el-button>
              </div>
            </el-card>
          </el-col>
        </el-row>

        <div style="position:absolute;top:120px;z-index:1050;left:450px;">
            <el-card v-show="showResult" style="background-color: black;">
            <p style="color:white;font-size:20px;">测试结果</p>
            <el-table
                :data="tableData"
                border
                style="width: 100%">
                <el-table-column
                  prop="num"
                  label="No."
                  width="90">
                </el-table-column>
                <el-table-column
                  prop="text"
                  label="Text"
                  width="380">
                </el-table-column>
                <el-table-column
                  prop="truth"
                   width="180"
                  label="Ground Truth">
                </el-table-column>
                <el-table-column
                  prop="test"
                   width="180"
                  label="Test Result">
                </el-table-column>
            </el-table>
            <el-button style="margin-left:0px;margin-top:20px;" size="medium" type="primary" @click="closeTest()">关闭</el-button>
            </el-card>
        </div>

</div>
</template>

<script>
// import axios from './plugins/axios'
import StaffManagement from '@/components/People_new/StaffManagement';
import SidePer from '@/components/People_new/SidePer';

  export default {
    props:['requester_ID'],

      components:{
          StaffManagement,
          SidePer,
      },

    data() {
      return {
        show_am1:true,
        show_am2:true,
        // 右
         per_staff_id:" ",
         per_job:" ",
         per_name:" ",
         per_phone:" ",
         per_iD_num:" ",
         per_date:" ",
         imgpic:null,

        //  机器学习
        file:"",
        batchPredictVisible:false,
        loading:false,
        resultData:{},
        tableData:[
          {
            num:1,
            text:"Last session of the day  http://twitpic.com/67ezh",
            truth:'neutral',
            test:'neutral',
          },
          {
            num:2,
            text:"Shanghai is also really exciting (precisely -- skyscrapers galore). Good tweeps in China:  (SH)  (BJ).",
            truth:'positive',
            test:'neutral',
          },
          {
            num:3,
            text:"Recession hit Veronique Branquinho, she has to quit her company, such a shame!",
            truth:'negative',
            test:'neutral',
          },
          {
            num:4,
            text:"happy bday!",
            truth:'positive',
            test:'neutral',
          },
          {
            num:5,
            text:"http://twitpic.com/4w75p - I like it!!",
            truth:'positive',
            test:'neutral',
          },
          {
            num:6,
            text:"that`s great!! weee!! visitors!",
            truth:'positive',
            test:'neutral',
          },
          {
            num:7,
            text:"I THINK EVERYONE HATES ME ON HERE   lol",
            truth:'negative',
            test:'neutral',
          },
          {
            num:8,
            text:"soooooo wish i could, but im in school and myspace is completely blocked",
            truth:'negative',
            test:'neutral',
          },
          {
            num:9,
            text:"and within a short time of the last clue all of them",
            truth:'neutral',
            test:'neutral',
          },
          {
            num:10,
            text:"What did you get?  My day is alright.. haven`t done anything yet. leaving soon to my stepsister though!",
            truth:'neutral',
            test:'neutral',
          },
        ],
        total:0,
        blogContent:[
          {picPath: require("../../assets/TL1.png"), text:"TF-IDF+LR", turnRoute:""},
          {picPath: require("../../assets/TR1.png"), text:"TF-IDF+RF", turnRoute:""},
          {picPath: require("../../assets/CL1.png"), text:"Count+LR", turnRoute:""},
          {picPath: require("../../assets/CR1.png"), text:"Count+RF", turnRoute:""},
      ],
      showResult:true,
      };
    },

     mounted(){
        //this.showper();
        //this.perPicture();
        this.showResult=false;
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

    //判断授权
    //点击员工信息按钮
    showAuth_Info(){
        this.$axios.get("/api/Employee/employee_authority_check", {
      params: {
      requester_id:this.requester_ID+'',
      }
      })
      .then(response=> {
        switch(response.data){
          case 0:
            alert('您没有被授权！');
            break;
          default:
            // this.addStaff();
            this.$router.push({path: "/StaffManagement",});
            break;
        }
      })
      .catch((error) => {
          console.log(error);
          alert("请求失败!");
        });
      },

    //点击员工信息按钮
    showAuth_Sal(){
        this.$axios.get("/api/Employee/employee_authority_check", {
      params: {
      requester_id:this.requester_ID+'',
      }
      })
      .then(response=> {
        switch(response.data){
          case 0:
            alert('您没有被授权！');
            break;
          default:
            // this.addStaff();
            this.$router.push({path: "/SalaryManagement",});
            break;
        }
      })
      .catch((error) => {
          console.log(error);
          alert("请求失败!");
        });
      },

    // 机器学习测试
    getData() {
      // 设置对应python的接口，这里使用的是localhost:5000
      const path = 'http://127.0.0.1:5000/get_result';
      axios.get(path).then(res => {
        // 这里服务器返回response为一个json对象
        // 通过.data来访返回的数据，然后在通过.变量名进行访问
        // 可以直接通过response.data取得key-value
        alert('here');
        var msg = res.data.msg;
        this.serverResponse = msg; // 因为不能直接使用this作为指针，因此在这之前将this赋给了then指针
        console.log('Success' + res.status + ',' + res.data + ',' + msg); // 成功后显示提示
      }).catch(error => {
        console.error(error);
      });
    },

    // 机器学习测试
    getData1() {
      // 设置对应python的接口，这里使用的是localhost:5000
      const path = 'http://127.0.0.1:5000/get_result';
      this.$axios.get(path).then(res => {
        // 这里服务器返回response为一个json对象
        // 通过.data来访返回的数据，然后在通过.变量名进行访问
        // 可以直接通过response.data取得key-value
        alert('here');
        var msg = res.data.msg;
        this.serverResponse = msg; // 因为不能直接使用this作为指针，因此在这之前将this赋给了then指针
        console.log('Success' + res.status + ',' + res.data + ',' + msg); // 成功后显示提示
      }).catch(error => {
        console.error(error);
      });
    },

    getFile(event){
      this.file=event.target.files[0];
      // alert(this.file);
    },

    batchPredict(event){
      event.preventDefault();
      let formData=new FormData();
      formData.append('filename',(this.file).name)
      formData.append('file',this.file)
      let config={
        headers:{
          'Content-Type':'multipart/form-data'
        }
      }
      this.batchPredictVisible=false;
      this.loading=true;
      var that=
      this;
      that.$axios.post("http://127.0.0.1:5000/get_result_tfidf_l",formData,config).then(function(response){
        that.loading=false;
        console.log(response)
        alert(response.status)
        if(response.status===200){
          // that.tableData=(JSON.parse(response.data))
          that.resultData=response.data
          console.log("这里")
          console.log(that.resultData)
          alert(that.resultData.accuracy)

          // 给表格赋值
          for (let i=0;i<10;i++){
            that.tableData[i].text=that.resultData.text[i];
            that.tableData[i].truth=that.resultData.ground[i];
            that.tableData[i].test=that.resultData.result[i];
          }
          
          that.showResult=true;
        }
      }).catch(err =>{
        alert("错误！")
        this.$message.error(err.message);
        alert(err);
      })
    },

    batchFilter(event,text)
    {
      if (text=="TF-IDF+LR"){
        this.batchPredict(event)
      }
      else if (text=="TF-IDF+RF"){
        this.batchPredict(event)
      }
      else if (text=="Count+LR"){
        this.batchPredict(event)
      }
      else if (text=="Count+RF"){
        this.batchPredict(event)
      }
    },

    closeTest(){
      this.showResult=false;
    }

  }
}
</script>

<style scoped>
/* 左 */
.empInfo_but{
    width:200px;
    height:200px;

    /* position:absolute;
    left:300px;
    top:30px; */
    margin-left:20px;
    margin-top:65px;

    font-size:30px;
}

.empSal_but{
    width:200px;
    height:200px;

    /* position:absolute;
    left:300px; */
    margin-left:20px;
    margin-top:65px;

    font-size:30px;
}

/* 右 */
.am_col1{
    background-color:rgb(241, 217, 176);
    position:absolute;
    left:220px;
    width:800px;
    height:600px;
}

.am_col2{
    background-color:rgb(241, 217, 176);
    position:absolute;
    right:20px;
    width:450px;
    height:600px;
}

.all_pStaffID{
  font-size:20px;
  position:absolute;
  left:130px;
  top:300px;
}

.all_pJob{
  font-size:20px;
  position:absolute;
  left:130px;
  top:330px;
}

.all_pName{
  font-size:20px;
  position:absolute;
  left:130px;
  top:360px;
}

.all_pPhone{
  font-size:20px;
  position:absolute;
  left:130px;
  top:390px;
}

.all_pIDNum{
  font-size:20px;
  position:absolute;
  left:130px;
  top:420px;
}

.all_pDate{
  font-size:20px;
  position:absolute;
  left:130px;
  top:450px;
}

.all_pNote{
  font-size:25px;
  position:absolute;
  width:160px;
  left:130px;
  top:510px;
  color:purple;
}
</style>
