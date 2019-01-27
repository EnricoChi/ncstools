<template>
  <v-dialog
    v-model="dialog.show"
    fullscreen
    hide-overlay
    transition="dialog-bottom-transition"
    scrollable
  >
    <v-card tile>
      
      <v-toolbar card dark color="primary">
        
        <v-btn icon dark @click="toggleDialog(dialog.name)">
          <v-icon>fa-angle-double-left</v-icon>
        </v-btn>
        
        <v-spacer></v-spacer>
        <v-toolbar-title>Projects</v-toolbar-title>
        <v-spacer></v-spacer>

        <v-toolbar-items class="fab-container">
          <v-btn fab small color="teal accent-3" @click="toggleDialog(projectNew)">
            <v-icon>fa-plus</v-icon>
          </v-btn>
          <v-btn fab small color="deep-orange accent-3" @click="fetchProjects">
            <v-icon>fa-refresh</v-icon>
          </v-btn>
        </v-toolbar-items>
        
      </v-toolbar>
      
      
      <v-card-text>

        <v-list three-line subheader>
          <v-subheader>User Controls</v-subheader>
          <v-list-tile avatar>
            <v-list-tile-content>
              <v-list-tile-title>Content filtering</v-list-tile-title>
              <v-list-tile-sub-title>Set the content filtering level to restrict apps that can be downloaded</v-list-tile-sub-title>
            </v-list-tile-content>
          </v-list-tile>
          <v-list-tile avatar>
            <v-list-tile-content>
              <v-list-tile-title>Password</v-list-tile-title>
              <v-list-tile-sub-title>Require password for purchase or use password to restrict purchase</v-list-tile-sub-title>
            </v-list-tile-content>
          </v-list-tile>
        </v-list>
        <v-divider></v-divider>
        <v-list three-line subheader>
          <v-subheader>General</v-subheader>

        </v-list>
      </v-card-text>

      <div style="flex: 1 1 auto;"></div>
    </v-card>
  </v-dialog>
</template>

<script>
  import { mapActions, mapMutations, mapState } from 'vuex';
  
  export default {
    
    computed: {
      ...mapState({
        dialog: state => state.dialogs.projects,
        projectNew: state => state.dialogs.projectNew.name,
      }),
    },
    
    methods: {
      ...mapActions([ 'fetchProjects', ]),
      ...mapMutations([ 'toggleDialog', ]),
    },
    
  }
</script>

<style scoped>
  .fab-container {
    position: fixed;
    top: 30px;
    left: 50px;
  }
</style>
