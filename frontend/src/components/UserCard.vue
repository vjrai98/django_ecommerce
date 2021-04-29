  
<template>
  <v-card class="v-card-profile">
    <div class="v-card-avatar">
      <img class="img" :src="cardUserImage" />
    </div>

    <v-content>
      <h6 class="category text-gray">CEO / Co-Founder</h6>
      <h4 class="card-title">Alec Thompson</h4>
      <p class="card-text">
        Don't be scared of the truth because we need to restart the human
        foundation in truth And I love you like Kanye loves Kanye I love Rick
        Owens’ bed design but the back is...
      </p>
      <v-btn class="v-round v-success">Follow</v-btn>
    </v-content>
  </v-card>
</template>
<script>
export default {
  name: "user-card",
  props: {
    cardUserImage: {
      type: String,
      default: require("@/assets/img/home/deal1.jpg")
    }
  },
  data() {
    return {};
  }
};
</script>
<style></style>