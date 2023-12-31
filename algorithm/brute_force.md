# 반복과 재귀

- 반복
    - 수행하는 작업이 완료될 때 까지 계속 반복
- 재귀
    - 주어진 문제의 해를 구하기 위해 동일하면서 더 작은 문제의 해를 이용하는 방법
    - 하나의 큰 문제를 해결할 수 있는 더 작은 문제로 쪼개고 결과들을 결합

## 반복 구조

- 초기화
    - 반복되는 명령문을 실행하기 전에 조건 검사에 사용할 변수의 초기값 설정
- 조건 검사
- 반복할 명령문 시행
- 업데이트

```jsx
def SelectionSort(A):
		n = len(A)
		
		for i in range(0, n - 1):
				minI = i
				for j in range(i + 1, n):
						if A[j] < A[minI]:
								minI = j
				A[minI], A[i] = A[i], A[minI]
```

## 재귀적 알고리즘

- 재귀적 정의는 두 부분으로 나뉜다.
- 하나 또는 그 이상의 기본 경우
    - 집합에 포함되어 있는 원소로 induction을 생성하기 위한 시드 역할
- 하나 또는 그 이상의 유도된 경우
    - 새로운 집합의 원소를 생성하기 위해 결합되어지는 방법

### 재귀 함수(recursive function)

- 함수 내부에서 직접 혹은 간접적으로 자기 자신을 호출하는 함수
- 일반적으로 재귀적 정의를 이용해서 재귀 함수를 구현
- 기본 부분과 유도부분으로 구성
- 재귀적 프로그램을 작성하는 것은 반복 구조에 비해 간결하고 이해하기 쉬움
- 함수 호출은 프로그램 메모리 구조에서 스택을 사용
    - 재귀 호출을 반복적인 스택의 사용을 의미
    - 메모리 및 속도에서 성능저하가 발생

```python
def rec_selection_sort(i, N, B):
    if i == N:
        print(B)
        return
    else:
        minI = i
        for j in range(i + 1, N):
            if B[j] < B[minI]:
                minI = j
        B[i], B[minI] = B[minI], B[i]
        rec_selection_sort(i + 1, N, B)

N = 6
B = [7, 3, 4, 8, 1, 5]
rec_selection_sort(0, N, B)
```

## 반복 VS 재귀

- 해결할 문제를 고려해서 반복이나 재귀의 방법 선택
- 재귀는 문제 해결을 위한 알고리즘 설계가 간단하고 자연스러움
    - 추상 자료형(list, tree 등)의 알고리즘은 재귀적 구현이 간단하고 자연스러운 경우가 다수
- 일반적으로, 재귀적 알고리즘은 반복 알고리즘보다 **더 많은 메모리와 연산을 필요**로 함
- **입력 값 n이 커질수록** 재귀 알고리즘은 반복에 비해 **비효율적**일 수 있음

|  | 재귀 | 반복 |
| --- | --- | --- |
| 종료 | 재귀 함수 호출이 종료되는 베이스 케이스 | 반복문의 종료 조건 |
| 수행 시간 | 느림 | 빠름 |
| 메모리 공간 | 많이 사용 | 적게 사용 |
| 소스 코드 길이 | 짧고 간결 | 길다 |
| 소스 코드 형태 | 선택 구조 | 반복 구조 |
| 무한 반복시 | 스택 오버플로우 | CPU 반복해서 점유 |

# Brute-force(완전 탐색)

- 문제를 해결하기 위한 간단하고 쉬운 접근법
- 상대적으로 빠른 시간에 문제 해결을 할 수 있음
- 문제에 포함된 자료의 크기가 작다면 유용
- 학술적 또는 교육적 목적을 위해 알고맂므의 효율성을 판단하기 위한 척도로 사용됨
- 자료들의 리스트에서 키 값을 찾기 위해 첫 번째 자료부터 비교하며 진행

```python
def SequentialSearch(A[0:n + 1], k):
		A[n] = k
		i = 0
		while A[i] != k:
				i += 1
		if i < n:
				return i
		else:
				return -1
```

## 완전 검색으로 시작하라

- 모든 경우의 수를 생성하고 테스트하기 때문에 수행 속도는 느리지만, 해답을 찾아내지 못할 확률이 작음
    - 완전 검색은 입력의 크기를 작게해서 간편하고 빠르게 답을 구하는 프로그램을 작성
- 이를 기반으로 그리디 기법이나 동적 계획법을 이용하여 효율적인 알고리즘을 찾을 수 있음
- 검정 등에서 주어진 문제를 풀 때, 우선 완전 검색으로 접근하여 해답을 도출한 후, 성능 개선을 위해 다른 알고리즘을 사용하고 해답을 확인하는 것이 바람직

### 완전 검색

- 많은 종류의 문제들이 특정 조건을 만족하는 경우나 요소를 찾는 것
- 또한, 이들은 전형적으로 순열, 조합, 그리고 부분 집합과 같은 조합적 문제들과 연관됨
- 완전 검색은 조합적 문제에 대한  brute-force 방법임

# 순열

