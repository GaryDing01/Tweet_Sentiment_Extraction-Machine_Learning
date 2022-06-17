<template>
  <div>

    <div style="line-height: 50px">
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/StaffEnter' }"
          >首页</el-breadcrumb-item
        >
        <el-breadcrumb-item>员工管理</el-breadcrumb-item>
        <el-breadcrumb-item>工资管理</el-breadcrumb-item>
      </el-breadcrumb>
    </div>

    <div style="line-height: 30px">
      <el-card class="box-card" style="margin-top: 20px;">

<!-- 查询员工薪水 -->
 <div class="searchSalary">
           <el-select v-model="sal_attribute" placeholder="请选择属性" style="size:large;width:200px;">
             <el-option label="员工编号" value="staff_id"></el-option>
             <el-option label="工作" value="job"></el-option>
             <el-option label="姓名" value="name"></el-option>
             <el-option label="基础工资" value="basic_salary"></el-option>
            <el-option label="奖金" value="bonus"></el-option>
           </el-select>

    <el-input style="width:280px" placeholder="请输入员工信息" v-model="sal_value" clearable></el-input>
    <div class="search_sal_but"><el-button type="primary" @click="checkSearchSal()" icon="el-icon-search">搜索</el-button></div>
    <p class="search_sal_hintText">{{sal_hint}}</p>
  </div>

  <!-- <div class="salBlock">
    <el-date-picker
      v-model="sal_time"
      type="daterange"
      align="right"
      unlink-panels
      range-separator="至"
      start-placeholder="开始日期"
      end-placeholder="结束日期"
      value-format="yyyy-MM-dd"
      :picker-options="pickerOptions"
      style="width:230px;">
    </el-date-picker>
    <div class="search_sal_but"><el-button type="primary" @click="checkSearch()">搜索</el-button></div>
  </div> -->

<!-- 员工薪水表格 -->
<div class="empSalTable">
        <el-table
          v-loading="loading"
          element-loading-text="拼命加载中"
          element-loading-spinner="el-icon-loading"
          :data="tableData.slice((currentPage - 1) * pagesize,currentPage * pagesize)"
          :default-sort = "{prop: 'staff_id', order: 'ascending'}"
          @sort-change="sortChange"
          style="width: 100%;margin-bottom:20px"
          max-height="1000"
          border
          stripe
        >
          <el-table-column prop="staff_id" label="员工编号" width="140%" align="center" sortable></el-table-column>
          <el-table-column prop="job" label="工作" width="130%" align="center" column-key="job" :filters="[{text: '经理', value: '经理'}, {text: '财务', value: '财务'}, {text: '厨师', value: '厨师'}, 
      {text: '服务员', value: '服务员'},]"
      :filter-method="filterHandler"></el-table-column>
          <el-table-column prop="name" label="姓名" width="140%" align="center"></el-table-column>
          <el-table-column prop="basic_salary" label="基础工资" width="150%" align="center" sortable></el-table-column>
          <el-table-column prop="bonus" label="奖金" width="110%" align="center" sortable></el-table-column>
          <el-table-column prop="s_id" label="流水编号" width="140%" align="center" sortable></el-table-column>
          <el-table-column prop="s_time" label="流水日期" width="160%" align="center" sortable></el-table-column>
          <el-table-column fixed="right" label="操作" width="250%" align="center">
            <template slot-scope="scope">
              <el-button type="success" size="mini" @click="setOneSAInfo(scope.row)">记录</el-button>
              <el-button type="primary" size="mini" @click="setNewBonus(scope.row)">修改</el-button>
              <el-button type="danger" size="mini" @click="setrevSal(scope.row)">删除</el-button>
            </template>
          </el-table-column>
        </el-table>

        <el-pagination
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :page-sizes="[5, 10]"
          :page-size="pagesize"
          layout="total, sizes, prev, pager, next"
          :total="tableData.length"
        >
        </el-pagination>

        </div>
<!-- 相关功能按钮 -->
<div class="sal_related_but">
    <!-- <el-button type="info" class="sal_add_but">新增工资</el-button> -->
    <!-- <el-button type="info" class="sal_del_but">批量删除</el-button> -->
    <el-button type="warning" class="sal_rel_but" @click="releaseSal()">发放工资</el-button>
