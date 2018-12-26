import Vue from 'vue'
import Router from 'vue-router'

import PageMain from '../components/PageMain.vue'

Vue.use(Router);

export default new Router({
  mode: 'history',

  routes: [
    { path: '/', name: 'main', component: PageMain },
  ],
});
