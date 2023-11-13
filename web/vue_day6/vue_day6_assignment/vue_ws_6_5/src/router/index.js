import { createRouter, createWebHistory } from 'vue-router'
import Homeview from '../views/Homeview.vue'
import QuizView from '../views/QuizView.vue'
import AnswerView from '../views/AnswerView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Homeview
    },
    {
      path: '/quiz',
      name: 'quiz',
      component: QuizView
    },
    {
      path: '/answer/:pk/:answer',
      name: 'answer',
      component: AnswerView
    }
  ]
})

export default router
