<template>
<div style="line-height: 20px">
    <!-- <div>
    <el-form label-width="300px" size="mini"> -->
 <!-- <div>
  <el-form-item size="middle" label="查询指定编号的员工" style="width:900px">
    <el-input
    style="width:500px"
  placeholder="请输入顾客编号"
  v-model="customer_id"
  clearable>
</el-input>
    <el-button type="primary" @click="showVIP()">查询</el-button>
    <el-button type="primary" @click="showAllVIP()" class="butso">查看全部员工</el-button>
  </el-form-item>
      </div>
</el-form>
</div> -->

  <el-table
     :data="tableData.slice((currentPage-1)*pagesize,currentPage*pagesize)"
    style="width: 100%"
    max-height="480px"
    :default-sort = "{prop: 'staff_id', order: 'ascending'}"
    :row-class-name="tableRowClassName"
    >
    <el-table-column
      prop="customer_id"
      label="顾客编号"
      sortable
      width="250px" >
    </el-table-column>

    <el-table-column
      prop="customer_name"
      label="姓名"
      width="250px" 
      align="center">
    </el-table-column>

    <el-table-column
      prop="birthday"
      label="生日"
      sortable
      width="250px" 
      align="center">
    </el-table-column>

    <el-table-column
      prop="phone_num"
      label="联系方式"
      width="250px" 
      align="center">
    </el-table-column>

    <el-table-column
      prop="credit"
      label="积分"
      sortable
      width="250px" 
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
      .get("/api/Canteen/getALLCustomerInfo", {
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
    
  data() {
    return {
       stripe:true,
        currentPage:1,
        pagesize:10,
        total:0,
        currentHeight:522,
      staff_id:'',
      tableData:[]
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
      showVIP(){
      this.$axios.get("/api/Canteen/getCustomerInformation", {
      params: {
      "id":this.customer_id,
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

      tableRowClassName({row,rowIndex}) {
        if (row.credit === -1) {
          return 'normal';
        } 
        else {
          return 'vip';
        }
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
  .el-table .normal {
    background: rgb(184, 171, 171);
  }

  .el-table .vip {
    background: rgb(209, 209, 79);
  }

  /* .el-table .broken-row {
    background: rgba(128, 128, 128, 0.6);
  } */
  .butso{
    position:fixed;
    left:1350px;
    z-index: 1;
  }
</style>