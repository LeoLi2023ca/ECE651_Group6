<template>
  <div class="messages-view">
    <div class="header">
      <input v-if="isManaging" type="checkbox" @change="toggleSelectAll" :checked="isAllSelected">
      <button v-if="!isManaging" @click="addMessage">新增</button>
      <button v-if="!isManaging" @click="enterManageMode">管理</button>
      <button v-if="isManaging" @click="deleteSelectedMessages">删除</button>
      <button v-if="isManaging" @click="cancelManageMode">取消</button>
    </div>
    <div class="messages-list">
      <div v-for="(message, index) in messages" :key="index" class="message-card">
        <input v-if="isManaging" type="checkbox" v-model="selectedMessages[index]">
        <div>{{ message.title }}</div>
        <div>{{ message.content }}</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

// 初始化messages数组，包含一些示例信息
const messages = ref([
  { title: '信息1', content: '这是信息1的内容。' },
  { title: '信息2', content: '这是信息2的内容，包含更多详细信息。' },
  { title: '信息3', content: '信息3的内容，简短摘要。' }
]);

const isManaging = ref(false);
const selectedMessages = ref({});

const addMessage = () => {
  // 实现新增信息的逻辑
  // 例如：messages.value.push({ title: '新信息', content: '新信息的内容' });
};

const enterManageMode = () => {
  isManaging.value = true;
};

const cancelManageMode = () => {
  isManaging.value = false;
  selectedMessages.value = {};
};

const deleteSelectedMessages = () => {
  // 实现删除选中信息的逻辑
  // 只保留未被选中的消息
  messages.value = messages.value.filter((_, index) => !selectedMessages.value[index]);
  isManaging.value = false;
};

const toggleSelectAll = (event) => {
  const isSelected = event.target.checked;
  messages.value.forEach((_, index) => {
    selectedMessages.value[index] = isSelected;
  });
};

const isAllSelected = computed(() => {
  return messages.value.length > 0 && Object.keys(selectedMessages.value).length === messages.value.length && Object.values(selectedMessages.value).every(value => value);
});
</script>
