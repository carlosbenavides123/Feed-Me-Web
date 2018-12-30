import Vue from "vue";
import './plugins/vuetify'
import App from "./App.vue";
import router from "./router";
import store from "./Store/store";

import Vuetify from 'vuetify'

Vue.use(Vuetify)

import 'roboto-fontface/css/roboto/roboto-fontface.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css'

import 'vuetify/dist/vuetify.min.css' // Ensure you are using css-loader

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");