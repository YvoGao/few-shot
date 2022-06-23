import Vue from 'vue'
import VueX from 'vuex'
import tab from './tab'
Vue.use(VueX)

export default new VueX.Store({
    modules:{
        tab
    }
})