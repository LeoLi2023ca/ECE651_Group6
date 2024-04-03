<script setup>
import { RouterLink, RouterView } from 'vue-router'
import StudentHeader from './components/StudentHeader.vue';
import TutorHeader from './components/TutorHeader.vue';
import Footer from './components/Footer.vue';
import { ref, computed } from 'vue';
import { useStore } from 'vuex';
const store = useStore();
const role = computed(() => store.getters.userRole);
import { provide } from 'vue';
provide('role', role);
</script>

<template>
  <a-layout class="layout">
    <div>
      <TutorHeader v-if="role == '2'" />
      <StudentHeader v-else-if="role == '1'" />
      <!-- <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" /> -->
      <br>
      <br>
      <a-layout-content style="padding: 0 50px">
        <div :style="{ minHeight: '80vh' }">
          <RouterView />
        </div>
      </a-layout-content>

      <Footer />
    </div>
  </a-layout>
</template>

<style scoped>
.layout {
  min-height: 100vh;
}

[data-theme='dark'] .site-layout-content {
  background: #141414;
}
</style>
