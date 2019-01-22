import Vue from 'vue'
import Vuex from 'vuex'

import * as actions from './actions'
import * as mutations from './mutations'


Vue.use(Vuex);


const API = '/api/v1/';

const state = {
    apiUrl: API,
    apiUrlProjects: `${API}projects/`,

    dialogFeatures: {name: 'features', show: false},
    dialogFiles: {name: 'files', show: false},
    dialogProjects: {name: 'projects', show: false},
};


export default new Vuex.Store({
  actions,
  mutations,
  state: state,
})
