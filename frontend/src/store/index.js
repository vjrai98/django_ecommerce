import Vue from 'vue'
import Vuex from 'vuex'
import product from './modules/product'
// load Vuex
Vue.use(Vuex)


export default new Vuex.Store({
  modules:{
    product
  }

});