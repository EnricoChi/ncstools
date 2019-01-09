<template>
  <app-navigation />
</template>

<script>
  import Navigation from './appNavigation.vue'
  
  export default {
    
    components: {
      appNavigation: Navigation
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
