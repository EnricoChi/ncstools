<template>
  <v-footer height="40" inset app>
    <!--<span class="px-3">&copy; {{ new Date().getFullYear() }}</span>-->
        <v-text-field
          id="command"
          box clearable hide-details
          placeholder="Type your command here:"
          clear-icon="fa-times"
          prepend-inner-icon="fa-angle-right"
          ></v-text-field>
  </v-footer>
</template>

<script>
  export default {}
</script>

<style>
  
  #command {
    margin-top: 0;
    padding: 4px 0 0 0;
  }
  
  .v-text-field--box > .v-input__control > .v-input__slot, .v-text-field--outline > .v-input__control > .v-input__slot {
    min-height: 36px;
}
  
  .v-text-field.v-text-field--enclosed .v-input__prepend-outer, .v-text-field.v-text-field--enclosed .v-input__prepend-inner, .v-text-field.v-text-field--enclosed .v-input__append-inner, .v-text-field.v-text-field--enclosed .v-input__append-outer {
    margin-top: 4px;
}

</style>
