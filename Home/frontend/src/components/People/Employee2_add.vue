<template>
    <div>
        <el-form ref="form" :model="form" label-width="120px">
        
        <el-form-item label="工作" style="width:360px;">
            <el-input v-model="form.job"></el-input>
        </el-form-item>
        <el-form-item label="姓名" style="width:360px;">
            <el-input v-model="form.name"></el-input>
        </el-form-item>
        <el-form-item label="电话" style="width:360px;">
            <el-input v-model="form.phone"></el-input>
        </el-form-item>
        <el-form-item label="身份证号" style="width:360px;">
            <el-input v-model="form.ID_num"></el-input>
        </el-form-item>

        <el-form-item>
            <el-button type="primary" @click="showAuthority()" class="butea1">确定</el-button>
            <el-button @click="callOff()" class="butea2">取消</el-button>
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
          job: '',
          name: '',
          phone: '',
          ID_num: '',
          }
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
        switch(response.data){
          case 0:
            alert('您没有被授权！');
            break;
          default:
            this.addStaff();
            break;
        }
      })
      .catch((error) => {
          console.log(error);
          alert("请求失败!");
        });
      },

      addStaff(){
        this.$axios.post("/api/Canteen/addEmployee", {

        "job": this.form.job,
        "name": this.form.name,
        "phone": this.form.phone,
        "id_num": this.form.ID_num,
        
        })
        .then(response=> {
            switch(response.data){
              case -1:
              	alert("添加员工失败！");
                this.msg="添加员工失败！";
                this.callOff();
              	break;
              default:
                alert("添加员工成功！请通过查看功能进行验证");
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
          this.$router.push({path:'/StaffOverall'})
        },

        callOff(){
          this.form.job='';
          this.form.name='';
          this.form.phone='';
          this.form.ID_num='';
          this.$router.push({path:'/StaffRewrite'});
        },
    }
  }
  
</script>

<style>
.butea1{
  margin-top:0px;
  position:absolute;
  left:0px;
}

.butea2{
  margin-top:0px;
  position:absolute;
  left:100px;
}
.butea3{
    position:fixed;
    left:1360px;
    top:80px;
    z-index: 1;
  }
</style>