<template>
<!--    filename-->
    <div>
        <h1>{{filename}}</h1>
        <button @click="downloadFile" >
            下载</button>
    </div>
</template>

<script>
    import axios from "axios";

    export default {
        // eslint-disable-next-line vue/multi-word-component-names
        name: "send",
        data() {
            return {
                filename: "query_reuters.json",
                fileobj: ""
            };
        },
        methods:{

            downloadFile() {
                let formData = new FormData()
                console.log(this.tmpfile)
                formData.append('file', this.tmpfile)
                formData.append('filename', this.filename)
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

<style scoped>

</style>