</div>

      </el-card>

    </div>

    <!-- 某一员工工资记录的弹窗 -->
    <div>

      <el-dialog
        title="员工工资记录"
        :visible.sync="dialogOnesSalary"
        width="39%"
        :before-close="handleCloseOnesSalary">

      <div style="height:500px;">
      <!-- 员工基本信息 -->
      <div><el-descriptions-item label="员工编号"  prop="staff_id" class="onesa_si">员工编号：{{this.onesa_staff_id}}</el-descriptions-item></div>
      <div><el-descriptions-item label="工作"   prop="job" class="onesa_j">工作：<el-tag size="large">{{this.onesa_job}}</el-tag></el-descriptions-item></div>
      <div><el-descriptions-item label="姓名"   prop="name" class="onesa_n">姓名：{{this.onesa_name}}</el-descriptions-item></div>

      <!-- 员工工资记录表 -->
      <div class="onesa_table">
        <el-table
          v-loading="loading"
          element-loading-text="拼命加载中"
          element-loading-spinner="el-icon-loading"
          :data="tableDataOneSa.slice((currentPage_1 - 1) * pagesize,currentPage_1 * pagesize)"
          :default-sort = "{prop: 'staff_id', order: 'ascending'}"
          @sort-change="sortChange"
          style="width: 100%;margin-bottom:20px"
          max-height="1000"
          border
          stripe
        >
          <el-table-column prop="s_amount" label="总工资" width="180%" align="center" sortable></el-table-column>
          <el-table-column prop="s_id" label="流水编号" width="180%" align="center" sortable></el-table-column>
          <el-table-column prop="s_time" label="流水日期" align="center" sortable></el-table-column>
        </el-table>

        <el-pagination
          @size-change="handleSizeChange_1"
          @current-change="handleCurrentChange_1"
          :current-page="currentPage_1"
          :page-sizes="[5, 10]"
          :page-size="pagesize"
          layout="total, sizes, prev, pager, next"
          :total="tableDataOneSa.length"
        >
        </el-pagination>

        </div>
    </div>

      </el-dialog>

</div>

<!-- 修改某一员工奖金的弹窗 -->
<div>
    <el-dialog
        title="员工奖金修改"
        :visible.sync="dialogOnesBonus"
        width="39%"
        :before-close="handleCloseOnesBonus">

        <div style="height:100px;">
            <p class="sal_p_newB">请输入该员工新的奖金：</p>
            <el-input placeholder="该员工新的奖金" v-model="input_newbonus" clearable class="sal_input_newB"></el-input>
            <p class="sal_hint_newB">{{this.newB_hint}}</p>
        </div>

        <span slot="footer" class="dialog-footer">
          <el-button @click="dialogOnesBonus = false, callOff_newB()" class="sal_but2_newB">取 消</el-button>
          <el-button type="primary" @click="checknewB()" class="sal_but1_newB">确 定</el-button>
        </span>
        
      </el-dialog>
</div>

<!-- 删除某一员工工资的弹窗 -->
<div>
    <el-dialog
        title="员工奖金删除"
        :visible.sync="dialogOnesRev"
        width="39%"
        :before-close="handleCloseOnesRev">

        <div style="height:110px;">
        <!-- <span slot="footer" class="dialog-footer"> -->
          <el-button @click="dialogOnesRev = false" class="sal_but3_rev">取消删除</el-button>
          <el-button type="danger" @click="revOne()" class="sal_but1_rev">删除本次</el-button>
          <el-button type="info" @click="revAll()" class="sal_but2_rev">删除全部</el-button>
        <!-- </span> -->
        </div>
        
      </el-dialog>
</div>

  </div>
</template>

<script>

