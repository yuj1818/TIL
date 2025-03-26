# 기타 알고리즘
## LIS(Longest Increasing Subsequence)

- 원소가 n개 있는 배열의 일부 원소로 만든 부분 수열 중, 각 원소가 이전 인덱스의 원소보다 크다는 조건을 만족하고, 그 길이가 최대인 부분 수열
- 예)
    - [1, 5, 4, 2, 3, 8, 6, 7, 9, 3, 4, 5]
    - LIS ⇒ [1, 2, 3, 6, 7, 9]

### 1) DP

- 시간 복잡도: O(N^2)

```python
dp = [1] * n
for i in range(n):
	for j in range(i):
		if arr[i] > arr[j]:
			dp[i] = max(dp[i], dp[j] + 1)
```

### 2) Binary Search

- 시간 복잡도: O(NlogN)

```python
def bs(s, e, t):
    while s < e:
        mid = (s + e) // 2
        if t > seq[mid]: s = mid + 1
        else: e = mid
    return e

seq = [a[0]]
for i in range(1, n):
    if a[i] > seq[-1]:
        seq.append(a[i])
    else:
        ni = bs(0, len(seq) - 1, a[i])
        seq[ni] = a[i]
print(len(seq)
```