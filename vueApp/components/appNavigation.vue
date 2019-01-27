<template>
  <v-navigation-drawer absolute fixed clipped permanent width="300" app>
    
    <v-menu full-width offset-x nudge-right="8" transition="slide-x-transition">
      
      <v-btn block flat slot="activator">
        {{ selectedProject ? selectedProject.name : ''}}
        <v-spacer></v-spacer>
        <v-icon right>fa-angle-right</v-icon>
      </v-btn>
      
      <v-list>
        <v-list-tile
          v-for="project in projects"
          :key="project.id"
          @click="setSelectedProject(project)"
        ><v-list-tile-title>{{ project.name }}</v-list-tile-title>
        </v-list-tile>
      </v-list>
      
    </v-menu>
  
  </v-navigation-drawer>

</template>

<script>
  import { mapMutations, mapState, } from 'vuex'
  
  export default {
    
    computed: {
      ...mapState([ 'projects', 'selectedProject', ])
    },
    
    methods: {
      ...mapMutations([ 'setSelectedProject', ]),
    },
  }
</script>

<style scoped>
  >>>.v-menu {
    width: 100%
  }

</style>
