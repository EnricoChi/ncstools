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
              <v-form v-model="valid">
                <v-text-field
                  id="login"
                  v-model="login"
                  :rules="loginRules"
                  label="Signum"
                  type="text"
                  required autofocus
                ></v-text-field>
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
        valid: false,
        login: '',
        loginLength: 7,
        loginRules: [
          v => !!v || 'Login required.',
          v => v.length <= this.loginLength || 'Login must be less than 7 characters'
        ],
      }
    },
    
    methods: {
      
      validateLogin: async function() {
        const login = document.getElementById('login');
        login.setAttribute('disabled', 'true');
        
        const response = await fetch( '/auth/login/', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', },
          body: JSON.stringify({'user': this.login}),
          },
        );
        
        console.log('validateLogin ->\n', await response)

//        if (resp.ok) {
//          window.localStorage.jwt = (await resp.json()).token;
//          this.setToken(window.localStorage.jwt);
//          this.setCurrentComponent('Upload');
//          console.log("validateSignum->\n", window.localStorage.jwt);
//        } else {
//          login.removeAttribute('disabled');
//          login.focus();
//          console.log("validateSignum->\n", await resp);
//        }
      
      },
    },
    
    watch: {
      login() {
        if (this.login.length === this.loginLength) { this.validateLogin() }
      }
    }
  }
</script>

<style scoped>

</style>
