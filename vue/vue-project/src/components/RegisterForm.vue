<template>
    <div class="form-container">
      <a-typography-title :level="4" class="form-title">Register</a-typography-title>
      <a-form name="basic" layout="vertical" autocomplete="off">
        <a-form-item label="Username" name="username">
          <a-input v-model:value="username" />
        </a-form-item>
  
        <a-form-item label="Email" name="email">
          <a-input v-model:value="email" />
        </a-form-item>
  
        <a-form-item label="Password" name="password">
          <a-input-password v-model:value="password" />
        </a-form-item>
  
        <a-form-item label="Role">
          <a-radio-group v-model:value="role">
            <a-radio value="Student">Student</a-radio>
            <a-radio value="Tutor">Tutor</a-radio>
          </a-radio-group>
        </a-form-item>
  
        <a-form-item>
          <a-button type="primary" @click="register()" class="register-button">Register</a-button>
        </a-form-item>
  
        <!-- <a-form-item class="form-switch">
          Already have an account?
        </a-form-item> -->
      </a-form>
    </div>
  </template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
import { useStore } from 'vuex';

const store = useStore();
const router = useRouter();

const role = ref('Student')
const username = ref('');
const email = ref('');
const password = ref('');

const register = () => {
    var data = new FormData();
    data.append('username', username.value);
    data.append('password', password.value);
    data.append('role', role.value)
    data.append('email', email.value)

    var config = {
        method: 'post',
        url: 'http://127.0.0.1:5000/register',
        data: data
    };

    axios(config)
        .then(function (response) {
            sessionStorage.setItem('role', response.data.code);
            sessionStorage.setItem('user_info', JSON.stringify(response.data.user_info))
            store.commit('setUserRole', response.data.code);
            if(response.data.code == '1'){
              router.push({ name: 'home' });
            }
            else{
              router.push({ name: 'welcome-tutor' });
            }

        })
        .catch(function (error) {
            if(error.response.status == 409){
                alert('Username already exists!');
            }
            else if(error.response.status == 400){
                alert('Email Format is invalid!');
            }
            else{
                alert('Something went wrong');
            }
            console.log(error);
        });
}
</script>


<style scoped>
.form-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.form-title {
  margin-bottom: 24px;
  color: rgb(33, 150, 243);
}

.register-button {
  width: 100%;
  background-color: rgb(63, 195, 128);
  border-radius: 4px;
  border: none;
  color: white;
}

.register-button:hover {
  background-color: rgb(63, 195, 128);
}

.a-form-item {
  margin-bottom: 24px;
}

.a-input,
.a-input-password {
  border-radius: 4px;
}

.form-switch {
  text-align: center;
  margin-top: 12px;
  font-size: 0.9em;
  color: #a9a9a9;
  cursor: pointer;
}

.form-switch:hover {
  color: #1890ff;
}
</style>