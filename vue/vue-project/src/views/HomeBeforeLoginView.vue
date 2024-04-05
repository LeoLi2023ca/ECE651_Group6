<template>
    <div id="hero_background" class="flex-center">
      <div id="hero" class="navy flex-center">
        <h1 class="bold">Unlock Your Learning Potential with TutorEase</h1>
        <h3>Connecting Students and Tutors for Personalized Learning Journeys</h3>
        <div class="sperator-40px"></div>
        <router-link to="/login">
            <a class="hero_button flex-center" @click="">Login / Register</a>
        </router-link>
        <!-- <div id="hero_button_holder">
          <a class="hero_button flex-center">Become a Student</a>
          <div class="sperator-20px" style="display: inline-block;"></div>
          <a class="hero_button flex-center">Become a Tutor</a>
        </div> -->
      </div>
    </div>
    <div class="sperator-40px"></div>
    <div id="intro" class="navy flex-center">
        <h1 class="bold">How It Works</h1>
        <div class="sperator-20px"></div>
        <div class="sperator-40px"></div>
        <div id="timeline">
          <div class="timeline_container left">
            <h3 class="bold  timeline_fadein_1">STEP 01</h3>
            <h2 class="bold timeline_fadein_1">Sign Up</h2>
            <h3 class="timeline_fadein_1">Kickstart your journey to academic excellence by creating your free student account on TutorEase. Our sign-up process is quick and straightforward, requiring only essential information to connect you with the right tutors. Privacy and security are paramount, ensuring your personal details are safe with us.</h3>
          </div>
          <div class="timeline_container right">
            <h3 class="bold timeline_fadein_2">STEP 02</h3>
            <h2 class="bold timeline_fadein_2">Post Your Needs</h2>
            <h3 class="timeline_fadein_2">Once registered, it's time to let tutors know what you're looking for. Create a detailed advertisement including the subject matter you need help with (e.g., Calculus, English Literature), your academic level (e.g., high school, undergraduate), preferred language of instruction, and your budget. This information helps us match you with the ideal tutors who specialize in your area of need.</h3>       
          </div>
          <div class="timeline_container left">
            <h3 class="bold timeline_fadein_3">STEP 03</h3>
            <h2 class="bold timeline_fadein_3">Match and Learn</h2>
            <h3 class="timeline_fadein_3">With your requirements posted, tutors who match your criteria can reach out to you. Browse through tutor profiles, read reviews from other students, and view introductory videos to make an informed choice. Once you've found your match, schedule sessions at times that suit you both and embark on a personalized learning journey that aims to not just meet, but exceed your academic goals.</h3>
          </div>
        </div>
        
      </div>
      <div class="sperator-40px"></div>
      <div id="features" class="flex-center padding-40">
          <h1 class="bold">Why TutorEase?</h1>
          <div class="sperator-40px"></div>
          <div class="flex-center row" style="gap: 90px;">
            <div class="feature_container flex-center ">
              <i class="fa-solid fa-people-arrows"></i>
              <div>
                <h3 style="text-align: center">Personalized Matches</h3>
              </div>
            </div>
            <div class="feature_container flex-center ">
              <i class="fa-solid fa-calendar-days"></i>
              <div>
                <h3 style="text-align: center">Flexibility</h3>
              </div>
            </div>
            <div class="feature_container flex-center ">
                <i class="fa-solid fa-comments"></i>
              <div>
                <h3 style="text-align: center">Trusted Reviews</h3>
              </div>
            </div>
          </div>
          <div class="sperator-40px"></div>
          <div class="sperator-40px"></div>
          <div class="flex-center row" style="gap: 90px;">
            <div class="feature_container flex-center ">
                <i class="fa-brands fa-bandcamp"></i>
              <div>
                <h3 style="text-align: center">Build Your Brand</h3>
              </div>
            </div>
            <div class="feature_container flex-center ">
                <i class="fa-solid fa-money-bill"></i>
              <div>
                <h3 style="text-align: center">Flexible Earnings</h3>
              </div>
            </div>
            <div class="feature_container flex-center ">
              <i class="fa-regular fa-circle-question"></i>
              <div>
                <h3 style="text-align: center">Supportive Community</h3>
              </div>
            </div>
          </div>
          <div class="sperator-40px"></div>
    </div>
    <div class="sperator-40px"></div>
    
  </template>
  
  <script setup>
  import { inject } from 'vue';
  import StudentHome from './StudentHomeView.vue';
  import TutorHome from './TutorHomeView.vue';
  import $ from 'jquery';
  
  const role = inject('role');

  window.onscroll = function() {
    // Set the height to check for
  if (window.pageYOffset >= 20) {
    // If more show the element
    $(".timeline_fadein_1").addClass( "opacity100" );
  }
  if (window.pageYOffset >= 500) {
    // If more show the element
    $(".timeline_fadein_2").addClass( "opacity100" );
  }
  if (window.pageYOffset >= 800) {
    // If more show the element
    $(".timeline_fadein_3").addClass( "opacity100" );
  }
}

  </script>
  
  <style scoped>
    *{
      margin: 0;
      box-sizing: border-box;
    }
  
    #hero_background{
      background-image: url(../assets/geometric_pattern.jpg);
      background-size: 100% 100%;
      width: 100%;
      height: 800px;
      display: flex;
    }
  
    #hero{
  
    }
  
  
    #hero_button_holder{
      display: flex;
      justify-content: center;
      align-items: center;
      flex-direction: row;
      gap: 17px
    }
  
    #timeline{
      position: relative;
      height: 1050px;
      width: 80%;
    }
  
    #timeline::after{
      content: "";
      position: absolute;
      width: 7px;
      top: 0;
      bottom: 0;
      left: 50%;
      margin-left: -5px;
      background-color: #001628;
    }
  
    .timeline_container{
      position: relative;
      height: 350px;
      width: 50%;
      padding: 80px 100px;
      /* background-color: white; */
    }
  
    .timeline_container::after{
      position: absolute;
      content: '';
      top: 0;
      width: 30px;
      height: 30px;
      border: 7px solid #001628;
      background-color: white;
      border-radius: 50%;
      right: -14px;
      z-index: 1;
    }

    .timeline_fadein_1{
        opacity: 0;
        transition: opacity 0.9s, transform 0.9s;
        /* transform: translateY(20vh); */
        /* visibility: visible; */
    }

    .timeline_fadein_2{
        opacity: 0;
        transition: opacity 0.9s, transform 0.9s;
        /* transform: translateY(20vh); */
        /* visibility: visible; */
    }

    .timeline_fadein_3{
        opacity: 0;
        transition: opacity 0.9s, transform 0.9s;
        /* transform: translateY(20vh); */
        /* visibility: visible; */
    }

    .opacity100{
        opacity: 100;
        transform: translateY(-60px);
        /* visibility: visible */
    }
  
    .feature_container{
      padding: 40px;
      width: 240px;
      height: 240px;
      background-color: white;
      /* text-align: justify; */
      border-radius: 20px;
      gap: 20px;
    }
  
    .feature_container i{
      font-size: 70px
    }

    #faqs{
        width: 60%;
    }
  
    .faq{
      padding: 13px 0px;
    }
  
    .left{
      left: 0
    }
  
    .right{
      left: 50%
    }
  
    .right::after{
      left: -16px;
    }
  
    #features{
      background-color: #d1d7e2;
    }
  
    .hero_button{
      font-size: 1.4em;
      /* padding: 30px ; */
      width: 230px;
      height: 57px;
      border: 1px solid #001628;
      border-radius: 13px;
      color: white;
      background-color: #001628;
      transition: 0.4s
    }

    .hero_button:hover{
      background-color: #244a6b;
      transition: 0.4s
    }
  
    h1 {
    display: block;
    font-size: 3.9em;
    padding-top: 0.55em;
    padding-bottom: 0.55em;
    padding-left: 0;
    padding-right: 0;
    margin-bottom: 0;
  }
  
  h2 {
    display: block;
    font-size: 2.5em;
    padding-top: 0.2em;
    padding-bottom: 0.2em;
    padding-left: 0;
    padding-right: 0;
  }
  
  h3 {
    display: block;
    font-size: 1.5em;
    padding-top: 0.2em;
    padding-bottom: 0.2em;
    padding-left: 0;
    padding-right: 0;
  }
  
  h3 {
    display: block;
    font-size: 1.4em;
    padding-top: 0.2em;
    padding-bottom: 0.2em;
    padding-left: 0;
    padding-right: 0;
  }
  
  .sperator-20px{
    height: 20px;
  }
  
  .sperator-40px{
    height: 40px;
  }
  
  .padding-40{
    padding: 40px;
  }
  
  .bold{
    font-weight: bold;
  }
  
  .white{
    color: white;
  }
  
  .navy{
    color: #001628;
  }
  
  .flex-center{
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
  }
  
  .row{
    flex-direction: row;
  }
  </style>
  