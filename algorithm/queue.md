# Day11_20230817

생성일: 2023년 8월 17일 오전 8:56

# 큐(Queue)

- 스택과 마찬가지로 삽입과 삭제의 위치가 제한적인 자료 구조
- 큐의 뒤에서는 삽입만 하고, 큐의 앞에서는 삭제만 이루어지는 구조
- 선입선출구조(FIFO: First In First Out)
    - 큐에 삽입한 순서대로 원소가 저장되어, 가장 먼저 삽입(First In)된 원소는 가장 먼저 삭제(First Out)된다.

## 큐의 구조 및 기본 연산

<img src="https://github.com/yuj1818/TIL/assets/95585314/cd9895cf-ba83-414e-b5cd-e60d72dc9641" />

- 삽입: enQueue
- 삭제: deQueue

## 큐의 주요 연산

| 연산 | 기능 |
| --- | --- |
| enQueue(item) | 큐의 뒤쪽(rear 다음)에 원소를 삽입하는 연산 |
| deQueue() | 큐의 앞쪽(front)에서 원소를 삭제하고 반환하는 연산 |
| createQueue() | 공백 상태의 큐를 생성하는 연산 |
| isEmpty() | 큐가 공백상태인지를 확인하는 연산 |
| isFull() | 큐가 포화상태인지를 확인하는 연산 |
| Qpeek() | 큐의 앞쪽(front)에서 원소를 삭제 없이 반환하는 연산 |

1) 공백 큐 생성: createQueue()

<img src="https://github.com/yuj1818/TIL/assets/95585314/ef809c57-239a-4940-8783-ce0477cf8210" />

3) 원소 A, B 삽입: enQueue(A), enQueue(B)

<img src="https://github.com/yuj1818/TIL/assets/95585314/b3a45f27-ab2b-45cb-96cf-b4753e4b46f8" />

4) 원소 반환/삭제: deQueue()

<img src="https://github.com/yuj1818/TIL/assets/95585314/27c0f893-7ac4-45c6-b7c4-188913f9f053" />

## 선형 큐의 구현

- 1차원 배열을 이용한 큐
    - 큐의 크기 = 배열의 크기
    - front : 저장된 첫 번째 원소의 인덱스
    - rear : 저장된 마지막 원소의 인덱스
- 상태 표현
    - 초기 상태 : front = rear = -1
    - 공백 상태 : front == rear
    - 포화 상태 : rear == n - 1 (n: 배열의 크기, n - 1: 배열의 마지막 인덱스)

### 초기 공백 큐 생성

- 크기 n인 1차원 배열 생성
- front와 rear를 -1으로 초기화

### 삽입 : enQueue(item)

- 마지막 원소 뒤에 새로운 원소를 삽입하기 위해
    
    1) rear 값을 하나 증가시켜 새로운 원소를 삽입할 자리를 마련
    
    2) 그 인덱스에 해당하는 배열원소 Q[rear]에 item을 저장
    
    ```python
    def enQueue(item):
        global rear
        if isFull(): print("Queue_Full")
        else:
            rear += 1
            Q[rear] = item
    ```
    

### 삭제 : deQueue()

- 가장 앞에 있는 원소를 삭제하기 위해
    
    1) front 값을 하나 증가시켜 큐에 남아있게 될 첫 번째 원소 이동
    
    2) 새로운 첫 번째 원소를 리턴함으로써 삭제와 동일한 기능
    
    ```python
    def deQueue():
        if isEmpty(): print("Queue_Empty")
        else:
            front += 1
            return Q[front]
    ```
    

### 공백상태 및 포화상태 검사 : isEmpty(), isFull()

- 공백상태: front == rear
- 포화상태: rear == n - 1

```python
def isEmpty():
    return front == rear

def isFull():
    return rear == len(Q) - 1
```

### 검색 : Qpeek()

