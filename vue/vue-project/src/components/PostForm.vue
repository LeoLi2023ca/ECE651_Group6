<script setup>
import { ref } from 'vue';
const props = defineProps({
  show: Boolean
})
const title = ref('');
const subject = ref('');
const msg = ref('');
const salary = ref('');
const available_time = ref('');
</script>

<template>
  <Transition name="modal">
    <div v-if="show" class="modal-mask">
      <div class="modal-container">
        <div class="modal-header">
          <slot name="header">New Post</slot>
        </div>
        <slot>
          <div>
          <label for="title">Title: </label>
          <input v-model="title"> {{ title }}
        </div>
        <div>
          <label for="subject">Subject: </label>
          <input v-model="subject"> {{ subject }}
        </div>
        <div>
          <label for="msg">Message: </label>
          <input v-model="msg"> {{ msg }}
        </div>
        <div>
          <label for="salary">Salary: </label>
          <input v-model="salary"> {{ salary }}
        </div>
        <div>
          <label for="available_time">Available Time: </label>
          <input v-model="available_time"> {{ available_time }}
        </div>
        <br/>
        <div>
          <button class="modal-default-button" @click="$emit('close')">Submit</button>
          <button class="modal-default-button" @click="$emit('close')">Cancel</button>
        </div>
        </slot>
      </div>
    </div>
  </Transition>
</template>

<style>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  transition: opacity 0.3s ease;
}

.modal-container {
  width: 300px;
  margin: auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
}

.modal-header h3 {
  margin-top: 0;
  color: #42b983;
}

.modal-body {
  margin: 20px 0;
}

.modal-default-button {
  float: right;
}

/*
 * 对于 transition="modal" 的元素来说
 * 当通过 Vue.js 切换它们的可见性时
 * 以下样式会被自动应用。
 *
 * 你可以简单地通过编辑这些样式
 * 来体验该模态框的过渡效果。
 */

.modal-enter-from {
  opacity: 0;
}

.modal-leave-to {
  opacity: 0;
}

.modal-enter-from .modal-container,
.modal-leave-to .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
</style>