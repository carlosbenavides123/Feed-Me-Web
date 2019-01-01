import Vue from "vue";
import Vuex from "vuex";
import foodsearch from './Modules/foodsearch'

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    foodsearch
  }
});