<template>
    <form @submit.prevent="handleSubmit">
      <div>
        <label for="username">用户名:</label>
        <input id="username" v-model="username" type="text" placeholder="请输入用户名" />
      </div>
      <div>
        <label for="email">电子邮件:</label>
        <input id="email" v-model="email" type="email" placeholder="请输入电子邮件" />
      </div>
      <div>
        <label for="password">密码:</label>
        <input id="password" v-model="password" type="password" placeholder="请输入密码" />
      </div>
      <div>
        <label for="confirmPassword">确认密码:</label>
        <input id="confirmPassword" v-model="confirmPassword" type="password" placeholder="请再次输入密码" />
      </div>
      <button type="submit">注册</button>
    </form>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const username = ref('');
  const email = ref('');
  const password = ref('');
  const confirmPassword = ref('');
  
  const handleSubmit = () => {
    console.log('提交注册', {
      username: username.value,
      email: email.value,
      password: password.value,
      confirmPassword: confirmPassword.value,
    });
  };
  const handleLogin = () => {
    router.push('/login');
  };
  </script>
  
  
  <style scoped>
  </style>
  