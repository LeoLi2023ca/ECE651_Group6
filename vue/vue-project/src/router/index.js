import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import TutorListView from '../views/TutorListView.vue'
import PostView from '../views/PostView.vue'
import TutorView from '../views/TutorView.vue'
import PostListView from '../views/PostListView.vue'
import PostForm from '@/components/PostForm.vue'
import MyPostList from '@/components/MyPostList.vue'
import PostHistory from '@/components/PostHistory.vue'
import ChatPage from '@/components/ChatPage.vue'

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
      children: [
        {
          path: 'my-post',
          name: 'my-post',
          component: MyPostList
        },
        {
          path: 'create-post',
          name: 'create-post',
          component: PostForm
        },        
        {
          path: 'post-history',
          name: 'post-history',
          component: PostHistory
        },
      ]
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
    },
    {
      path: '/chat/:id',
      name: 'chat',
      component: ChatPage
    }
  ]
})

router.beforeEach((to, from, next) => {
  const token = sessionStorage.getItem('token');
  if (to.name !== 'login' && token !== '1' && token !== '2') next({ name: 'login' });
  else next();
});

export default router;
