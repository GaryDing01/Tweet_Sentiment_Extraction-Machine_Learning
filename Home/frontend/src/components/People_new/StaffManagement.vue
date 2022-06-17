<template>
  <div>
    <div>

      <el-dialog
        title="修改员工信息"
        :visible.sync="dialogVisible"
        width="30%"
        :before-close="handleClose">
        <!-- <span>这是一段信息</span> -->
        
        <div style="height:150px">
         <el-form ref="form" :model="form" label-width="120px">
  
        <!-- <el-form-item label="目标员工编号" style="width:330px">
            <el-input v-model="form.staff_id" placeholder="请输入编号"></el-input>
        </el-form-item> -->

        <el-form-item label="要更改的属性" style="width:330px">
            <el-select v-model="form.attribute" placeholder="请选择属性">
            <el-option label="工作" value="job"></el-option>
            <el-option label="姓名" value="name"></el-option>
            <el-option label="联系方式" value="phone"></el-option>
            <el-option label="身份证号" value="ID_num"></el-option>
            </el-select>
        </el-form-item>
  
        <el-form-item label="新的数值" style="width:330px">
            <el-input v-model="form.newvalue" placeholder="请输入数值"></el-input>
            <p class="emp_hint_rewrite">{{this.rewrite_hint}}</p>
        </el-form-item>
        </el-form>
        </div>

        <span slot="footer" class="dialog-footer">
          <el-button @click="dialogVisible = false, callOff()" class="buteu2">取 消</el-button>
          <el-button type="primary" @click="onUpdate()" class="buteu1">确 定</el-button>
        </span>
      </el-dialog>

</div>
    <div style="line-height: 50px">
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/StaffEnter' }"
          >首页</el-breadcrumb-item
        >
        <el-breadcrumb-item>员工管理</el-breadcrumb-item>
        <el-breadcrumb-item>员工信息</el-breadcrumb-item>
      </el-breadcrumb>
    </div>

    <div style="line-height: 30px">
      <el-card class="box-card" style="margin-top: 20px;">
 
 <!-- 查询员工 -->
 <div class="searchEmployee">
           <el-select v-model="search_attribute" placeholder="请选择属性" style="size:large;">
             <el-option label="员工编号" value="staff_id"></el-option>
             <el-option label="工作" value="job"></el-option>
             <el-option label="姓名" value="name"></el-option>
             <el-option label="联系方式" value="phone"></el-option>
            <el-option label="身份证号" value="ID_num"></el-option>
           </el-select>

    <el-input style="width:300px" placeholder="请输入员工信息" v-model="search_value" clearable></el-input>
    <el-button type="primary" icon="el-icon-search" @click="checkSearch()">搜索</el-button>
    <p class="search_hintText">{{search_hint}}</p>

  </div>
      
<!-- </el-form> -->
        <el-button type="success" size="medium" style="line-height:20px" @click="addNewEmp()" class="addEmployee">新增员工</el-button>
        <!-- <el-button icon="el-icon-refresh" circle @click="getAllIngredient()"></el-button> -->

<div class="employeeTable">
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
          <el-table-column prop="staff_id" label="员工编号" width="150%" align="center" sortable></el-table-column>
          <el-table-column prop="job" label="工作" width="150%" align="center" column-key="job" :filters="[{text: '经理', value: '经理'}, {text: '财务', value: '财务'}, {text: '厨师', value: '厨师'}, 
      {text: '服务员', value: '服务员'},]"
      :filter-method="filterHandler"></el-table-column>
          <el-table-column prop="name" label="姓名" width="160%" align="center"></el-table-column>
          <el-table-column prop="phone" label="联系方式" width="190%" align="center"></el-table-column>
          <el-table-column prop="iD_num" label="身份证号" width="160%" align="center"></el-table-column>
          <el-table-column prop="entry_date" label="入职日期" width="190%" align="center" sortable></el-table-column>
          <el-table-column fixed="right" label="操作" width="190%" align="center">
            <template slot-scope="scope">
              <el-button type="primary" size="mini" @click="setstaffRow(scope.row)">修改</el-button>
              <el-button type="danger" size="mini" @click="deleteEmpRow(scope.row)">删除</el-button>
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

        <!-- 新增员工弹窗 -->
        <div>
    <el-dialog
        title="新增员工"
        :visible.sync="dialogEmpAdd"
        width="36%"
        :before-close="handleCloseEmpAdd"
        >

        <div style="height:290px;">
        <el-form ref="form_add" :model="form_add" label-width="120px" style="position:absolute;left:50px;">
        
        <div>
        <el-form-item label="工作" style="width:360px;" :rules="[{ required: true, message: '工作不能为空'},]" >
            <el-input placeholder="请输入汉字" v-model="form_add.job" ></el-input>
        </el-form-item>
        </div>
        <el-form-item label="姓名" style="width:360px;" :rules="[{ required: true, message: '姓名不能为空'},]">
            <el-input placeholder="请输入汉字" v-model="form_add.name"></el-input>
        </el-form-item>
        <el-form-item label="电话号码" style="width:360px;" :rules="[{ required: true, message: '电话号码不能为空'},]">
            <el-input placeholder="请输入号码，电话为11位数字" v-model="form_add.phone"></el-input>
        </el-form-item>
        <el-form-item label="身份证号" style="width:360px;" :rules="[{ required: true, message: '身份证号不能为空'},]">
            <el-input placeholder="请输入身份证号" v-model="form_add.ID_num"></el-input>
        </el-form-item>
        <p style="color:red;">{{this.empAdd_hint}}</p>

        </el-form>
        </div>

        <span slot="footer" class="dialog-footer">
          <el-button @click="calloff_add()" class="emp_add_but2">取 消</el-button>
          <el-button type="primary" @click="checkAdd()" class="emp_add_but1">确 定</el-button>
        </span>
        
      </el-dialog>
