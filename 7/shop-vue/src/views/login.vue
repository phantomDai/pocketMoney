<template>
  <div class='index'>
    <p class="title">
      森林病虫害预防系统-登录
    </p>
    <div class="login">
      <el-input
        placeholder="请输入账号"
        v-model="username"
        clearable
      >
      </el-input>

      <el-input
        placeholder="请输入密码"
        v-model="password"
        clearable
      >
      </el-input>

    </div>
    <div class="sublit">
      <el-button type="primary">登录</el-button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: "",
      password: ""
    };
  },
  mounted() {},
  methods: {},
  components: {}
};
</script>

<style lang='scss' scoped>
.login {
  position: relative;
  width: 100%;
  padding: 0 10px;
  box-sizing: border-box;
  top: 30px;
  .el-input {
    margin-bottom: 20px;
    width: 100%;
    flex: 1;
  }
}
.sublit {
  width: 100%;
  height: 45px;
  position: relative;
  top: 20px;
  display: flex;
  justify-content: center;
  .el-button {
    position: relative;
    margin: 0 auto;
    text-align: center;
    top: 20px;
  }
}

.title {
  position: relative;
  width: 100%;
  font-size: 20px;
  line-height: 40px;
  height: 40px;
  text-align: center;
  margin-top: 20px;
}
</style>
 