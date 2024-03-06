<template>
  <table>
    <thead>
      <tr>
        <th>Name</th>
        <th>Subject</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="teacher in teachers" :key="teacher.id" @click="navigateToTeacher(teacher.id)">
        <td>{{ teacher.name }}</td>
        <td>{{ teacher.subject }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

export default {
  setup() {
    const teachers = ref([
      { id: 1, name: 'Alice', subject: 'Mathematics' },
      { id: 2, name: 'Bob', subject: 'Physics' },
      { id: 3, name: 'Charlie', subject: 'Chemistry' },
    ]);
    const router = useRouter();

    const navigateToTeacher = (id) => {
      router.push('/tutor/${id}');
    };

    return { teachers, navigateToTeacher };
  },
};
</script>
