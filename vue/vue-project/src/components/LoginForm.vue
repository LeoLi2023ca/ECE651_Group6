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
        <div>
            <input type="radio" id="radio_1" value="Student" v-model="role">
            <label for="radio_1">Student</label>
            <input type="radio" id="radio_2" value="Tutor" v-model="role">
            <label for="radio_2">Tutor</label>
        </div>
        <button type="submit">登录</button>
    </form>
</template>
  
<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router'; // 导入useRouter，如果你使用Vue Router来导航

const username = ref('');
const password = ref('');
const router = useRouter(); // 使用useRouter
const role = ref('Student')

const handleSubmit = async () => {
    console.log(role.value)
    try {
        const response = await axios.post('YOUR_API_ENDPOINT/login', {
            username: username.value,
            password: password.value,
        });
        if (response.data.token) {
            localStorage.setItem('token', response.data.token);
            console.log('登录成功');
        } else {
            console.log('登录失败');
        }
    } catch (error) {
        console.error('登录请求失败', error);
    }
};
const handleRegister = async () => {
    try {
        const response = await axios.post('YOUR_API_ENDPOINT/login', {
            username: username.value,
            password: password.value,
        });
        if (response.data.code==1) {
            localStorage.setItem('token', response.data.token);
            console.log('注册成功');
        } else {
            console.log('注册失败');
        }
    } catch (error) {
        console.error('注册请求失败', error);
    }
};


</script>
  