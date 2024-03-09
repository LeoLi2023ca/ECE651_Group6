<template>
  <a-layout-header>
    <div class="logo" />
    <a-menu v-model:selectedKeys="selectedKeys" theme="dark" mode="horizontal" :style="{ lineHeight: '64px' }">
      <a-menu-item key="1">
        <router-link to="/">Home</router-link>
      </a-menu-item>
      <a-menu-item key="2">
        <router-link to="/post/my-post">Post</router-link>
      </a-menu-item>
      <a-menu-item key="3">
        <router-link to="/tutor-list">Tutors</router-link>
      </a-menu-item>
    </a-menu>
  </a-layout-header>
</template>

<script setup>
import { ref, watch } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const selectedKeys = ref(['1']);
watch(() => route.path, (newPath) => {
  switch (newPath) {
    case '/':
      selectedKeys.value = ['1'];
      break;
    case '/post/my-post':
      selectedKeys.value = ['2'];
      break;
    case '/post/create-post':
      selectedKeys.value = ['2'];
      break;
    case '/post/post-history':
      selectedKeys.value = ['2'];
      break;
    case '/tutor-list':
      selectedKeys.value = ['3'];
  }
}, { immediate: true });
</script>

<style scoped>
.site-layout-content {
  min-height: 280px;
  padding: 24px;
  background: #fff;
}

#components-layout-demo-top .logo {
  float: left;
  width: 120px;
  height: 31px;
  margin: 16px 24px 16px 0;
  background: rgba(255, 255, 255, 0.3);
}

.ant-row-rtl #components-layout-demo-top .logo {
  float: right;
  margin: 16px 0 16px 24px;
}

[data-theme='dark'] .site-layout-content {
  background: #141414;
}
</style>