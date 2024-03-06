<template>
  <a-layout>
    <a-layout-sider width="200" style="background: #fff">
      <a-menu v-model:selectedKeys="selectedKeys" mode="inline"
        :style="{ height: '100%', borderRight: 0, background: '#fff' }">
        <template #title>
          <span>
            <user-outlined />
            subnav 1
          </span>
        </template>
        <a-menu-item key="1">Posts</a-menu-item>
        <a-menu-item key="2">Create Post</a-menu-item>
        <a-menu-item key="3">History</a-menu-item>
      </a-menu>
    </a-layout-sider>
    <a-layout style="padding: 0 5px 0px">
      <a-layout-content :style="{ background: '#fff', padding: '24px', margin: 0, minHeight: '80vh' }">
        Content
      </a-layout-content>
    </a-layout>
  </a-layout>
</template>

<script setup>
import { ref } from 'vue';
const selectedKeys = ref(['1']);
</script>

<style scoped>

.site-layout-background {
  background: #fff;
}
</style>