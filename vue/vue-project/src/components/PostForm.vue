<template>
  <a-form ref="formRef" :model="formState" :label-col="labelCol" :wrapper-col="wrapperCol" style="max-width: 500px;">
    <a-form-item ref="title" label="Title" name="title">
      <a-input v-model:value="formState.title" />
    </a-form-item>
    <a-form-item label="Subject" name="subject">
      <a-select v-model:value="formState.subject" placeholder="Select a subject">
        <a-select-option value="English">English</a-select-option>
        <a-select-option value="Math">Math</a-select-option>
        <a-select-option value="Science">Science</a-select-option>
        <a-select-option value="History">History</a-select-option>
        <!-- Add more subjects as needed -->
      </a-select>
    </a-form-item>
    <a-form-item ref="timezone" label="Timezone" name="timezone">
      <a-select v-model:value="formState.timezone" placeholder="Select timezone">
        <a-select-option v-for="tz in timezones" :key="tz.value" :value="tz.value">{{ tz.label }}</a-select-option>
      </a-select>
    </a-form-item>
    <a-form-item label="From" name="available_time">
      <a-time-picker
        format="HH:mm"
        v-model:value="formState.from"
        placeholder="Start Time"
      />
    </a-form-item>
    <a-form-item label="To">
      <a-time-picker
        format="HH:mm"
        v-model:value="formState.to"
        placeholder="End Time"
      />
    </a-form-item>
    <a-form-item ref="salary" label="Salary" name="salary">
      <a-input v-model:value="formState.salary" />
    </a-form-item>
    <a-form-item ref="message" label="Message" name="message">
      <a-textarea v-model:value="formState.message" :rows="4" />
    </a-form-item>
    <a-form-item v-if="!props.post_id" :wrapper-col="{ span: 14, offset: 4 }">
      <a-button type="primary" @click="onSubmit">Create</a-button>
      <a-button style="margin-left: 17px" @click="resetForm">Reset</a-button>
    </a-form-item>


    <!-- <a-form-item ref="name" label="Activity name" name="name">
      <a-input v-model:value="formState.name" />
    </a-form-item>
    <a-form-item label="Activity zone" name="region">
      <a-select v-model:value="formState.region" placeholder="please select your zone">
        <a-select-option value="shanghai">Zone one</a-select-option>
        <a-select-option value="beijing">Zone two</a-select-option>
      </a-select>
    </a-form-item>
    <a-form-item label="Activity time" required name="date1">
      <a-date-picker
        v-model:value="formState.date1"
        show-time
        type="date"
        placeholder="Pick a date"
        style="width: 100%"
      />
    </a-form-item>
    <a-form-item label="Instant delivery" name="delivery">
      <a-switch v-model:checked="formState.delivery" />
    </a-form-item>
    <a-form-item label="Activity type" name="type">
      <a-checkbox-group v-model:value="formState.type">
        <a-checkbox value="1" name="type">Online</a-checkbox>
        <a-checkbox value="2" name="type">Promotion</a-checkbox>
        <a-checkbox value="3" name="type">Offline</a-checkbox>
      </a-checkbox-group>
    </a-form-item>
    <a-form-item label="Resources" name="resource">
      <a-radio-group v-model:value="formState.resource">
        <a-radio value="1">Sponsor</a-radio>
        <a-radio value="2">Venue</a-radio>
      </a-radio-group>
    </a-form-item>
    <a-form-item label="Activity form" name="desc">
      <a-textarea v-model:value="formState.desc" />
    </a-form-item>
    <a-form-item :wrapper-col="{ span: 14, offset: 4 }">
      <a-button type="primary" @click="onSubmit">Create</a-button>
      <a-button style="margin-left: 10px" @click="resetForm">Reset</a-button>
    </a-form-item> -->
  </a-form>
</template>
<script setup>
import { reactive, ref, onMounted } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';


const props = defineProps({
  post_id: -1,
});
onMounted(() => {
  if (props.post_id) {
    fillPostWithID(props.post_id)
  }
});
const router = useRouter();
const user_info = JSON.parse(sessionStorage.getItem('user_info'));
// console.log(user_info);

