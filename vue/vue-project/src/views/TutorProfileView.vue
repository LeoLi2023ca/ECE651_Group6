<template>
        <a-layout-content style="display: flex; align-items: center; justify-content: center; min-height: 80vh;">
            <div class="form-container">
                <a-typography-title :level="4" class="form-title">Tutor Profile</a-typography-title>
                <a-form :model="formState" layout="vertical" :disabled="componentDisabled">
                    <a-form-item ref="nickname" label="Nickname" name="nickname">
                        <a-input v-model:value="formState.nickname" />
                    </a-form-item>
                    <a-form-item ref="email" label="Email" name="email">
                        <a-input v-model:value="formState.email" />
                    </a-form-item>
                    <a-form-item ref="school_name" label="School Name" name="school_name">
                        <a-input v-model:value="formState.school_name" />
                    </a-form-item>
                    <a-form-item ref="edu_level" label="Education" name="edu_level">
                        <a-select v-model:value="formState.edu_level" placeholder="Select a subject">
                            <a-select-option value="highschool">highschool</a-select-option>
                            <a-select-option value="bachelor">bachelor</a-select-option>
                            <a-select-option value="master">master</a-select-option>
                            <a-select-option value="phd">phd</a-select-option>
                        </a-select>
                    </a-form-item>
                    <a-form-item label="Subjects" name="subjects">
                        <a-checkbox-group v-model:value="formState.subjects">
                            <a-checkbox class="checkbox-text" :value="'Chinese'">Chinese</a-checkbox>
                            <a-checkbox class="checkbox-text" :value="'English'">English</a-checkbox>
                            <a-checkbox class="checkbox-text" :value="'Math'">Math</a-checkbox>
                            <a-checkbox class="checkbox-text" :value="'Chemistry'">Chemistry</a-checkbox>
                            <a-checkbox class="checkbox-text" :value="'Physics'">Physics</a-checkbox>
                            <a-checkbox class="checkbox-text" :value="'Biology'">Biology</a-checkbox>
                            <!-- <a-checkbox :value="'Business_Management'">Business Management</a-checkbox> -->
                            <a-checkbox :value="'Geography'">Geography</a-checkbox>
                            <a-checkbox :value="'History'">History</a-checkbox>
                        </a-checkbox-group>
                    </a-form-item>
                    <a-form-item label="Salary" name="salaryRange">
                        <div style="display: flex; justify-content: space-between;">
                            <div style="flex: 1; margin-right: 10px;">
                            <label for="tuition-min">Min</label>
                            <a-input-number id="tuition-min" v-model:value="formState.salaryRange.min" style="width: 100%;" />
                            </div>
                            <div style="flex: 1;">
                            <label for="tuition-max">Max</label>
                            <a-input-number id="tuition-max" v-model:value="formState.salaryRange.max" min="formState.salaryRange.min" style="width: 100%;" />
                            </div>
                        </div>
                    </a-form-item>    
                    <a-form-item ref="timezone" label="Timezone" name="timezone">
                        <a-select v-model:value="formState.timezone" placeholder="Select timezone">
                            <a-select-option v-for="tz in timezones" :key="tz.value" :value="tz.value" :default="'UTC -04:00'">{{ tz.label }}</a-select-option>
                        </a-select>
                    </a-form-item>
                    <!-- <a-form-item ref="available_time" label="Available" name="available_time">
                        <a-input v-model:value="formState.available_time" />
                    </a-form-item> -->
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
    nickname: user_info.username,
    email: '',
    school_name: '',
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
    // getProfile(user_info.username);
    loadProfile();
});

function loadProfile() {
    if(!user_info){
        console.log('user_info is null');
        return;
    }
    formState.nickname = user_info.username;
    // console.log(user_info.email);
    formState.email = user_info.email;
    formState.school_name = user_info.school_name;
    formState.edu_level = user_info.edu_level;
    // if(user_info.timezone == null){
    //     formState.timezone = 'UTC-4';
    // }
    formState.timezone = user_info.timezone;
    // console.log(user_info.salary)
    // if(user_info.salary == null){
    //     formState.salaryRange.min = 0;
    //     formState.salaryRange.max = 0;
    // }
    // else{
    //     console.log(user_info.salary);
    //     formState.salaryRange.min = user_info.salary.split('-')[0];
    //     formState.salaryRange.max = user_info.salary.split('-')[1];
    // }
    formState.salaryRange.min = user_info.salary.split('-')[0];
    formState.salaryRange.max = user_info.salary.split('-')[1];
    if (user_info.subjects != null){
        formState.subjects = user_info.subjects.split(',');
    }
    else{
        formState.subjects = [];
    }
    // console.log(formState.subjects);
    formState.available_time = user_info.available_time;
    formState.msg = user_info.msg;
}
function getProfile(username_) {
    const params = {
        username: username_
    };
    let config = {
        method: 'get',
        maxBodyLength: Infinity,
        url: 'http://127.0.0.1:5000/getTutorProfileByUsername',
        headers: {},
        params: params
    };

    axios.request(config)
        .then((response) => {
            // update user_info
            sessionStorage.setItem('user_info', JSON.stringify(response.data.user_info));
            // console.log(JSON.stringify(response.data));
        })
        .catch((error) => {
            console.log(error);
        });

};

const updateProfile = async () => {
    var data = new FormData();
    data.append('username', user_info.username);
    data.append('nickname', formState.nickname);
    data.append('email', formState.email);
    data.append('edu_level', formState.edu_level);
    data.append('timezone', formState.timezone || 'UTC-4');
    data.append('available_time', formState.available_time || '');
    data.append('message', formState.msg || '');
    data.append('school_name', formState.school_name);
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
    background: linear-gradient(to right, #ffffff, #abd0ea);
    display: flex;
    flex-direction: column;
    text-align: center;
}

.form-title {
    color:  rgb(33, 150, 243);
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
  background-color:  rgb(33, 150, 243);
  color: white;
}

/* .checkbox-text {
  color: rgb(14, 15, 17);
} */

</style>