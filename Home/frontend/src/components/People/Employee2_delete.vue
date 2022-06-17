<template>
    <div>

        <el-form ref="form" :model="form" label-width="120px">
        
        <el-form-item label="员工编号" style="width:360px;">
            <el-input v-model="form.staff_id"></el-input>
        </el-form-item>

        <el-form-item>
            <el-button type="primary" @click="showAuthority()" class="buted1">确定</el-button>
            <el-button @click="callOff()" class="buted2">取消</el-button>
        </el-form-item>
        </el-form>

    </div>

</template>


<script>

  export default {

    props:['requester_ID'],

    data () {
      return {
        form: {
          staff_id: '',
          },
      }  
    },

    methods:{

      //判断该员工是否被授权
      showAuthority(){
        this.$axios.get("/api/Canteen/employee_authority_check", {
      params: {
      requester_id:this.requester_ID+'',
      }
      })
      .then(response=> {
        console.log(this.requester_ID);
        switch(response.data){
          case 0:
            alert('您没有被授权！');
            break;
          default:
            this.deleteStaff();
            break;
        }
      })
      },

      deleteStaff(){

        this.$axios.post('/api/Canteen/deleteEmployee', {
          "staff_id":this.form.staff_id+'',
        })

        .then(response=> {
         
            switch(response.data){
              case -1:
              	alert("删除员工失败！");
                this.msg="删除员工失败！";
                this.callOff();
              	break;
              default:
                alert("删除员工成功！请通过查看功能进行验证");
                this.msg=response.data;
                this.callOff();
                break;
            }
          })
          .catch((error)=>{
            console.log('请求失败');
            console.log(error);
            this.callOff();
          })
        },

         backtoAll(){
          this.$router.push({path:'/StaffOverall'});
        },
        
        callOff(){
          this.form.staff_id='';
          this.$router.push({path:'/StaffRewrite'});
        }

    }
  }
  
</script>

<style>
.buted1{
  margin-top:0px;
  position:absolute;
  left:0px;
}

.buted2{
  margin-top:0px;
  position:absolute;
  left:100px;
}

.buted3{
    position:fixed;
    left:1360px;
    top:80px;
    z-index: 1;
  }
</style>