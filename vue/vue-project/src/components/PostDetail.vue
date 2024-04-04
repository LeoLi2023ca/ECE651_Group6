<template>
  <div>
    <a-modal v-model:open="open" title="Post Detail">
      <template #footer>
        <a-button key="back" @click="handleCancel">Return</a-button>
        <!-- <a-button key="submit" type="primary" :loading="loading" @click="handleOk">Contact</a-button> -->
      </template>
      <a-descriptions title="Post Info" size="small" bordered>
        <a-descriptions-item label="Title" :span="4">{{ title }}</a-descriptions-item>
        <a-descriptions-item label="Subject" :span="2">{{ subject }}</a-descriptions-item>
        <a-descriptions-item label="Salary" :span="2">{{ salary }}</a-descriptions-item>
        <a-descriptions-item label="Time" :span="2">{{ available_time }}</a-descriptions-item>
        <a-descriptions-item label="Timezone" :span="2">{{ timezone }}</a-descriptions-item>
        <a-descriptions-item label="Message" :span="4">{{ message }} </a-descriptions-item>
      </a-descriptions>
    </a-modal>
  </div>
</template>
<script setup>
import { ref } from 'vue';
import axios from 'axios';
const open = ref(false);
const message = ref('');
const salary = ref('');
const subject = ref('');
const title = ref('');
const available_time = ref('');
const timezone = ref('');

function showModal(post_id) {
  fillPostWithID(post_id);
  open.value = true;
};
function fillPostWithID(post_id) {
  const params = {
    post_id: post_id
  };
  let config = {
    method: 'get',
    maxBodyLength: Infinity,
    url: 'http://127.0.0.1:5000/getPostByPostID',
    headers: {},
    params: params
  };

  axios.request(config)
    .then((response) => {
      console.log("Test" + response);
      const post = JSON.parse(JSON.stringify(response.data.post));
      message.value = post.msg
      salary.value = post.salary
      subject.value = post.subject_name
      title.value = post.title
      available_time.value = post.available_time
      timezone.value = post.timezone
      console.log(post)
      console.log(JSON.stringify(response.data));
    })
    .catch((error) => {
      console.log(error);
    });

};
// const handleOk = () => {
//   loading.value = true;
//   setTimeout(() => {
//     loading.value = false;
//     open.value = false;
//   }, 2000);
// };

const handleCancel = () => {
  open.value = false;
};
defineExpose({
  showModal
});
</script>