export default {
    
    watch:{
      dialogOnesSalary(val){
        if(val==true){
          this.currentPage_1=1;
        }
      }
    },


    mounted(){
    this.showRecentSalary();
    },

    data() {
    return {
       stripe:true,
        currentPage:1,
        currentPage_1:1,
        pagesize:5,
        total:0,
        currentHeight:522,
      staff_id:'',
      tableData:[],
      loading: true,
      dialogVisible: false,
      form: {
          // employee_id: '',
          attribute: '',
          newdata:'',
      },
      rowID:'',
      // 查询员工信息
      sal_attribute:'',
      sal_value:'',
      sal_hint:'',
      //time
        // pickerOptions: {
        //   shortcuts: [{
        //     text: '最近一周',
        //     onClick(picker) {
        //       const end = new Date();
        //       const start = new Date();
        //       start.setTime(start.getTime() - 3600 * 1000 * 24 * 7);
        //       picker.$emit('pick', [start, end]);
        //     }
        //   }, {
        //     text: '最近一个月',
        //     onClick(picker) {
        //       const end = new Date();
        //       const start = new Date();
        //       start.setTime(start.getTime() - 3600 * 1000 * 24 * 30);
        //       picker.$emit('pick', [start, end]);
        //     }
        //   }, {
        //     text: '最近三个月',
        //     onClick(picker) {
        //       const end = new Date();
        //       const start = new Date();
        //       start.setTime(start.getTime() - 3600 * 1000 * 24 * 90);
        //       picker.$emit('pick', [start, end]);
        //     }
        //   }]
        // },
        // sal_time:"",

        // 员工工资记录弹窗
        dialogOnesSalary:false,
        tableDataOneSa:[],
        onesa_staff_id:'',
        onesa_job:'',
        onesa_name:'',

        // 员工奖金修改弹窗
        dialogOnesBonus:false,
        newB_staff_id:'',
        input_newbonus:'',
        newB_hint:'',
        
        //员工工资删除弹窗
        dialogOnesRev:false,
        rev_staff_id:'',
        rev_s_id:'',
        
    };
  },


   methods: {
      handleClose(done) {
        this.$confirm('确认关闭？')
          .then(_ => {
            done();
          })
          .catch(_ => {});
      },

    handleSizeChange(val) {
        this.pagesize = val;
        if(val==5)
          this.currentHeight = 285;
        else if(val==10)
          this.currentHeight = 522;
      },
      

    handleCurrentChange(val) {
        this.currentPage = val;
      },

    handleSizeChange_1(val) {
        this.pagesize = val;
        if(val==5)
          this.currentHeight = 285;
        else if(val==10)
          this.currentHeight = 522;
      },
      

    handleCurrentChange_1(val) {
        this.currentPage_1 = val;
      },

    filterHandler(value, row, column) {
        const property = column['property'];
        return row[property] === value;
      },
    handleEdit(index, row) {
        console.log(index, row);
    },

    //显示所有的员工
    async  showRecentSalary(){
        this.$axios.get("/api/Employee/getALLSalary", {
        params: {
        // requester_id:this.requester_ID+'',
        }
        })
        .then(response=> {
            this.tableData=response.data;  
          })
          .catch((error) => {
          console.log(error);
          alert("请求失败!");
        });
        this.loading = false;
      },

      //点击修改按钮，修改员工信息
  setstaffRow(rows){
    this.dialogVisible = true;
    // console.log('setRow');
    // console.log(rows);
    this.rowID=rows.staff_id;
  },
  
  //点击确定按钮
  onUpdate(){
        this.dialogVisible = false;
        this.$axios.post('/api/Employee/updateEmployee', {
          "staff_id":this.rowID,
          "attribute":this.form.attribute,
          "newvalue":this.form.newvalue,
        })

        .then(response=> {

        // console.log(response);
        // console.log(response.data);
        // console.log(response.status);
            switch(response.data){
              case 0:
              	alert("没有该员工！");
                this.msg="没有该员工！";
                this.callOff();
              	break;
                case -1:
              	alert("您没有权限更改！");
                this.msg="您没有权限更改！";
                this.callOff();
              	break;
              default:
                alert("更新成功！");
                this.msg=response.data;
                this.callOff();
                this.showAllStaff();
                break;
            }
            console.log(response.data);
          })
          .catch((error)=>{
            console.log('请求失败');
            console.log(error);
            this.callOff();
          })
        },

        callOff(){
          this.form.attribute='';
          this.form.newvalue='';
          this.$router.push({path:'/StaffManagement'});
        },

  // 查询员工工资
  checkSearchSal(){
    if(this.sal_attribute==''||this.sal_value=='')
    {
      this.sal_hint='*查询不能为空！';
      return;
    }
    if(this.sal_attribute=="staff_id")
    {
      if(/^[0-9]*$/.test(this.sal_value)===false)
      {
        this.sal_hint="*员工编号由数字组成。"
        return;
      }
    }
    else if(this.sal_attribute=="job")
    {
      if(/^[\u4e00-\u9fa5]*$/.test(this.sal_value)===false)
      {
        this.sal_hint="*员工工作由汉字组成。"
        return;
      }
      if(this.sal_value!="经理"&&this.sal_value!="厨师"&&this.sal_value!="服务员"&&this.sal_value!="财务")
      {
        this.sal_hint="*暂无该工作。"
        return;
      }
    }
    else if(this.sal_attribute=="name")
    {
      if(/^[\u4e00-\u9fa5]*$/.test(this.sal_value)===false)
      {
        this.sal_hint="*员工姓名由汉字组成。"
        return;
      }
    }
    else if(this.sal_attribute=="basic_salary")
    {
      if(/^[1-9]\d*$/.test(this.sal_value)===false)
      {
        this.sal_hint="*基础工资为正整数。"
        return;
      }
    }
    else if(this.sal_attribute=="bonus")
    {
      if(/^[1-9]\d*$/.test(this.sal_value)===false&&this.sal_value!="0")
      {
        this.sal_hint="*奖金为自然数。"
        return;
      }
    }
    this.sal_hint="";
    this.searchEmployeeSalary();
  },

  searchEmployeeSalary(){
     this.$axios.get("/api/Employee/getOnesSalary", {
      params: {
      attribute:this.sal_attribute+'',
      value:this.sal_value+'',
      }
      })
      .then(response=> {
            this.tableData=response.data;
            this.sal_attribute="";
            this.sal_value="";
      })
      .catch((error) => {
          console.log(error);
          alert("请求失败!");
          this.sal_attribute="";
          this.sal_value="";
        });
  },

  //员工工资记录
        handleCloseOnesSalary(done) {
          // this.currentPage_1=1;
          // console.log(this.currentPage_1);
        this.$confirm('确认关闭？')
          .then(_ => {
            done();
          })
          .catch(_ => {});
      },

    //点击记录按钮
    setOneSAInfo(rows){
        this.onesa_staff_id=rows.staff_id;
        this.onesa_job=rows.job;
        this.onesa_name=rows.name;
        this.dialogOnesSalary=true;

        // 开始查找某一员工工资记录
        this.$axios.get("/api/Employee/getOnesHistorySalary", {
      params: {
      staff_id:this.onesa_staff_id+'',
      }
      })
      .then(response=> {
            this.tableDataOneSa=response.data;
      })
      .catch((error) => {
          console.log(error);
          alert("请求失败!");
        });
    },

    //员工奖金修改
    handleCloseOnesBonus(done) {
        this.$confirm('确认关闭？')
          .then(_ => {
            done();
          })
          .catch(_ => {});
      },
    
    //点击修改按钮
    setNewBonus(rows){
        this.newB_staff_id=rows.staff_id;
        this.dialogOnesBonus=true;
    },

    //在修改奖金弹窗中点击确认
    checknewB(){
        if(/^[1-9]\d*$/.test(this.input_newbonus)===false&&this.input_newbonus!="0")
        {
          this.newB_hint="*奖金为自然数。"
          return;
        }
        else if(this.input_newbonus=='')
        {
            this.newB_hint="*奖金不能为空。"
            return;
        }
        this.newB_hint="";
        this.updateBonus();
    },

    //修改奖金
    updateBonus(){

        this.$axios.post('/api/Employee/setbonus?staff_id='+this.newB_staff_id+'&newbonus='+this.input_newbonus, {
        //   "staff_id":this.newB_staff_id,
        //   "newbonus":this.input_newbonus,
        // "staff_id":'0000',
        // "newbonus":'200',
        })

        .then(response=> {
            switch(response.data){
              case -1:
              	alert("修改奖金失败！");
                this.callOff_newB();
                this.dialogOnesBonus=false;
              	break;
              case parseInt(this.input_newbonus):
                console.log(response.data);
                

                alert("奖金更新成功！下一次发放工资时，该员工总工资将发生变化！");
                this.callOff_newB();
                this.dialogOnesBonus=false;
                this.showRecentSalary();
                break;
              default:
                alert(response.data);
                this.callOff_newB();
                this.dialogOnesBonus=false;
                break;
            }
          })
          .catch((error)=>{
            console.log('请求失败');
            console.log(error);
            this.dialogOnesBonus=false;
            this.callOff_newB();
          })
    },

    //清理修改奖金输入框
    callOff_newB(){
        this.input_newbonus='';
    },

    //发放工资
    releaseSal(){
        this.$axios.post('/api/Employee/paysalary')

        .then(response=> {
            switch(response.data){
              case 0:
              	alert("发放失败！");
                  this.showRecentSalary();
              	break;
              case 1:
                alert("发放成功！");
                this.showRecentSalary();
                break;
              default:
                alert('发送未成功！');
                this.showRecentSalary();
                break;
            }
          })
          .catch((error)=>{
            console.log('请求失败');
            console.log(error);
          })
    },

    // 删除某一员工工资
    handleCloseOnesRev(done) {
        this.$confirm('确认关闭？')
          .then(_ => {
            done();
          })
          .catch(_ => {});
      },

    //点击删除按钮
    setrevSal(rows){
        this.rev_staff_id=rows.staff_id;
        this.rev_s_id=rows.s_id;
        this.dialogOnesRev=true;
    },

    //删除本次
    revOne(){
        this.$axios.post('/api/Employee/revokeRecentSalary', {
          "staff_id":this.rev_staff_id,
          "s_id":this.rev_s_id,
        })

        .then(response=> {

            switch(response.data){
              case 0:
              	alert("删除失败！");
                this.dialogOnesRev=false;
              	break;
                case 1:
              	alert("删除成功！");
                this.dialogOnesRev=false;
                this.showRecentSalary();
              	break;
              default:
                alert("删除未成功！");
                this.msg=response.data;
                this.dialogOnesRev=false;
                break;
            }
          })
          .catch((error)=>{
            console.log('请求失败');
            console.log(error);
            this.dialogOnesRev=false;
          })
    },

    //删除全部
    revAll(){
        this.$axios.post('/api/Employee/removeHistorySalary?staff_id='+this.rev_staff_id, {
        //   "staff_id":"1111",
        })

        .then(response=> {

            switch(response.data){
              case 0:
              	alert("删除失败！");
                this.dialogOnesRev=false;
              	break;
                case 1:
              	alert("删除成功！");
                this.dialogOnesRev=false;
                this.showRecentSalary();
              	break;
              default:
                alert("删除未成功！");
                this.msg=response.data;
                this.dialogOnesRev=false;
                break;
            }
          })
          .catch((error)=>{
            console.log('请求失败');
            console.log(error);
            this.dialogOnesRev=false;
          })
    },


  //测试

  },

  
  
};
</script>

