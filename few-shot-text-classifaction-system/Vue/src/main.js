import Vue from 'vue'
import App from './App.vue'
// import ElementUI from 'element-ui';
import { Button, Select, Option, Radio, Container, Main, Header, Aside, Menu, Table, TableColumn,Submenu, MenuItem, Upload,MenuItemGroup,Row, Card, Col, Form,Input, FormItem} from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css';
import './assets/less/index.css'
import store from './store'
import router from './router'
Vue.config.productionTip = false
Vue.use(Select);
Vue.use(Option);
Vue.use(Form);
Vue.use(TableColumn);
Vue.use(Table);
Vue.use(Upload);
Vue.use(Input);
Vue.use(FormItem);
Vue.use(Button);
Vue.use(Radio);
Vue.use(Container);
Vue.use(Header);
Vue.use(Aside);
Vue.use(Main);
Vue.use(Menu);
Vue.use(MenuItemGroup);
Vue.use(MenuItem);
Vue.use(Submenu);
Vue.use(Row);
Vue.use(Card);
Vue.use(Col);
new Vue({
  store,
  router,
  render: h => h(App),
}).$mount('#app')
