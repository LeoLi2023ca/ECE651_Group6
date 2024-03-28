<template>
  <a-layout>
    <div :style="{ display: 'flex', margin: '10px' }"><a-input placeholder="Search" v-model:value="searchText"
        style="margin-right: 10px;" />
      <a-button style="margin-right: 10px;" type="primary" @click="search">Search</a-button>
      <a-button @click="reset">Reset</a-button>
    </div>
    <TutorDetail ref="tutor_detail" />
    <a-row :gutter="16">
      <a-col v-for="(item, index) in paginatedData" :key="index" :span="8">
        <a-card :title="item.nickname" :style="{ margin: '10px' }" @click="showProfile(item.username)">
          <p>{{ item.subject_name }}</p>
          <p>{{ item.edu_level }}</p>
          <p>{{ item.salary }}</p>
        </a-card>
      </a-col>
    </a-row>
    <a-pagination :total="data.length" :pageSize="pageSize" @change="handlePageChange"
      @showSizeChange="handlePageSizeChange" />
  </a-layout>
</template>

<script setup>
import { computed, ref, onMounted } from 'vue';
import TutorDetail from '@/components/TutorDetail.vue';

import axios from 'axios';

const pageSize = ref(9);
const currentPage = ref(1);
const data = ref([]);
const searchText = ref('');
const searched = ref(false);
const filteredData = ref([]);
const tutor_detail = ref(null);
const paginatedData = ref([]);
onMounted(async () => {
  await loadData();
  const start = (currentPage.value - 1) * pageSize.value;
  const end = start + pageSize.value;
  if (searched.value) {
    paginatedData.value = filteredData.value.slice(start, end);

  } else {
    paginatedData.value = data.value.slice(start, end);

  }
});

function search() {
  const lowerSearchText = searchText.value.toLowerCase();
  filteredData.value = data.value.filter((item) => {
    return Object.keys(item).some((key) => {
      if (key === 'username') {
        return false;
      }
      return String(item[key]).toLowerCase().includes(lowerSearchText);
    });
  });
  searched.value = true;
  const start = (currentPage.value - 1) * pageSize.value;
  const end = start + pageSize.value;
  if (searched.value) {
    paginatedData.value = filteredData.value.slice(start, end);
  } else {
    paginatedData.value = data.value.slice(start, end);
  }
}

async function loadData() {
  await axios.get('http://127.0.0.1:5000/getAllTutor')
    .then(response => {
      console.log(response.data.list);
      for (let i = 0; i < response.data.list.length; i++) {
        data.value.push({
          username: response.data.list[i].username,
          nickname: response.data.list[i].nickname,
          edu_level: response.data.list[i].edu_level,
          subject_name: response.data.list[i].subject_name,
          msg: response.data.list[i].msg,
          salary: response.data.list[i].salary,
          timezone: response.data.list[i].timezone,
          available_time: response.data.list[i].available_time,
        })
      }
    })
    .catch(error => {
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

function reset() {
  searched.value = false;
  searchText.value = '';
  const start = (currentPage.value - 1) * pageSize.value;
  const end = start + pageSize.value;
  paginatedData.value = data.value.slice(start, end);
  currentPage.value = 1;
}
</script>
