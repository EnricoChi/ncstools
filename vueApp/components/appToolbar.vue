<template>
  <v-toolbar clipped-left app height="24">
    
    <v-toolbar-side-icon>
      <v-icon color="white">fa-ellipsis-v</v-icon>
    </v-toolbar-side-icon>
    
    <v-toolbar-items>
      <v-btn flat @click="toggleDialog(projects)">PROJECTS</v-btn>
      <v-btn flat @click="toggleDialog(files)">FILES</v-btn>
      <v-btn flat>FEATURES</v-btn>
    </v-toolbar-items>
    
    <dialog-projects />
    <dialog-files />

  </v-toolbar>
</template>

<script>
  import { mapMutations, mapState, } from 'vuex';
  
  import DialogProjects from './appDialogProjects.vue'
  import DialogFiles from './appDialogFiles.vue'

  export default {
    
    components: {
      dialogProjects: DialogProjects,
      dialogFiles: DialogFiles,
    },
    
    computed: {
      ...mapState({
        projects: state => state.dialogs.projects.name,
        files: state => state.dialogs.files.name,
      }),
    },
    
    methods: {
        ...mapMutations([ 'toggleDialog', ]),
    },
  }
</script>

<style scoped>

</style>
