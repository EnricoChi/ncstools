<template>
  <v-app>
    <transition name="fade" mode="out-in">
      <router-view />
    </transition>
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
