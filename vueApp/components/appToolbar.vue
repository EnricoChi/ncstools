<template>
  <v-toolbar clipped-left app height="24">
    
    <v-toolbar-side-icon>
      <v-icon color="white">fa-ellipsis-v</v-icon>
    </v-toolbar-side-icon>
    
    <v-toolbar-items>
      <v-btn flat @click="toggleDialog(projects)">PROJECTS</v-btn>
      <v-btn flat>FILES</v-btn>
      <v-btn flat>FEATURES</v-btn>
    </v-toolbar-items>
    
    <dialog-projects />

  </v-toolbar>
</template>

<script>
  import { mapMutations, mapState, } from 'vuex';
  
  import DialogProjects from './appDialogProjects.vue'
  
  export default {
    
    components: {
      dialogProjects: DialogProjects,
    },
    
    computed: {
      ...mapState({
        projects: state => state.dialogs.projects.name,
      }),
    },
    
    methods: {
        ...mapMutations([ 'toggleDialog', ]),
    },
  }
</script>

<style scoped>

</style>
