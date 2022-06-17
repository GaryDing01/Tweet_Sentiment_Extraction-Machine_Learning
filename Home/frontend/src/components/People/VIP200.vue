<template>
  <div>
    <el-row>
      <el-col :span="1000">
        <div>
          <el-row class="button-position">
            <!-- <el-button @click="ToAddNew()"><i class="el-icon-circle-plus"></i>新增会员</el-button> -->
            <el-button @click.native="ToManagement()"><i class="el-icon-s-custom" ></i>所有会员</el-button>
          </el-row>
        </div>
        <!-- 搜索框 -->
        <div class="search-border">
          <el-input
            placeholder="搜索：姓名、手机号、会员号……"
            v-model="inputMes"
            clearable
            :maxlength="11"
            class="input-with-select"
          >
            <el-button
              slot="append"
              icon="el-icon-search"
              @click="searchCustomer(inputMes)"
              >搜索</el-button
            >
          </el-input>
        </div>
      </el-col>
      <!-- 卡片区域 -->
          <div class="card">
            <el-row>
            <div class="demo-avatar">
              <el-col :span="300">
              <div class="avatar_block_div">
                <el-image
                style="width:120px;height:120px;"
                  :src="'data:image/jpeg;base64,' + customer_pic1"
                ></el-image>
              </div>
              </el-col>
              <el-col :span="300">
              <ul class="customer_message">
                <li class="li">会员号：{{ this._customer_id }}</li>
                <li class="li">姓名：{{ this._customer_name }}</li>
                <li class="li">手机号：{{ this._phone_num }}</li>
                <li class="li">生日：{{this._birthday }}</li>
                <li class="li">会员积分：{{ this._credit }}</li>
              </ul>
              </el-col>
              <el-row>
              <el-button class="payRecord"
                type="primary"
                :disabled="send_disabled"
                size="mini"
                plain
                @click="ViewRecords(_customer_id)">消费记录
                </el-button>
                </el-row>
            </div>
            </el-row>
          </div>
    </el-row>
    <!-- 消费记录 -->
    <el-scrollbar>
      <el-dialog
        title="消费记录"
        :visible.sync="dialogTableVisible"
        v-loading="vloading"
        style="line-height: 15px; width: 60%; margin-left: 300px;margin-top:-80px"
      >
        <div class="block">
          <div class="radio">
            时间排序：
            <el-radio-group v-model="reverse">
              <el-radio :label="true">倒序</el-radio>
              <el-radio :label="false">正序</el-radio>
            </el-radio-group>
          </div>
          <div class="timeline">
            <el-timeline :reverse="reverse">
              <el-timeline-item
                v-for="(activity, index) in activities"
                :key="index"
                :timestamp="activity.s_time"
              >
                编号：{{ activity.s_id }}<br />消费金额：￥{{
                  activity.s_amount
                }}
                <!-- &ensp; -->
              </el-timeline-item>
            </el-timeline>
          </div>
        </div>
      </el-dialog>
    </el-scrollbar>
  </div>
</template>

