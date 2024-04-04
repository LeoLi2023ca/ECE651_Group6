<template>
  <StudentHome v-if="role === '1'" />
  <TutorHome v-else />
</template>

<script setup>
import { inject } from 'vue';
import StudentHome from './StudentHomeView.vue';
import TutorHome from './TutorHomeView.vue';
import $ from 'jquery';

const role = inject('role');
</script>

<style scoped>
  
</style>
