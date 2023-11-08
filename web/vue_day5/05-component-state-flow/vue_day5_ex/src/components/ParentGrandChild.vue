<template>
  <div>
    <button @click="updateName">이름 변경</button>
  </div>
</template>

<script setup>
  const emit = defineEmits(['updateName'])
  const updateName = function() {
    emit('updateName')
  }
</script>