<script>
import VIPmessage from '@/components/People/VIPmessage';
export default {
  components:{
      VIPmessage,
  },
  data() {
    return {
      loading: false,
      vloading: false,
      is_show: false,
      is_empty_show: true,
      select: "",
      // url:"../assets/_customer_id.png",
      url: "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png",

      circleUrl:
        "https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png",
      squareUrl:
        "https://cube.elemecdn.com/9/c2/f0ee8a3c7c9638a54940382568c9dpng.png",
      sizeList: ["large"],
      send_disabled: true,
      activities: [
        {
          s_id: "",
          s_time: "",
          s_amount: "",
        },
      ],
      reverse: true,
      dialogTableVisible: false,
      searchData: [],
      inputMes: "",

      _customer_id: "-",
      _customer_name: "-",
      _phone_num: "-",
      _birthday: "-",
      _credit: "-",

      customer_pic1:null,
    };
  },
  mounted() {
      console.log('mounted');
    this.returnDefault();
    this._customer_id = "--";
      this._customer_name = "--";
      this._phone_num = "--";
      this._birthday = "--";
      this._credit = "--";
      console.log(this._customer_id);

       this.$axios.get("/api/Customer/getCustomerPict?customer_id="+"2109080000", {
        // params: {
        // customer_id:"2109080000"
        // }
        })
        .then(response=> {
          console.log(this._customer_id);
            this.customer_pic1=response.data;  
            console.log(this.customer_pic1);
          })
          .catch((error) => {
          console.log(error);
          alert("请求失败!");
        });
  },
  methods: {
    ToManagement(){
      console.log("to VIP");
      this.$router.push({ path: "/VIPmessage" });
    },
    returnDefault() {
      this._customer_id = "--";
      this._customer_name = "--";
      this._phone_num = "--";
      this._birthday = "--";
      this._credit = "--";
      this.url =
        "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png";
    },
    async ViewRecords(customerid) {
      this.vloading = true;
      console.log(customerid);
      this.dialogTableVisible = true;
      await this.$axios
        .get("/api/VIP/getHistoryPayment", {
          params: {
            customer_id: customerid + "",
          },
        })
        .then((response) => {
          this.activities = response.data;
          this.total = response.data.total;
        });
      this.vloading = false;
    },
    handleShow(index) {
      this.send_disabled = false;
      this._customer_id = this.searchData[index].customer_id;
      this._customer_name = this.searchData[index].customer_name;
      this._phone_num = this.searchData[index].phone_num;
      this._birthday = this.searchData[index].birthday;
      this._credit = this.searchData[index].credit;
      console.log(this.searchData[index].customer_name);
    //   switch (this.searchData[index].customer_name) {
    //     case "刘备":
    //       this.url = require("../../assets/刘备.png");
    //       break;
    //     case "曹操":
    //       this.url = require("../../assets/曹操.png");
    //       break;
    //     case "孙权":
    //       this.url = require("../../assets/孙权.png");
    //       break;
    //     default:
    //       this.url =
    //         "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png";
    //       break;
    //   }
      console.log(this.url);

      this.$axios.get("/api/Customer/getCustomerPict?customer_id="+this._customer_id, {
        // params: {
        // "customer_id":this._customer_id
        // }
        })
        .then(response=> {
          console.log(this._customer_id);
            this.customer_pic1=response.data;  
            console.log(this.customer_pic1);
          })
          .catch((error) => {
          console.log(error);
          alert("请求失败!");
        });
    },
    async searchCustomer(inputMes) {
      // 验证输入内容
      // var re_phone = /^[1][3,4,5,7,8][0-9]{9}$/;
      var re_phone = /^\d{11}$/;
      var re_id = /^\d{10}$/;
      var re_name = /^[\u4e00-\u9fa5]*$/;
      console.log(re_phone.test(inputMes));
      console.log(re_id.test(inputMes));
      console.log(re_name.test(inputMes));
      if (!inputMes) {
        // this.$message('输入不能为空！');
        this.$alert("输入不能为空！", "提示", {
          confirmButtonText: "确定",
        });
        return;
      } else if (re_phone.test(inputMes)) {
        this.loading = true;
        await this.$axios
          .get("/api/VIP/getVIPByPhone", {
            params: {
              phone_num: inputMes + "",
            },
          })
          .then((response) => {
            this.searchData = response.data;
            this.total = response.data.total;
            if (this.searchData.length > 0) {
              this.handleShow(0);
              this.is_empty_show = false;
              this.is_show = true;
              return;
            }
          });
        this.loading = false;
      } else if (re_id.test(inputMes)) {
        this.loading = true;
        await this.$axios
          .get("/api/VIP/getVIPByID", {
            params: {
              customer_id: inputMes + "",
            },
          })
          .then((response) => {
            this.searchData = response.data;
            this.total = response.data.total;
            if (this.searchData.length > 0) {
              this.handleShow(0);
              this.is_empty_show = false;
              this.is_show = true;
              return;
            }
          });
        this.loading = false;
      } else if (re_name.test(inputMes)) {
        this.loading = true;
        await this.$axios
          .get("/api/VIP/getVIPByName", {
            params: {
              customer_name: inputMes + "",
            },
          })
          .then((response) => {
            this.searchData = response.data;
            this.total = response.data.total;

            if (this.searchData.length > 0) {
              this.handleShow(0);
              this.is_empty_show = false;
              this.is_show = true;
              return;
            }
          });

        this.loading = false;
      } else {
        // this.$message('请正确输入姓名、手机号或会员号');
        this.$alert("请正确输入姓名、手机号或会员号", "提示", {
          confirmButtonText: "确定",
        });
        this.returnDefault();
        return;
      }
      if (this.searchData.length == 0) {
        this.$alert("未查询到相关结果", "提示", {
          confirmButtonText: "确定",
        });
        this.send_disabled = true;
        this.is_show = false;
        this.is_empty_show = true;
        this.returnDefault();
        this.customer_pic1=null;
      }
    },
    ToAddNew() {
      this.$router.push({ path: "/VIP2_add" });
    },
  },
};
</script>

<style scoped>
.button-position > .el-button {
  margin: 0;
  margin-left: 10px;
  padding: 0;
  height: 40px;
  width: 100px;
  float: left;
  /* border: 10px red solid; */
  /* z-index:100000; */
}
.search-border {
  text-align: center;
  margin-top: 30px;
  margin-left: 350px;
  margin-bottom: 30px;
  /* border: 10px red solid; */
}
.el-input {
  width: 500px;
}
.el-select .el-input {
  width: 100px;
}
.input-with-select .el-input-group__prepend {
  background-color: #ecf2f7;
  width: 10%;
}
.descr {
  width: 50%;
  background-color: white;
  border: 1px rgb(175, 170, 170) solid;
  float: center;
}

.card {
  display: inline-block;
  position: relative;
  height: 350px;
  width: 600px;
  margin-right: 85px;
  /* border: 1px rgb(175, 170, 170) solid; */
  background-color: rgb(253, 253, 253);
  /* background-color: rgb(99, 13, 13); */
  /* line-height: 20px; */
}

.avatar_block_div {
  /* border: 1px rgb(218, 70, 70) solid; */
  width: 100px;
  margin: 80px;
  height: 100px;
  margin-bottom: 100px;
  margin-top: 65px;
  margin-left: 120px;
}
.customer_message {
  /* border: 1px rgb(175, 170, 170) solid; */
  list-style-type: none;
  width: 200px;
  margin-left: 0px;
  margin-top: 50px;
  margin-bottom: 40px;
  /* margin-bottom:45px; */
}
.li {
  line-height: 40px;
  text-align: left;
}
.table {
  width: 100%;
  line-height: 30px;
  /* margin: 30px; */
  text-align: center;
  margin-left: 15%;
  left: -width/2;
}
.disableButton {
  /* border: 1px rgb(175, 170, 170) solid; */
  background-color: unset;
  border-style: none;
  width: 100%;
  height: 100%;
}
.radio {
  /* border: 1px rgb(175, 170, 170) solid; */
  text-align: left;
  margin-bottom: 30px;
  margin-left: 20px;
}
.timeline {
  text-align: left;
  line-height: 20px;
}

.payRecord{
    position:absolute;
    left:140px;
    top:215px;
}

</style>
