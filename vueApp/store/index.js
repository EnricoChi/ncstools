import Vue from 'vue'
import Vuex from 'vuex'

import * as actions from './actions'
import * as mutations from './mutations'


Vue.use(Vuex);


const API = '/api/v1/';

const state = {
  apiUrl: API,
  apiUrlProjects: `${API}projects/`,

  dialogs: {
    features: {name: 'features', show: false},
    projects: {name: 'projects', show: false},
    projectNew: {name: 'projectNew', show: false},

    files: {name: 'files', show: true},
  },

  projects: [],
  selectedProject: null,

};


export default new Vuex.Store({
  actions,
  mutations,
  state: state,
})
