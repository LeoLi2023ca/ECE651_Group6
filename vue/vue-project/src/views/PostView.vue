<template>
  <a-layout>
    <a-layout-sider width="200" style="background: #fff">
      <a-menu v-model:selectedKeys="selectedKeys" mode="inline"
        :style="{ height: '100%', borderRight: 0, background: '#fff' }">
        <a-menu-item key="1"><router-link to="/post/my-post">My Post</router-link></a-menu-item>
        <a-menu-item key="2"><router-link to="/post/create-post">Create Post</router-link></a-menu-item>
        <a-menu-item key="3"><router-link to="/post/post-history">Post History</router-link></a-menu-item>
      </a-menu>
    </a-layout-sider>
    <a-layout style="padding: 0px 30px 0px">
      <a-layout-content :style="{ background: '#fff', padding: '140px', minHeight: '80vh' }">
        <div>
          <router-view></router-view>
        </div>
      </a-layout-content>
    </a-layout>
  </a-layout>
</template>

<script setup>
import { ref, watch } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const selectedKeys = ref(['1']);
watch(() => route.path, (newPath) => {
  switch (newPath) {
    case '/post/my-post':
      selectedKeys.value = ['1'];
      break;
    case '/post/create-post':
      selectedKeys.value = ['2'];
      break;
    case '/post/post-history':
      selectedKeys.value = ['3'];
  }
}, { immediate: true });
</script>

<style scoped>
.site-layout-background {
  background: #fff;
}

.center-flex {
  margin-left: auto;
  margin-right: auto;
  display: block;
}
</style>