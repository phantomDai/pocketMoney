<template>
  <div class='index'>
    <div class="head">
      校园订单系统
    </div>
    <div class="main">
      <div class="left">
        <div class="goods">
          <div
            v-for="(item,index) in goodsList"
            :key="index"
            class="list"
          >
            <p class="title">
              {{item.name}}
            </p>
            <p class="info">
              {{item.info}}
            </p>
            <el-button
              @click="goodsAddCont(item)"
              type="primary"
              size="small"
            >添加购物车</el-button>
          </div>
        </div>
      </div>
      <div class="right">
        <p class="title">
          购物车
        </p>
        <div class="cart">
          <div
            v-for="(item,index) in cartList"
            :key="index"
            class="list"
          >
            <p class="name">{{item.name}}</p>
            <p
              @click="movueCartCont(index)"
              class="del"
            >X</p>
          </div>
        </div>

        <el-button
          class="cart-submit"
          @click="cartSubmitCont"
          type="primary"
        >确定下单</el-button>
      </div>
    </div>
    <!-- user login -->
    <el-dialog
      title="用户登录"
      :visible.sync="loginShow"
    >
      <el-form :model="loginForm">
        <el-form-item
          label="用户名"
          label-width="120px"
        >
          <el-input
            v-model="loginForm.username"
            auto-complete="off"
          ></el-input>
        </el-form-item>
        <el-form-item
          label="用户密码"
          label-width="120px"
        >
          <el-input
            type="password"
            v-model="loginForm.password"
            auto-complete="off"
          ></el-input>
        </el-form-item>

      </el-form>
      <div
        slot="footer"
        class="dialog-footer"
      >
        <el-button
          type="primary"
          @click="userLoginSubmitCont"
        >确 定</el-button>
      </div>
    </el-dialog>
    <!-- order -->
    <el-dialog
      title="用户下单"
      :visible.sync="orderShow"
    >
      <el-form :model="orderForm">
        <el-form-item
          label="配送时间"
          label-width="120px"
        >
          <el-input
            v-model="orderForm.time"
            auto-complete="off"
          ></el-input>
        </el-form-item>
        <el-form-item
          label="配送方式"
          label-width="120px"
        >
          <el-select
            v-model="orderForm.fenlei"
            placeholder="请选择配送方式"
          >
            <el-option
              label="自取"
              value="0"
            ></el-option>
            <el-option
              label="派送"
              value="1"
            ></el-option>
          </el-select>
        </el-form-item>
        <el-form-item
          label="是否打包"
          label-width="120px"
        >
          <el-select
            v-model="orderForm.dabao"
            placeholder="请选择打包方式"
          >
            <el-option
              label="打包"
              value="0"
            ></el-option>
            <el-option
              label="非打包"
              value="1"
            ></el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <div
        slot="footer"
        class="dialog-footer"
      >
        <el-button @click="orderShow = false">取 消</el-button>
        <el-button
          type="primary"
          @click="orderSubmitCont"
        >确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import querystring from "querystring";

export default {
  data() {
    return {
      loginShow: true,
      orderShow: false,
      loginForm: {
        username: "",
        password: ""
      },
      orderForm: {
        time: "",
        fenlei: "",
        dabao: ""
      },
      goodsList: [],
      cartList: [],
      userList: [],
      userInfo: {}
    };
  },
  mounted() {
    this.start();
  },
  methods: {
    start() {
      this.getGoodsList();
      this.getUserList();
    },
    // 用户登录
    userLoginSubmitCont() {
      let userList = this.userList;
      userList.map(item => {
        if (item.username == this.loginForm.username) {
          if (item.password == this.loginForm.password) {
            this.loginShow = false;
            this.$message({
              message: "登录成功",
              type: "success"
            });
            this.userInfo = item;
            return;
          }
        }
        this.$message.error("账号或密码错误");
      });
    },
    // 添加到购物车
    goodsAddCont(data) {
      this.cartList.push(data);
    },
    // 移除购物车
    movueCartCont(index) {
      this.cartList.splice(index, 1);
    },
    getUserList() {
      this.$http({
        url: `/user/list`,
        method: "POST"
      }).then(res => {
        let data = res.data.data.list;
        this.userList = data;
      });
    },
    getGoodsList() {
      this.$http({
        url: `/goods/list`,
        method: "POST"
      }).then(res => {
        let data = res.data.data.list;
        this.goodsList = data;
      });
    },
    // 购物车下的那
    cartSubmitCont() {
      this.orderShow = true;
    },
    // 确定下单
    orderSubmitCont() {
      this.$http({
        url: `/orders/add`,
        method: "POST",
        data: querystring.stringify({
          orderid: this.userInfo.phone,
          good: JSON.stringify(this.cartList),
          fenlei: this.orderForm.fenlei,
          dabao: this.orderForm.dabao,
          time: this.orderForm.time
        })
      }).then(res => {
        this.$message({
          message: "添加成功",
          type: "success"
        });
        this.orderShow = false;
        this.cartList = [];
        let formData = this.formData;
        Object.keys(formData).forEach(key => { 
          this.formData[key] = "";
        });
      });
    }
  },
  components: {}
};
</script>

<style lang='scss' scoped>
.index {
  position: relative;
  width: 1100px;
  margin: 0 auto;
}
.head {
  position: relative;
  width: 100%;
  text-align: center;
  height: 50px;
  font-size: 20px;
  line-height: 50px;
}

.main {
  position: relative;
  width: 100%;
  height: 800px;
  display: flex;
  top: 30px;
  .left {
    width: 100%;
    position: relative;
    height: 100%;
    .goods {
      position: relative;
      width: 100%;
      float: left;
      padding: 20px;
      box-sizing: border-box;
      .list {
        padding: 10px 20px;
        box-sizing: border-box;
        width: 100%;
        margin-bottom: 20px;
        height: 180px;
        box-shadow: 0 0 10px 5px #f0f0f0;
        border-radius: 5px;
        position: relative;
        .title {
          line-height: 40px;
          width: 100%;
          height: 40px;
          font-weight: 600;
          word-wrap: break-word;
        }
        .info {
          position: relative;
          width: 100%;
          height: 60px;
          color: #888;
          font-size: 14px;
          float: left;
        }
        .el-button {
          position: absolute;
          right: 20px;
          bottom: 20px;
        }
      }
    }
  }
  .right {
    width: 100%;
    position: relative;
    height: 100%;
    padding: 20px;
    box-sizing: border-box;
    .cart-submit {
      position: absolute;
      bottom: 20px;
      right: 20px;
    }
    .title {
      position: relative;
      width: 100%;
      text-align: center;
      height: 50px;
      font-size: 20px;
      line-height: 50px;
    }
    .cart {
      width: 80%;
      box-sizing: border-box;
      padding: 0 10px;
      margin: 0 auto;
      margin-top: 20px;
      .list {
        width: 100%;
        height: 45px;
        line-height: 45px;
        box-sizing: border-box;
        border-radius: 5px;
        padding: 0 10px;
        margin-bottom: 20px;
        box-shadow: 0 0 10px 5px #f0f0f0;
        .name {
          float: left;
          user-select: none;
        }
        .del {
          float: right;
          cursor: pointer;
          user-select: none;
        }
      }
    }
  }
}
</style>

