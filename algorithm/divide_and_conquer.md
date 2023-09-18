# 분할 정복(Divide and Conquer)

## 설계 전략

- 분할(Divide)
    - 해결할 문제를 여러 개의 작은 부분으로 나눔
        - 나눌 수 없을 때 까지
        - 문제를 쉽게 해결할 수 있을 때까지
- 정복(Conquer)
    - 나눈 작은 문제를 각각 해결
- 통합(Combine)
    - 해결된 해답을 모음

### Top-down approach

![Untitled](https://github.com/yuj1818/TIL/assets/95585314/bc5782d1-5d42-4a57-94dd-615b3458872f)

## 분할 정복 예시 - 거듭제곱

```python
def recursive_power(x, n):
		if n == 1:
				return x
		if n % 2 == 0:
				y = recursive_power(x, n/2)
				return y * y
		else:
				y = recursive_power(x, (n-1)/2)
				return y * y * x
```

## 병합 정렬

- 여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식
- 자료를 최소 단위의 문제까지 나눈 후에 차례대로 정렬하여 최종 결과를 얻어냄
    - top-down 방식
- 시간 복잡도
    - O(n log n)

### 병합 정렬 과정

- {69, 10, 30, 2, 16, 8, 31, 22}를 병합 정렬하는 과정
    - 분할 - 전체 자료 집합에 대하여, 최소 크기의 부분 집합이 될 때까지 분할 작업 계속
    
    ![Untitled 1](https://github.com/yuj1818/TIL/assets/95585314/86d1ccea-05cc-4331-971b-4915e8211840)
    
    ```python
    def merge_sort(m)):
    		if len(m) == 1:
    				return m
    		left = []
    		right = []
    		middle = len(m) // 2
    		for x in m[:middle]:
    				left.append(x)
    		for x in m[middle:]:
    				right.append(x)
    		left = merge_sort(left)
    		right = merge_sort(right)
    		
    		return merge(left, right)    # 하나의 정렬된 리스트로 반환
    ```
    
    - 병합 - 2개의 부분 집합을 정렬하면서 하나의 집합으로 병합
        - 8개의 부분 집합이 1개로 병합될 때까지 반복
    
    ![Untitled 2](https://github.com/yuj1818/TIL/assets/95585314/498ff374-537a-47f8-a0d0-ffc86299543d)
    
    ```python
    def merge(left, right):
    		result = []
    		while len(left) > 0 or len(right) > 0:
    				if len(left) > 0 and len(right) > 0:
    						if left[0] <= right[0]:    # 더 작은 것을 result 배열에 넣음
    								result.append(left.pop(0))
    						else:
    								result.append(right.pop(0))
    				elif len(left) > 0:    # 남은 데이터 모두 넣음
    						result.append(left.pop(0))
    				elif len(right) > 0:
    						result.append(right.pop(0))
    		return result
    ```
    

## 퀵 정렬

- 주어진 배열을 두 개로 분할하고, 각각을 정렬
- 평균적으로 시간 복잡도가 굉장히 좋음(O(n log n))
- 큰 데이터를 다룰 때 좋음
- 단점 - 역순 정렬 등 최악의 경우 O(N^2) ⇒ 특수 케이스

| 퀵 정렬 | 병합 정렬 |
| --- | --- |
| 분할 할 때, 기준 아이템(pivot item)으 중심으로, 기준 보다 작은 것은 왼편, 큰 것은 오른편에 위치시킴 | 그냥 두 부분으로 나눔 |
| 부분 정렬 후, 병합 과정 필요X |  부분 정렬 후, 병합 후처리 작업 필요 |

### 퀵 정렬 과정 - Hoare-Partition 알고리즘

- 피봇 선택
    - 왼쪽 끝, 오른쪽 끝, 임의의 세 개 값 중에 중간 값
- 피봇 값들보다 큰 값은 오른쪽, 작은 값들은 왼쪽 집합에 위치 시킴
    
    ![Untitled 3](https://github.com/yuj1818/TIL/assets/95585314/aa51718b-75c1-4624-81c1-3ae14a0a78ae)
    
    - i는 큰 값, j는 작은 값을 찾음
    
    ![Untitled 4](https://github.com/yuj1818/TIL/assets/95585314/657c78da-75e1-451c-afbb-bed95fa1cabe)
    
    - i, j 위치 바꿈
    - i, j가 교차될 때 까지 위의 과정 반복
- 피봇을 두 집합의 가운데에 위치 시킴
    - i와 j가 교차되면 j가 위치한 값과 피봇의 위치 변경
    
    ![Untitled 5](https://github.com/yuj1818/TIL/assets/95585314/ef0cae90-ef6c-4daf-a8fa-de2a72b10945)
    

```python
def partition(l, r):
		p = A[l]
		i = l
		j = r
		while i <= j:
				while i <= j and A[i] <= p:
						i += 1
				while i <= j and A[j] >= p:
						j -= 1
				if i < j:
						A[i], A[j] = A[j], A[i]
		A[l], A[j] = A[j], A[l]
		return j

def quick_sort(left, right):
		if left >= right:
				return
		pivot = partition(left, right)
		quick_sort(left, pivot - 1)
		quick_sort(pivot + 1, right)

A = [3, 2, 4, 6, 9, 1, 8, 7, 5]
quick_sort(0, len(arr) - 1)
print(arr)
```

### 퀵 정렬 과정 - Lomuto partition 알고리즘

```python
def partition(A, p, r):
		x = A[r]
		i = p - 1
		
		for j in range(p, r):
				if A[j] <= x:
						i += 1
						A[i], A[j] = A[j], A[i]
		A[i + 1], A[r] = A[r], A[i + 1]
		return i + 1

def quick_sort(A, l, r):
		if l < r:
				pivot = partition(A, l, r)
				quick_sort(A, l, pivot - 1)
				quick_sort(A, pivot + 1, right)

quick_sort(A, 0, len(A) - 1)
print(arr)
```

[https://ldgeao99.tistory.com/376](https://ldgeao99.tistory.com/376) 참고

## [⭐⭐⭐이진 검색(Binary Search)⭐⭐⭐](./search.md#⭐⭐이진-검색(Binary-Search)⭐⭐)

- 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
    - 목적 키를 찾을 때 까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위를 반으로 줄여가면서 보다 빠르게 검색을 수행
- 이진 검색을 하기 위해서는 **자료가 정렬된 상태**여야 함
- 시간 복잡도: O(logN)

### 이진 검색 과정

1. 자료의 중앙에 있는 원소를 고름
2. 중앙 원소의 값과 찾고자하는 목표 값 비교
3. 목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해 재검색 수행, 크다면 오른쪽 반에 대해 재검색 수행
4. 찾고자 하는 값을 찾을 때 까지 1~3의 과정 반복

```python
# loop
def binarySearch(a, N, key):
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == key:
            return True
        elif a[mid] > key:
            end = mid - 1
        else:
            start = mid + 1
    return False

arr = [2, 4, 7, 9, 11, 19, 23]

print(binarySearch(arr, len(arr), 7))   # 검색 성공, True 반환
print(binarySearch(arr, len(arr), 20))  # 검색 실패, False 반환
```

```python
# 재귀
def binarySearch2(a, low, high, key):
    if low > high:  # 검색 실패
        return False
    else:
        mid = (low + high) // 2
        if key == a[mid]:
            return True
        elif key < a[mid]:
            return binarySearch2(a, low, mid - 1, key)
        elif a[mid] < key:
            return binarySearch2(a, mid + 1, high, key)

arr = [2, 4, 7, 9, 11, 19, 23]

print(binarySearch2(arr, 0, len(arr), 7))   # 검색 성공, True 반환
print(binarySearch2(arr, 0, len(arr), 20))  # 검색 실패, False 반환
```

## 분할 정복의 활용

- 병합 정렬은 외부 정렬의 기본이 되는 정렬 알고리즘
- Multi-core CPU나 다수의 프로세서에서 정렬 알고리즘을 병렬화하기 위해 병합 정렬 알고리즘이 활용됨
- 퀵 정렬은 매우 큰 입력 데이터에 대해서 좋은 성능을 보임