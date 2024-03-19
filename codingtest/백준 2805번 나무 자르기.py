N, M = map(int, input().split())
trees = list(map(int, input().split()))
    
def bs(trees, low, high, key):
  if low > high:
    return high
  else:
    mid = (low + high) // 2
    total = sum([x-mid for x in trees if x-mid > 0])
    if total < key:
      return bs(trees, low, mid - 1, key)
    else:
      return bs(trees, mid + 1, high, key)
    
ans = bs(trees, 1, max(trees), M)
print(ans)
