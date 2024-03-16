<template>
    <a-form name="basic" :label-col="{ span: 6 }" :wrapper-col="{ span: 12 }" autocomplete="off">
        <a-form-item label="Username" name="username">
            <a-input v-model:value="username" />
        </a-form-item>

        <a-form-item label="Password" name="password">
            <a-input-password v-model:value="password" />
        </a-form-item>
        <a-form-item label="Password" name="password"
            :rules="[{ required: true, message: 'Please input your password!' }]">
            <a-input-password v-model:value="password" />
        </a-form-item>

        <a-form-item :wrapper-col="{ offset: 6, span: 12 }">
            <a-button style="width: 225px;" type="primary" @click="login()">Login</a-button>
        </a-form-item>
    </a-form>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';
import { useStore } from 'vuex';

const store = useStore();
const router = useRouter();

const username = ref('');
const password = ref('');

const login = async () => {
    var data = new FormData();
    data.append('username', username.value);
    data.append('password', password.value);

    var config = {
        method: 'post',
        url: 'http://127.0.0.1:5000/login',
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
};
</script>
