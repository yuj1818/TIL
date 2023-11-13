import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useBalanceStore = defineStore('balance', () => {
  const balances = ref([
    {
      name: '김하나',
      balance: 100000
      },
      {
      name: '김두리',
      balance: 10000
      },
      {
      name: '김서이',
      balance: 100
      },
  ])

  const getUserInfo = computed(() => {
    return (userName) => balances.value.find((balance) => balance.name === userName)
  })

  const addBalance = function(userName) {
    const idx = balances.value.findIndex(balance => balance.name === userName)
    balances.value[idx].balance += 1000
  }

  return { balances, getUserInfo, addBalance }
})