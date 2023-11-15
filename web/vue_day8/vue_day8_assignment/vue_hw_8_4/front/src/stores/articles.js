import axios from 'axios'
import { ref } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'

export const useArticleStore = defineStore('article', () => {
  const router = useRouter()

  const articles = ref([])

  const getArticles = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/articles'
    })
    .then(res => {
      //console.log(res)
      articles.value = res.data
    })
  }

  const createArticle = function(title, content) {
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/api/v1/articles/',
      data: {
        title: title,
        content: content
      }
    })
    .then(() => {
      router.push({name: 'home'})
    })
    .catch(err => console.log(err))
  }

  return { articles, getArticles, createArticle }
})
