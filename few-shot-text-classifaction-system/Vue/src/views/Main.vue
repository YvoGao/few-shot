<template>
    <el-container>
        <el-container style="height:100%">
            <el-aside width="auto" style="height: 100%">
                <common-aside></common-aside>
            </el-aside>
            <el-container>
                <el-header>
                    <common-header></common-header>
                </el-header>
                <el-main class="el-main-test">
                    <router-view></router-view>
                </el-main>
            </el-container>
        </el-container>

    </el-container>

</template>

<script>
    import CommonAside from '../components/CommonAside.vue'
    import CommonHeader from '../components/CommonHeader.vue'
    // import axios from 'axios';


    export default {
        // eslint-disable-next-line vue/multi-word-component-names
        name: "Home",
        // eslint-disable-next-line vue/no-unused-components
        components:{
            CommonAside,
            CommonHeader
        },
        data(){
            return{}
        }

    }


</script>


<style lang="less" scoped>
    .el-main-test{
        position: fixed;
        margin-left: 200px;
        margin-top: 60px;
    }
    .el-header{
        background-color: #333333;
    }
    .el-main{
        padding-top: 0;
    }
</style>