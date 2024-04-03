<!--../../public/dev1.png-->
<template>
  <a-layout class="layout">
    <a-layout-content class="content">
      <a-row type="flex" align="middle">
        <a-col :xs="24" :sm="24" :md="12" class="text-column">
          <div class="main-section">
            <h1 class="title">Use your teaching specialties to make money!</h1>
            <!-- <a-list>
              <a-list-item>
                <a-list-item-meta
                    :avatar="{ src: 'circle-icon-path' }"
                    title="Easy to find 1-to-1 students"
                />
              </a-list-item>
              <a-list-item>
                <a-list-item-meta
                    :avatar="{ src: 'circle-icon-path' }"
                    title="Free arrangement according to your time"
                />
              </a-list-item>
              <a-list-item>
                <a-list-item-meta
                    :avatar="{ src: 'circle-icon-path' }"
                    title="No intermediate costs"
                />
              </a-list-item>
            </a-list> -->
            <router-link to="/post/my-post">
              <a-button type="primary" size="large">Start now</a-button>
            </router-link>
          </div>
        </a-col>
        <a-col :xs="24" :sm="24" :md="12" class="image-column">
          <img src="/dev2.png" alt="Learn Image" class="responsive-image" />
        </a-col>
      </a-row>

      <a-carousel autoplay dotPosition="bottom">
        <div class="carousel-item">
          <div class="slogan">Learn Directly, Connect Personally — Education with No Middleman.</div>
        </div>

        <div class="carousel-item">
          <div class="slogan">One-on-one education</div>
        </div>

        <div class="carousel-item">
          <div class="slogan">Your Education, Your Terms — No Fees, Just Knowledge.</div>
        </div>

        <div class="carousel-item">
          <div class="slogan">Real Conversations, Real Progress — Learn with Freedom on Tutorease.</div>
        </div>

      </a-carousel>



      <div class="offers-section">
        <a-row :gutter="24">
          <a-col :span="24">
            <h2 class="offers-title">Tutorease for Tutors</h2>
          </a-col>
          <a-col :xs="24" :sm="12" :lg="8">
            <div class="feature">
              <img class="feature-icon" src="/offer11.png" alt="1-on-1 lessons" />
              <h3>Flexible Schedule</h3>
              <p>Set your own hours and teach at your convenience, from any location.</p>
            </div>
          </a-col>
          <a-col :xs="24" :sm="12" :lg="8">
            <div class="feature">
              <img class="feature-icon" src="/offer10.png" alt="Group Class" />
              <h3>Competitive Earnings</h3>
              <p>Enjoy fair compensation for your expertise with zero platform fees.</p>
            </div>
          </a-col>
          <a-col :xs="24" :sm="12" :lg="8">
            <div class="feature">
              <img class="feature-icon" src="/offer9.png" alt="All major subjects" />
              <h3>Global Community</h3>
              <p>Join a network of professionals and grow your teaching career.</p>
            </div>
          </a-col>
        </a-row>
      </div>


      <div class="site-layout-lower-content">



        <a-divider />

        <!-- About Us Section -->
        <div class="about-section">
          <h2>About Tutorease</h2>
          <a-collapse>
            <a-collapse-panel header="About Us" key="1">
              <p>Welcome to Tutorease — a dedicated one-on-one tutoring platform that champions accessible and personalized education. Here, we believe in the transformative power of education and its pivotal role in shaping futures. Our mission is to streamline the path to knowledge, ensuring that every student seeking enlightenment can directly connect with passionate educators.</p>
              <h2>Our Vision</h2>
              <p>We envision a world where education knows no bounds, where students are free from excessive intermediary fees and can freely find the tutors that match their learning needs. Educators can communicate directly with students, fostering robust teaching relationships without third-party intervention and fees.</p>

              <h2>A Unique Way to Connect</h2>
              <p>Tutorease is an open platform that offers students a transparent environment to browse tutor profiles, understand their academic credentials, and teaching styles. Our built-in instant messaging feature facilitates immediate and direct conversations, encouraging the development of tailored learning plans and quick resolution of inquiries within an intuitive interface.</p>

              <h2>Transparent Costs</h2>
              <p>We believe quality education shouldn’t come with a hefty price tag. At Tutorease, we have eliminated the traditional intermediary costs, making education fairer and more accessible. Students only pay for their lessons, with no hidden fees or surprise charges.</p>

            </a-collapse-panel>
          </a-collapse>
        </div>

        <a-divider />

        <!-- FAQ Section -->
        <div class="faq-section">
          <h2>Frequently Asked Questions AS A TUTOR</h2>
          <a-collapse default-active-key="1">
            <a-collapse-panel header="How do I become a tutor at Tutorease?" key="1">
              <p>To become a tutor, create a profile, submit your qualifications for review, and once approved, you can start offering your courses to students worldwide.</p>
            </a-collapse-panel>
            <a-collapse-panel header="What qualifications do I need to teach?" key="2">
              <p>You must have certified qualifications or proven experience in the subject you wish to teach, as well as strong communication skills and a passion for teaching.</p>
            </a-collapse-panel>
            <a-collapse-panel header="How can I manage my lessons?" key="3">
              <p>Tutorease provides a platform for you to set your schedule, manage your lessons, and communicate directly with your students.</p>
            </a-collapse-panel>
            <a-collapse-panel header="What is the payment process for tutors?" key="4">
              <p>Payment by yourself cash, paypal or bank transfer all fine, Tutorease just a platform</p>
            </a-collapse-panel>
            <a-collapse-panel header="How do I handle cancellations?" key="5">
              <p>You can set your own cancellation policy. It's important to clearly communicate your policy to your students before lessons begin.</p>
            </a-collapse-panel>
            <a-collapse-panel header="Can I teach multiple subjects?" key="6">
              <p>Yes, if you are qualified in more than one subject, you can offer lessons in all of them. Make sure to list all your subjects and qualifications on your profile.</p>
            </a-collapse-panel>
          </a-collapse>
        </div>

      </div>








    </a-layout-content>
  </a-layout>
</template>

<script setup>
</script>

<style scoped>
.site-layout-lower-content {
  max-width: 1000px;
  margin: 0 auto;
}

.carousel-item {
  position: relative;
  text-align: center;
}

.slogan {
  font-size: 24px;
  color: rgba(0, 0, 0, 0.6);
  padding: 10px 20px;
  display: inline-block;
  margin-bottom: 20px;
}


.layout {
  min-height: 50vh;
}

.content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 48px;
}

.text-column {
  text-align: left;
  padding: 24px;
}

.image-column {
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 15px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.responsive-image {
  max-width: 100%;
  height: auto;
}


.feature-card img {
  width: 100%;
  margin-bottom: 20px;
}



.offers-section {
  padding: 50px;
  background: #f0f2f6; /* Or any other background color you prefer */
  border-radius: 12px;
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.1);
}

.offers-title {
  text-align: center;
  margin-bottom: 40px;
}

.feature {
  text-align: center;
  padding: 20px;
  background: #fff; /* For the card background */
  border-radius: 10px;
  transition: box-shadow 0.3s;
}

.feature:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.feature-icon {
  height: 80px; /* Adjust the size as needed */
  margin-bottom: 16px;
}

h3 {
  margin-bottom: 16px;
}

.main-section {
  padding: 24px;
  border-radius: 8px;
}

.title {
  color: #f56a00;
  margin-bottom: 24px;
  font-size: 40px;
}

</style>



