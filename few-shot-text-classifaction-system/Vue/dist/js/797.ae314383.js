"use strict";(self["webpackChunkvue_demo"]=self["webpackChunkvue_demo"]||[]).push([[797],{6797:function(e,t,n){n.r(t),n.d(t,{default:function(){return k}});var l=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("el-container",[n("el-container",{staticStyle:{height:"100%"}},[n("el-aside",{staticStyle:{height:"100%"},attrs:{width:"auto"}},[n("common-aside")],1),n("el-container",[n("el-header",[n("common-header")],1),n("el-main",[n("router-view")],1)],1)],1)],1)},o=[],a=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("el-menu",{staticClass:"el-menu-vertical-demo",attrs:{"default-active":"1-4-1","background-color":"#545C64","text-color":"#fff","active-text-color":"#ffd04b",collapse:e.isCollapse},on:{open:e.handleOpen,close:e.handleClose}},e._l(e.noChildren,(function(t){return n("el-menu-item",{key:t.path,attrs:{index:t.path},on:{click:function(n){return e.clickMenu(t)}}},[n("i",{class:"el-icon-"+t.icon}),n("span",{attrs:{slot:"title"},slot:"title"},[e._v(e._s(t.label))])])})),1)},r=[],s={data(){return{menu:[{path:"/",name:"home",label:"首页",icon:"s-home",url:"Home/Home"},{path:"/lang_news",name:"lang_news",label:"长文本新闻分类",icon:"zoom-in",url:"Home/lang_news"},{path:"/short_news",name:"short_news",label:"短文本新闻分类",icon:"zoom-in",url:"Home/short_news"}]}},methods:{handleOpen(e,t){console.log(e,t)},handleClose(e,t){console.log(e,t)},clickMenu(e){this.$router.push({name:e.name})}},computed:{noChildren(){return this.menu.filter((e=>!e.children))},hasChildren(){return this.menu.filter((e=>e.children))},isCollapse(){return this.$store.state.tab.isCollapse}}},i=s,c=n(1001),u=(0,c.Z)(i,a,r,!1,null,"12566aaf",null),m=u.exports,h=function(){var e=this,t=e.$createElement;e._self._c;return e._m(0)},d=[function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("header",[n("div",{staticClass:"title"},[n("h3",{staticStyle:{color:"white"}},[e._v("基于小样本学习的新闻分类系统")])])])}],f={name:"CommonHeader.vue",methods:{handleMenu(){this.$store.commit("collapseMenu")}}},p=f,_=(0,c.Z)(p,h,d,!1,null,"aff0d832",null),C=_.exports,v={name:"Home",components:{CommonAside:m,CommonHeader:C},data(){return{}}},w=v,b=(0,c.Z)(w,l,o,!1,null,"79dd65b4",null),k=b.exports}}]);
//# sourceMappingURL=797.ae314383.js.map