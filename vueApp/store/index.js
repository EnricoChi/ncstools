import Vue from 'vue'
import Vuex from 'vuex'

import * as actions from './actions'
import * as mutations from './mutations'

Vue.use(Vuex);

export default new Vuex.Store({
  actions,
  mutations,

  state: {
    dialogFeatures: {name: 'features', show: false},
    dialogFiles: {name: 'files', show: false},
    dialogProjects: {name: 'projects', show: false},
  },
})