- 가장 앞에 있는 원소를 검색하여 반환하는 연산
- 현재 front의 한자리 뒤(front + 1)에 있는 원소, 즉 큐의 첫 번째에 있는 원소를 반환

```python
def Qpeek():
    if isEmpty(): print("Queue_Empty")
    else: return Q[front+1]
```

### 연습문제1

- 세 개의 데이터 1, 2, 3 을 차례로 큐에 삽입
- 큐에서 세 개의 데이터를 차례로 꺼내서 출력

```python
def enQueue(item):
    global rear
    if isFull(): print("Queue_Full")
    else:
        rear += 1
        Q[rear] = item

def deQueue():
    global front
    if isEmpty(): print("Queue_Empty")
    else:
        front += 1
        return Q[front]

def isEmpty():
    return front == rear

def isFull():
    return rear == len(Q) - 1

Q = [0]*3
front = -1
rear = -1
enQueue(1)
print(Q)    #[1, 0, 0]
enQueue(2)
print(Q)    #[1, 2, 0]
enQueue(3)
print(Q)    #[1, 2, 3]
print(deQueue())    # 1
print(deQueue())    # 2
print(deQueue())    # 3
```

### 선형 큐 이용시의 문제점

- 잘못된 포화상태 인식
    - 선형 큐를 이용하여 원소의 삽입과 삭제를 계속할 경우, 배열의 앞부분에 활용할 수 있는 공간이 있음에도 불구하고, rear=n-1인 상태. 즉, 포화상태로 인식하여 더 이상의 삽입을 수행하지 않게 됨

<img src="https://github.com/yuj1818/TIL/assets/95585314/fe0e9c71-eb26-4778-aaab-997ad5c942cf" />

- 해결 방법1
    - 매 연산이 이루어질 때마다 저장된 원소들을 배열의 앞부분으로 모두 이동시킴
    - 원소 이동에 많은 시간이 소요되어 큐의 효율성이 급격히 떨어짐

<img src="https://github.com/yuj1818/TIL/assets/95585314/1643b633-45ad-46b3-ac13-756caae1feaa" />

- 해결 방법2
    - 1차원 배열을 사용하되, 논리적으로는 배열의 처음과 끝이 연결되어 원형 형태의 큐를 이런다고 가정하고 사용

## 원형 큐의 구현

### 원형 큐의 논리적 구조

<img src="https://github.com/yuj1818/TIL/assets/95585314/8945efae-57c7-403f-a284-626ac95acf54" />

- 초기 공백 상태
    - front = rear = 0
- Index의 순환
    - front와 rear의 위치가 배열의 마지막 인덱스인 n - 1를 가리킨 후, 그 다음에는 논리적 순환을 이루어 배열의 처음 인덱스인 0으로 이동해야 함
    - 이를 위해 나머지 연산자 mod를 사용
- front 변수
    - 공백 상태와 포화 상태 구분을 쉽게 하기 위해 front가 있는 자리는 사용하지 않고 항상 빈자리로 둠
- 삽입 위치 및 삭제 위치
    
    
    |  | 삽입 위치 |  삭제 위치 |
    | --- | --- | --- |
    | 선형 큐 | rear = rear + 1 | front = front + 1 |
    | 원형 큐 | rear = (rear + 1) % n | front = (front + 1) % n |

### 초기 공백 큐 생성

- 크기 n인 1차원 배열 생성
- front와 rear를 0으로 초기화

### 공백 상태 및 포화 상태 검사 : isEmpty(), isFull()

- 공백 상태 : front == rear
- 포화 상태 : 삽입할 rear의 다음 위치 == 현재 front
    - (rear + 1) % n == front

```python
def isEmpty():
    return front == rear

def isFull():
    return (rear + 1) % len(Q) == front
```

### 삽입 : enQueue(item)

- 마지막 원소 뒤에 새로운 원소를 삽입하기 위해
    
    1) rear값을 조정하여 새로운 원소를 삽입할 자리를 마련
    
        rear = (rear + 1) % n
    
    2) 그 인덱스에 해당하는 배열 원소 Q[rear]에 item 저장
    

