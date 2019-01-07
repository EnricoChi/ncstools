<template>
  <v-app>
    <v-content>
      <transition name="fade" mode="out-in">
        <router-view />
      </transition>
    </v-content>
  </v-app>
</template>

<script>
  import { mapActions, } from 'vuex'
  
  export default {
    data() {
      return {
        appName: 'NCS Tools'
      }
    },

  }
</script>

<style scoped></style>
