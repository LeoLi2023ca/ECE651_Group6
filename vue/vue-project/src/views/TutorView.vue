<template>
    <div class="teacher-profile">
        <div class="basic-info">
            <img :src="teacher" alt="Teacher's Avatar" class="avatar" />
            <h2>{{ teacher }}</h2>
            <p>{{ teacher }}</p>
        </div>
        <div class="video-introduction">
            <video controls>
                <source :src="teacher" type="video/mp4">
                Your browser does not support the video tag.
            </video>
        </div>
        <button @click="contactTeacher">Contact</button>
    </div>
</template>
  
<script>
import { useRoute } from 'vue-router';


export default {
    setup() {
        const route = useRoute();
        const teacherId = route.params.id;
        return { teacherId };
    },
    props: ['teacher'],
    methods: {
        contactTeacher() {
            alert('requested');
        }
    }
}
</script>
  
<style>
.teacher-profile {
    max-width: 800px;
    margin: auto;
    text-align: center;
}

.basic-info .avatar {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    margin: 20px 0;
}

.video-introduction video {
    width: 100%;
    max-width: 800px;
    margin: 20px 0;
}
</style>
  