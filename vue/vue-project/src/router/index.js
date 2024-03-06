import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import TutorListView from '../views/TutorListView.vue'
import PostView from '../views/PostView.vue'
import TutorView from '../views/TutorView.vue'
import PostListView from '../views/PostListView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/post',
      name: 'post',
      component: PostView,
    },
    {
      path: '/post-list',
      name: 'post-list',
      component: PostListView,
    },
    {
      path: '/tutor-list',
      name: 'tutor-list',
      component: TutorListView
    },
    {
      path: '/tutor/:id',
      name: 'tutor',
      component: TutorView
    }
  ]
})

router.beforeEach((to, from, next) => {
  const token = sessionStorage.getItem('token');
  if (to.name !== 'login' && token!=='1') next({ name: 'login' });
  else next();
});

export default router;
