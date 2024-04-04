<template>
    <a-layout-content style="display: flex; align-items: center; justify-content: center; min-height: 80vh;">
        <div class="grid-container">
        <a-card class="login-register-form">
            <RegisterForm/>
            <a-form-item :wrapper-col="{ offset: 6, span: 12 }">
            <div class="center-button">
                <router-link to="/login">
                    <a-button >Already have an account?</a-button>
                </router-link>
            </div>
            </a-form-item>
        </a-card>
        </div>
    </a-layout-content>
    <div id="activation_reminder">
        <svg class="checkmark" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 52 52">
            <circle class="checkmark__circle" cx="26" cy="26" r="25" fill="none"/>
            <path class="checkmark__check" fill="none" d="M14.1 27.2l7.1 7.2 16.7-16.8"/>
        </svg>
        <h1>Thank you for considering TutorEase!</h1>
        <h2>A activation email have been sent to your email.</h2>
        <h2>Click the activate button in the confirmation email to complete the registration.</h2>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
import { useStore } from 'vuex';
import $ from 'jquery';
import RegisterForm from '../components/RegisterForm.vue';

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

                // sessionStorage.setItem('role', response.data.code);
                // sessionStorage.setItem('user_info', JSON.stringify(response.data.user_info))
                // store.commit('setUserRole', response.data.code);
                // router.push({ name: 'home' });
            }

        })
        .catch(function (error) {
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
            console.log(response.status)
            if(!response.data.isValid){
                $("#username_warning").css( "display", "block" );
            }else{
                $("#username_warning").css( "display", "none" );
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
                $("#email_warning").css( "display", "block" );
            }else{
                $("#email_warning").css( "display", "none" );
            }
        })
        .catch(function (error) {
            console.log(error);
        });
}

const validate_password = () => {
    if(password.value.length < 8){
        $("#password_warning").css( "display", "block" );
    }else{
        $("#password_warning").css( "display", "none" );
    }
}
</script>


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