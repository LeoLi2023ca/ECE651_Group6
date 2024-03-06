<template>
  <a-layout-header>
    <div class="logo" />
    <a-menu v-model:selectedKeys="selectedKeys" theme="dark" mode="horizontal" :style="{ lineHeight: '64px' }">
      <a-menu-item key="1">      
        <router-link to="/">Home</router-link>
      </a-menu-item>
      <a-menu-item key="2">
        <router-link to="/post-list">Posts</router-link>
      </a-menu-item>
    </a-menu>
  </a-layout-header>
</template>

<script>
import { ref } from 'vue';
const selectedKeys = ref('1');

export default {
  name: 'Header',
};
</script>

<style></style>