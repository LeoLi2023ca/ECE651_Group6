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
        <input type="checkbox" name="subjects" value="chinese" v-model="tutorInfo.subjects"> <span class="checkbox-text">Chinese</span><br>
        <input type="checkbox" name="subjects" value="english" v-model="tutorInfo.subjects"> <span class="checkbox-text">English</span><br>
        <input type="checkbox" name="subjects" value="math" v-model="tutorInfo.subjects"> <span class="checkbox-text">Math</span><br>
        <input type="checkbox" name="subjects" value="chemistry" v-model="tutorInfo.subjects"> <span class="checkbox-text">Chemistry</span><br>
        <input type="checkbox" name="subjects" value="physics" v-model="tutorInfo.subjects"> <span class="checkbox-text">Physics</span><br>
        <input type="checkbox" name="subjects" value="biology" v-model="tutorInfo.subjects"> <span class="checkbox-text">Biology</span><br>
        <input type="checkbox" name="subjects" value="business_management" v-model="tutorInfo.subjects"> <span class="checkbox-text">Business management</span><br>
        <input type="checkbox" name="subjects" value="geography" v-model="tutorInfo.subjects"> <span class="checkbox-text">Geography</span><br>
        <input type="checkbox" name="subjects" value="history" v-model="tutorInfo.subjects"> <span class="checkbox-text">History</span><br>
      </div>
      <div class="form-group">
        <label for="tuition">Expected tuition per hour:</label>
        <input type="number" id="tuition" v-model="tutorInfo.tuition" required>
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
