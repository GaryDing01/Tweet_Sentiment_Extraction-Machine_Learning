<template>
<div>
  <div style="line-height: 50px">
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/VIP200' }">返回</el-breadcrumb-item>
      <el-breadcrumb-item>会员管理</el-breadcrumb-item>
    </el-breadcrumb>
  </div>

  <div style="line-height:30px">     
    <el-card class="box-card" style="margin-top:20px">
    <el-table
      v-loading="loading"
      element-loading-text="拼命加载中"
      element-loading-spinner="el-icon-loading"
      :data="VIPList.slice((currentPage-1)*pagesize,currentPage*pagesize)"
      style="width: 100%"
      max-height="400" border stripe>
      <el-table-column label="#" type="index"></el-table-column> 
      <el-table-column
        prop="customer_id"
        label="会员编号"
        sortable
        width="210"
        align="center">
      </el-table-column>
      <el-table-column
        prop="customer_name"
        label="会员姓名"
        width="180"
        align="center">
      </el-table-column>
      <el-table-column
        prop="phone_num"
        label="手机号"
        width="220"
        align="center">
      </el-table-column>
      <el-table-column
        prop="birthday"
        label="生日" 
        width="220"
        align="center">
      </el-table-column>
      <el-table-column
        prop="credit"
        label="积分"
        width="200"
        align="center">
      </el-table-column>
      <el-table-column
        label=""
        align="center">
        <template slot-scope="scope">
          <!-- <el-button size="mini" type="text" @click="deleteRow(scope.$index, scope.row)">删除</el-button> -->
        </template>
      </el-table-column>
    </el-table>
    <!-- 分页器 -->
    <el-pagination
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
      :page-sizes="[5,10]"
      :page-size="pagesize"
      layout="total, sizes, prev, pager, next"
      :total="VIPList.length">
    </el-pagination>
  </el-card>
  </div>
</div>
</template>

<script>
export default {
  methods: {
      async deleteRow(index, rows) {
        const confirm_result= await this.$confirm('此操作将永久删除该订单, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).catch(() => {
           this.$message({
            type: 'info',
            message: '已取消删除'
          });          
        });
        if(confirm_result!=='confirm'){
          return this.$message.info('已取消删除')
        }
        else{
          await this.$axios.post('/api/VIP/removeCustomer',{             //删除历史订单？
            customer_id:rows.customer_id+'',
          })
          .then(res=>{
            switch(res.data){
              case 1:
                break;
              case -1:
                return this.$message.info('该用户有未支付的订单，无法注销！');
              default:
                return this.$message.info('连接失败，订单未移除，请重试！');
            }
          })
          this.getVIPList();
          return this.$message.success('已删除')
        }
      },
    async getVIPList() {
      this.loading=true
      await this.$axios.get('/api/VIP/getAllCustomer',{})
        .then(response=>{
          this.VIPList=response.data
          this.total = response.data.total
        }) 
        this.loading=false
    },
    handleSizeChange(val) {
      this.pagesize = val;
      if(val==5)
        this.currentHeight = 285;
      else if(val==10)
        this.currentHeight = 522;
        this.getVIPList()
    },

    handleCurrentChange(val) {
      this.currentPage = val;
      this.getVIPList()
    },
  },
  mounted () {
    this.getVIPList()
  },
  data(){
    return{
      formData: {
        createTime:[],
      },
      total: 0,
      currentHeight:522,
      currentPage:1,
      pagesize:5,
      VIPList: [],
      chosen_dish:[],
      grid:false,
      loading: true,
      dloading:true
    }
  }
}
</script>

<style scoped>

</style>