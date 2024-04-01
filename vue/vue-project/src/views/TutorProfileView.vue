<template>
    <a-layout style="padding: 0px 30px 0px">
        <a-layout-content
            :style="{ background: '#fff', padding: '80px', minHeight: '80vh', display: 'flex', justifyContent: 'center', alignItems: 'center' }">

            <div style="max-width: 600px;">
                <a-form :model="formState" :label-col="labelCol" :wrapper-col="wrapperCol" layout="horizontal"
                    :disabled="componentDisabled">
                    <a-form-item ref="nickname" label="Nickname" name="nickname">
                        <a-input v-model:value="formState.nickname" />
                    </a-form-item>
                    <a-form-item ref="email" label="Email" name="email">
                        <a-input v-model:value="formState.email" />
                    </a-form-item>
                    <a-form-item ref="edu_level" label="Education" name="edu_level">
                        <a-select v-model:value="formState.edu_level" placeholder="Select a subject">
                            <a-select-option value="highschool">highschool</a-select-option>
                            <a-select-option value="bachelor">bachelor</a-select-option>
                            <a-select-option value="master">master</a-select-option>
                            <a-select-option value="phd">phd</a-select-option>
                            <!-- Add more subjects as needed -->
                        </a-select>
                    </a-form-item>
                    <a-form-item label="Subjects" name="subjects">
                        <a-checkbox-group v-model:value="formState.subjects">
                            <a-checkbox :value="'Chinese'">Chinese</a-checkbox>
                            <a-checkbox :value="'English'">English</a-checkbox>
                            <a-checkbox :value="'Math'">Math</a-checkbox>
                            <a-checkbox :value="'Chemistry'">Chemistry</a-checkbox>
                            <a-checkbox :value="'Physics'">Physics</a-checkbox>
                            <a-checkbox :value="'Biology'">Biology</a-checkbox>
                            <a-checkbox :value="'Business_management'">Business Management</a-checkbox>
                            <a-checkbox :value="'Geography'">Geography</a-checkbox>
                            <a-checkbox :value="'History'">History</a-checkbox>
                            <!-- Add more subjects as needed -->
                        </a-checkbox-group>
                    </a-form-item>
                    <a-form-item label="Salary" name="salaryRange">
                        <div style="display: flex; justify-content: space-between;">
                        <a-input-number
                            v-model:value="formState.salaryRange.min"
                            style="width: 45%;"
                            placeholder="Min"
                            min="0"
                        />
                        <a-input-number
                            v-model:value="formState.salaryRange.max"
                            style="width: 45%;"
                            placeholder="Max"
                            :min="formState.salaryRange.min"
                        />
                        </div>
                    </a-form-item>    
                    <a-form-item ref="timezone" label="Timezone" name="timezone">
                        <a-select v-model:value="formState.timezone" placeholder="Select timezone">
                            <a-select-option v-for="tz in timezones" :key="tz.value" :value="tz.value">{{ tz.label }}</a-select-option>
                        </a-select>
                    </a-form-item>
                    <a-form-item ref="available_time" label="Available" name="available_time">
                        <a-input v-model:value="formState.available_time" />
                    </a-form-item>
                    <a-form-item ref="msg" label="Message" name="msg">
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

const timezones = Array.from({ length: 25 }, (_, i) => {
  const value = i - 12;
  const sign = value >= 0 ? '+' : '-';
  return { label: `UTC ${sign}${Math.abs(value).toString().padStart(2, '0')}:00`, value: `${sign}${Math.abs(value).toString().padStart(2, '0')}:00` };
});

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
    subjects: [],
    salaryRange: {
        min: 0,
        max: 0,
    },
})

onMounted(() => {
    loadProfile();
});

function loadProfile() {
    formState.nickname = user_info.nickname;
    formState.email = user_info.email;
    formState.edu_level = user_info.edu_level;
    // if(user_info.timezone == null){
    //     formState.timezone = 'UTC-4';
    // }
    formState.timezone = user_info.timezone;
    if(user_info.salary == null){
        formState.salaryRange.min = 0;
        formState.salaryRange.max = 0;
    }
    else{
        formState.salaryRange.min = user_info.salary.split('-')[0];
        formState.salaryRange.max = user_info.salary.split('-')[1];
    }
    formState.subjects = user_info.subjects.split(',');
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
    data.append('timezone', formState.timezone || 'UTC-4');
    data.append('available_time', formState.available_time || '');
    data.append('message', formState.msg || '');
    // console.log(formState.subjects);
    data.append('subjects', formState.subjects);
    data.append('salary', `${formState.salaryRange.min}-${formState.salaryRange.max}`)


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