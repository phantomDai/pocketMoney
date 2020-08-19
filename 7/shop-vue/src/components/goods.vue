<template>
  <div class='base'>
    <el-table
      :data="dataList"
      style="width: 100%"
    >
      <el-table-column
        v-for="(item,index) in objList"
        :key="index"
        :label="item.val"
      >
        <div slot-scope="scope">
          {{scope.row[item.key]}}
        </div>
      </el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button
            size="mini"
            type="danger"
            @click="handleDelete(scope.row)"
          >删除</el-button>
          <el-button
            size="mini"
            type="danger"
            @click="handleUpdate(scope.row)"
          >修改</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-button
      class="add-button"
      type="primary"
      @click="handleAdd()"
    >添加</el-button>
    <el-dialog
      :title="formTitle"
      :visible.sync="dialogFormVisible"
    >
      <el-form :model="formData">
        <el-form-item
          v-for="(item,index) in objList"
          :key="index"
          :label="item.val"
          label-width="140px"
        >
          <el-input
            v-model="formData[item.key]"
            auto-complete="off"
            :placeholder="formData[item.key]"
          ></el-input>

        </el-form-item>
      </el-form>
      <div
        slot="footer"
        class="dialog-footer"
      >
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button
          type="primary"
          @click="formDataSubmit"
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
      dialogFormVisible: false,
      dialogFormState: 0, // 0 添加 1删除
      formTitle: "操作",
      objList: [],
      dataObj: {
        number: "编号",
        name: "名称",
        info: "信息"
      },
      formData: {},
      dataList: [],
      url: "goods"
    };
  },
  mounted() {
    this.start();
  },
  methods: {
    start() {
      let data = this.dataObj;
      this.formData = this.dataObj;
      Object.keys(data).forEach(key => {
        this.objList.push({
          key: key,
          val: data[key]
        });
        this.formData[key] = "";
      });
      this.getDataList();
    },
    getDataList() {
      this.dialogFormVisible = false;
      this.$http({
        url: `/${this.url}/list`,
        method: "POST"
      }).then(res => {
        this.dataList = res.data.data.list;
      });
    },
    updateCont() {
      console.log("update");
      this.$http({
        url: `/${this.url}/update`,
        method: "POST",
        data: querystring.stringify({
          ...this.formData,
          id: this.formData.id
        })
      }).then(res => {
        this.$message({
          message: "修改成功",
          type: "success"
        });
        this.getDataList();
      });
    },
    handleAdd() {
      this.dialogFormState = 0;
      this.dialogFormVisible = true;
      let formData = this.formData;
      Object.keys(formData).forEach(key => {
        formData[key] = "";
      });
    },
    handleUpdate(row) {
      this.dialogFormState = 1;
      this.dialogFormVisible = true;
      let formData = this.formData;
      Object.keys(formData).forEach(key => {
        formData[key] = row[key];
      });
      this.formData.id = row.id;
    },
    handleDelete(row) {
      console.log("submit");
      this.$http({
        url: `/${this.url}/delete`,
        method: "POST",
        data: querystring.stringify({
          id: row.id
        })
      }).then(res => {
        this.$message({
          message: "删除成功",
          type: "success"
        });
        this.getDataList();
      });
    },
    formDataSubmit() {
      if (this.dialogFormState == 0) {
        this.addCont();
        return;
      }
      if (this.dialogFormState == 1) {
        this.updateCont();
        return;
      }
    },
    addCont() {
      console.log("submit");
      this.$http({
        url: `/${this.url}/add`,
        method: "POST",
        data: querystring.stringify(this.formData)
      }).then(res => {
        this.$message({
          message: "添加成功",
          type: "success"
        });
        this.getDataList();
      });
      this.dialogFormVisible = false;
    }
  },
  components: {}
};
</script>

<style lang='scss' scoped>
.add-button {
  position: relative;
  top: 30px;
}
</style>
