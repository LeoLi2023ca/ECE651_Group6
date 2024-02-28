<template>
  <div>
    <LoginForm v-if="isLoginForm" @switchForm="toggleForm" />
    <RegisterForm v-else @switchForm="toggleForm" />
    <button @click="toggleForm">{{ isLoginForm ? 'register' : 'login' }}</button>
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
