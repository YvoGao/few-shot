<template>
    <el-row class="home" :gutter="20">
<!--        <h3 align="center">reuters新闻分类</h3>-->
        <el-col :span="8" style="margin-top: 20px">
            <el-row :gutter="20">
                <el-card shadow="hover" class="el-card-01">
                    <h3 style="margin-top: 20px">支持集</h3>
                    <div class="support" ref="support">
                        <el-form ref="form" label-width="100px" size="mini">
                            <el-select v-model="values[0]" @blur="handleFocus" @change="handleChange"
                                       placeholder="支持集类别1"
                                       style="margin-top: 20px">
                                <el-option
                                        v-for="item in options"
                                        :key="item.value"
                                        :label="item.label"
                                        :disabled="item.disabled"
                                        :value="item.value">
                                </el-option>
                            </el-select>
                            <el-select v-model="values[1]" @blur="handleFocus" @change="handleChange"
                                       placeholder="支持集类别2" style="margin-top: 20px">
                                <el-option
                                        v-for="item in options"
                                        :key="item.value"
                                        :label="item.label"
                                        :disabled="item.disabled"
                                        :value="item.value">
                                </el-option>
                            </el-select>
                            <el-select v-model="values[2]" @blur="handleFocus" @change="handleChange"
                                       placeholder="支持集类别3"
                                       style="margin-top: 20px">
                                <el-option
                                        v-for="item in options"
                                        :key="item.value"
                                        :label="item.label"
                                        :disabled="item.disabled"
                                        :value="item.value">
                                </el-option>
                            </el-select>
                            <el-select v-model="values[3]" @blur="handleFocus" @change="handleChange"
                                       placeholder="支持集类别4"
                                       style="margin-top: 20px">
                                <el-option
                                        v-for="item in options"
                                        :key="item.value"
                                        :label="item.label"
                                        :disabled="item.disabled"
                                        :value="item.value">
                                </el-option>
                            </el-select>
                            <el-select v-model="values[4]" @blur="handleFocus" @change="handleChange"
                                       placeholder="支持集类别5"
                                       style="margin-top: 20px">
                                <el-option
                                        v-for="item in options"
                                        :key="item.value"
                                        :label="item.label"
                                        :disabled="item.disabled"
                                        :value="item.value">
                                </el-option>
                            </el-select>
                        </el-form>
                    </div>
                </el-card>
            </el-row>


        </el-col>
        <el-col :span="16" style="margin-top: 20px">
            <el-card shadow="hover" class="el-card-01">
                <h3 align="center">查询集</h3>
                <div class="couple" ref="upload_div">
                    <el-form ref="form" :inline="true">
                        <el-form-item label="多组查询">
                            <el-upload
                                    class="upload-demo"
                                    action="http://127.0.0.1:5000/reuters"
                                    name="file"
                                    :data="file_info"
                                    :on-success="upload_success"
                                    :on-preview="handlePreview"
                                    :on-remove="handleRemove"
                                    :on-change="handleOnChange"
                                    :before-remove="beforeRemove"
                                    :auto-upload="false">
                                <el-button size="mini" plain type="primary">上传</el-button>
                            </el-upload>
                        </el-form-item>

                    </el-form>
                    <el-button type="primary" @click="fileUpload">提交</el-button>


                </div>
                <div>准确率：{{acc}}</div>
                <el-table
                        :data="predata"
                        max-height="380"
                        style="width: 100%">
                    <el-table-column
                            fixed
                            prop="news"
                            label="新闻"
                    >
                    </el-table-column>
                    <el-table-column
                            prop="tru"
                            label="标签"
                            width="80">
                    </el-table-column>
                    <el-table-column
                            prop="pre"
                            label="预测值"
                            width="80">
                    </el-table-column>
                </el-table>
                <el-button size="mini" plain type="primary" @click="download">下载结果</el-button>
            </el-card>
        </el-col>
    </el-row>

</template>

