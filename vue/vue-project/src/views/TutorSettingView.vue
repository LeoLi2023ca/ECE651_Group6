  <template>
    <a-layout-content style="display: flex; align-items: center; justify-content: center; min-height: 80vh;">
      <div class="form-container">
        <a-form
          ref="formRef"
          name="custom-validation"
          :model="formState"
          :rules="rules"
          @finish="handleFinish"
          @validate="handleValidate"
          @finishFailed="handleFinishFailed"
          layout="vertical"
        >
          <a-typography-title :level="4" class="form-title">Update Password</a-typography-title>
          <a-form-item label="Previous password" name="old_pass">
            <a-input v-model:value="formState.oldPass" type="password" autocomplete="off" />
          </a-form-item>
          <a-form-item label="New password" name="pass">
            <a-input v-model:value="formState.pass" type="password" autocomplete="off" />
          </a-form-item>
          <a-form-item label="Confirm" name="checkPass">
            <a-input v-model:value="formState.checkPass" type="password" autocomplete="off" />
          </a-form-item>
          <a-form-item>
            <a-button type="primary" html-type="submit" class="submit-button">Submit</a-button>
          </a-form-item>
        </a-form>
      </div>
    </a-layout-content>
  </template>
  
  <script setup>
  import { reactive, ref } from 'vue';
  import axios from 'axios';
  import { message } from 'ant-design-vue';
  
  const formRef = ref();
  const formState = reactive({
    oldPass: '',
    pass: '',
    checkPass: '',
  });
  
  const validatePass = async (_rule, value) => {
    if (value === '') {
      return Promise.reject('Please input the new password');
    } else {
      if (formState.checkPass !== '') {
        formRef.value.validateFields('checkPass');
      }
      return Promise.resolve();
    }
  };
  
  const validatePass2 = async (_rule, value) => {
    if (value === '') {
      return Promise.reject('Please input the new password again');
    } else if (value !== formState.pass) {
      return Promise.reject("Two inputs don't match!");
    } else {
      return Promise.resolve();
    }
  };
  
  const rules = {
    oldPass: [
      {
        required: true,
        validator: validatePass,
        trigger: 'change',
      }
    ],
    pass: [
      {
        required: true,
        validator: validatePass,
        trigger: 'change',
      },
    ],
    checkPass: [
      {
        required: true,
        validator: validatePass2,
        trigger: 'change',
      },
    ],
  };
  
  function updatePassword() {
    var data = new FormData();
    const user_info = JSON.parse(sessionStorage.getItem('user_info'));
    data.append('username', user_info.username);
    data.append('old_pass', formState.oldPass);
    data.append('new_pass', formState.pass);
  
    var config = {
      method: 'post',
      url: 'http://127.0.0.1:5000/updatePassword',
      data: data
    };
  
    axios(config)
      .then(function (response) {
        console.log(response);
        formState.oldPass = '';
        formState.checkPass = '';
        formState.pass = '';
        message.success('Password updated successfully!');
      })
      .catch(function (error) {
        console.log(error);
        formState.oldPass = '';
        formState.checkPass = '';
        formState.pass = '';
        message.error('Previous password incorrect!');
      });
  }
  
  const handleFinish = values => {
    updatePassword();
    console.log(values, formState);
  };
  
  const handleFinishFailed = errors => {
    console.log(errors);
  };
  
  const handleValidate = (...args) => {
    console.log(args);
  };
  </script>
  
  <style scoped>
  .form-container {
    max-width: 600px;
    margin: 5vh auto 0px auto;
    padding: 40px;
    background: #fff;
    border: 2px solid #e0e0e0;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    background: linear-gradient(to right, #ffffff, #f2f2f2);
    display: flex;
    flex-direction: column;
    text-align: center;

  }
  
  .form-title {
    color: rgb(33, 150, 243);
    margin-bottom: 24px;
  }
  
  .form-container .ant-form-item {
    margin-bottom: 24px;
  }
  
  .form-container .ant-form-item:last-child {
    margin-bottom: 0;
  }
  
  .form-container .ant-input {
    border-radius: 4px;
  }
  
  .submit-button {
    width: 60%;
    margin: 0 auto;
  }
  
  .form-container .ant-btn {
    background-color: rgb(63, 195, 128);
    color: white;
    border: none;
    border-radius: 4px;
  }
  
  .form-container .ant-btn:hover {
    background-color: rgb(33, 150, 243);
    color: white;
  }
  </style>
  