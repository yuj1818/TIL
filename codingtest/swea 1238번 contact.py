def bfs(s):
    q = list()
    q.append(s)
    visited[s] = visited.get(s, 1)
    while q:
        t = q.pop(0)
        for w in adj_l.get(t, []):
            if not visited.get(w, 0):
                q.append(w)
                visited[w] = visited.get(t, 0) + 1

for tc in range(1, 11):
    E, S = map(int, input().split())
    arr = list(map(int, input().split()))
    adj_l = dict()
    visited = dict()
    for i in range(E // 2):
        adj_l[arr[i * 2]] = adj_l.get(arr[i * 2], [])
        adj_l[arr[i * 2]].append(arr[i * 2 + 1])
    bfs(S)
    answer = sorted(visited.items(), key=lambda x: (x[1], x[0]), reverse=True)[0][0]
    print(f'#{tc} {answer}')