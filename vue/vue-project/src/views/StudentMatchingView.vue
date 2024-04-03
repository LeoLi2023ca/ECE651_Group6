<template>
    <a-layout>
        <TutorDetail ref="tutor_detail" />
        <div class="section">
        <h2 class="title">Matched Tutors</h2>
        <a-row :gutter="16">
            <a-col v-for="(item, index) in matchedData" :key="index" :span="8">
            <a-card :title="item.nickname" :style="{ margin: '10px' }" @click="showProfile(item.username)">
                <p>{{ "Subjects: "+item.subject_name }}</p>
                <p>{{ "Education: "+item.edu_level }}</p>
                <p>{{ "Expected Salary: "+item.salary }}</p>
            </a-card>
            </a-col>
        </a-row>
        </div>
        
        <div class="section">
        <h2 class="title">Asked For Matching</h2>
        <a-row :gutter="16">
            <a-col v-for="(item, index) in askedPaginatedData" :key="index" :span="8">
            <a-card :title="item.nickname" :style="{ margin: '10px' }" @click="showProfile(item.username)">
                <p>{{ "Subjects: "+item.subject_name }}</p>
                <p>{{ "Education: "+item.edu_level }}</p>
                <p>{{ "Expected Salary: "+item.salary }}</p>
            </a-card>
            </a-col>
        </a-row>
        <a-pagination :total="askedForMatching.length" :pageSize="pageSize" @change="handlePageChange"
            @showSizeChange="handlePageSizeChange" />
        </div>
    </a-layout>
  </template>
  
  <script setup>
  import { computed, ref, onMounted } from 'vue';
  import TutorDetail from '@/components/TutorDetail.vue';
  
  import axios from 'axios';
  
  const pageSize = ref(9);
  const currentPage = ref(1);
  const tutor_detail = ref(null);
  const paginatedData = ref([]);
  const askedPaginatedData = ref([]);
  const askedForMatching = ref([]);
  const Matched = ref([]);
  const user_info = JSON.parse(sessionStorage.getItem('user_info'));
  
  onMounted(async () => {
    await loadData();
    const start = (currentPage.value - 1) * pageSize.value;
    const end = start + pageSize.value;
    paginatedData.value = Matched.value.slice(start, end);
    askedPaginatedData.value = askedForMatching.value.slice(start, end);
  });
  
  async function loadData() {
    const params = {
      student_username: user_info.username,
    };
    const config = {
      method: 'get',
      url: 'http://127.0.0.1:5000/getStudentsAskedTutor',
      params: params
    };
    await axios.request(config)
      .then((response) => {
        for(let i = 0; i < response.data.list.length; i++) {
          askedForMatching.value.push({
            username: response.data.list[i].username,
            nickname: response.data.list[i].nickname,
            edu_level: response.data.list[i].edu_level,
            subject_name: response.data.list[i].subjects,
            msg: response.data.list[i].msg,
            salary: response.data.list[i].salary,
            timezone: response.data.list[i].timezone,
            available_time: response.data.list[i].available_time,
          })
        }
      })
      .catch((error) => {
        console.error(error);
      });
    
    const config2 = {
      method: 'get',
      url: 'http://127.0.0.1:5000/getStudentMatchedTutor',
      params: params
    };
    await axios.request(config2)
      .then((response) => {
        for(let i = 0; i < response.data.list.length; i++) {
          Matched.value.push({
            username: response.data.list[i].username,
            nickname: response.data.list[i].nickname,
            edu_level: response.data.list[i].edu_level,
            subject_name: response.data.list[i].subjects,
            msg: response.data.list[i].msg,
            salary: response.data.list[i].salary,
            timezone: response.data.list[i].timezone,
            available_time: response.data.list[i].available_time,
          })
        }
      })
      .catch((error) => {
        console.error(error);
      });
  }
  
  function showProfile(username) {
    tutor_detail.value.showModal(username);
  }
  
  function handlePageChange(page) {
    currentPage.value = page;
  }
  
  function handlePageSizeChange(current, size) {
    pageSize.value = size;
  }
  
  </script>
  