<template>
  <form>
    <v-card>
      <v-card-title :data-background-color="dataBackgroundColor">
        <h4 class="title">Edit Profile</h4>
        <p class="category">Complete your profile</p>
      </v-card-title>

      <v-content>
        <div class="v-layout">
          <div class="v-layout-item v-small-size-100 v-size-33">
            <v-field>
              <label>Company (disabled)</label>
              <v-text-field v-model="disabled" disabled></v-text-field>
            </v-field>
          </div>
          <div class="v-layout-item v-small-size-100 v-size-33">
            <v-field>
              <label>User Name</label>
              <v-text-field v-model="username" type="text"></v-text-field>
            </v-field>
          </div>
          <div class="v-layout-item v-small-size-100 v-size-33">
            <v-field>
              <label>Email Address</label>
              <v-text-field v-model="emailadress" type="email"></v-text-field>
            </v-field>
          </div>
          <div class="v-layout-item v-small-size-100 v-size-50">
            <v-field>
              <label>First Name</label>
              <v-text-field v-model="firstname" type="text"></v-text-field>
            </v-field>
          </div>
          <div class="v-layout-item v-small-size-100 v-size-50">
            <v-field>
              <label>Last Name</label>
              <v-text-field v-model="lastname" type="text"></v-text-field>
            </v-field>
          </div>
          <div class="v-layout-item v-small-size-100 v-size-100">
            <v-field>
              <label>Adress</label>
              <v-text-field v-model="address" type="text"></v-text-field>
            </v-field>
          </div>
          <div class="v-layout-item v-small-size-100 v-size-33">
            <v-field>
              <label>City</label>
              <v-text-field v-model="city" type="text"></v-text-field>
            </v-field>
          </div>
          <div class="v-layout-item v-small-size-100 v-size-33">
            <v-field>
              <label>Country</label>
              <v-text-field v-model="country" type="text"></v-text-field>
            </v-field>
          </div>
          <div class="v-layout-item v-small-size-100 v-size-33">
            <v-field>
              <label>Postal Code</label>
              <v-text-field v-model="code" type="number"></v-text-field>
            </v-field>
          </div>
          <div class="v-layout-item v-size-100">
            <v-field maxlength="5">
              <label>About Me</label>
              <v-textarea v-model="aboutme"></v-textarea>
            </v-field>
          </div>
          <div class="v-layout-item v-size-100 text-right">
            <v-button class="v-raised v-success">Update Profile</v-button>
          </div>
        </div>
      </v-content>
    </v-card>
  </form>
</template>
<script>
export default {
  name: "edit-profile-form",
  props: {
    dataBackgroundColor: {
      type: String,
      default: ""
    }
  },
  data() {
    return {
      username: null,
      disabled: null,
      emailadress: null,
      lastname: null,
      firstname: null,
      address: null,
      city: null,
      country: null,
      code: null,
      aboutme:
        "Lamborghini Mercy, Your chick she so thirsty, I'm in that two seat Lambo."
    };
  }
};
</script>
<style></style>