<script>
    import axios from "axios";
    import {Message} from 'element-ui'

    export default {
        // eslint-disable-next-line vue/multi-word-component-names
        name: "short_news",
        data() {
            return {
                //预测的结果
                predata: [
                    // {
                    //     news: "新闻",
                    //     tru: "标签",
                    //     pre: "预测值"
                    //
                    // }
                ],
                //类别数据,我希望是后端传来的
                options: [
                    {value: 20, label: "ipi"},
                    {value: 21, label: "iron-steel"},
                    {value: 22, label: "rubber"},
                    {value: 23, label: "jobs"},
                    {value: 24, label: "bop"},
                    {value: 25, label: "gnp"},
                    {value: 26, label: "veg-oil"},
                    {value: 27, label: "pet-chem"},
                    {value: 28, label: "gas"},
                    {value: 29, label: "wpi"},
                    {value: 30, label: "livestock"}

                ],
                //用来绑定显示的选项值
                values: ['', '', '', '', ''],
                tmpfile: '',
                acc: '',
                lastSelectId: ''
            }
        },
        computed: {
            file_info() {
                return {
                    user_id: '1'
                }
            },
        },
        methods: {
            upload_success(resp) {
                Message({
                    message: resp.msg,
                    type: 'success',
                    duration: 5 * 1000
                })
            },
            fileUpload() {
                let formData = new FormData()
                console.log(this.tmpfile)
                formData.append('file', this.tmpfile)
                formData.append('classes', this.values)
                console.log(formData)
                let config = {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                }
                var that = this;
                const path = "http://127.0.0.1:5000/reuters";
                axios.post(path, formData, config)
                    .then(function (response) {
                        console.log(response)
                        that.predata = response.data['predata']
                        that.acc = response.data['acc']
                        console.log(response)
                        that.$refs.upload_div.style.display="none"
                        // 坑二：这里直接按类型解析，若再通过 JSON.stringify(msg) 转，会得到带双引号的字串

                    })
                    .catch(function (error) {
                        alert("Error " + error);
                    });
                // this.get_data()
            },
            handleOnChange(file) {
                this.tmpfile = file.raw
            },
            handleRemove(file) {
                console.log(file);
            },
            handlePreview(file) {
                console.log(file);
            },
            beforeRemove(file) {
                return this.$confirm(`确定移除 ${file.name}？`);
            },
            handleChange(value) {
                console.log(value)
                let selected = this.options.find(item => item.value == value);
                selected.disabled = true
                let lastSelected = this.options.find(item => item.value == this.lastSelectId);
                if (lastSelected != null) {
                    lastSelected.disabled = false
                }
            },
            handleFocus(value) {
                let lastSelected = this.options.find(item => item.label == value.target.value);
                if (lastSelected != null) {
                    this.lastSelectId = lastSelected.value
                }
            },
            download() {
                let formData = new FormData()
                console.log(this.tmpfile)
                // formData.append('file', this.tmpfile)
                formData.append('filename','result.json')
                console.log(formData)
                const path = "http://127.0.0.1:5000/send";
                axios.post(path, formData).then(
                    response => {
                        const conent = response.data;
                        const blob = new Blob([conent], {type: ""});
                        // let fileName = response.headers["content-disposition"].split("=")[1];
                        let fileName = "result.json"
                        if (window.navigator.msSaveOrOpenBlob) {
                            window.navigator.msSaveOrOpenBlob(blob, fileName);
                        }
                        console.log(fileName);
                        // console.log(response.data);
                        let url = window.URL.createObjectURL(blob);
                        // console.log(url)
                        let a = document.createElement("a");
                        document.body.appendChild(a);
                        a.href = url;
                        a.download = decodeURI(fileName); //命名下载名称
                        a.click(); //点击触发下载
                        window.URL.revokeObjectURL(url);
                    }
                    // eslint-disable-next-line no-unused-vars
                ).catch(function (error) {
                    alert("Error " + error);
                });
            },
        }

    }
</script>

<style lang="less" scoped>
    .qurey {

    }

    .single {
    }

    .single1 {
        display: inline-flex;
        height: 100%;
        width: 100%;
        justify-content: space-between;
        align-items: center;
    }

    .couple {
        display: inline-flex;
        height: 100%;
        width: 100%;
        justify-content: space-between;
        align-items: center;
    }

    .el-card-01 {
        height: 29.3em;
    }


</style>