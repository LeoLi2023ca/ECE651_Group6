<template>
  <div style="margin-bottom: 16px">
    <a-button type="primary" :disabled="!hasSelected" :loading="state.loading" @click="deletePosts">
      Delete
    </a-button>
    <span style="margin-left: 8px">
      <template v-if="hasSelected">
        {{ `Selected ${state.selectedRowKeys.length} items` }}
      </template>
    </span>
  </div>
  <a-table :columns="columns" :data-source="listData"
    :row-selection="{ selectedRowKeys: state.selectedRowKeys, onChange: onSelectChange }"
    :rowKey="record => record.post_id">
    <template #bodyCell="{ column, text, record }">
      <template v-if="column.key === 'operation'">
        <a-button @click="repost(record.post_id)">Repost</a-button>
      </template>
    </template>
  </a-table>
</template>
<script setup>
import { onMounted, ref, computed, reactive } from 'vue';
import axios from 'axios';

const state = reactive({
  selectedRowKeys: [],
  // Check here to configure the default column
  loading: false,
});
const hasSelected = computed(() => state.selectedRowKeys.length > 0);
const deletePosts = () => {
  state.loading = true;
  var data = new FormData();
  console.log(state.selectedRowKeys)
  data.append('post_id_list', JSON.stringify(state.selectedRowKeys));

  var config = {
    method: 'post',
    url: 'http://127.0.0.1:5000/delete_posts',
    data: data
  };

  axios(config)
    .then(function (response) {
      console.log(response)
    })
    .catch(function (error) {
      console.log(error);
    });
  setTimeout(() => {
    state.loading = false;
    state.selectedRowKeys = [];
    listData.value = []
    getPostList();
  }, 1000);
};
const onSelectChange = selectedRowKeys => {
  console.log('selectedRowKeys changed: ', selectedRowKeys);
  state.selectedRowKeys = selectedRowKeys;
};
const columns = [
  {
    title: 'title',
    // width: 50,
    dataIndex: 'title',
    key: 'title',
    fixed: 'left',
  },
  {
    title: 'date',
    // width: 50,
    dataIndex: 'post_date',
    key: 'date',
    fixed: 'left',
  },
  {
    title: 'subject',
    // width: 50,
    dataIndex: 'subject_name',
    key: 'subject',
    fixed: 'left',
  },
  {
    title: 'Action',
    key: 'operation',
    fixed: 'right',
    // width: 100,
  },
];
const listData = ref([]);
onMounted(() => {
  getPostList();
})
function getPostList() {
  const user_info = JSON.parse(sessionStorage.getItem('user_info'));
  const params = {
    username: user_info.username
  };
  axios.get('http://127.0.0.1:5000/getAllClosedPostsByUsername', { params })
    .then(response => {
      for (let i = 0; i < response.data.list.length; i++) {
        listData.value.push({
          post_id: response.data.list[i].post_id,
          title: response.data.list[i].title,
          post_date: response.data.list[i].post_date,
          msg: response.data.list[i].msg,
          salary: response.data.list[i].salary,
          subject_name: response.data.list[i].subject_name,
          available_time: response.data.list[i].available_time,
          status: response.data.list[i].status,
        })
      }
      console.log(response.data.list);
    })
    .catch(error => {
      console.error(error);
    });
}
function repost(post_id) {
  var data = new FormData();
  data.append('post_id', post_id);

  var config = {
    method: 'post',
    url: 'http://127.0.0.1:5000/activate_post',
    data: data
  };

  axios(config)
    .then(function (response) {
      console.log(response)
    })
    .catch(function (error) {
      console.log(error);
    });
  setTimeout(() => {
    state.loading = false;
    state.selectedRowKeys = [];
    listData.value = []
    getPostList();
  }, 1000);
}
const pagination = {
  onChange: page => {
    console.log(page);
  },
  pageSize: 4,
};
</script>