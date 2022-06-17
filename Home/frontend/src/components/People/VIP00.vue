<template>
  <div>
    <el-row>
      <el-col :span="1000">
        <div>
          <el-row class="button-position">
            <!-- <el-button @click="ToAddNew()"><i class="el-icon-circle-plus"></i>新增会员</el-button> -->
            <el-button
              ><i class="el-icon-s-custom" @click="ToManagement()"></i
              >会员管理</el-button
            >
            <!-- <el-button><i class="el-icon-s-tools"></i>会员设置</el-button> -->
            <el-button><i class="el-icon-chat-square"></i>发送短信</el-button>
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
          <span
            ><el-button
              slot="append"
              icon="el-icon-takeaway-box"
              type="warning"
              @click="noCard()"
              >刷卡</el-button
            ></span
          >
        </div>
        <!-- 表格区域 -->
        <div class="table">
          <template>
            <el-table
              v-loading="loading"
              v-show="is_show"
              :data="searchData"
              style="width: 100%"
            >
              <el-table-column type="index" :index="indexMethod">
              </el-table-column>
              <el-table-column prop="customer_name" label="姓名" width="150">
              </el-table-column>
              <el-table-column prop="phone_num" label="手机号" width="180">
              </el-table-column>
              <el-table-column prop="customer_id" label="会员号">
              </el-table-column>
              <el-table-column fixed="right" label="" width="100">
                <template slot-scope="scope">
                  <div class="disableButton" @click="handleShow(scope.$index)">
                    &emsp;
                  </div>
                </template>
              </el-table-column>
            </el-table>
            <el-empty
              v-show="is_empty_show"
              description="什么也没有找到欸~"
            ></el-empty>
          </template>
        </div>
      </el-col>
      <!-- 卡片区域 -->
        <el-card class="aside">
          <div class="card">
            <div class="demo-avatar">
              <div class="avatar_block_div">
                <el-avatar
                  shape="square"
                  :size="100"
                  :fit="fit"
                  :src="url"
                ></el-avatar>
              </div>
              <ul class="customer_message">
                <li class="li">会员号：{{ _customer_id }}</li>
                <li class="li">姓名：{{ _customer_name }}</li>
                <li class="li">手机号：{{ _phone_num }}</li>
                <li class="li">生日：{{ _birthday }}</li>
                <li class="li">会员积分：{{ _credit }}</li>
              </ul>
              <el-button
                type="primary"
                :disabled="send_disabled"
                size="mini"
                plain
                @click="ViewRecords(_customer_id)"
                >消费记录</el-button
              >
            </div>
          </div>
        </el-card>
        
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
export default {
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
    };
  },
  mounted: function () {
    this.returnDefault();
  },
  methods: {
    noCard() {
      this.$alert("未设置或未初始化IC读卡器", "提示", {
        confirmButtonText: "确定",
      });
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
      switch (this.searchData[index].customer_name) {
        case "刘备":
          this.url = require("../../assets/刘备.png");
          break;
        case "曹操":
          this.url = require("../../assets/曹操.png");
          break;
        case "孙权":
          this.url = require("../../assets/孙权.png");
          break;
        default:
          this.url =
            "https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png";
          break;
      }
      console.log(this.url);
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
  margin-top: 10px;
  margin-left: 170px;
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
.aside {
  float: right;
  width: 300px;
  height: 100%;
  margin-right: 10px;
}
.card {
  display: inline-block;
  position: relative;
  height: 100%;
  width: 100%;
  /* border: 1px rgb(175, 170, 170) solid; */
  background-color: rgb(253, 253, 253);
  /* line-height: 20px; */
}

.avatar_block_div {
  /* border: 1px rgb(218, 70, 70) solid; */
  width: 100px;
  margin: 80px;
  height: 100px;
  margin-bottom: 45px;
  margin-top: 50px;
}
.customer_message {
  /* border: 1px rgb(175, 170, 170) solid; */
  list-style-type: none;
  width: 200px;
  margin-left: 20px;
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
</style>
