<template>
    <el-row class="home" :gutter="20">
        <el-col :span="16" style="margin-top: 20px">
            <el-card shadow="hover">
                <div class="model">
                    <h3 align="center">模型结构图</h3>
                    <img :src="model" align="center" width="700px" height="400px" >
                </div>
            </el-card>
        </el-col>
        <el-col :span="8" style="margin-top: 20px">
            <h3 style="margin-top: 20px">训练数据集</h3>
            <el-row :gutter="20">
                <el-card shadow="hover">
                    <div class="data_Reuters">
                        <h3 align="left">Reuters-21578数据集</h3>
                        <h3 align="left">5-way 1-shot 准确率：82.3</h3>
                        <h3 align="left">5-way 5-shot 准确率：96.7</h3>
                    </div>
                </el-card>
            </el-row>
            <el-row :gutter="20" style="margin-top: 20px">
                <el-card shadow="hover">
                    <div class="data_20">
                        <h3 align="left">20news数据集</h3>
                        <h3 align="left">5-way 1-shot 准确率：59.6 </h3>
                        <h3 align="left">5-way 5-shot 准确率：77.8 </h3>
                    </div>
                </el-card>
            </el-row>

        </el-col>
    </el-row>
</template>

<script>
    export default {
        // eslint-disable-next-line vue/multi-word-component-names
        name: "home",
        data(){
            return{
                model:require('../../assets/image/model.png')
            }
        }

    }
</script>

<style scoped>

</style>