import Vue from "vue";
import Router from "vue-router";
import VueRouter from "vue-router";

/** Components list */
import Home from './components/Home/index.vue'


Vue.use(Router);

const routes = [{
  path: '/',
  component: Home
}]

export default new VueRouter({
  mode: 'history',
  routes
  // scrollBehavior(from, to, savedPosition) {
  //   return {

  //   }
  // }
})