<template>
    <div class="form-container">
      <a-typography-title :level="4" class="form-title">Register</a-typography-title>
      <a-form name="basic" layout="vertical" autocomplete="off">
        <a-form-item label="Username" name="username">
          <a-input v-model:value="username" @change="validate_username"/>
          <div id="username_warning" class="red" style="visibility: hidden;">This username has already been registered</div>
        </a-form-item>
  
        <a-form-item label="Email" name="email">
          <a-input v-model:value="email" @change="validate_email"/>
          <div id="email_warning" class="red" style="visibility: hidden;">This email has already been registered</div>
        </a-form-item>
  
        <a-form-item label="Password" name="password">
          <a-input-password v-model:value="password" @change="validate_password"/>
          <div id="password_warning" class="red" style="visibility: hidden;">Password must have at least 8 characters</div>
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
import $ from 'jquery';

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

            console.log(response.status)
            if(response.data.isSuccess){
                $("#register_form").css( "display", "None" );
                $("#activation_reminder").css( "display", "flex" );
            }

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


const validate_username = () => {
    var data = new FormData();
    data.append('username', username.value);

    var config = {
        method: 'post',
        url: 'http://127.0.0.1:5000/validate_username',
        data: data
    };

    axios(config)
        .then(function (response) {
            console.log(response.data)
            if(!response.data.isValid){
                $("#username_warning").css( "visibility", "visible" );
            }else{
                $("#username_warning").css( "visibility", "hidden" );
            }
        })
        .catch(function (error) {
            console.log(error);
        });
}

const validate_email = () => {
    var data = new FormData();
    data.append('email', email.value);

    var config = {
        method: 'post',
        url: 'http://127.0.0.1:5000/validate_email',
        data: data
    };

    axios(config)
        .then(function (response) {
            console.log(response.status)
            if(!response.data.isValid){
                $("#email_warning").css( "visibility", "visible" );
            }else{
                $("#email_warning").css( "visibility", "hidden" );
            }
        })
        .catch(function (error) {
            console.log(error);
        });
}

const validate_password = () => {
    if(password.value.length < 8){
        $("#password_warning").css( "visibility", "visible" );
    }else{
        $("#password_warning").css( "visibility", "hidden" );
    }
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

<style scoped>
.red{
    color: red;
}

#register_form{
    display: block;
}

#activation_reminder{
  display: none;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  margin-top: auto;
  position: absolute;
  top:0;
  bottom: 0;
  left: 0;
  right: 0;
}

h1 {
  display: block;
  font-size: 3em;
  margin-top: 0.67em;
  margin-bottom: 0.67em;
  margin-left: 0;
  margin-right: 0;
  font-weight: bold;
}

h2 {
  display: block;
  font-size: 1.4em;
  margin-top: 0.2em;
  margin-bottom: 0.2em;
  margin-left: 0;
  margin-right: 0;
}

.wrapper{
    height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    background-color:#eee
}

.checkmark__circle{
    stroke-dasharray: 166;
    stroke-dashoffset: 166;
    stroke-width: 2;
    stroke-miterlimit: 10;
    stroke: #7ac142;
    fill: none;
    animation: stroke 0.6s cubic-bezier(0.65, 0, 0.45, 1) forwards

}
.checkmark{
    width: 56px;
    height: 56px;
    border-radius: 50%;
    display: block;
    stroke-width: 2;
    stroke: #fff;
    stroke-miterlimit: 10;
    box-shadow: inset 0px 0px 0px #7ac142;
    animation: fill .4s ease-in-out .4s forwards, scale .3s ease-in-out .9s both
}

.checkmark__check{
    transform-origin: 50% 50%;
    stroke-dasharray: 48;
    stroke-dashoffset: 48;
    animation: stroke 0.3s cubic-bezier(0.65, 0, 0.45, 1) 0.8s forwards
}

@keyframes stroke{
    100%{stroke-dashoffset: 0}
}

@keyframes scale{
    0%, 100%{transform: none}
    50%{transform: scale3d(1.1, 1.1, 1)}
}

@keyframes fill{
    100%{box-shadow: inset 0px 0px 0px 30px #7ac142}
}
</style>

<style>
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