<template>
    <header>
        <div class="title">
<!--            <el-button @click="handleMenu" plain icon="el-icon-menu" size="mini"></el-button>-->
            <h3 style="color: white">基于小样本学习的新闻分类系统</h3>
        </div>
    </header>

</template>

<script>
    export default {
        name: "CommonHeader.vue",
        methods:{
            handleMenu(){
                this.$store.commit('collapseMenu')
            }
        }
    }

</script>

<style lang="less" scoped>
header{
    display: flex;
    height: 100%;
    justify-content: space-between;
    align-items: center;
}.title{
    display: flex;
    align-items: center;
    margin-left: 200px;
    .el-button{
        margin-right: 20px;
    }
 }
</style>