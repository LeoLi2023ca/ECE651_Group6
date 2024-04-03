<!--../../public/dev1.png-->
<template>
  <a-layout class="layout">
    <a-layout-content class="content">
      <a-row type="flex" align="middle">
        <a-col :xs="24" :sm="24" :md="12" class="text-column">
          <div class="main-section">
            <h1 class="title">Become a PRO in any subject</h1>
            <a-list>
              <a-list-item>
                <a-list-item-meta
                    :avatar="{ src: 'circle-icon-path' }"
                    title="Customized 1-on-1 Lessons"
                />
              </a-list-item>
              <a-list-item>
                <a-list-item-meta
                    :avatar="{ src: 'circle-icon-path' }"
                    title="Learn from certified teachers according to your budget and schedule"
                />
              </a-list-item>
              <a-list-item>
                <a-list-item-meta
                    :avatar="{ src: 'circle-icon-path' }"
                    title="All major courses offered, including English Math Science Geography History and more!"
                />
              </a-list-item>
            </a-list>
            <router-link to="/post/my-post">
              <a-button type="primary" size="large">Start now</a-button>
            </router-link>
          </div>
        </a-col>
        <a-col :xs="24" :sm="24" :md="12" class="image-column">
          <img src="../../public/dev1.png" alt="Learn Image" class="responsive-image" />
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
            <h2 class="offers-title">See what Tutorease offers</h2>
          </a-col>
          <a-col :xs="24" :sm="12" :lg="8">
            <div class="feature">
              <img class="feature-icon" src="../../public/offer6.png" alt="1-on-1 lessons" />
              <h3>1-on-1 Lessons</h3>
              <p>Find tutors from around the world sharing their language, dialects, knowledge and culture.</p>
            </div>
          </a-col>
          <a-col :xs="24" :sm="12" :lg="8">
            <div class="feature">
              <img class="feature-icon" src="../../public/offer5.png" alt="Group Class" />
              <h3>Free Chat, Free Use</h3>
              <p>We provide a platform to communicate directly with the tutor, no charges, no intermediary costs!</p>
            </div>
          </a-col>
          <a-col :xs="24" :sm="12" :lg="8">
            <div class="feature">
              <img class="feature-icon" src="../../public/offer7.png" alt="All major subjects" />
              <h3>All major subjects</h3>
              <p>You can find almost any school subject and study with global or local tutors from Tutorease.</p>
            </div>
          </a-col>
        </a-row>
      </div>


      <div class="site-layout-lower-content">
        <!-- Carousel for images and slogans -->



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
          <h2>Frequently Asked Questions</h2>
          <a-collapse default-active-key="1">
            <!-- Existing FAQ items -->
            <a-collapse-panel header="How do I find the right mentor?" key="1">
              <p>The tutor list uses filters that allow you to search and select the best tutor for you based on subject, rating and availability.</p>
            </a-collapse-panel>
            <a-collapse-panel header="What are the payment options?" key="2">
              <p>Unfortunately, we only provide a platform for you to communicate with your tutors, and do not offer any payment guarantees that require you to communicate with your tutors.</p>
            </a-collapse-panel>
            <a-collapse-panel header="How do I book a lesson?？" key="3">
              <p>Direct communication with tutors you like.</p>
            </a-collapse-panel>

            <a-collapse-panel header="Signing up and finding a tutor incurs any fees?" key="4">
              <p>No, signing up and searching for a tutor on Tutorease is completely free. No-Fee in Tutorease</p>
            </a-collapse-panel>
            <a-collapse-panel header="How are the tutors qualified?" key="5">
              <p>Each tutor is required to provide authentic teaching experience and credentials in their profile to ensure they are knowledgeable and passionate about teaching.</p>
            </a-collapse-panel>
            <a-collapse-panel header="Can I cancel a tutoring session?" key="6">
              <p>Each tutor has their own cancellation policy listed on their profile. We suggest you to agree on a cancellation policy with your tutor before booking your sessions.</p>
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



