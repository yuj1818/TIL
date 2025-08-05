function solution(progresses, speeds) {
    const dday = []
    for (i = 0; i < progresses.length; i++) {
        dday.push(Math.ceil((100 - progresses[i]) / speeds[i]))
    }
    ans = []
    let cnt = 1
    let time = dday[0]
    for (i = 1; i < dday.length; i++) {
        if (dday[i] > time) {
            ans.push(cnt)
            cnt = 1
            time = dday[i]
        } else {
            cnt += 1
        }
    }
    ans.push(cnt)
    return ans
}