<template>
  <a-list item-layout="vertical" size="large" :pagination="pagination" :data-source="listData">
    <template #renderItem="{ item }">
      <a-list-item key="item.post_id">
        <a-list-item-meta :description="item.post_date">
          <template #title>
            {{ item.title }}
          </template>
        </a-list-item-meta>
        {{ item.msg }}
      </a-list-item>
    </template>
  </a-list>
  <!-- <ul>
    <li v-for="item in listData" :key="item.post_id">
      <h3>{{ item.title }}</h3>
      <p>{{ item.msg }}</p>
      <p>{{ item.post_date }}</p>
    </li>
  </ul> -->
</template>

<script>
// import { onMounted } from 'vue';
import axios from 'axios';

export default {
  data() {
    return {
      listData: [],
      pagination: null,
    }
  },
  mounted() {
    var that = this;
    const user_info = JSON.parse(sessionStorage.getItem('user_info'));
    const params = {
      username: user_info.username
    };
    axios.get('http://localhost:5000/getAllOpeningPostsByUsername', { params })
      .then(response => {
        for (let i = 0; i < response.data.list.length; i++) {
          that.listData.push({
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
    this.pagination = {
      onChange: page => {
        console.log(page);
      },
      pageSize: 3,
    };
  }
}

// const listData = [];

// const user_info = JSON.parse(sessionStorage.getItem('user_info'));
// onMounted(async () => {
//   const params = {
//     username: user_info.username
//   };
//   await axios.get('http://localhost:5000/getAllOpeningPostsByUsername', { params })
//     .then(response => {
//       for (let i = 0; i < response.data.list.length; i++) {
//         listData.push({
//           post_id: response.data.list[i].post_id,
//           title: response.data.list[i].title,
//           post_date: response.data.list[i].post_date,
//           msg: response.data.list[i].msg,
//           salary: response.data.list[i].salary,
//           subject_name: response.data.list[i].subject_name,
//           available_time: response.data.list[i].available_time,
//           status: response.data.list[i].status,
//         })
//       }
//       // console.log(response.data.list);
//     })
//     .catch(error => {
//       console.error(error);
//     });

//   console.log('11111111111111')
//   console.log(listData)
// });
// listData.push({ post_id: 1, title: 'wocao', msg: 'wocaonima', subject: 'cnm' })
// listData.push({ post_id: 2, title: 'wocao', msg: 'wocaonima', subject: 'cnmb' })
// const pagination = {
//   onChange: page => {
//     console.log(page);
//   },
//   pageSize: 3,
// };
</script>