</div>

      </el-card>

    </div>

  </div>
</template>

<script>

export default {
    mounted(){
    this.showAllStaff();
    },

    data() {
    return {
       stripe:true,
        currentPage:1,
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
      search_attribute:'',
      search_value:'',
      search_hint:'',

      //修改员工信息
      rewrite_hint:'',

      //新增员工
      dialogEmpAdd:false,
      form_add:{
        job:'',
        name:'',
        phone:'',
        ID_num:'',
      },
      empAdd_hint:'',

      //删除员工
      emp_del_staff_id:'',
    };
  },


   methods: {
      handleClose(done) {
        this.$confirm('确认关闭？')
          .then(_ => {
            this.callOff();
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

    filterHandler(value, row, column) {
        const property = column['property'];
        return row[property] === value;
      },
    handleEdit(index, row) {
        console.log(index, row);
    },

    //显示所有的员工
    async  showAllStaff(){
        this.$axios.get("/api/Employee/getALLEmployeeInfo", {
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
    console.log(rows);
    this.rowID=rows.staff_id;
  },
  
  //点击确定按钮
  onUpdate(){
        
        if(this.form.attribute==''||this.form.newvalue=='')
        {
          this.rewrite_hint='*输入不能为空！';
          return ;
        }
        else if(this.form.attribute=="job")
        {
          if(/^[\u4e00-\u9fa5]*$/.test(this.form.newvalue)===false)
          {
            this.rewrite_hint="*员工工作由汉字组成。"
            return;
          }
          if(this.form.newvalue!="经理"&&this.form.newvalue!="厨师"&&this.form.newvalue!="服务员"&&this.form.newvalue!="财务")
          {
            this.rewrite_hint="*暂无该工作。"
            return;
          }
        }
        else if(this.form.attribute=="name")
        {
          if(/^[\u4e00-\u9fa5]*$/.test(this.form.newvalue)===false)
          {
            this.rewrite_hint="*员工姓名由汉字组成。"
            return;
          }
        }
        else if(this.form.attribute=="phone")
        {
          if(/^[1][3,4,5,7,8][0-9]{9}$/.test(this.form.newvalue)===false)
          {
            this.rewrite_hint="*电话输入错误。"
            return;
          }
        }
        else if(this.form.attribute=="ID_num")
        {
          if(/^[1-9]\d{5}(18|19|20|(3\d))\d{2}((0[1-9])|(1[0-2]))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$/.test(this.form.newvalue)===false)
          {
            this.rewrite_hint="*身份证输入错误。"
            return;
          }
        }

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
          this.rewrite_hint='';
        },

  // 查询员工
  checkSearch(){
    if(this.search_attribute==''||this.search_value=='')
    {
      this.search_hint='*查询不能为空！';
      return;
    }
    if(this.search_attribute=="staff_id")
    {
      if(/^[0-9]*$/.test(this.search_value)===false)
      {
        this.search_hint="*员工编号由数字组成。"
        return;
      }
    }
    else if(this.search_attribute=="job")
    {
      if(/^[\u4e00-\u9fa5]*$/.test(this.search_value)===false)
      {
        this.search_hint="*员工工作由汉字组成。"
        return;
      }
      if(this.search_value!="经理"&&this.search_value!="厨师"&&this.search_value!="服务员"&&this.search_value!="财务")
      {
        this.search_hint="*暂无该工作。"
        return;
      }
    }
    else if(this.search_attribute=="name")
    {
      if(/^[\u4e00-\u9fa5]*$/.test(this.search_value)===false)
      {
        this.search_hint="*员工姓名由汉字组成。"
        return;
      }
    }
    else if(this.search_attribute=="phone")
    {
      if(/^[1][3,4,5,7,8][0-9]{9}$/.test(this.search_value)===false)
      {
        this.search_hint="*电话输入错误。"
        return;
      }
    }
    else if(this.search_attribute=="ID_num")
    {
      if(/^[1-9]\d{5}(18|19|20|(3\d))\d{2}((0[1-9])|(1[0-2]))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$/.test(this.search_value)===false)
      {
        this.search_hint="*身份证输入错误。"
        return;
      }
    }
    this.search_hint="";
    this.searchEmployee();
  },

  searchEmployee(){
     this.$axios.get("/api/Employee/getEmployeeInfobyAttr", {
      params: {
      attribute:this.search_attribute+'',
      value:this.search_value+'',
      }
      })
      .then(response=> {
            // console.log(this.form.attribute);
            // console.log(this.input);
            // console.log(response.data);
            // alert("找到相关员工！");
            this.tableData=response.data;
            this.search_attribute="";
            this.search_value="";
      })
      .catch((error) => {
          console.log(error);
          alert("请求失败!");
          this.search_attribute="";
          this.search_value="";
        });
  },

  // 新增员工
  handleCloseEmpAdd(done) {
        this.$confirm('确认关闭？')
          .then(_ => {
            this.calloff_add();
            done();
          })
          .catch(_ => {});
      },

  //点击新增员工按钮
  addNewEmp(){
    this.dialogEmpAdd=true;
  },

  calloff_add(){
    this.empAdd_hint='';
    this.form_add.job='';
    this.form_add.name='';
    this.form_add.phone='';
    this.form_add.ID_num='';
    this.dialogEmpAdd=false;
  },

  checkAdd(){
    if( this.form_add.job==''||this.form_add.name==''||this.form_add.phone==''||this.form_add.ID_num=='')
    {
      this.empAdd_hint='*输入不能为空！';
      return ;
    }
    if(/^[\u4e00-\u9fa5]*$/.test(this.form_add.job)===false)
    {
      this.empAdd_hint="*员工工作由汉字组成。"
      return;
    }
    if(this.form_add.job!="经理"&&this.form_add.job!="厨师"&&this.form_add.job!="服务员"&&this.form_add.job!="财务")
    {
      this.empAdd_hint="*暂无该工作。"
      return;
    }
    if(/^[\u4e00-\u9fa5]*$/.test(this.form_add.name)===false)
    {
      this.empAdd_hint="*员工姓名由汉字组成。"
      return;
    }
    if(/^[1][3,4,5,7,8][0-9]{9}$/.test(this.form_add.phone)===false)
    {
      this.empAdd_hint="*电话输入错误。"
      return;
    }
    if(/^[1-9]\d{5}(18|19|20|(3\d))\d{2}((0[1-9])|(1[0-2]))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$/.test(this.form_add.ID_num)===false)
    {
      this.empAdd_hint="*身份证输入错误。"
      return;
    }
    this.empAdd_hint=""
    this.empAdd()
  },

  empAdd(){
    this.$axios.post("/api/Employee/addEmployee", {

        "job": this.form_add.job,
        "name": this.form_add.name,
        "phone": this.form_add.phone,
        "id_num": this.form_add.ID_num,
        
        })
        .then(response=> {
          console.log(response.data);
            switch(response.data){
              case -1:
              	alert("添加员工失败！");
                this.calloff_add();
              	break;
              default:
                alert("添加员工成功！");
                this.showAllStaff();
                this.calloff_add();
                break;
            }
          })
          .catch((error)=>{
            console.log('请求失败');
            console.log(error);
            this.showAllStaff();
            this.calloff_add();
          })
  },

  //删除员工
  deleteEmpRow(rows){
    this.emp_del_staff_id=rows.staff_id;
    console.log( this.emp_del_staff_id);

    this.$axios
      .post("/api/Employee/deleteEmployee", {
        "staff_id": this.emp_del_staff_id,
      })
      .then((response) => {
        switch (response.data) {
          case -1:
            alert("删除员工失败！");
            break;
          default:
            alert("删除员工成功！");
            this.showAllStaff();
            break;
        }
      }) .catch((error)=>{
        console.log('请求失败');
        console.log(error);
      });
      
  },

  //测试
  async Hellotime(){
    console.log("Hello!");
  },
  async modifyRow(rows) {
      this.$router.push({path: "/setUpdateIngredient",query:{ingre_name:rows.ingre_name,buy_date:rows.buy_date,}});
    },

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

/* 新增员工按钮 */
.addEmployee{
  position:absolute;
    right:50px;
    top:186px;
}

/* 查询员工按钮 */
.searchEmployee{
  position:absolute;
  left:250px;
  top:186px;
}

/* 查询员工校验 */
  .search_hintText{
    position:absolute;
    left:640px;
    top:-12px;
    width:200px;
    color: red;
  }

/* 员工桌面 */
.employeeTable{
  margin-top:80px;
}

/* 修改员工提示 */
.emp_hint_rewrite{
  position:absolute;
    left:0px;
    width:150px;
    top:30px;
    color: red;
}

/* 新增员工 */
.emp_add_but1{
  position:absolute;
  left:275px;
  top:380px;
}

.emp_add_but2{
  position:absolute;
  left:170px;
  top:380px;
}

</style>