<template>
  <div>
    <app-navigation />
    <app-toolbar />
    <app-footer />
  </div>
</template>

<script>
  import Navigation from './appNavigation.vue'
  import Toolbar from './appToolbar.vue'
  import Footer from './appFooter.vue'
  
  export default {
    
    components: {
      appNavigation: Navigation,
      appToolbar: Toolbar,
      appFooter: Footer,
    },
    
    data() {
      return {}
    },
    
//    beforeRouteEnter(to, from, next) {
//      next(vm => {
////        console.log('beforeRouteEnter ->\t', localStorage.jwt, vm.$router);
//        if (!localStorage.jwt) {
//          vm.$router.push('login')
//        }
//
//      })
//    }
  }

</script>

<style scoped></style>
