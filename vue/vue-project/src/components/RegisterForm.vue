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
      <div>
            <input type="radio" id="radio_1" value="Student" v-model="role">
            <label for="radio_1">Student</label>
            <input type="radio" id="radio_2" value="Tutor" v-model="role">
            <label for="radio_2">Tutor</label>
        </div>
      <button type="submit">注册</button>
    </form>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  const role = ref('Student')
  const username = ref('');
  const email = ref('');
  const password = ref('');
  const confirmPassword = ref('');
  
  const handleSubmit = () => {
    var data = new FormData();
    data.append('username', username.value);
    data.append('password', password.value);

    var config = {
        method: 'post',
        url: 'http://localhost:5000/login',
        data: data
    };

    axios(config)
        .then(function (response) {
            console.log(JSON.stringify(response.data));
        })
        .catch(function (error) {
            console.log(error);
        });
  }
  </script>
  
  
  <style scoped>
  </style>
  