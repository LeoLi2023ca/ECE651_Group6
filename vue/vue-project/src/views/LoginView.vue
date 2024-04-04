<template>
  <a-layout-content style="display: flex; align-items: center; justify-content: center; min-height: 80vh;">
    <div class="grid-container">
      <a-card class="login-register-form">
        <LoginForm/>
        <!-- <RegisterForm v-else @switchForm="toggleForm" /> -->
        <a-form-item :wrapper-col="{ offset: 6, span: 12 }">
          <div class="center-button">
            <router-link to="/register">
              <a-button >Don't have an account?</a-button>
            </router-link>
          </div>
        </a-form-item>
      </a-card>
    </div>
  </a-layout-content>
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
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 2vh auto; 
}

.login-register-form {
  margin: 5vh auto 20px auto;
  max-width: 600px;
  padding: 20px;
  border: 2px solid #e0e0e0;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  background: linear-gradient(to right, #ffffff, #f2f2f2);
  margin-bottom: 2vh; 
}

.center-button {
  display: flex; 
  justify-content: center; 
  width: 100%; 
}

.toggle-button {
  background: none; 
  border: none; 
  text-decoration: underline; 
  color: rgb(33, 150, 243);
}

</style>
