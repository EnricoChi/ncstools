<template>
  <v-navigation-drawer absolute fixed clipped permanent width="300" app>
    <v-menu full-width offset-x nudge-right="8" transition="slide-x-transition">
      
      <v-btn block flat slot="activator">
        {{ selectedProject }}
        <v-spacer></v-spacer>
        <v-icon right>fa-angle-right</v-icon>
      </v-btn>
      
      <v-list>
        <v-list-tile
          v-for="(project, index) in userProjects"
          :key="index"
          @click="setSelectedProject(project)"
        ><v-list-tile-title>{{ project }}</v-list-tile-title>
        </v-list-tile>
      </v-list>
      
    </v-menu>
  </v-navigation-drawer>

</template>

<script>
  export default {
    data: () => ({
      userProjects: [ 'project1', 'project2', 'project3', ],
      selectedProject: ''
    }),
    
    methods: {
      setSelectedProject(project) { this.selectedProject = project },
    },
    
    created() {
      this.setSelectedProject(this.userProjects[0])
    },
  }
</script>

<style scoped>
  >>>.v-menu {
    width: 100%
  }

</style>
