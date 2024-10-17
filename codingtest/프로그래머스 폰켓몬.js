function solution(nums) {
  const species = new Set(nums)
  ans = species.size
  n = nums.length / 2
  if (n >= ans) {
      return ans
  } else {
      return n
  }
}