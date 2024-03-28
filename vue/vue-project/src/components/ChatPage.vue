<template>
    <div class="chat-container">
      <div class="chat-history">
        <div v-for="message in messages" :key="message.id" class="message">
          <strong>{{ message.sender }}:</strong> {{ message.text }}
        </div>
      </div>
      <div class="chat-input">
        <input v-model="newMessage" @keyup.enter="sendMessageApi" placeholder="Type a message..." />
        <button @click="sendMessageApi">Send</button>
      </div>
    </div>
  </template>
  
  <script setup>
  import { message } from 'ant-design-vue';
  import axios from 'axios';
  import { ref } from 'vue';
  import { computed } from 'vue';
  import { useStore } from 'vuex';
  import { onMounted } from 'vue';

  const store = useStore();
  const user_info = sessionStorage.getItem('user_info') ? JSON.parse(sessionStorage.getItem('user_info')) : null;
  const username = user_info ? user_info.username : 'Anonymous';  

  const messages = ref([
    { id: 1, sender: username, text: 'Hello, how are you?' },
    { id: 2, sender: 'bsdf', text: 'I\'m good, thanks! And you?' },
    // Add initial chat history here
  ]);

  onMounted(() => {
    getMessage();
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
    data.append('receiver', 'bsdf');
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
        receiver: 'bsdf',
    };
    const config = {
      method: 'get',
      url: 'http://127.0.0.1:5000/get_message',
      params: params
    };
    axios(config)
      .then(function (response) {
        console.log(JSON.stringify(response.data));
        response.data.forEach(element => {
          messages.value.push({
            id: element.id,
            sender: element.sender,
            text: element.text,
          });
        });
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
  