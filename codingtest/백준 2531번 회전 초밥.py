n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]
sushi = sushi
ans, s, e = 0, 0, 0
check = [0] * (d + 1)
check[c] = 1
cnt = 1

while e < k:
    check[sushi[e]] += 1
    if check[sushi[e]] == 1:
        cnt += 1
    e += 1
    
for _ in range(n):
    if ans < cnt:
        ans = cnt
        
    check[sushi[e % n]] += 1
    
    if check[sushi[e % n]] == 1:
        cnt += 1
        
    check[sushi[s % n]] -= 1
    
    if check[sushi[s % n]] == 0:
        cnt -= 1
        
    e += 1
    s += 1
    
print(ans)