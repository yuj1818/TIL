N, K, B = map(int, input().split())
missing = set(int(input()) for _ in range(B))
cnt = [0] * (N + 1)
ans = B
for i in range(1, N + 1):
    cnt[i] = cnt[i - 1] + (1 if i in missing else 0) 
for e in range(K, N + 1):
    ans = min(ans, cnt[e] - cnt[e - K])
print(ans)
