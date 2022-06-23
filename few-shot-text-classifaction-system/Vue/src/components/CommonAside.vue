<template>
    <el-menu default-active="1-4-1" class="el-menu-vertical-demo" background-color="#545C64" text-color="#fff" active-text-color="#ffd04b" @open="handleOpen" @close="handleClose" :collapse="isCollapse">
        <el-menu-item @click="clickMenu(item)" v-for="item in noChildren" :index="item.path" :key="item.path">
            <i :class="'el-icon-'+item.icon"></i>
            <span slot="title">{{item.label}}</span>
        </el-menu-item>
    </el-menu>
</template>

<style lang="less" scoped>
    .el-menu-vertical-demo:not(.el-menu--collapse) {
        width: 200px;
        height: 100%;
        position: fixed;
    }
    .el-menu{
        height: 100%;
        border: none;
    }
</style>

<script>
    export default {
        data() {
            return {
                menu:[
                    {
                        path:'/',
                        name:'home',
                        label:'首页',
                        icon:'s-home',
                        url:'Home/Home'
                    },
                    {
                        path: '/20news',
                        name: '20news',
                        label: '20news新闻分类',
                        icon: 'zoom-in',
                        url: 'Home/lang_news'
                    },
                    {
                        path: '/retuers',
                        name: 'retuers',
                        label: 'retuers新闻分类',
                        icon: 'zoom-in',
                        url: 'Home/short_news'
                    },
                ],
                // isCollapse: false
            };
        },
        methods: {
            handleOpen(key, keyPath) {
                console.log(key, keyPath);
            },
            handleClose(key, keyPath) {
                console.log(key, keyPath);
            },
            clickMenu(item){
                this.$router.push({
                    name:item.name
                })
            }
        },
        computed:{
            noChildren(){
                return this.menu.filter(item => !item.children)
            },
            hasChildren(){
                return this.menu.filter(item => item.children)
            },
            isCollapse(){
                return this.$store.state.tab.isCollapse;
            }
        }
    }
</script>