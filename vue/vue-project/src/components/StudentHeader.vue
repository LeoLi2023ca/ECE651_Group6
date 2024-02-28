<template>
    <header>
      <nav>
        <ul>
          <li><router-link to="/">Home</router-link></li>
          <li><router-link to="/post">Post</router-link></li>
          <li><router-link to="/tutor-list">Tutors</router-link></li>
          <li><router-link to="/tutor-list">Me</router-link></li>

          <!-- 添加更多导航链接 -->
        </ul>
      </nav>
    </header>
  </template>
  
  <script>
  export default {
    name: 'Header',
  };
  </script>
  
  <style>
  </style>
  