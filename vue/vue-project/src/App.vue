<script setup>
import { RouterLink, RouterView } from 'vue-router'
import StudentHeader from './components/StudentHeader.vue';
import TutorHeader from './components/TutorHeader.vue';
import Footer from './components/Footer.vue';
import { ref, onMounted } from 'vue';

const isStudent = ref(true);

onMounted(() => {
  isStudent.value = localStorage.getItem('isStudent');
});
</script>

<template>
  <div>
    <StudentHeader v-if="isStudent" />
    <TutorHeader v-else />
    <!-- <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" /> -->

    <div class="wrapper">
      <!-- <HelloWorld msg="You did it!" /> -->
      <!-- <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
      </nav> -->
    </div>

    <RouterView />
    <Footer />
  </div>
</template>

<style scoped></style>
