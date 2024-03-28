<template>
    <div>
        <a-modal v-model:open="open" title="Post Detail">
            <template #footer>
                <a-button key="back" @click="handleCancel">Return</a-button>
                <a-button key="submit" type="primary" @click="handleOk">Contact</a-button>
            </template>
            <a-descriptions :column="4" title="Tutor Info" size="small" bordered>
                <a-descriptions-item label="nickname" :span="2">{{ nickname }}</a-descriptions-item>
                <a-descriptions-item label="Salary" :span="2">{{ salary }}</a-descriptions-item>
                <a-descriptions-item label="Subject" :span="2">{{ subject_name }}</a-descriptions-item>
                <a-descriptions-item label="Education" :span="2">{{ edu_level }}</a-descriptions-item>
                <a-descriptions-item label="Time" :span="2">{{ available_time }}</a-descriptions-item>
                <a-descriptions-item label="Timezone" :span="2">{{ timezone }}</a-descriptions-item>
                <a-descriptions-item label="message" :span="4">{{ msg }} </a-descriptions-item>
            </a-descriptions>
        </a-modal>
        <a-modal v-model:open="chatOpen" title="Chat">
            <ChatPage v-if="chatOpen" :tutor-username="username" @close="chatOpen = false" />
        </a-modal>
    </div>
</template>
<script setup>
import { ref } from 'vue';
import axios from 'axios';
import ChatPage from './ChatPage.vue';
const open = ref(false);

const username = ref('');
const nickname = ref('');
const edu_level = ref('');
const subject_name = ref('');
const msg = ref('');
const salary = ref('');
const timezone = ref('');
const available_time = ref('');

const chatOpen = ref(false);

function showModal(username) {
    fillProfileWithUsername(username);
    open.value = true;
};
function fillProfileWithUsername(username_) {
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
            const tutor_info = response.data.user_info;
            username.value = tutor_info.username;
            nickname.value = tutor_info.nickname;
            edu_level.value = tutor_info.edu_level;
            subject_name.value = tutor_info.subject_name;
            msg.value = tutor_info.msg;
            salary.value = tutor_info.salary;
            timezone.value = tutor_info.timezone;
            available_time.value = tutor_info.available_time;
            // console.log(JSON.stringify(response.data));
        })
        .catch((error) => {
            console.log(error);
        });

};
const handleOk = () => {
    chatOpen.value = true;
};

const handleCancel = () => {
    open.value = false;
};
defineExpose({
    showModal
});
</script>