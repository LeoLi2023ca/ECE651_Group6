<template>
  <div>
    <StudentHome v-if="role === '1'" />
    <TutorHome v-else />
  </div>
</template>

<script setup>
import { inject } from 'vue';
import StudentHome from './StudentHomeView.vue';
import TutorHome from './TutorHomeView.vue';

const role = inject('role');
</script>
