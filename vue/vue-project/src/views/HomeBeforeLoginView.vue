<template>
    <div id="hero_background" class="flex-center">
      <div id="hero" class="navy flex-center">
        <h1 class="bold">Unlock Your Learning Potential with TutorEase</h1>
        <h3>Connecting Students and Tutors for Personalized Learning Journeys</h3>
        <div class="sperator-40px"></div>
        <router-link to="/login">
            <a class="hero_button flex-center" @click="">Register</a>
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
            <h3 class="bold">STEP 01</h3>
            <h2 class="bold">Sign Up</h2>
            <h3>Kickstart your journey to academic excellence by creating your free student account on TutorEase. Our sign-up process is quick and straightforward, requiring only essential information to connect you with the right tutors. Privacy and security are paramount, ensuring your personal details are safe with us.</h3>
          </div>
          <div class="timeline_container right">
            <h3 class="bold">STEP 02</h3>
            <h2 class="bold">Post Your Needs</h2>
            <h3>Once registered, it's time to let tutors know what you're looking for. Create a detailed advertisement including the subject matter you need help with (e.g., Calculus, English Literature), your academic level (e.g., high school, undergraduate), preferred language of instruction, and your budget. This information helps us match you with the ideal tutors who specialize in your area of need.</h3>       
          </div>
          <div class="timeline_container left">
            <h3 class="bold">STEP 03</h3>
            <h2 class="bold">Match and Learn</h2>
            <h3>With your requirements posted, tutors who match your criteria can reach out to you. Browse through tutor profiles, read reviews from other students, and view introductory videos to make an informed choice. Once you've found your match, schedule sessions at times that suit you both and embark on a personalized learning journey that aims to not just meet, but exceed your academic goals.</h3>
          </div>
        </div>
        
      </div>
      <div class="sperator-40px"></div>
      <div id="features" class="flex-center padding-40">
          <h1 class="bold">Why TutorEase?</h1>
          <div class="sperator-40px"></div>
          <div class="flex-center row" style="gap: 90px;">
            <div class="feature_container flex-center ">
              <i class="fa-solid fa-calendar-days"></i>
              <div>
                <h3 class="bold" style="text-align: center; font-size: 1.8em;">Flexibility</h3>
                <p style="text-align: center; font-size: 1.05em;">Your education, your schedule. TutorEase offers unparalleled flexibility, allowing you to choose tutoring sessions that fit into your life, not the other way around. Whether you’re an early bird or a night owl, our platform enables you to learn on your terms, anytime, anywhere</p>
              </div>
            </div>
            <div class="feature_container flex-center ">
              <i class="fa-solid fa-calendar-days"></i>
              <div>
                <h3 class="bold" style="text-align: center; font-size: 1.8em;">Flexibility</h3>
                <p style="text-align: center; font-size: 1.05em;">Your education, your schedule. TutorEase offers unparalleled flexibility, allowing you to choose tutoring sessions that fit into your life, not the other way around. Whether you’re an early bird or a night owl, our platform enables you to learn on your terms, anytime, anywhere</p>
              </div>
            </div>
            <div class="feature_container flex-center ">
              <i class="fa-solid fa-calendar-days"></i>
              <div>
                <h3 class="bold" style="text-align: center; font-size: 1.8em;">Supportive Community</h3>
                <p style="text-align: center; font-size: 1.05em;">Join an engaging community of like-minded professionals. TutorEase is not just a platform for teaching but a space to grow, learn, and collaborate. Share resources, exchange teaching strategies, and stay updated with the latest in education technology. Together, we’re not just teaching; we’re making a difference</p>
              </div>
            </div>
          </div>
    </div>
    <div id="faq" class="flex-center">
      <h1 class="bold">FAQ</h1>
      <div>
        <div class="faq">
          <h3 class="bold">Q: How do I become a tutor at Tutorease?</h3>
          <h4>A: To become a tutor, create a profile, submit your qualifications for review, and once approved, you can start offering your courses to students worldwide.</h4>
        </div>
        <div class="faq">
          <h3 class="bold">Q: What qualifications do I need to teach?</h3>
          <h4>A: You must have certified qualifications or proven experience in the subject you wish to teach, as well as strong communication skills and a passion for teaching.</h4>
        </div>
        <div class="faq">
          <h3 class="bold">Q: How can I manage my lessons?</h3>
          <h4>A: Tutorease provides a platform for you to set your schedule, manage your lessons, and communicate directly with your students.</h4>
        </div>
        <div class="faq">
          <h3 class="bold">Q: What is the payment process for tutors?</h3>
          <h4>A: Payment by yourself cash, paypal or bank transfer all fine, Tutorease just a platform.</h4>
        </div>
        <div class="faq">
          <h3 class="bold">Q: How do I handle cancellations?</h3>
          <h4>A: You can set your own cancellation policy. It's important to clearly communicate your policy to your students before lessons begin.</h4>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { inject } from 'vue';
  import StudentHome from './StudentHomeView.vue';
  import TutorHome from './TutorHomeView.vue';
  import $ from 'jquery';
  
  const role = inject('role');

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
  
    .feature_container{
      padding: 40px;
      width: 300px;
      background-color: white;
      /* text-align: justify; */
      border-radius: 20px;
      gap: 20px;
    }
  
    .feature_container i{
      font-size: 80px
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
  