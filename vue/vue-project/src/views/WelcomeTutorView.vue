<template>
    <div>
      <div>Welcome to TutorEase!</div>
      <div>To start your journey, please spend some time to fill in some of your information. This will help us recommend students which is suitable for you.</div>
      <button>Let's get started</button>
      <button>Remind me later</button>
    </div>
    <div class="form-container">
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label for="name">Name:</label>
          <input type="text" id="name" v-model="userInfo.name" required>
        </div>
  
        <div class="form-group">
          <label for="email">Email:</label>
          <input type="email" id="email" v-model="userInfo.email" required>
        </div>
  
        <div class="form-group">
          <label for="bio">Short Bio:</label>
          <textarea id="bio" v-model="userInfo.bio"></textarea>
        </div>
  
        <button type="submit">Submit</button>
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
        // In a real app, you'd likely send this data to a server
        console.log('Submitting:', this.userInfo);
        // Optionally, clear the form or provide user feedback
      }
    }
  }
  </script>
  
  <style scoped>
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
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  button[type="submit"]:hover {
    background-color: #45a049;
  }
  </style>
  