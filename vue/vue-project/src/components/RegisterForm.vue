<template>
  <a-form name="basic" :label-col="{ span: 6 }" :wrapper-col="{ span: 12 }" autocomplete="off">
      <a-form-item label="Username" name="username">
          <a-input v-model:value="username" />
      </a-form-item>

      <a-form-item label="Email" name="email">
          <a-input v-model:value="email" />
      </a-form-item>

      <a-form-item label="Password" name="password">
          <a-input-password v-model:value="password" />
      </a-form-item>

      <a-form-item label="Role">
      <a-radio-group v-model:value="role">
        <a-radio value="Student">Student</a-radio>
        <a-radio value="Tutor">Tutor</a-radio>
      </a-radio-group>
    </a-form-item>

      <a-form-item :wrapper-col="{ offset: 6, span: 12 }">
          <a-button style="width: 225px;" type="primary" @click="login()">Register</a-button>
      </a-form-item>
  </a-form>
</template>
  
  <script setup>
  import { ref } from 'vue';
  const role = ref('Student')
  const username = ref('');
  const email = ref('');
  const password = ref('');
  
  const handleSubmit = () => {
    var data = new FormData();
    data.append('username', username.value);
    data.append('password', password.value);
    data.append('id', role.value)
    data.append('email', email.value)

    var config = {
        method: 'post',
        url: 'http://localhost:5000/register',
        data: data
    };

    axios(config)
        .then(function (response) {
            console.log(JSON.stringify(response.data));
        })
        .catch(function (error) {
            console.log(error);
        });
  }
  </script>
  
  
  <style scoped>
  </style>
  