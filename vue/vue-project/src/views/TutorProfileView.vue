<template>
    <a-layout style="padding: 0px 30px 0px">
        <a-layout-content
            :style="{ background: '#fff', padding: '80px', minHeight: '80vh', display: 'flex', justifyContent: 'center', alignItems: 'center' }">

            <div style="max-width: 600px;">
                <a-form :model="formState" :label-col="labelCol" :wrapper-col="wrapperCol" layout="horizontal"
                    :disabled="componentDisabled">
                    <a-form-item ref="nickname" label="nickname" name="nickname">
                        <a-input v-model:value="formState.nickname" />
                    </a-form-item>
                    <a-form-item ref="email" label="email" name="email">
                        <a-input v-model:value="formState.email" />
                    </a-form-item>
                    <a-form-item ref="edu_level" label="edu_level" name="edu_level">
                        <a-input v-model:value="formState.edu_level" />
                    </a-form-item>
                    <a-form-item ref="timezone" label="timezone" name="timezone">
                        <a-input v-model:value="formState.timezone" />
                    </a-form-item>
                    <a-form-item ref="available_time" label="available" name="available_time">
                        <a-input v-model:value="formState.available_time" />
                    </a-form-item>
                    <a-form-item ref="msg" label="message" name="msg">
                        <a-textarea :rows="4" v-model:value="formState.msg" />
                    </a-form-item>
                </a-form>
                <div v-if="componentDisabled">
                    <a-button @click="e => (componentDisabled = !componentDisabled)">
                        Edit
                    </a-button>
                </div>
                <div v-else :label-col="labelCol" :wrapper-col="wrapperCol">
                    <a-button @click="e => (updateProfile(), componentDisabled = !componentDisabled)">
                        Submit
                    </a-button>
                    <a-button style="margin-left: 17px"
                        @click="e => (loadProfile(), componentDisabled = !componentDisabled)">
                        Cancel
                    </a-button>
                </div>
            </div>
        </a-layout-content>
    </a-layout>
</template>
<script setup>
import { ref, reactive, onMounted } from 'vue';
import axios from 'axios';
import { message } from 'ant-design-vue';

const componentDisabled = ref(true);
const user_info = JSON.parse(sessionStorage.getItem('user_info'));

const labelCol = {
    style: {
        width: '80px',
    },
};
const wrapperCol = {
    span: 20,
};
const formState = reactive({
    nickname: '123',
    email: '',
    edu_level: '',
    timezone: '',
    available_time: '',
    msg: '',
})

onMounted(() => {
    loadProfile();
});

function loadProfile() {
    formState.nickname = user_info.nickname;
    formState.email = user_info.email;
    formState.edu_level = user_info.edu_level;
    formState.timezone = user_info.timezone;
    formState.available_time = user_info.available_time;
    formState.msg = user_info.msg;
}
// const getProfile = async () => {
//   var data = new FormData();

//   data.append('username', user.username);

//   var config = {
//     method: 'get',
//     url: 'http://localhost:5000/getStudentProfileByUsername',
//     data: data
//   };

//   axios(config)
//     .then(function (response) {
//       sessionStorage.setItem('role', response.data.code);
//       sessionStorage.setItem('user_info', JSON.stringify(response.data.user_info))
//       store.commit('setUserRole', response.data.code);
//       router.push({ name: 'home' });
//     })
//     .catch(function (error) {
//       console.log(error);
//     });
// }

const updateProfile = async () => {
    var data = new FormData();
    data.append('username', user_info.username);
    data.append('nickname', formState.nickname);
    data.append('email', formState.email);
    data.append('edu_level', formState.edu_level);
    data.append('timezone', formState.timezone);
    data.append('available_time', formState.available_time)
    data.append('message', formState.msg);


    var config = {
        method: 'post',
        url: 'http://127.0.0.1:5000/updateTutorProfile',
        data: data
    };

    axios(config)
        .then(function (response) {
            sessionStorage.setItem('user_info', JSON.stringify(response.data.user_info));
            console.log(response);
            message.success('Profile updated successfully!');
        })
        .catch(function (error) {
            console.log(error);
        });
};
</script>