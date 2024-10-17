function solution(phone_book) {
  let ans = true
  const book = {}
  phone_book.forEach(num => book[num] = 1)
  phone_book.sort((a, b) => a.length - b.length).reverse()
  phone_book.forEach(num => {
      let temp = ''
      for (let i = 0; i < num.length - 1; i++) {
          temp += num[i]
          if (temp in book) {
              ans = false
              return
          }
      }
  })
  
  return ans
}