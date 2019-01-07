import Vue from 'vue'
import Vuetify from 'vuetify'
import App from './App.vue'
import store from './store'
import router from './router'

import 'vuetify/dist/vuetify.css'

Vue.use(Vuetify);

new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
});
