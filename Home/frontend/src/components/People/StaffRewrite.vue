<template>
<div style="line-height: 20px">
    <div>
    <el-form label-width="300px" size="mini">
 <!-- <div>
  <el-form-item size="middle" label="查询指定编号的员工" style="width:900px">
    <el-input
    style="width:500px"
  placeholder="请输入员工编号"
  v-model="staff_id"
  clearable>
</el-input>
    <el-button type="primary" @click="showStaff()">查询</el-button>
    
  </el-form-item>
      </div> -->
    <h2 class="hcr">请选择您希望进行的操作：</h2>
    <el-button type="success" round @click="showAuthority_Add()" class="funacr">添加</el-button>
    <el-button type="info" round @click="showAuthority_Delete()" class="fundcr">删除</el-button>
   <el-button type="warning" round @click="showAuthority_Update()" class="funucr">更新</el-button>
</el-form>
</div>

  <el-table
    class="tr"
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
      .get("/api/Employee/getALLEmployeeInfo", {
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
      staff_id:'',
      tableData:[],
      funacrS:true,
      fundcrS:true,
      funucrS:true,
    };
  },

    methods: {
       //判断该员工是否被授权（跳转至查找相应的员工）
      showAuthority_Add(){
          console.log(this.requester_ID);
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
            this.$router.push({path:'/Employee2_add'})
            break;
        }
      })
      .catch((error) => {
          console.log(error);
          alert("请求失败!");
        });
      },

      showAuthority_Delete(){
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
            this.$router.push({path:'/Employee2_delete'})
            break;
        }
      })
      .catch((error) => {
          console.log(error);
          alert("请求失败!");
        });
      },

      showAuthority_Update(){
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
            this.$router.push({path:'/Employee2_update'})
            break;
        }
      })
      .catch((error) => {
          console.log(error);
          alert("请求失败!");
        });
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

      //查找指定员工编号的元组
      showStaff(){
      this.$axios.get("/api/Employee/getEmployeeInfobyAttr", {
      params: {
      attribute:"staff_id",
      value:this.staff_id,
      }
      })
      .then(response=> {
        console.log(response.data);
            alert("找到相关员工！");
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
        // else if (row.job === '损坏') {
        //   return 'broken-row';
        // }
        return '';
      },
     filterHandler(value, row, column) {
        const property = column['property'];
        return row[property] === value;
      },
      handleEdit(index, row) {
        console.log(index, row);
      }
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

  /* .el-table .broken-row {
    background: rgba(128, 128, 128, 0.6);
  } */
  .funacr{
      position:absolute;
      left:560px;
      top:110px;
  }
  .fundcr{
      position:absolute;
      left:635px;
      top:110px;
  }
  .funucr{
      position:absolute;
      left:720px;
      top:110px;
  }
  .tr{
      margin-top:100px;
  }
  .hcr{
      position:absolute;
      left:230px;
      top:100px;
      /* font-size:100px; */
      /* font-style:initial; */
  }
  .butao{
    position:fixed;
    left:1350px;
    z-index: 1;
  }
</style>