```python
def enQueue(item):
    global rear
    if isFull():
        print("Queue_Full")
    else:
        rear = (rear + 1) % len(Q)
        Q[rear] = item
```

### 삭제 : deQueue(), delete()

- 가장 앞에 있는 원소를 삭제하기 위해
    
    1) front 값을 조정하여 삭제할 자리를 준비
    
    2) 새로운 front 원소를 리턴 함으로써 삭제와 동일한 기능
    

```python
def deQueue():
    global front
    if isEmpty():
        print("Queue_Empty")
    else:
        front = (front + 1) % len(Q)
        return Q[front]
```

## 우선순위 큐(Priority Queue)

- 우선순위를 가진 항목들을 저장하는 큐
- FIFO 순서가 아니라 우선순위가 높은 순서대로 먼저 나가게 된다
- 우선순위 큐의 적용 분야
    - 시뮬레이션 시스템
    - 운영체제의 태스크 스케줄링
    - 네트워크 트래픽 제어

### 우선순위 큐의 기본 연산

- 우선순위 큐의 기본 연산
    - 삽입: enQueue
    - 삭제: deQueue

<img src="https://github.com/yuj1818/TIL/assets/95585314/4f9c5fa2-8bd1-4899-b5f0-01ef7c22a684" />

### 우선순위 큐의 구현

- 배열을 이용한 우선순위 큐
    - 배열을 이용하여 자료 저장
    - 원소를 삽입하는 과정에서 우선순위를 비교하여 적절한 위치에 삽입하는 구조
    - 가장 앞에 최고 우선순위의 원소가 위치하게 됨
    - 문제점
        - 배열을 사용하므로, 삽입이나 삭제 연산이 일어날 때, 원소의 재배치 발생
        - 이에 소요되는 시간이나 메모리 낭비가 큼
- 리스트를 이용한 우선순위 큐
- 내장 함수 사용 예시

```python
from queue import PriorityQueue

# q = PriorityQueue()
q = PriorityQueue(maxsize=8)

# 추가
q.put(1)
q.put(2)
q.put(3)
q.put(4)

print(q.get())
print(q.get())
print(q.get())
print(q.get())

q.put((1, '윤태우'))
q.put((2, '황호철'))
q.put((3, '원종현'))
q.put((0, '허범성'))

print(q.get()[1])
print(q.get())
print(q.get())
print(q.get())
```

## 큐의 활용 : 버퍼(Buffer)

- 데이터를 한 고셍서 다른 한 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리의 영역
- 버퍼링
    - 버퍼를 활용하는 방식 또는 버퍼를 채우는 동작을 의미

### 버퍼의 자료 구조

- 버퍼는 일반적으로 입출력 및 네트워크와 관련된 기능에서 이용됨
- 순서대로 입력/출력/전달되어야 하므로 FIFO 방식의 자료구조인 큐가 활용됨

### 예시) 키보드 버퍼

<img src="https://github.com/yuj1818/TIL/assets/95585314/eedf5d5b-f4f5-4be0-b490-6ecfcf2c28c1" />

### 연습문제2 - 마이쮸 시뮬레이션

```python
def isEmpty():
    return front == rear

def isFull():
    return (rear + 1) % len(Q) == front

def enQueue(item):
    global rear
    if isFull():
        print("Queue_Full")
    else:
        rear = (rear + 1) % len(Q)
        Q[rear] = item

def deQueue():
    global front
    if isEmpty():
        print("Queue_Empty")
    else:
        front = (front + 1) % len(Q)
        return Q[front]

Q = [0] * 100
front = 0
rear = 0
chu = 20
en_count = []
s_num = 1
enQueue(s_num)
en_count.append(1)
s_num += 1
while chu > 0:
    d = deQueue()
    chu -= en_count[d - 1]
    print(f'큐에 있는 사람 수:{abs(rear - front)}')
    print(f'현재 일인당 나눠주는 사탕 수:{en_count[d - 1]}')
    print(f'현재까지 나눠준 사탕의 수:{20 - chu}')
    enQueue(d)
    en_count[d - 1] += 1
    enQueue(s_num)
    en_count.append(1)
    s_num += 1
print(f'마지막 사탕을 가져간 사람:{d}')
```

