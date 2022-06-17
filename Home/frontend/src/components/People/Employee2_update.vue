<template>
    
    <div>

        <el-form ref="form" :model="form" label-width="120px">
  
        <el-form-item label="目标员工编号" style="width:330px">
            <el-input v-model="form.staff_id" placeholder="请输入编号"></el-input>
        </el-form-item>

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
        </el-form-item>
  
        <el-form-item>
            <el-button type="primary" @click="showAuthority()" class="buteu1">更新</el-button>
            <el-button @click="callOff()" class="buteu2">取消</el-button>
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
          employee_id: '',
          attribute: '',
          newdata:'',
        }
      }
    },

    methods:{
      //判断该员工是否被授权
      showAuthority(){
        this.$axios.get("/api/Employee/employee_authority_check", {
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
            this.onUpdate();
            break;
        }
      })
      },

      onUpdate(){

        this.$axios.post('/api/Employee/updateEmployee', {
          "staff_id":this.form.staff_id,
          "attribute":this.form.attribute,
          "newvalue":this.form.newvalue,
        })

        .then(response=> {

        console.log(response);
        console.log(response.data);
        console.log(response.status);
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

         backtoAll(){
          this.$router.push({path:'/StaffOverall'});
        },

        callOff(){
          this.form.staff_id='';
          this.form.attribute='';
          this.form.newvalue='';
          this.$router.push({path:'/StaffRewrite'});
        },
      }
    }
  
</script>

<style>
.buteu1{
  margin-top:0px;
  position:absolute;
  left:0px;
}

.buteu2{
  margin-top:0px;
  position:absolute;
  left:100px;
}

.buteu3{
    position:fixed;
    left:1360px;
    top:80px;
    z-index: 1;
  }
</style>