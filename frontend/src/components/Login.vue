<template lang="html" class="primary_bg">
<div class="primary_bg">
<v-container fluid class="mb-15">
  <v-layout row>
    <v-flex md6 lg6 sm12 xs12 x6>
      <img src="../assets/logo.png" width="50%">
     </v-flex>
    <v-flex md6 lg6 sm12 xs12 x6 pl-3>
      <h1 class="white--text font-weight-medium mt-16 d-sm-pl-8 d-xs-pl-6">Roni<span class="red--text">X</span></h1>
      <h2 class="white--text d-sm-pl-6">Discover great music <span class="yellow--text">that rules out </span></h2>
      <p class="white--text d-sm-pl-6">Music is eternal that has limitless potential in grasping and treating of great forces on the earth.However to get started login to your existing account or create one if you dont have.</p>
      <v-dialog v-model="dialog" scrollable max-width="300px">
        <!-- Login popup modal -->
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            color="black--text white"
            dark
            v-bind="attrs"
            v-on="on"
          >
            Login
          </v-btn>
          
        </template>
        <v-card>
          <v-card-title>Login</v-card-title>
          <v-divider></v-divider>
          <v-card-text class="mt-2">
            <v-text-field
            v-model="email"
            solo
            label="Email"
            prepend-inner-icon="mdi-email"
          ></v-text-field>

     <!-- Allowing user to toggle visibility of password -->
       <v-text-field
            v-model="password"
            :type="show1 ? 'text' : 'password'"
            name="input-10-1"
            @click:append="show1 = !show1"
            solo
            :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
            label="Password"
            prepend-inner-icon="mdi-account-key"
         ></v-text-field>
          </v-card-text>
          <v-divider></v-divider>
          <v-card-actions>
            <v-btn color="blue darken-1" text @click="dialog = false">Close</v-btn>
            <v-btn color="blue darken-1" text @click.prevent="authenticate">login</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
<v-btn class="ml-2" outlined color="white"> <router-link to="/signup" tag='span'>Create account</router-link> </v-btn>
        <p><v-chip
      color="black"
      text-color="white"
      class="mt-12"
    >
      <v-avatar
        left
        class="red darken-4"
      >
        <v-icon size="16">mdi-newspaper-plus</v-icon>
      </v-avatar>
      Updated with Private Music streams >
    </v-chip></p>
    </v-flex>
  </v-layout>
  </v-container>
  <v-footer
   color="primary_bg"
    padless
  >
    <v-row
      justify="center"
      no-gutters
    >
      <v-col
        class="text-center white--text"
        cols="12"
      >
        {{ new Date().getFullYear() }}
        
      </v-col>
    </v-row>
  </v-footer>
</div>


</template>

<script>
import axiosInstance from '../axios-auth'
import VFacebookLogin from 'vue-facebook-login-component'
export default {
  data () {
    return {
      show1: false,
      email: '',
      password: '',
      dialog: false,
    }
  },
  components:{
      VFacebookLogin
  },
  methods: {
    authenticate () {
      const payload = {
        username: this.email,
        password: this.password,
        grant_type: "password",
        client_id: "0uyb250PnYmQia88JC0fDx1MU54jPQZbUNZ7sR0S",
        client_secret: "ZV3FI71JHU602flI0ogj8k1BIVKdpyaQhd8qGfIkVX5wOE2itt4fMD4jqmQRxmziJ8Bvcwei8AM90CJEAjc45DVn8cWBOmqRmacp3T0YJiBwx74ssgBR2SLSE5WvsKEB"
      }
      
      axiosInstance.post("auth/token/", payload)
        .then((response) => {
          console.log("response data is :",response.data.access_token)
          console.log("refresh data is :",response.data.refresh_token)
          this.$store.commit('updateToken', response.data.access_token,response.data.refresh_token)
          
          // get and set auth user
          
          axiosInstance.get("/accounts/user/")
            .then((response) => {
              this.$store.commit("setAuthUser",
                {authUser: response.data, isAuthenticated: true}
              )
              this.$router.push({name: 'Home'})
            })
        })
        .catch((error) => {
          console.log(error);
          console.debug(error);
          console.dir(error);
        })
    }
  }
}
</script>

<style lang="css" scoped>
.primary_bg{
  background-color:#9921e8;
  background-image:linear-gradient(315deg, #9921e8 0%, #5f72be 74%);
}
.v-text-field{
      width: 400px;
}
</style>