- 서로 다른 것들 중 몇 개를 뽑아서 한 줄로 나열하는 것
- 서로 다른 n개 중 r개를 택하는 순열은 nPr로 표현
- nPr = n * (n - 1) * (n - 2) * … * (n - r + 1)
- nPn = n!
- 다수의 알고리즘 문제들은 순서화된 요소들의 집합에서 최선의 방법을 찾는 것과 관련 있음
- N개의 요소들에 대해서 n!개의 순열들이 존재

## 단순하게 순열을 생성하는 방법

- ex) {1, 2, 3}을 포함하는 모든 순열을 생성하는 함수
    - 동일한 숫자가 포함되지 않았을 때, 각 자리 수 별로 loop을 이용해 아래와 같이 구현
    
    ```python
    for i1 in range(1, 4):
    		for i2 in range(1, 4):
    				if i2 != i1:
    						for i3 in range(1, 4):
    								if i3 != i1 and i3 != i2:
    										print(i1, i2, i3)
    ```
    

## 순열 생성 방법

- 사전적 순서(Lexicographic-Order)
    - {1, 2, 3}, n = 3 인 경우 다음과 같이 생성됨
    - [1 2 3] [1 3 2] [2 1 3] [2 3 1] [3 1 2] [3 2 1]
- 최소 변경을 통한 방법
    - 각각의 순열들은 이전의 상태에서 단지 두 개의 요소들 교환을 통해 생성
    - [1 2 3] [3 2 1] [2 3 1] [2 1 3] [3 1 2] [1 3 2]
- 최소한의 변경을 통해 다음 순열을 생성하는 방법
- 재귀 호출을 통한 순열 생성
- 1, 2, 3으로 구성된 순열

```python
#가능한 것을 모두 나열
def perm( n,  k ): # p[n]을 채워서 k개의 숫자로 만드는 순열, 인덱스가 사전순으로 생성
    if n == k:
        print(p)
    else:
        for i in range(k):        # 모든 원소에 대해
            if used[i] == 0:    # 사용된 적이 없으면
                p[n] = arr[i]    # 순열에 사용
                used[i] = 1     # 사용됨으로 표시
                perm(n+1, k)
                used[i] = 0    # 다른 자리에서 사용가능

arr = [1,2,3]
p = [0]*3
used = [0]*3
perm(0, 3)
```

```python
# 순열 베이스 코드
def f(i, N):
    global p
    if i == N: #순열 완성
        print(p)
        return
    else:   #card[i]에 들어갈 숫자를 결정
        for j in range(N):
            if used[j] == 0:
                p[i] = card[j]
                used[j] = 1
                f(i+1, N)
                used[j] = 0

card = list(map(int,input().split()))
N = 6
used = [0] * N #카드의 사용유무 표시
p =[0] * 6 #카드를 늘어놓은 결과
print(f(0,6))
```

```python
# 순열 1 => 모든 숫자 나열
#      2 => n개 중 x개만 나열

#1.숫자를 모두 사용하는경우
def f(i, N):
    if i == N: #순열 완성
        print(p)
        return
    else:   #card[i]에 들어갈 숫자를 결정
        for j in range(N):
            if used[j] == 0:
                p[i] = card[j]
                used[j] = 1
                f(i+1, N)
                used[j] = 0

card = [1,2,3]
N = 3
used = [0] * N #카드의 사용유무 표시
p =[0] * N #카드를 늘어놓은 결과
print(f(0,N))

#5개중 3개만 고르는경우
def f(i, N, K): # i:이전에 고른 개수, N개에서 K개를 고르는 순열
    if i == K: #순열 완성 : K개를 모두 고른경우
        print(p)
        return
    else:   #card[i]에 들어갈 숫자를 결정
        for j in range(N):
            if used[j] == 0:
                p[i] = card[j]
                used[j] = 1
                f(i+1, N, K)
                used[j] = 0

card = [1,2,3,4,5]
N = 5
K = 3
used = [0] * N #카드의 사용유무 표시
p =[0] * K #카드를 늘어놓은 결과
f(0,N,K)
```

# 조합

- 서로 다른 n개의 원소 중 r개를 순서 없이 골라낸 것을 조합이라고 부른다.
- 조합의 수식

$$
nCr = {n!\over(n-r)!r!}, (n \geq r)
$$

$$
nCr = _{n-1}C_{r-1} + _{n-1}C_r
$$

$$
_nC_0 = 1
$$

- 재귀 호출을 이용한 조합 생성 알고리즘

```python
def comb(n, r):
		if r == 0:
				print(arr)
		elif n < r:
				return
		else:
				tr[r - 1] = an[n - 1]
				comb(n - 1, r - 1)
				comb(n - 1, r)
```

![Untitled](https://github.com/yuj1818/TIL/assets/95585314/b762c1db-3cd0-4a15-862e-dcd37af8be57)

```python
# 10개의 원소 중 3개를 고르는 조합
for i in range(0, 8):
		for j in range(i + 1, 9):
				for k in range(j + 1, 10):
						f(a[i], a[j], a[k])
```

```python
# n개에서 r개를 고르는 조합(재귀)
def nCr(n, r, s):
		if r == 0:
				print(*comb)
		else:
				for i in range(s, n - r + 1):
						comb[r - 1] = A[i]
						nCr(n, r - 1, i + 1)
```