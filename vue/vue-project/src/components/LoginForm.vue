<template>
    <form @submit.prevent="handleSubmit">
        <div>
            <label for="username">用户名:</label>
            <input id="username" v-model="username" type="text" placeholder="请输入用户名" />
        </div>
        <div>
            <label for="password">密码:</label>
            <input id="password" v-model="password" type="password" placeholder="请输入密码" />
        </div>

        <button type="submit">登录</button>
    </form>
</template>
  
<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router'; // 导入useRouter，如果你使用Vue Router来导航
import axios from 'axios';

const username = ref('');
const password = ref('');

const handleSubmit = async () => {
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
};


</script>
  