const formRef = ref();
const labelCol = { span: 4 };
const wrapperCol = { span: 14 };
const formState = reactive({
  title: '',
  message: '',
  timezone: !props.post_id?user_info.timezone:'UTC -04:00',
  subject: '',
  salary: '',
  from: '',
  to: '',
});

const timezones = Array.from({ length: 25 }, (_, i) => {
  const value = i - 12;
  const sign = value >= 0 ? '+' : '-';
  return { label: `UTC ${sign}${Math.abs(value).toString().padStart(2, '0')}:00`, value: `${sign}${Math.abs(value).toString().padStart(2, '0')}:00` };
});

// const rules = {
//   title: [
//     {
//       required: true,
//       message: 'Please input Activity name',
//       trigger: 'change',
//     },
//     {
//       min: 3,
//       max: 5,
//       message: 'Length should be 3 to 5',
//       trigger: 'blur',
//     },
//   ],
//   timezone: [
//     {
//       required: true,
//       message: 'Please select Activity zone',
//       trigger: 'change',
//     },
//   ],
//   date1: [
//     {
//       required: true,
//       message: 'Please pick a date',
//       trigger: 'change',
//       type: 'object',
//     },
//   ],
//   type: [
//     {
//       type: 'array',
//       required: true,
//       message: 'Please select at least one activity type',
//       trigger: 'change',
//     },
//   ],
//   resource: [
//     {
//       required: true,
//       message: 'Please select activity resource',
//       trigger: 'change',
//     },
//   ],
//   desc: [
//     {
//       required: true,
//       message: 'Please input activity form',
//       trigger: 'blur',
//     },
//   ],
// };
// const onSubmit = () => {
//   formRef.value
//     .validate()
//     .then(() => {
//       console.log('values', formState, toRaw(formState));
//     })
//     .catch(error => {
//       console.log('error', error);
//     });
// };

const onSubmit = async () => {
  var data = new FormData();
  const availableTime = `${formState.from.format('HH:mm')} to ${formState.to.format('HH:mm')}`;

  data.append('title', formState.title)
  data.append('subject', formState.subject)
  data.append('timezone', formState.timezone)
  data.append('salary', formState.salary)
  data.append('msg', formState.message)
  data.append('available_time', availableTime)
  data.append('username', user_info.username)
  var config = {
    method: 'post',
    url: 'http://127.0.0.1:5000/create_post',
    data: data
  };

  axios(config)
    .then(function (response) {
      console.log(response)
      router.push({ name: 'my-post' });
    })
    .catch(function (error) {
      console.log(error);
    });
};
const handleUpdate = async () => {
  var data = new FormData();
  const availableTime = `${formState.from.format('HH:mm')} to ${formState.to.format('HH:mm')}`;
  data.append('post_id', props.post_id)
  data.append('title', formState.title)
  data.append('subject', formState.subject)
  data.append('timezone', formState.timezone)
  data.append('salary', formState.salary)
  data.append('msg', formState.message)
  data.append('available_time', availableTime)
  data.append('username', user_info.username)
  var config = {
    method: 'post',
    url: 'http://127.0.0.1:5000/update_post',
    data: data
  };

  axios(config)
    .then(function (response) {
      console.log(response)
      router.push({ name: 'my-post' });
    })
    .catch(function (error) {
      console.log(error);
    });
};
const resetForm = () => {
  formRef.value.resetFields();
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
      const post = JSON.parse(JSON.stringify(response.data.post));
      formState.message=post.msg
      formState.salary=post.salary
      formState.subject=post.subject_name
      formState.title=post.title
      if (post.time) {
        const times = post.time.split(' to ');
        if (times.length === 2) {
          formState.from = times[0];
          formState.to = times[1];
        }
        else{
          formState.from = '';
          formState.to = '';
        }
      }
      formState.timezone=post.timezone
      console.log(post)
      console.log(JSON.stringify(response.data));
    })
    .catch((error) => {
      console.log(error);
    });

};
defineExpose({handleUpdate})
</script>

<style scoped></style>