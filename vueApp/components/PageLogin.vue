<template>
    <v-container fluid fill-height>
      <v-layout align-center justify-center>
        <v-flex xs12 sm8 md4>
          <v-card class="elevation-12">
            <v-toolbar dark color="primary">
              <v-toolbar-title>Login</v-toolbar-title>
              <v-spacer></v-spacer>
            </v-toolbar>
              <v-card-text>
                <v-form>
                  <v-text-field name="login" label="Signum" type="text"></v-text-field>
                </v-form>
              </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
</template>

<script>
  export default {
    data() {
      return {
        drawer: null
      }
    },
    
    props: {
      source: String
    }
  }
</script>

<style scoped>
  >>>input[name='login'] {
    border-bottom: none;
  }
</style>
