function solution(participant, completion) {
  const pd = {}
  participant.forEach((key) => {
      if (key in pd) {
          pd[key] += 1
      } else {
          pd[key] = 1
      }
  })
  
  completion.forEach((key) => {
      if (pd[key] === 1) {
          delete pd[key]
      } else {
          pd[key] -= 1   
      }
  })
  
  return Object.keys(pd)[0]
}