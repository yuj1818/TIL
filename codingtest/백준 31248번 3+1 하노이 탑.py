def hanoi(i, s, e, v):
    global cnt
    
    if i == 0:
        return
    else:
        hanoi(i - 1, s, v, e)
        ans.append(f"{'ABC'[s]} {'ABC'[e]}")
        hanoi(i - 1, v, e, s)
        
    cnt += 1

n = int(input())
cnt = 0
ans = []
cur = 0

while n >= 2:
    hanoi(n - 2, cur, 2 - cur, 1)
    ans.append(f"{'ABC'[cur]} B")
    ans.append(f"{'ABC'[cur]} D")
    ans.append('B D')
    cnt += 3
    n -= 2
    cur = 2 - cur
    
if n == 1:
    ans.append(f"{'ABC'[cur]} D")
    cnt += 1
    
print(cnt)
print('\n'.join(ans))