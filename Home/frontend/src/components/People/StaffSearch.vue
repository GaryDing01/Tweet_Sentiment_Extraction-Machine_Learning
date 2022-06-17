<template>

<div style="line-height: 20px">

    <div>
    <el-form label-width="300px" size="medium">
 <div>
     <el-form-item label="用于查找的属性"  style="width:550px">
           <el-select v-model="form.attribute" placeholder="请选择属性" style="size:large;">
             <el-option label="员工编号" value="staff_id"></el-option>
             <el-option label="工作" value="job"></el-option>
             <el-option label="姓名" value="name"></el-option>
             <el-option label="联系方式" value="phone"></el-option>
            <el-option label="身份证号" value="ID_num"></el-option>
           </el-select>
        </el-form-item>

  <el-form-item size="middle" label="您要查找的员工信息" style="width:900px">
    <el-input
    style="width:500px"
  placeholder="请输入员工信息"
  v-model="form.value"
  clearable>
</el-input>
    <el-button type="primary" @click="showStaff()">确定</el-button>
    <el-button @click="callOff()" :class="{caos:caosS}">取消</el-button>
  </el-form-item>
      </div>
</el-form>
</div>

  <el-table
     :data="tableData.slice((currentPage-1)*pagesize,currentPage*pagesize)"
    style="width: 100%"
    max-height="600px"
    :default-sort = "{prop: 'staff_id', order: 'ascending'}"
    :row-class-name="tableRowClassName"
    >
    <el-table-column
      prop="staff_id"
      label="员工编号"
      sortable
      width="200px"
      align="center" >
    </el-table-column>

    <el-table-column
      prop="job"
      label="工作"
      width="200px" 
      align="center"
      column-key="job"
      :filters="[{text: '经理', value: '经理'}, {text: '财务', value: '财务'}, {text: '厨师', value: '厨师'}, 
      {text: '服务员', value: '服务员'},]"
      :filter-method="filterHandler">
    </el-table-column>

    <el-table-column
      prop="name"
      label="姓名"
      width="200px" 
      align="center">
    </el-table-column>

    <el-table-column
      prop="phone"
      label="联系方式"
      width="200px" 
      align="center">
    </el-table-column>

    <el-table-column
      prop="iD_num"
      label="身份证号"
      width="200px" 
      align="center">
    </el-table-column>

    <el-table-column
      prop="entry_date"
      label="入职日期"
      sortable
      width="200px" 
      align="center">
    </el-table-column>

  </el-table>

<el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :page-sizes="[5,10]"
        :page-size="pagesize"
        layout="total, sizes, prev, pager, next"
        :total="tableData.length">
       </el-pagination>

</div>
</template>


<script>
  export default {
    props:['requester_ID'],
    
    mounted(){
      this.$axios
      .get("/api/Canteen/getALLEmployeeInfo", {
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
    },
    
  data() {
    return {
       stripe:true,
        currentPage:1,
        pagesize:10,
        total:0,
        currentHeight:522,
        form:{
            attribute:'',
            value:'',
        },
      staff_id:'',
      tableData:[],
      caosS:true,
    };
  },

    methods: {
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

      //查找指定员工编号的元组
      showStaff(){
      this.$axios.get("/api/Canteen/getEmployeeInfobyAttr", {
      params: {
      attribute:this.form.attribute+'',
      value:this.form.value+'',
      }
      })
      .then(response=> {
            console.log(this.form.attribute);
            console.log(this.input);
            console.log(response.data);
            // alert("找到相关员工！");
            this.tableData=response.data;
      })
      .catch((error) => {
          console.log(error);
          alert("请求失败!");
        });
    },

      tableRowClassName({row,rowIndex}) {
        if (row.job === '经理') {
          return 'manager';
        } 
        else if (row.job === '财务') {
          return 'finance';
        }
        return '';
      },
     filterHandler(value, row, column) {
        const property = column['property'];
        return row[property] === value;
      },
      handleEdit(index, row) {
        console.log(index, row);
      },

      //显示所有的员工
      showAllStaff(){
        this.$axios.get("/api/Canteen/getALLEmployeeInfo", {
        params: {
        }
        })
        .then(response=> {
            this.tableData=response.data;  
          })
          .catch((error) => {
          console.log(error);
          alert("请求失败!");
        });
      },

      callOff(){
          this.form.attribute='';
          this.form.value='';
      },
    }
  }
</script>

<style>
  .el-table .manager {
    background: rgba(143, 143, 177, 0.6);
  }

  .el-table .finance {
    background: rgba(112, 23, 1, 0.6);
  }

  .caos{
      position:absolute;
      left:580px;
      top:1px;
  }
  .attrs{
      position:absolute;
      left:9000px !important;
      top:1px; 
      /* margin-left:20px; */
      /* background-color: aqua; */
  }
  .butss{
    position:fixed;
    left:1350px;
    top:88px;
    z-index: 1;
  }
</style>