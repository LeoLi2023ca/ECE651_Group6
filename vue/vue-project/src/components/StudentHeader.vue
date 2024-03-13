<template>
  <a-layout-header>
    <a-menu v-model:selectedKeys="selectedKeys" theme="dark" mode="horizontal"
      :style="{ lineHeight: '64px', display: 'flex', justifyContent: 'flex-end' }">
      <a-menu-item key="1">
        <router-link to="/">Home</router-link>
      </a-menu-item>
      <a-menu-item key="2">
        <router-link to="/post/my-post">Post</router-link>
      </a-menu-item>
      <a-menu-item key="3">
        <router-link to="/tutor-list">Tutors</router-link>
      </a-menu-item>
      <a-menu-item>
        <a-dropdown>
          <a class="ant-dropdown-link" @click.prevent>
            Me
            <DownOutlined />
          </a>
          <template #overlay>
            <a-menu v-if="token=='1'">
              <a-menu-item>
                <a href="javascript:;">Profile</a>
              </a-menu-item>
              <a-menu-item>
                <a href="javascript:;">Setting</a>
              </a-menu-item>
              <a-menu-item>
                <a href="javascript:;">Sign Out</a>
              </a-menu-item>
            </a-menu>
          </template>
        </a-dropdown>
      </a-menu-item>
    </a-menu>
  </a-layout-header>
</template>

<script setup>
import { ref, watch } from 'vue';
import { useRoute } from 'vue-router';
import { DownOutlined } from '@ant-design/icons-vue';

const route = useRoute();
const selectedKeys = ref(['1']);
const token = sessionStorage.getItem('token');
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

[data-theme='dark'] .site-layout-content {
  background: #141414;
}
</style>