<style scoped>

  .buteu1{
  margin-top:-30px;
  position:absolute;
  left:130px;
}

.buteu2{
  margin-top:-30px;
  position:absolute;
  left:230px;
}

.buteu3{
    position:fixed;
    left:1360px;
    top:80px;
    z-index: 1;
  }

/* 工资相关按钮 */
/* 新增工资 */
.sal_add_but{
    position:absolute;
    /* right:365px; */
    right:204px;
    top:186px;
}

/* 批量删除
.sal_del_but{
    position:absolute;
    right:206px;
    top:186px;
} */

/* 发布工资 */
.sal_rel_but{
    position:absolute;
    right:50px;
    top:186px;
}

/* 新增员工按钮 */
.addEmployee{
  position:absolute;
  right:110px;
  top:186px;
}

/* 查询员工工资 */
.searchSalary{
  position:absolute;
  left:250px;
  top:186px;
}

.salBlock{
  position:absolute;
  left:535px;
  top:186px;
}

.search_sal_but{
    position:absolute;
    left:500px;
    top:0px;
}

/* 查询员工校验 */
  .search_sal_hintText{
    position:absolute;
    left:640px;
    top:-12px;
    width:200px;
    color: red;
  }

/* 员工工资桌面 */
.empSalTable{
  margin-top:80px;
}

