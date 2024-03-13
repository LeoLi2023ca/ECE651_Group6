<template>
  <div class="grid-container">
    <a-card style="width: 500px; ">
      <LoginForm v-if="isLoginForm" @switchForm="toggleForm" />
      <RegisterForm v-else @switchForm="toggleForm" />
      <a-form-item :wrapper-col="{ offset: 6, span: 12 }">
        <a-button @click="toggleForm" style="width: 225px;">{{ isLoginForm ? 'Don\'t have an account?' : 'Already have an account?' }}</a-button>
      </a-form-item>
    </a-card>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import LoginForm from '../components/LoginForm.vue';
import RegisterForm from '../components/RegisterForm.vue';

const isLoginForm = ref(true);

const toggleForm = () => {
  isLoginForm.value = !isLoginForm.value;
};
</script>

<style scoped>
.grid-container {
  display: grid;
  place-items: center;
  height: 60vh;
}
</style>