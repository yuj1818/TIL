<template>
  <div>
    <p>{{ myMsg }}</p>
    <p>{{ dynamicProps}}</p>
    <ParentGrandChild :my-msg="myMsg" @update-name="updateName"/>
    <!-- <button @click="buttonClick">클릭</button>
    <button @click="emitArgs">추가 인자 전달</button> -->
  </div>
</template>

<script setup>
  import ParentGrandChild from '@/components/ParentGrandChild.vue'
  // defineProps(['myMsg'])
  const props = defineProps({
    myMsg:String,
    dynamicProps: String
  })
  
  // const emit = defineEmits(['someEvent', 'emitArgs'])
  // const buttonClick = function() {
  //   emit('someEvent')
  // }
  // const emitArgs = function() {
  //   emit('emitArgs', 1, 2, 3)
  // }

  const emit = defineEmits(['updateName'])
  const updateName = function() {
    emit('updateName')
  }
</script>