/* 某位员工工资记录弹窗 */
.onesa_si{
    font-size:18px;
    position:absolute;
    left:20px;
    top:75px;
}

.onesa_j{
    font-size:18px;
    position:absolute;
    left:265px;
    top:75px;
}

.onesa_n{
    font-size:18px;
    position:absolute;
    left:460px;
    top:75px;
}

.onesa_table{
    width:560px;
    position:absolute;
    top:120px;
}

/* 修改某一员工奖金弹窗 */
.sal_p_newB{
    font-size:18px;
    position:absolute;
    left:20px;
    top:80px;
}

.sal_input_newB{
    position:absolute;
    left:246px;
    width:230px;
    top:90px;
}

.sal_hint_newB{
    /* background-color: rgb(83, 144, 202); */
    position:absolute;
    left:235px;
    width:150px;
    top:130px;
    color: red;
}

.sal_but2_newB{
    position:absolute;
    left:175px;
    top:190px;
}

.sal_but1_newB{
    position:absolute;
    left:315px;
    top:190px;
}

/* 删除某一员工工资弹窗 */
.sal_but1_rev{
    position:absolute;
    left:75px;
    top:120px;
}

.sal_but2_rev{
    position:absolute;
    left:235px;
    top:120px;
}

.sal_but3_rev{
    position:absolute;
    left:395px;
    top:120px;
}

</style>