<template>
    <a-form id="register_form" name="basic" :label-col="{ span: 6 }" :wrapper-col="{ span: 12 }" autocomplete="off">
        <a-form-item label="Username" name="username">
            <a-input v-model:value="username" @change="validate_username"/>
            <div id="username_warning" class="red" style="display: none;">This username has already been registered</div>
        </a-form-item>

        <a-form-item label="Email" name="email">
            <a-input v-model:value="email" @change="validate_email"/>
            <div id="email_warning" class="red" style="display: none;">This email has already been registered</div>
        </a-form-item>

        <a-form-item label="Password" name="password">
            <a-input-password v-model:value="password" @change="validate_password"/>
            <div id="password_warning" class="red" style="display: none;">Password must have at least 8 characters</div>
        </a-form-item>

        <a-form-item label="Role">
            <a-radio-group v-model:value="role">
                <a-radio value="Student">Student</a-radio>
                <a-radio value="Tutor">Tutor</a-radio>
            </a-radio-group>
        </a-form-item>

        <a-form-item :wrapper-col="{ offset: 6, span: 12 }">
            <a-button style="width: 225px;" type="primary" @click="register()">Register</a-button>
        </a-form-item>
    </a-form>
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