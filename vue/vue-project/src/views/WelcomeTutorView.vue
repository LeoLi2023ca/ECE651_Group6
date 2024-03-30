<template>
    <div class="title margin-20">
      <h1>Welcome to TutorEase!</h1>
      <h4>Before matching with students, please spend some time to fill in some of your information. This will help us to recommend students who are suitable for you.</h4>
      <h5>You can make changes to these afterwards by going to settings -> my information</h5>
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
          <input type="checkbox" name="subjects" value="chinese" v-model="tutorInfo.subjects"> Chinese<br>
          <input type="checkbox" name="subjects" value="english" v-model="tutorInfo.subjects"> English<br>
          <input type="checkbox" name="subjects" value="math" v-model="tutorInfo.subjects"> Math<br>
          <input type="checkbox" name="subjects" value="chemistry" v-model="tutorInfo.subjects"> Chemistry<br>
          <input type="checkbox" name="subjects" value="physics" v-model="tutorInfo.subjects"> Physics<br>
          <input type="checkbox" name="subjects" value="biology" v-model="tutorInfo.subjects"> Biology<br>
          <input type="checkbox" name="subjects" value="business_management" v-model="tutorInfo.subjects"> Business management<br>
          <input type="checkbox" name="subjects" value="geography" v-model="tutorInfo.subjects"> Geography<br>
          <input type="checkbox" name="subjects" value="history" v-model="tutorInfo.subjects"> History<br>
        </div>
        <div class="form-group">
          <label for="tuition">Expected tuition per hour:</label>
          <input type="number" id="tuition" v-model="tutorInfo.tuition" required>
        </div>
        <div class="form-group">
          <label for="bio">Tell us more about yourself:</label>
          <textarea id="bio" v-model="tutorInfo.bio"></textarea>
        </div>
        <button type="submit">Done</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        tutorInfo: {
          education_level: '',
          school_name: '',
          subjects: [],
          tuition: '',
          bio: ''
        },
      };
    },
    methods: {
      submitForm() {
        console.log('Submitting:', this.tutorInfo);
      }
    }
  }
  </script>
  
  <style scoped>
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
  </style>
  