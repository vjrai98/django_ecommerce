<template>
  <div class="content">
    <div class="v-layout">
      <div class="v-layout-item v-medium-size-100 v-size-33">
        <user-card> </user-card>
      </div>
    </div>
  </div>
</template>

<script>
import  EditProfileForm from './EditProfileForm';
import UserCard from './UserCard';
export default {
  components: {
    EditProfileForm,
    UserCard,
  }
};
</script>