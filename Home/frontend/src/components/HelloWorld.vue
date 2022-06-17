<!-- html部分 -->
<template>
  <div>
    <span>{{ serverResponse }}</span>
    <!--这里使用{{}}来引用JavaScript中赋给this的值-->
    <button @click="getData">get data</button>
  </div>
</template>
<!-- js部分 -->
<script>
import axios from 'axios';
export default {
  data: function () {
    return {
      serverResponse: 'res_test'
    };
  },
  methods: {
    getData() {
      // 设置对应python的接口，这里使用的是localhost:5000
      const path = 'http://127.0.0.1:5000/open';
      axios.get(path).then(res => {
        // 这里服务器返回response为一个json对象
        // 通过.data来访返回的数据，然后在通过.变量名进行访问
        // 可以直接通过response.data取得key-value
        var msg = res.data.msg;
        this.serverResponse = msg; // 因为不能直接使用this作为指针，因此在这之前将this赋给了then指针
        console.log('Success' + res.status + ',' + res.data + ',' + msg); // 成功后显示提示
      }).catch(error => {
        console.error(error);
      });
    }
  },
}
</script>
<!-- css部分 -->
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
