function permutation(arr, n) {
    let result = [];
    const visited = Array(arr.length).fill(false);
    
    function dfs(cur) {
        if (cur.length === n) {
            result.push([...cur])
            return
        }
        for (let i = 0; i < arr.length; i++) {
            if (!visited[i]) {
                visited[i] = true;
                cur.push(arr[i]);
                dfs(cur);
                cur.pop();
                visited[i] = false
            }
        }
    }
    
    dfs([]);
    
    return result;
}

function solution(k, dungeons) {
    const n = dungeons.length;
    let ans = 0;
    permutation(dungeons, n).forEach((perm) => {
        let hp = k;
        let cnt = 0;
        perm.forEach((dungeon) => {
            const [need, cost] = dungeon;
            if (hp < need) {
                return
            } else {
                hp -= cost
                cnt++
            }
        })
        if (cnt > ans) ans = cnt
    })
    return ans
}