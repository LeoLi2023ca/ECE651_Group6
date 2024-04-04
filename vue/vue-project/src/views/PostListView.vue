<template>
    <a-layout style="padding: 30px 30px 0px">
        <div :style="{ display: 'flex', marginBottom: '20px' }"><a-input placeholder="Search" v-model:value="searchText"
                style="margin-right: 10px;" />
            <a-button style="margin-right: 10px;" type="primary" @click="search">Search</a-button>
            <a-button @click="reset">Reset</a-button>
        </div>
        <a-table :columns="columns" :data-source="searched ? filteredData : listData" :pagination="{ pageSize: 10 }"
            :rowKey="record => record.post_id"> <template #bodyCell="{ column, text, record }">
                <template v-if="column.key === 'operation'">
                    <a-button @click="showPost(record.post_id)" style="margin-right: 10px;">Details</a-button>
                    <a-button @click="contact(record.post_id)" type="primary" ghost>Contact</a-button>
                </template>
            </template>
        </a-table>
        <PostDetail ref="post_detail" />
    </a-layout>
    <a-modal v-model:open="chatOpen" title="Chat">
        <ChatPage v-if="chatOpen" :receiver="receiverUsername" @close="chatOpen = false" />
    </a-modal>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';
import PostDetail from '@/components/PostDetail.vue';
import ChatPage from '@/components/ChatPage.vue';
const post_detail = ref(null);
const searchText = ref('');
const listData = ref([]);
const searched = ref(false);
const filteredData = ref([]);
const chatOpen = ref(false);
const receiverUsername = ref('');

function search() {
    const lowerSearchText = searchText.value.toLowerCase();
    console.log(searchText.value)
    filteredData.value = listData.value.filter((item) => {
        return Object.keys(item).some((key) => {
            if (key === 'username' || key === 'status' || key === 'post_id' || key === 'post_date') {
                return false;
            }
            return String(item[key]).toLowerCase().includes(lowerSearchText);
        });
    });
    searched.value = true;
}
const columns = [
    {
        title: 'title',
        dataIndex: 'title',
        key: 'title',
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
        title: 'salary',
        dataIndex: 'salary',
        key: 'salary',
        sorter: true,
        fixed: 'left',
        width: 150,
    },
    {
        title: 'Action',
        key: 'operation',
        fixed: 'right',
        width: 200,
    },
];
onMounted(() => {
    getAllPostList();
});
function getAllPostList() {
    axios.get('http://127.0.0.1:5000/getAllOpeningPost')
        .then(response => {
            console.log(response.data.list);
            for (let i = 0; i < response.data.list.length; i++) {
                listData.value.push({
                    username: response.data.list[i].username,
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
        })
        .catch(error => {
            console.error(error);
        });
}

function reset() {
    searched.value = false;
    searchText.value = '';
}

function showPost(post_id) {
    post_detail.value.showModal(post_id);
}

function contact(post_id) {
    axios.get('http://127.0.0.1:5000/GetUserNameByPostID', {
        params: {
            post_id: post_id
        }
    })
        .then(response => {
            console.log(response.data.username);
            receiverUsername.value = response.data.username;
        })
        .catch(error => {
            console.error(error);
        });
    chatOpen.value = true;
}

</script>