```python
# 내장함수 사용
from collections import deque

p = 1 #줄설 '첫번째' 사람번호
q = deque() #큐
N = 20 #마이쮸 개수
m = 0 #나눠준 개수

while m < N:
    q.append((p, 1, 0))
    v, c, my = q.popleft()
    # print(f'큐에 남아있는 사람수{len(q)+1} 받아갈 사탕수{c} 나눠준 사탕수{m}')
    m += c
    q.append((v, c+1, my+c))
    p += 1 #처음 줄서는 사람 번호
print(f'마지막 사탕을 받은사람{v}')
```

## ⭐⭐BFS(Breadth Frist Search)⭐⭐

- 너비우선탐색은 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후에, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식
- 인접한 정점들에 대해 탐색을 한 후, 차례로 다시 너비 우선 탐색을 진행해야 하므로, 선입선출 형태의 자료구조인 큐를 활용

<div style="text-align : center;"><img src="https://github.com/yuj1818/TIL/assets/95585314/14e312a6-66f2-41c3-825e-05a42ade8a82" width=50% /></div>

### 예제1

```python
def BFS(G, v):                      # G: 그래프, v: 탐색 시작점
    visited = [0] * (n + 1)         # n: 정점의 개수
    queue = []                      # 큐 생성
    queue.append(v)                 # 시작점 v를 큐에 삽입
    while queue:                    # 큐가 비어있지 않은 경우
        t = queue.pop(0)            # 큐의 첫번째 원소 반환
        if not visited[t]:          # 방문되지 않은 곳이라면
            visited[t] = True       # 방문한 것으로 표시
            visit(t)                # 정점 t에서 할 일
            for i in G[t]:          # t와 연결된 모든 정점에 대해
                if not visited[i]:  # 방문되지 않은 곳이라면
                    queue.append(i) # 큐에 넣기
```
<table>
    <tr>
        <td>
            1. 초기 상태<br>
            - visited 배열 초기화<br>
            - Q 생성<br>
            - 시작점 enqueue
        </td>
        <td>
            <div style="text-align : center;">
                <img src="https://github.com/yuj1818/TIL/assets/95585314/949b681b-f2fe-4586-9b42-779953111ee7" width=80%/>
            </div>
        </td>
    <tr>
</table>

<table>
    <tr>
        <td>
            2. A점부터 시작<br>
            - dequeue: A<br>
            - A 방문<br>
            - A의 인접점 enqueue
        </td>
        <td>
            <div style="text-align : center;">
                <img src="https://github.com/yuj1818/TIL/assets/95585314/3d5caf06-e145-4f81-b6e5-a71b09948bdc" width=80%/>
            </div>
        </td>
    <tr>
</table>

<table>
    <tr>
        <td>
            3. 탐색 진행<br>
            - dequeue: B<br>
            - B 방문<br>
            - B의 인접점 enqueue
        </td>
        <td>
            <div style="text-align : center;">
                <img src="https://github.com/yuj1818/TIL/assets/95585314/b498ff42-f262-4979-93d9-4ed387987beb" width=80%/>
            </div>
        </td>
    <tr>
</table>

4. 중략(4 ~ 9)
    - C 방문
    - D 방문(G, H, I enqueue)
    - E 방문
    - F 방문
    - G 방문
    - H 방문
    
