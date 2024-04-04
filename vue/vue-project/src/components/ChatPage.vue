<template>
    <div class="chat-container">
      <div>Chatting with: {{ receiverUsername }}</div>
      <div class="chat-history">
        <div v-for="message in messages" :key="message.id" class="message">
          <strong>{{ message.sender }}:</strong> {{ message.text }}
        </div>
      </div>
      <div class="chat-input">
        <input v-model="newMessage" @keyup.enter="sendMessageApi" placeholder="Type a message..." />
        <button @click="sendMessageApi">Send</button>
        <button v-if="user_role=='1'" @click="matchWithTutor" class="match-button">Match</button>
      </div>
    </div>
  </template>
  
  <script setup>
  import { message } from 'ant-design-vue';
  import axios from 'axios';
  import { ref } from 'vue';
  import { computed } from 'vue';
  import { useStore } from 'vuex';
  import { onMounted, onUnmounted} from 'vue';

  const store = useStore();
  const user_info = sessionStorage.getItem('user_info') ? JSON.parse(sessionStorage.getItem('user_info')) : null;
  const user_role = sessionStorage.getItem('role');
  const username = user_info ? user_info.username : 'Anonymous';  
  const props = defineProps({
    receiver: String,
  });
  const receiverUsername = ref(props.receiver);
  console.log(props);

  const messages = ref([]);

  onMounted(() => {   console.log(receiverUsername.value);   // Start polling for messages every second
    const intervalId = setInterval(getMessage, 1000);    // Stop polling when the component is unmounted   
    onUnmounted(() => {     clearInterval(intervalId);   }
    ); 
  });
//   getMessage();
  
  const newMessage = ref('');
  
  const sendMessage = () => {
    if (newMessage.value.trim() !== '') {
      messages.value.push({
        id: messages.value.length + 1,
        sender: 'User1', // Assume "User1" is the sender for the demo
        text: newMessage.value,
      });
      newMessage.value = ''; // Clear input after sending
    }
  };

  const sendMessageApi = () => {
    var data = new FormData();
    if(messages.value.length > 0){
        data.append('parent_message_id', messages.value[messages.value.length - 1].id);
    }
    else {
        data.append('parent_message_id', null);
    }
    data.append('sender', username);
    data.append('text', newMessage.value);
    data.append('receiver', receiverUsername.value);
    console.log(data)
    var config = {
      method: 'post',
      url: 'http://127.0.0.1:5000/send_message',
      data: data
    };
    messages.value.push({
      id: messages.value.length + 1,
      sender: username,
      text: newMessage.value,
    });
    axios(config)
      .then(function (response) {
        console.log(JSON.stringify(response.data));
      })
      .catch(function (error) {
        console.log(error);
      });
    newMessage.value = ''; // Clear input after sending
  };

  const getMessage = () => {
    const params = {
        sender: username,
        receiver: receiverUsername.value,
    };
    const config = {
      method: 'get',
      url: 'http://127.0.0.1:5000/get_message',
      params: params
    };
    var buffer = []
    axios(config)
      .then(function (response) {
        console.log(JSON.stringify(response.data));
        // messages.value = [];
        response.data.forEach(element => {
          buffer.push({
            id: element.id,
            sender: element.sender,
            text: element.text,
          });
        });
      }).then(() => {
        messages.value = buffer;
      })
      .catch(function (error) {
        console.log(error);
      });
      
   };
   

   const matchWithTutor = () => {
    const confirmMessage = `Do you want to ask for matching with ${receiverUsername.value}?`;
    if(confirm(confirmMessage) == false){
        return;
    };
    console.log(receiverUsername.value);
    console.log(username);
    const params = {
        student_username: username,
        tutor_username: receiverUsername.value,
    };
    const config = {
      method: 'post',
      url: 'http://127.0.0.1:5000/studentRequestMatching',
      params: params
    };
    axios(config)
      .then(function (response) {
        console.log(JSON.stringify(response.data));
        message.success('Match request sent successfully!');
      })
      .catch(function (error) {
        console.log(error);
      });
  };
  

   const closeChat = () => {
    emit('close');
   };
  </script>
  
  <style scoped>
  .chat-container {
    max-width: 600px;
    margin: 0 auto;
    border: 1px solid #ccc;
    padding: 20px;
  }
  
  .chat-history {
    height: 300px;
    overflow-y: auto;
    margin-bottom: 20px;
    border: 1px solid #ddd;
    padding: 10px;
  }
  
  .message {
    margin-bottom: 15px;
  }
  
  .chat-input {
    display: flex;
  }
  
  .chat-input input {
    flex-grow: 1;
    margin-right: 10px;
  }
  
  .chat-input button {
    padding: 6px 12px;
  }
  </style>
  