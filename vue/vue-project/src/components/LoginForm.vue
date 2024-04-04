  <template>
    <div class="form-container">
      <a-typography-title :level="4" class="form-title">Log in</a-typography-title>
      <a-form name="basic" layout="vertical" autocomplete="off">
        <a-form-item label="Username" name="username">
          <a-input v-model:value="username" />
        </a-form-item>
        <a-form-item label="Password" name="password">
          <a-input-password v-model:value="password" />
        </a-form-item>
        <a-form-item>
          <a-button type="primary" @click="login()" class="login-button">Login</a-button>
        </a-form-item>
        <!-- <a-form-item class="account-switch">
          Don't have an account?
        </a-form-item> -->
      </a-form>
    </div>
  </template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';
import { useStore } from 'vuex';

const store = useStore();
const router = useRouter();

const username = ref('');
const password = ref('');

const login = async () => {
    var data = new FormData();
    data.append('username', username.value);
    data.append('password', password.value);

    var config = {
        method: 'post',
        url: 'http://127.0.0.1:5000/login',
        data: data
    };

    axios(config)
        .then(function (response) {
            sessionStorage.setItem('role', response.data.code);
            sessionStorage.setItem('user_info', JSON.stringify(response.data.user_info))
            store.commit('setUserRole', response.data.code);
            router.push({ name: 'home' });
            alert('Login successful!');
        })
        .catch(function (error) {
            if(error.response.status == 401){
                console.log(error);
                alert(error.response.data["error"]);
            }
            else if(error.response.status == 404){
                alert('User not found');
            }
            else{
                alert('Something went wrong');
                console.log(error);
            }
        });
};
</script>

<style scoped>
.form-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.form-title {
  margin-bottom: 24px;
  color: rgb(33, 150, 243);
}

.login-button {
  width: 100%;
  background-color: rgb(63, 195, 128);
  border-radius: 4px;
  border: none;
  /* color: white; */
}

.login-button:hover {
  background-color: rgb(63, 195, 128);
}

.a-form-item {
  margin-bottom: 24px;
}

.account-switch {
  text-align: center;
  margin-top: 12px;
}

.a-input,
.a-input-password {
  border-radius: 4px;
}

.account-switch {
  font-size: 0.9em;
  color: #a9a9a9;
  cursor: pointer;
}

.account-switch:hover {
  color: #1890ff;
}
</style>