<template>
  <div class="parent">
    <h2>부모 컴포넌트</h2>
    <p>{{ family.father }}</p>
    <p>{{ family.mother }}</p>
    <ChildPage 
      v-for="child in family.children"
      :key="child.name"
      :name="child.name"
    />
  </div>
</template>

<script setup>
  import ChildPage from '@/components/ChildPage.vue';

  defineProps({
    family: Object
  })
</script>

<style scoped>
  .parent {
    border: 1px solid lightgray;
    background-color: #F0F0F0;
    text-align: center;
    margin: 1rem;
  }
</style>