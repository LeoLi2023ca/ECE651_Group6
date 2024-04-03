<template>
  <a-layout-content style="display: flex; align-items: center; justify-content: center; min-height: 80vh;">
    <div class="form-container">
      <a-typography-title :level="4" class="form-title">Student Profile</a-typography-title>
      <a-form :model="formState" layout="vertical" :disabled="componentDisabled">
        <a-form-item label="Nickname" name="nickname">
          <a-input v-model:value="formState.nickname" />
        </a-form-item>
        <a-form-item label="Email" name="email">
          <a-input v-model:value="formState.email" />
        </a-form-item>
        <a-form-item label="Grade" name="grade">
          <a-select v-model:value="formState.grade" placeholder="Select grade">
            <a-select-option value="kindergarten">Kindergarten</a-select-option>
            <a-select-option value="kindergarten">Kindergarten</a-select-option>
            <a-select-option value="primary">Primary</a-select-option>
            <a-select-option value="secondary">Secondary</a-select-option>
            <a-select-option value="bachelor">Bachelor</a-select-option>
            <a-select-option value="graduate">Graduate</a-select-option>
            <a-select-option value="other">Other</a-select-option>
          </a-select>
        </a-form-item>
        <a-form-item label="Timezone" name="timezone">
          <a-select v-model:value="formState.timezone" placeholder="Select timezone">
            <a-select-option v-for="tz in timezones" :key="tz.value" :value="tz.value">{{ tz.label }}</a-select-option>
          </a-select>
        </a-form-item>
        <a-form-item label="Message" name="message">
          <a-textarea :rows="4" v-model:value="formState.msg" />
        </a-form-item>
        <div style="text-align: center;">
          <a-button @click="e => (componentDisabled = !componentDisabled)">
            Edit
          </a-button>
        </div>
      </a-form>
    </div>
  </a-layout-content>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue';
import axios from 'axios';
import { message } from 'ant-design-vue';

const componentDisabled = ref(true);
const user_info = JSON.parse(sessionStorage.getItem('user_info'));

// const labelCol = {
//   style: {
//     width: '80px',
//   },
// };
// const wrapperCol = {
//   span: 20,
// };
const formState = reactive({
  nickname: '123',
  email: '',
  grade: '',
  timezone: '',
  msg: ''
})

onMounted(() => {
  loadProfile();
});

function loadProfile() {
  formState.nickname = user_info.nickname;
  formState.email = user_info.email;
  formState.grade = user_info.grade;
  formState.timezone = user_info.timezone;
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
const timezones = Array.from({ length: 25 }, (_, i) => {
  const value = i - 12;
  const sign = value >= 0 ? '+' : '-';
  return { label: `UTC ${sign}${Math.abs(value).toString().padStart(2, '0')}:00`, value: `${sign}${Math.abs(value).toString().padStart(2, '0')}:00` };
});

const updateProfile = async () => {
  var data = new FormData();
  data.append('username', user_info.username);
  data.append('nickname', formState.nickname);
  data.append('email', formState.email);
  data.append('grade', formState.grade);
  data.append('timezone', formState.timezone);
  data.append('msg', formState.msg);


  var config = {
    method: 'post',
    url: 'http://127.0.0.1:5000/updateStudentProfile',
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


<style scoped>
.form-container {
    width: 100%; 
    max-width: 400px;
    margin: 5vh auto 0px auto;
    padding: 40px;
    background: #fff;
    border: 2px solid #e0e0e0;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    background: linear-gradient(to right, #ffffff, #e49290);
    display: flex;
    flex-direction: column;
    text-align: center;
}

.form-title {
  color: rgb(232, 122, 121);
  margin-bottom: 24px;
  text-align: center;
}

.a-form-item {
  margin-bottom: 20px;
}

.form-container .ant-btn {
  background-color: rgb(63, 195, 128);
  color: white;
  border: none;
  border-radius: 4px;
}
  
.form-container .ant-btn:hover {
  background-color: rgb(232, 122, 121);
  color: white;
}
</style>
