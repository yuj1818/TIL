<template>
    <div>
        <h3>이름 : {{ info.name }}</h3>
        <p>직함 : {{  info.title }}</p>
    </div>
</template>

<script setup>
    defineProps({
        info: Object
    })
</script>

<style scoped>
    div {
        border: 1px solid lightgray;
        text-align: center;
        width: 40%;
        background-color: gainsboro;
    }
</style>