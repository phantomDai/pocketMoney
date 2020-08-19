<template>
  <div class='layout'>
    <el-menu
      default-active="1"
      class="el-menu-vertical-demo"
      @select="handleSelect"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b"
    >
      <el-menu-item
        v-for="(item,index) in menu"
        :key="index"
        :index="item.index"
      >
        <i class="el-icon-menu"></i>
        <span slot="title">{{item.name}}</span>
      </el-menu-item>
    </el-menu>
  </div>
</template>
 
<script>
export default {
  data() {
    return {
      menu: [
        {
          index: "1",
          name: "用户"
        },
        // {
        //   index: "2",
        //   name: "购物车"
        // },
        {
          index: "3",
          name: "商品"
        },
        {
          index: "4",
          name: "订单"
        }
      ]
    };
  },
  mounted() {},
  methods: {
    handleSelect(key) {
      this.$emit("handleSelect", key);
    }
  },
  components: {}
};
</script>

<style lang='scss' scoped>
.layout {
  position: relative;
  width: 100%;
  height: 100%;
}
.el-menu {
  height: 100%;
}
</style>
