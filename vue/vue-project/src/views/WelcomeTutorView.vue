<template>
  <div class="content-wrapper">
    <div class="title margin-20">
      <h1>Welcome to TutorEase!</h1>
      <h4>Before matching with students, please spend some time to fill in some of your information.</h4>
      <h4>This will help us to recommend students who are suitable for you.</h4>
     <!-- <h5>You can make changes to these afterwards by going to settings -> my information</h5> -->
    </div>
  </div>
  <div class="form-container">
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label for="education_level">Education level:</label>
        <select name="education_level" v-model="tutorInfo.education_level">
          <option value="highschool">Highschool</option>
          <option value="bachelor">Bachelor</option>
          <option value="master">Master</option>
          <option value="phd">Phd</option>
        </select>
      </div>
      <div class="form-group">
        <label for="school_name">School name:</label>
        <input type="text" id="school_name" v-model="tutorInfo.school_name" required>
      </div>
      <div class="form-group">
        <label for="subjects">Subjects that you are good at:</label>
        <input type="checkbox" name="subjects" value="Chinese" v-model="tutorInfo.subjects"> <span class="checkbox-text">Chinese</span><br>
        <input type="checkbox" name="subjects" value="English" v-model="tutorInfo.subjects"> <span class="checkbox-text">English</span><br>
        <input type="checkbox" name="subjects" value="Math" v-model="tutorInfo.subjects"> <span class="checkbox-text">Math</span><br>
        <input type="checkbox" name="subjects" value="Chemistry" v-model="tutorInfo.subjects"> <span class="checkbox-text">Chemistry</span><br>
        <input type="checkbox" name="subjects" value="Physics" v-model="tutorInfo.subjects"> <span class="checkbox-text">Physics</span><br>
        <input type="checkbox" name="subjects" value="Biology" v-model="tutorInfo.subjects"> <span class="checkbox-text">Biology</span><br>
        <input type="checkbox" name="subjects" value="Business_management" v-model="tutorInfo.subjects"> <span class="checkbox-text">Business management</span><br>
        <input type="checkbox" name="subjects" value="Geography" v-model="tutorInfo.subjects"> <span class="checkbox-text">Geography</span><br>
        <input type="checkbox" name="subjects" value="History" v-model="tutorInfo.subjects"> <span class="checkbox-text">History</span><br>
      </div>
      <div class="form-group">
        <label for="tuition-min">Minimum expected tuition per hour:</label>
        <input type="number" id="tuition-min" v-model="tutorInfo.tuition.min" required placeholder="Min" style="margin-right: 10px;">

        <label for="tuition-max">Maximum expected tuition per hour:</label>
        <input type="number" id="tuition-max" v-model="tutorInfo.tuition.max" required placeholder="Max" min="tutorInfo.tuition.min">
      </div>
      <div class="form-group">
        <label for="timezone">Timezone:</label>
        <select id="timezone" v-model="tutorInfo.timezone">
          <option v-for="tz in timezones" :key="tz.value" :value="tz.value">{{ tz.label }}</option>
        </select>
      </div>
      <div class="form-group">
        <label for="bio">Tell us more about yourself:</label>
        <textarea id="bio" v-model="tutorInfo.bio"></textarea>
      </div>
      <div class="center-button">
        <button type="submit">Done</button>
      </div>
    </form>
  </div>
</template>

<script>

import router from '@/router';
import axios from 'axios';

export const timezones = Array.from({ length: 25 }, (_, i) => {
  const value = i - 12;
  const sign = value >= 0 ? '+' : '-';
  return { label: `UTC ${sign}${Math.abs(value).toString().padStart(2, '0')}:00`, value: `${sign}${Math.abs(value).toString().padStart(2, '0')}:00` };
});
const user_info = JSON.parse(sessionStorage.getItem('user_info'));
export default {
  data() {
    return {
      tutorInfo: {
        education_level: '',
        school_name: '',
        subjects: [],
        tuition: {
          min: 0,
          max: 0
        },
        timezone: '',
        bio: ''
      },
      timezones: timezones,
      user_info: user_info
    };
  },
  methods: {
    submitForm() {
      console.log('Submitting:', this.tutorInfo);
      var data = new FormData();
      // console.log(this.tutorInfo.username);
      console.log(user_info.username);
      data.append('username', user_info.username); // Assuming username is part of tutorInfo
      data.append('nickname', user_info.username); // Assuming nickname is part of tutorInfo
      data.append('email', user_info.email); // Assuming email is part of tutorInfo
      data.append('edu_level', this.tutorInfo.education_level);
      data.append('school_name', this.tutorInfo.school_name);
      data.append('timezone', this.tutorInfo.timezone);
      // Assuming available_time and message are part of tutorInfo
      data.append('available_time', user_info.available_time || '');
      data.append('message', this.tutorInfo.bio || '');
      // console.log(formState.subjects);
      data.append('subjects', this.tutorInfo.subjects);
      data.append('salary', `${this.tutorInfo.tuition.min}-${this.tutorInfo.tuition.max}`)


      var config = {
          method: 'post',
          url: 'http://127.0.0.1:5000/updateTutorProfile',
          data: data
      };

      axios(config)
          .then(function (response) {
              sessionStorage.setItem('user_info', JSON.stringify(response.data.user_info));
              console.log(response);
              router.push({ name: 'home' });
          })
          .catch(function (error) {
              console.log(error);
          });
    }
  }
}
</script>

<!-- <style scoped>
.title{
  text-align:center
}

.margin-20{
  margin: 20px;
}

.form-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
}

.form-group {
  margin-bottom: 1em;
}

label {
  display: block;
  margin-bottom: .5em;
}

input[type="text"],
input[type="email"],
textarea {
  width: 100%;
  padding: 8px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button[type="submit"] {
  background-color: rgb(25, 29, 87);
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button[type="submit"]:hover {
  background-color: rgb(46, 54, 158);
}
</style> -->

<style scoped>
.content-wrapper {
  max-width: 630px;
  margin: 0 auto;
  padding: 0 20px;
}

.title {
  margin-bottom: 20px;
}

.form-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 30px;
  border: 2px solid #e0e0e0;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  background: linear-gradient(to right, #ffffff, #f2f2f2);
}

.form-group {
  margin-bottom: 20px;
}

h1 {
  text-align: center;
  font-size: 28px;
  font-weight: bold;
  margin-bottom: 10px;
  color: rgb(33, 150, 243);
}

h4 {
  max-width: 600px;
  color: rgb(121, 125, 129);
  text-align: left;
}

label {
  display: block;
  margin-bottom: .5em;
  color: rgb(33, 150, 243);
  font-weight: lighter;
  font-weight: bold;
}

input[type="text"],
input[type="number"],
textarea,
select {
  width: 100%;
  padding: 8px;
  margin-bottom: 10px;
  border: 1px solid #e0e0e0;
  border-radius: 4px;
  background: linear-gradient(to right, #ffffff, #f2f2f2);
}

input[type="checkbox"] {
  margin-right: 5px;
  border: 1px solid #e0e0e0;
  border-radius: 4px;
  width: 12px;
  height: 12px;
  vertical-align: middle;
  color: rgb(121, 125, 129);
}

button[type="submit"] {
  background-color: rgb(63, 195, 128);
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.center-button {
  text-align: center; 
}

/* .checkbox-text {
  color: rgb(121, 125, 129);
} */
</style>
