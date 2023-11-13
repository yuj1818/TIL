<template>
  <div>
    <h1>학생 상세 정보 목록 입니다.</h1>
    <p v-for="(student, idx) in students" @click="goDetail(idx)">{{ student.name }} 학생 정보 보기</p>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'  

  const router = useRouter()

  const students = ref([
    {name: '김하나'},
    {name: '김두리'},
    {name: '김서이'},
  ])

  const goDetail = function(idx) {
    router.push({name: 'studentDetail', params: {name: students.value[idx].name}})
  }

</script>