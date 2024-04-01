<template>
    <a-form name="basic" :label-col="{ span: 6 }" :wrapper-col="{ span: 12 }" autocomplete="off">
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
            <div id="password_warning" class="red" style="display: none;">This password has already been registered</div>
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
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
import { useStore } from 'vuex';
import $ from 'jquery'

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
            router.push({ name: 'home' });

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
            if(!response.data.isValid){
                $("#username_warning").css( "display", "block" );
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
            if(!response.data.isValid){
                $("#email_warning").css( "display", "block" );
            }
        })
        .catch(function (error) {
            console.log(error);
        });
}

const validate_password = () => {
    var data = new FormData();
    data.append('password', password.value);

    var config = {
        method: 'post',
        url: 'http://127.0.0.1:5000/validate_password',
        data: data
    };

    axios(config)
        .then(function (response) {
            if(!response.data.isValid){
                $("#password_warning").css( "display", "block" );
            }
        })
        .catch(function (error) {
            console.log(error);
        });
}
</script>


<style scoped>
.red{
    color: red;
}
</style>