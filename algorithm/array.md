# 배열

- **일정한 자료형**의 변수들을 하나의 이름으로 열거하여 사용하는 자료 구조

## 배열의 필요성

- 프로그램 내에서 여러 개의 변수가 필요할 때, 일일이 다른 변수명을 이용하여 자료에 접근하는 것은 매우 비효율적일 수 있다.
- 배열을 사용하면 하나의 선언을 통해서 둘 이상의 변수를 선언할 수 있다.
- 단순히 다수의 변수 선언을 의미하는 것이 아니라, 다수의 변수로는 하기 힘든 작업을 배열을 활용해 쉽게 할 수 있다.

## 1차원 배열

### 1차원 배열의 선언

- 별도의 선언 방법이 없으면 변수에 처음 값을 할당할 때 생성
- 이름: 프로그램에서 사용할 배열의 이름
    - Arr = list()
    - Arr = []
    - Arr = [1, 2, 3]
    - Arr = [0] * 10

### 1차원 배열의 접근

- Arr[idx] = num
    - 배열 Arr의 idx번 원소에 num을 저장하라

### 배열 활용 예제: Gravity

- 상자들이 쌓여있는 방이 있다. 방이 오른쪽으로 90도 회전하여 상자들이 중력의 영향을 받아 낙하한다고 할 때, 낙차가 가장 큰 상자를 구하여 그 낙차를 리턴하는 프로그램을 작성하시오.
- 중력은 회전이 완료된 후 적용된다.
- 상자들은 모두 한쪽 벽면에 붙여진 상태로 쌓여 2차원의 형태를 이루며 벽에서 떨어져서 쌓인 상자는 없다.
- 방의 가로길이는 항상 100이며, 세로 길이도 항상 100이다.
- 즉, 상자는 최소 0, 최대 100 높이로 쌓을 수 있다.
- 예시)

<img src="https://github.com/yuj1818/TIL/assets/95585314/1f4719b0-869f-4636-8d78-317aaa05aed7" />

```python
N = int(input())
heights = list(map(int, input().split()))
height = 0
max_fall = 0
for i in range(N-1):
    height = heights[i]
    cnt = 0
    for h in heights[i + 1:]:
        if h >= height:
            cnt += 1
    max_fall = max(max_fall, N - i - cnt - 1)

print(max_fall)
```

## 2차원 배열

- 1차원 리스트를 묶어 놓은 리스트
- 2차원 이상의 다차원 리스트는 차원에 따라 index를 선언
- 2차원 리스트의 선언
    - 세로 길이(행의 개수), 가로 길이(열의 개수)를 필요로 함
- Python에서는 데이터 초기화를 통해 변수 선언과 초기화가 가능
- ex) arr = [[0, 1, 2, 3], [4, 5, 6, 7]] ⇒ 2행 4열의 2차원 리스트

### ⭐ 배열 순회 ⭐

- n X m 배열의 n * m 개의 모든 원소를 빠짐 없이 조사하는 바업ㅂ

### 행 우선 순회

```python
# i 행의 좌표
# j 열의 좌표
for i in range(n):
	for j in range(m):
		func(Array[i][j])    # 필요한 연산 수행
```

### 열 우선 순회

```python
# i 행의 좌표
# j 열의 좌표
for j in range(m):
	for i in range(n):
		func(Array[i][j])    # 필요한 연산 수행
```

### 지그재그 순회

<img src="https://github.com/yuj1818/TIL/assets/95585314/ae9e9636-c7e1-4685-91ad-4dcdfd223a07" />

```python
# i 행의 좌표
# j 열의 좌표
for i in range(n):
	for j in range(m):
		func(Array[i][j + (m - 1 - 2 * j) * (i % 2)])    # 필요한 연산 수행
```

### ⭐⭐ 델타를 이용한 2차 배열 탐색 ⭐⭐

- 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법

```python
arr = [[0 for _ in range(N)] for _ in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for i in range(N):
    for j in range(N):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N: #유효한 인덱스면
                func(arr[ni][nj])   # 필요한 연산 수행
```

### 전치 행렬

<img src="https://github.com/yuj1818/TIL/assets/95585314/5f5cf954-d83e-4c0a-bb11-6f63b1a2bf26" />

```python
# i 행의 좌표, len(arr)
# j 열의 좌표, len(arr[0])

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # 3*3 행렬

for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
```

### 연습문제(배열 탐색)

- 5x5 2차 배열에 무작위로 25개의 숫자로 초기화 한 후, 25개의 각 요소에 대해서 그 요소와 이웃한 요소와의 차의 절댓값을 구하시오
- 예를 들어, 아래 그림에서 7 값의 이웃한 값은 2, 6, 8, 12 이며 차의 절댓값의 합은 12이다.

<img src="https://github.com/yuj1818/TIL/assets/95585314/cbf2c966-d783-4f2e-938a-cb413722e021" />

- 25개의 요소에 대해서 모두 조사하여 총합을 구하시오.
- 벽에 있는 요소는 이웃한 요소가 없을 수 있음을 주의하시오.

```python
arr = []
for i in range(5):
    arr.append([])
    for j in range(1, 6):
        arr[i].append(5 * i + j)
        
# arr
# [1,  2,  3,  4,  5]
# [6,  7,  8,  9,  10]
# [11, 12, 13, 14, 15]
# [16, 17, 18, 19, 20]
# [21, 22, 23, 24, 25]

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for i in range(5):
    for j in range(5):
        n_sum = 0
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < 5 and 0 <= nj < 5:
                n_sum += abs(arr[ni][nj] - arr[i][j])
        print(n_sum)
```