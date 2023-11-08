<template>
    <div>
        <h1>부모 페이지입니다.</h1>
        <!-- <ChildPage v-for="child in children" :key="child" @give-me-allowance="updateBalance" :name="child.name" :age="child.age" :balance="child.balance"/> -->
        <ChildPage v-for="child in children" :key="child" @give-me-allowance="updateBalance" :child="child"/>
    </div>
</template>

<script setup>
    import ChildPage from './ChildPage.vue'

    import { ref } from 'vue'

    const children = ref([
        {name: '김하나', age: 30, balance: 100000},
        {name: '김두리', age: 20, balance: 10000},
        {name: '김서이', age: 10, balance: 1000}
    ])

    const updateBalance = (child) => {
        child.balance += 1000
    }
</script>