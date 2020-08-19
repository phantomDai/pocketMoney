<template>
  <div class='index'>
    <div class="layout">
      <Layout @handleSelect="handleSelectCont" />
    </div>
    <div class="main">
      <div class="main-cont">
        <User v-if="layoutIndex== 1" />
        <Cart v-if="layoutIndex== 2" />
        <Goods v-if="layoutIndex== 3" />
        <Order v-if="layoutIndex== 4" />
      </div>
    </div>
  </div>
</template>

<script>
import Layout from "@/components/layout";
//
import User from "@/components/user";
import Cart from "@/components/cart";
import Goods from "@/components/goods";
import Order from "@/components/order";

export default {
  data() {
    return {
      layoutIndex: 1
    };
  },
  mounted() {},
  methods: {
    handleSelectCont(index) {
      this.layoutIndex = index;
    }
  },
  components: {
    Order,
    Goods,
    Cart,
    Layout,
    User
  }
};
</script>

<style lang='scss' scoped>
.index {
  position: absolute;
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: left;
  min-width: 1200px;
}
.layout {
  position: relative;
  width: 200px;
  height: 100%;
}
.main {
  position: relative;
  width: 100%;
  height: 100%;
  padding: 20px;
  box-sizing: border-box;
  min-width: 1000px;
  .main-cont {
    position: relative;
    width: 100%;
    height: 100%;
    padding: 20px;
    box-sizing: border-box;
    box-shadow: 0 0 10px 5px #f0f0f0;
    border-radius: 5px;
  }
}
</style>
