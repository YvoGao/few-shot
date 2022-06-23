<template>
    <!-- Form Module-->
    <div class="module form-module" style="margin-top: 50px">
        <div class="toggle"><i class="fa fa-times fa-pencil"></i>
            <div class="tooltip" @click="create">注册</div>
        </div>
        <div class="form">
            <h2>登录账户</h2>
            <form>
                <input type="text" placeholder="用户名"/>
                <input type="password" placeholder="密码"/>
                <button @click="loginsys">登录</button>
            </form>
        </div>
        <div class="form">
            <h2>创建账户</h2>
            <form>
                <input type="text" placeholder="用户名"/>
                <input type="password" placeholder="密码"/>
                <input type="email" placeholder="邮箱地址"/>
                <input type="tel" placeholder="电话"/>
                <button @click="registersys">注册</button>
            </form>
        </div>
<!--        忘记密码-->
        <div class="cta"><a href="http://localhost:8080/#/main">忘记密码？</a></div>
        <div class="form">
            <h2>找回密码</h2>
            <form>
                <input type="text" placeholder="用户名"/>
                <input type="email" placeholder="邮箱"/>
                <button @click="sendemail">发送验证码</button>
                <input type="text" placeholder="验证码"/>
                <input type="password" placeholder="新密码"/>
                <button @click="confirmpsd">确认</button>
            </form>
        </div>
    </div>
</template>

<script>

    export default {
        // eslint-disable-next-line vue/multi-word-component-names
        name: "login.vue",
        components:{
        },
        data(){
            return{
                form:{

                },
                rules:{
                    username:[
                        {
                            required:true, message:"请输入用户名",trigger:"blur"
                        },
                        {
                            min:3,
                            message: "用户名长度不能小于3位",
                            trigger: "blur"
                        }

                    ],
                    password:[
                        {
                            required:true, message:"请输入密码",trigger:"blur"
                        }
                    ]
                }
            }
        },
        methods:{
            // 打开创建爱账户页面，转换表单
            create(){
                if (this.display === "display:none") {
                    this.display = "";
                } else {
                    this.display = "display:none";
                }
            },
            //登录
            loginsys(){

            },
            //注册
            registersys(){

            },
            //发送email
            sendemail(){

            },
            //确认新密码
            confirmpsd(){

            }
        }
    }
</script>

<style lang="less" scoped>

    /* Form Module */
    .form-module {
        position: relative;
        background: #ffffff;
        max-width: 320px;
        width: 100%;
        border-top: 10px solid #14b3f5;
        box-shadow: 0 0 3px rgba(0, 0, 0, 0.3);
        margin: 0 auto;
    }
    .form-module .toggle {
        cursor: pointer;
        position: absolute;
        top: 0;
        right: 0;
        background: #14b3f5;
        width: 30px;
        height: 30px;
        margin: -5px 0 0;
        color: #ffffff;
        font-size: 12px;
        line-height: 30px;
        text-align: center;
    }
    /*.form-module .toggle .tooltip {*/
    /*    position: absolute;*/
    /*    top: 5px;*/
    /*    right: -65px;*/
    /*    display: block;*/
    /*    background: rgba(0, 0, 0, 0.006);*/
    /*    width: auto;*/
    /*    padding: 5px;*/
    /*    font-size: 10px;*/
    /*    line-height: 1;*/
    /*    text-transform: uppercase;*/
    /*}*/
    .form-module .toggle .tooltip:before {
        content: "";
        position: absolute;
        top: 5px;
        left: -5px;
        display: block;
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        border-right: 5px solid rgba(0, 0, 0, 0.6);
    }
    .form-module .form {
        display: none;
        padding: 40px;
    }
    .form-module .form:nth-child(2) {
        display: block;
    }
    .form-module h2 {
        margin: 0 0 20px;
        color: #112128;
        font-size: 18px;
        font-weight: 400;
        line-height: 1;
    }
    .form-module input {
        outline: none;
        display: block;
        width: 100%;
        border: 1px solid #d9d9d9;
        margin: 0 0 20px;
        padding: 10px 15px;
        box-sizing: border-box;
        font-wieght: 400;
        transition: 0.3s ease;
    }
    .form-module input:focus {
        border: 1px solid #03141a;
        color: #333333;
    }
    .form-module button {
        cursor: pointer;
        background: #14b3f5;
        width: 100%;
        border: 0;
        padding: 10px 15px;
        color: #ffffff;
        transition: 0.3s ease;
    }
    .form-module button:hover {
        background: #14b3f5;
    }
    .form-module .cta {
        background: #f2f2f2;
        width: 100%;
        padding: 15px 40px;
        box-sizing: border-box;
        color: #666666;
        font-size: 12px;
        text-align: center;
    }
    .form-module .cta a {
        color: #333333;
        text-decoration: none;
    }
</style>