<table>
    <tr>
        <td>
            5. 탐색 진행<br>
            - dequeue: I<br>
            - I 방문<br>
            - I 인접점 enqueue
        </td>
        <td>
            <div style="text-align : center;">
                <img src="https://github.com/yuj1818/TIL/assets/95585314/5b649347-edbf-4d85-ba83-de97b6136e6f" width=80%/>
            </div>
        </td>
    <tr>
</table>

6. Q가 비었으므로 탐색 종료

### [참고]예제2

<img src="https://github.com/yuj1818/TIL/assets/95585314/4f49e11a-927c-45e9-a685-78b3bf379407" />

```python
def BFS(G, v, n):    # G: 그래프, v: 탐색 시작점
    visited = [0] * (n + 1)    # n: 정점의 개수
    queue = []    # 큐 생성
    queue.append(v)    # 시작점 v를 큐에 삽입
    visited[v] = 1
    while queue:    # 큐가 비어있지 않은 경우
        t = queue.pop(0)    # 큐의 첫번째 원소 반환
        visit(t)    # 정점 t에서 할 일
        for i in G[t]:    # t와 연결된 모든 정점에 대해
            if not visited[i]:    # 방문되지 않은 곳이라면
                queue.append(i)    # 큐에 넣기
                visited[i] = visited[n] + 1    # n으로 부터 1만큼 이동
```

### 연습문제3 - 인접 리스트 사용

- 장점
    - 메모리 낭비를 막을 수 있음
- 단점
    - 순서가 없기 때문에 비교를 위해 순회를 해야하므로 조회에서 불리
- 너비 우선 탐색 경로 출력하기. 시작 정점: 1

<img src="https://github.com/yuj1818/TIL/assets/95585314/57e6cc30-ad75-411c-a697-d1de6722dae1" />

```python
'''
테스트 케이스
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def bfs(s, V):    # 시작정점 s, 정점 개수 V
    visited = [0] * (V+1)    # visited 생성
    q = []    # 큐 생성
    q.append(s)    # 시작점 enqueue
    visited[s] = 1    # 시작점 방문 표시
    while q:    # 큐에 정점이 남아있으면 front != rear
        t = q.pop(0)    # dequeue
        print(t)    # 방문한 정점에서 할 일
        # 인접한 정점 중 enqueue 되지 않은 정점 w가 있으면
        # w enqueue, 방문하였음을 표시
        for w in adj_l[t]:
            if not visited[w]:
                q.append(w)
                visited[w] = visited[t] + 1

V, E = map(int, input().split())
arr = list(map(int, input().split()))
# 인접 리스트
adj_l = [[] for _ in range(V + 1)]
for i in range(E):
    v1, v2 = arr[i * 2], arr[i * 2 + 1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)    # 방향이 없는 경우

bfs(1, 7)

'''
1
2
3
4
5
7
6
'''
```

### 예제3 - 인접 행렬 사용

- 장점
    - 작성하기 편리함
    - 조회가 빠름
- 단점
    - 메모리의 낭비가 심하다

```python
'''
테스트 케이스
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def bfs(s, V):    # 시작정점 s, 정점 개수 V
    visited = [0] * (V+1)    # visited 생성
    q = []    # 큐 생성
    q.append(s)    # 시작점 enqueue
    visited[s] = 1    # 시작점 방문 표시
    while q:    # 큐에 정점이 남아있으면 front != rear
        t = q.pop(0)    # dequeue
        print(t)    # 방문한 정점에서 할 일
        # 인접한 정점 중 enqueue 되지 않은 정점 w가 있으면
        # w enqueue, 방문하였음을 표시
        for w in range(1, V + 1):
            if adj_m[t][w] and not visited[w]:
                q.append(w)
                visited[w] = visited[t] + 1

V, E = map(int, input().split())
arr = list(map(int, input().split()))
# 인접 행렬
adj_m = [[0]*(V + 1) for _ in range(V + 1)]
for i in range(E):
    v1, v2 = arr[i * 2], arr[i * 2 + 1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1

bfs(1, 7)

'''
1
2
3
4
5
7
6
'''
```