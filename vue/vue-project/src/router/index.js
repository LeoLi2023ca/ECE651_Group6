import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import TutorListView from '../views/TutorListView.vue'
import PostView from '../views/PostView.vue'
import PostListView from '../views/PostListView.vue'
import PostForm from '@/components/PostForm.vue'
import MyPostList from '@/components/MyPostList.vue'
import PostHistory from '@/components/PostHistory.vue'
import StudentProfileView from '@/views/StudentProfileView.vue'
import StudentSettingView from '@/views/StudentSettingView.vue'
import TutorProfileView from '@/views/TutorProfileView.vue'
import TutorSettingView from '@/views/TutorSettingView.vue'
import ChatPage from '@/components/ChatPage.vue'
import WelcomeTutorView from '@/views/WelcomeTutorView.vue'
import RegisterView from '@/views/RegisterView.vue'
import StudentMatchingView from '@/views/StudentMatchingView.vue'
import TutorMatchingView from '@/views/TutorMatchingView.vue'

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
      path: '/tutor',
      name: 'tutor',
      children: [
        {
          path: 'my-profile',
          name: 'tutor-profile',
          component: TutorProfileView
        }, {
          path: 'settings',
          name: 'tutor-settings',
          component: TutorSettingView
        }
      ]
    },
    {
      path: '/student',
      name: 'student',
      children: [
        {
          path: 'my-profile',
          name: 'student-profile',
          component: StudentProfileView
        }, {
          path: 'settings',
          name: 'student-settings',
          component: StudentSettingView
        }
      ]
    },
    {
      path: '/welcome-tutor',
      name: 'welcome-tutor',
      component: WelcomeTutorView
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterView
    },
    {
      path: '/student-matching',
      name: 'student-matching',
      component: StudentMatchingView
    },
    {
      path: '/tutor-matching',
      name: 'tutor-matching',
      component: TutorMatchingView
    }
    // {
    //   path: '/chat/:id',
    //   name: 'chat',
    //   component: ChatPage
    // },
    // {
    //   path: '/tutor/:id',
    //   name: 'tutor',
    //   component: TutorView
    // }
  ]
})

router.beforeEach((to, from, next) => {
  const token = sessionStorage.getItem('role');
  if (to.name !== 'login' && token !== '1' && token !== '2') next({ name: 'login' });
  else next();
});

export default router;