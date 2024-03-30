<template>
    <div class="title margin-20">
      <h1>Welcome to TutorEase!</h1>
      <h4>Before matching with students, please spend some time to fill in some of your information. This will help us to recommend students who are suitable for you.</h4>
    </div>
    <div class="form-container">
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label for="education_level">Education level:</label>
          <select name="country">
            <option value="usa">Highschool</option>
            <option value="usa">Bachelor</option>
            <option value="canada">Master</option>
            <option value="mexico">Phd</option>
          </select>
        </div>
        <div class="form-group">
          <label for="school_name">School name:</label>
          <input type="text" id="school_name" v-model="userInfo.email" required>
        </div>
        <div class="form-group">
          <label for="subjects">Subjects that you are good at:</label>
          <input type="checkbox" name="subjects" value="chinese"> Chinese<br>
          <input type="checkbox" name="subjects" value="english"> English<br>
          <input type="checkbox" name="subjects" value="math"> Math<br>
          <input type="checkbox" name="subjects" value="chemistry"> Chemistry<br>
          <input type="checkbox" name="subjects" value="physics"> Physics<br>
          <input type="checkbox" name="subjects" value="biology"> Biology<br>
          <input type="checkbox" name="subjects" value="business_management"> Business management<br>
          <input type="checkbox" name="subjects" value="geography"> Geography<br>
          <input type="checkbox" name="subjects" value="history"> History<br>
        </div>
        <div class="form-group">
          <label for="bio">Tell us more about yourself:</label>
          <textarea id="bio" v-model="userInfo.bio"></textarea>
        </div>
        <button type="submit">Done</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        userInfo: {
          name: '',
          email: '',
          bio: '',
        },
      };
    },
    methods: {
      submitForm() {
        console.log('Submitting:', this.userInfo);
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
  