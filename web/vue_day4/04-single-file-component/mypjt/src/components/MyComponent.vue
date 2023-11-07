<template>
    <div class="greeting">{{ msg }}</div>
    <div>
        <h2>MyComponent</h2>
        <MyComponentItem />
        <MyComponentItem />
        <MyComponentItem />
    </div>
</template>

<script setup>
    import {ref} from 'vue'
    import MyComponentItem from './MyComponentItem.vue';

    const msg = ref('Hello World!')
</script>

<style scoped>
    .greeting {
        color: red;
    }
</style>