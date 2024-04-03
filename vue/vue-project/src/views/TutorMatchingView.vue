<template>
    <a-layout>
        <!-- <TutorDetail ref="tutor_detail" /> -->
        <div class="section">
        <h2 class="title">Matched Students</h2>
        <a-row :gutter="16">
            <a-col v-for="(item, index) in paginatedData" :key="index" :span="8">
            <a-card :title="item.nickname" :style="{ margin: '10px' }" @click="setUsername(item.username)">
                <p>{{ "Grade: "+item.grade }}</p>
                <!-- <p>{{ "Education: "+item.edu_level }}</p>
                <p>{{ "Expected Salary: "+item.salary }}</p> -->
            </a-card>
            </a-col>
        </a-row>
        </div>
        
        <div class="section">
        <h2 class="title">Asked For Matching</h2>
        <a-row :gutter="16">
            <a-col v-for="(item, index) in askedPaginatedData" :key="index" :span="8">
            <a-card :title="item.nickname" :style="{ margin: '10px' }" @click="setUsername(item.username)">
                <p>{{ "Grade: "+item.grade }}</p>
                <!-- <p>{{ "Education: "+item.edu_level }}</p>
                <p>{{ "Expected Salary: "+item.salary }}</p> -->
            </a-card>
            </a-col>
        </a-row>
        <a-pagination :total="askedForMatching.length" :pageSize="pageSize" @change="handlePageChange"
            @showSizeChange="handlePageSizeChange" />
        </div>
    </a-layout>
    <a-modal v-model:open="chatOpen" title="Chat">
        <ChatPage v-if="chatOpen" :receiver="currentChatUsername" @close="chatOpen = false" />
    </a-modal>
  </template>
  
  <script setup>
  import { computed, ref, onMounted } from 'vue';
  import ChatPage from '@/components/ChatPage.vue';
  
  import axios from 'axios';
  
  const pageSize = ref(9);
  const currentPage = ref(1);
  const tutor_detail = ref(null);
  const paginatedData = ref([]);
  const askedPaginatedData = ref([]);
  const askedForMatching = ref([]);
  const Matched = ref([]);
  const user_info = JSON.parse(sessionStorage.getItem('user_info'));
  const chatOpen = ref(false);
  const currentChatUsername = ref('');
  
  onMounted(async () => {
    await loadData();
    const start = (currentPage.value - 1) * pageSize.value;
    const end = start + pageSize.value;
    paginatedData.value = Matched.value.slice(start, end);
    askedPaginatedData.value = askedForMatching.value.slice(start, end);
  });
  
  async function loadData() {
    const params = {
      tutor_username: user_info.username,
    };
    const config = {
      method: 'get',
      url: 'http://127.0.0.1:5000/getTutorsAskedStudent',
      params: params
    };
    await axios.request(config)
      .then((response) => {
        for(let i = 0; i < response.data.list.length; i++) {
          askedForMatching.value.push({
            username: response.data.list[i].username,
            nickname: response.data.list[i].nickname,
            grade: response.data.list[i].grade,
            msg: response.data.list[i].msg,
            timezone: response.data.list[i].timezone,
          })
        }
      })
      .catch((error) => {
        console.error(error);
      });
    
    const config2 = {
      method: 'get',
      url: 'http://127.0.0.1:5000/getTutorMatchedStudent',
      params: params
    };
    await axios.request(config2)
      .then((response) => {
        for(let i = 0; i < response.data.list.length; i++) {
          Matched.value.push({
            username: response.data.list[i].username,
            nickname: response.data.list[i].nickname,
            grade: response.data.list[i].grade,
            msg: response.data.list[i].msg,
            timezone: response.data.list[i].timezone,
          })
        }
      })
      .catch((error) => {
        console.error(error);
      });
  }
  
  function setUsername(username) {
    currentChatUsername.value = username;
    chatOpen.value = true;
  }
  
  function handlePageChange(page) {
    currentPage.value = page;
  }
  
  function handlePageSizeChange(current, size) {
    pageSize.value = size;
  }
  
  </script>
  