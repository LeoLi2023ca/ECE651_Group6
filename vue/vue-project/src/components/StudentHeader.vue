<template>
  <a-layout-header>
    <div :style="{ lineHeight: '64px', display: 'flex', justifyContent: 'flex-end' }">
      <a-menu v-model:selectedKeys="selectedKeys" theme="dark" mode="horizontal"
        :style="{ lineHeight: '64px', display: 'flex' }">
        <a-menu-item key="1" class="custom-separator">
          <router-link to="/home-loginned">Home</router-link>
        </a-menu-item>
        <a-menu-item key="2" class="custom-separator">
          <router-link to="/post/my-post">Post</router-link>
        </a-menu-item>
        <a-menu-item key="3" class="custom-separator">
          <router-link to="/tutor-list">Tutors</router-link>
        </a-menu-item>
        <a-menu-item key="4" class="custom-separator">
          <router-link to="/student-matching">Matching</router-link>
        </a-menu-item>
      </a-menu>
      <a-avatar shape="square" :size="64">
        <template #icon>
          <a-dropdown>
            <a class="ant-dropdown-link" @click.prevent>
              <UserOutlined />
            </a>
            <template #overlay>
              <a-menu v-if="role == '1'">
                <a-menu-item>
                  <router-link to="/student/my-profile">Profile</router-link>
                </a-menu-item>
                <a-menu-item>
                  <router-link to="/student/settings">Settings</router-link>
                </a-menu-item>
                <a-menu-item>
                  <a @click="signOut()">Sign Out</a>
                </a-menu-item>
              </a-menu>
            </template>
          </a-dropdown>
        </template>
      </a-avatar>
    </div>
  </a-layout-header>
</template>

<script setup>
import { ref, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { UserOutlined } from '@ant-design/icons-vue';
import { useStore } from 'vuex';

const store = useStore();
const route = useRoute();
const router = useRouter();

const selectedKeys = ref(['1']);
const role = sessionStorage.getItem('role')
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
      break;
    case '/student-matching':
      selectedKeys.value = ['4'];
      break;
    default:
      selectedKeys.value = ['0'];
      break;
  }
}, { immediate: true });

function signOut() {
  store.dispatch("signOut");
  router.push({ name: 'login' });

}
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
.custom-separator {
  margin-right: 24px; /* Adjust as needed */
}
</style>