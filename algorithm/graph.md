# 그래프

- 아이템(사물 또는 추상적 개념)들과 이들 사이의 연결 관계를 표현
- 정점(Vertex)들의 집합과 이들을 연결하는 간선(Edge)들의 집합으로 구성된 자료 구조
    - V개의 정점을 가지는 그래프는 최대 V(V-1)/2 간선이 가능(V : 정점의 개수, E : 그래프에 포함된 간선의 개수)
- 선형 자료구조나 트리 자료구조로 표현하기 어려운 N:N 관계를 가지는 원소들을 표현하기에 용이

## 그래프 유형

- 무향 그래프(Undirected Graph)
- 유향 그래프(Directed Graph)
- 가중치 그래프(Weighted Graph)
- 사이클 없는 방향 그래프(DAG, Directed Acyclic Graph)
- 완전 그래프
    - 정점들에 대해 가능한 모든 간선들을 가진 그래프
- 부분 그래프
    - 원래 그래프에서 일부의 정점이나 간선을 제외한 그래프

## 인접 정점

- 인접(Adjacency)
    - 두 개의 정점에 간선이 존재(연결됨)하면 서로 인접해 있다고 함
    - 완전 그래프에 속한 임의의 두 정점들은 모두 인접

## 그래프 경로

- 경로란 간선들을 순서대로 나열한 것
    - 간선들 - (0, 2), (2, 4), (4, 6)
    - 정점들 - 0, 2, 4, 6
- 경로 중 한 정점을 최대한 한번만 지나는 경로를 **단순경로**라고 함
    - 예) 0 - 2 - 4 - 6, 0 - 1 - 6
- 시작한 정점에서 끝나는 경로를 사이클(Cycle)이라고 함
    - 예) 1 - 3 - 5 - 1

## 그래프 표현

- 간선의 정보를 저장하는 방식, 메모리나 성능을 고려해서 결정

### 인접 행렬(Adjacent matrix)

- V x V 크기의 2차원 배열을 이용해서 간선 정보를 저장
- 배열의 배열(포인터 배열)
- 두 정점을 연결하는 간선의 유무를 행렬로 표현
    - V x V 정방 행렬
    - 행 번호와 열 번호는 그래프의 정점에 대응
    - 두 정점이 인접되어 있으면 1, 그렇지 않으면 0으로 표현
    - 무향 그래프
        - i번째 행의 합 = i번째 열의 합 = Vi의 차수
    - 유향 그래프
        - 행 i의 합 = Vi의 진출 차수
        - 열 i의 합 = Vi의 진입 차수

### 인접 리스트(Adjacent List)

- 각 정점마다 해당 정점으로 나가는 간선의 정보를 저장
- 하나의 정점에 대한 인접 정점들을 각각 노드로 하는 연결 리스트로 저장

### 간선의 배열

- 간선(시작 정점, 끝 정점)을 배열에 연속적으로 저장

## 그래프 순회(탐색)

- 비선형 구조인 그래프로 표현된 모든 자료(정점)를 빠짐없이 탐색하는 것을 의미

### [깊이 우선 탐색(Depth First Search, DFS)](./stack.md#dfs깊이-우선-탐색)

- 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더 이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회 방법
- 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 후입선출 구조의 스택 사용

#### 스택

- 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료 구조
- 선형 구조: 자료 간의 관계가 1대 1의 관계를 가짐
    - 비선형 구조: 자료 간의 관계가 1대 N의 관계를 가짐(ex: 트리)
- 마지막에 삽입한 자료를 가장 먼저 꺼냄
    - 후입선출(LIFO, Last-In-First-Out)
- 스택을 구현하기 위해 필요한 저장소와 연산
    - 자료를 선형으로 저장할 저장소
        - C언어에서는 배열 사용
        - 저장소 자체를 스택이라고 부르기도 함
        - 스택에서 마지막 삽입된 원소의 위치를 top이라 함
    - 연산
        
        
        | push | 저장소에 자료를 삽입(저장) |
        | --- | --- |
        | pop | 저장소에서 자료를 꺼냄(삽입한 자료의 역순) |
        | isEmpty | 스택이 공백인지 아닌지를 확인 |
        | peek | 스택의 top에 있는 item(원소)을 반환하는 연산 |
    
    ```python
    # 스택의 push, pop 알고리즘
    
    def push(stack, x):
    	top += 1
    	if top >= len(stack):
    		print('error overflow!')
    	else:
    		S[top] = x
    
    def pop(stack):
    	if top < 0:
    		print('error underflow!')
    	else:
    		top -= 1
    		return stack[top + 1]
    ```
    

```python
# DFS 알고리즘 - 재귀

def dfs_recursive(g, v):
	visited[v] = 1

	for w in adj[v]:
		if not visited[w]:
			dfs_recursive(g, w)
```

```python
# DFS 알고리즘 - 반복

def dfs(s):
	stack.append(s)
	while stack:
		v = s.pop()
		if not visited[v]:
			visited[v] = 1
			for w in adj[v]:
				if not visited[w]:
					stack.append(w)

stack = []
visited = []
dfs(v)
```

### [너비 우선 탐색(Breadth First Search, BFS)](./queue.md#⭐⭐bfsbreadth-frist-search⭐⭐)

- 너비 우선 탐색은 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후에, 방문했떤 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식
- 인접한 정점들에 대해 탐색을 한 후, 차례로 다시 너비우선탐색을 진행해야 하므로, 선입선출 형태의 자료구조인 큐를 활용

#### 큐

- 스택과 마찬가지로 삽입과 삭제의 위치가 제한적인 자료구조
    - 큐의 뒤에서는 삽입만 하고, 큐의 앞에서는 삭제만 이루어지는 구조
- 큐에 삽입한 순서대로 원소가 저장되어, 가장 먼저 삽입된 원소는 가장 먼저 삭제됨
    - 선입선출(FIFO: First In First Out)
- 큐의 구조

![Untitled](https://github.com/yuj1818/TIL/assets/95585314/3fa55d38-d427-485a-b0b3-109e450b9388)

- 큐의 기본 연산
    - 삽입: enQueue
    - 삭제: deQueue
    
    ```python
    def isEmpty():
    	if front == rear:
    		return True
    	else:
    		return False
    
    def isFull():
    	if rear == n - 1: #n: 배열의 크기, n-1: 배열의 마지막 인덱스
    		return True
    	else:
    		return False
    
    def enQueue(Q, x):
    	if isFull():
    		print('Queue Full')
    	else:
    		rear += 1
    		Q[rear] = x
    
    def deQueue(Q):
    	if isEmpty():
    		print('Queue Empty')
    	else:
    		front += 1
    		return Q[front]
    ```
    

```python
# G: 그래프, v: 탐색 시작점
def bfs(G, v):
	queue = []
	queue.append(v)
	visited[v] = 1
	while queue:
		t = queue.pop(0)
		for w in adj[t]:
			if not visited[w]:
				queue.append(w)
				visited[w] = 1
```

## 서로소 집합(Disjoint-sets)

- 상호배타 집합을 표현하는 방법
    - 연결 리스트
        - 같은 집합의 원소들은 하나의 연결리스트로 관리
        - 연결리스트의 맨 앞의 원소를 집합의 대표 원소로 삼음
        - 각 원소는 집합의 대표 원소를 가리키는 링크를 가짐
        
        ![Untitled 1](https://github.com/yuj1818/TIL/assets/95585314/e71b2f2c-b349-4a15-affe-298b98828c3d)
        
    - 트리
        - 하나의 집합을 하나의 트리로 표현
        - 자식 노드가 부모 노드를 가리키면 루트 노드가 대표자가 됨
        
        ![Untitled 2](https://github.com/yuj1818/TIL/assets/95585314/c827201b-9577-4600-963a-720a704b04ea)
        
- 상호배타 집합 연산
    - Make-Set(x)
        - 유일한 멤버 x를 포함하는 새로운 집합을 생성하는 연산
    - Find-Set(x)
        - x를 포함하는 집합을 찾는 연산
    - Union(x, y)
        - x와 y를 포함하는 두 집합을 통합하는 연산
    
    ```python
    # 0 ~ 9
    # make set - 집합을 만들어 주는 과정
    # 각 요소가 가리키는 값이 부모
    parent = [i for i in range(10)]
    
    # find-set
    def find_set(x):
        if parent[x] == x:
            return x
    
        # return find_set(parent[x])
    
        # 경로 압축
        parent[x] = find_set(parent[x])
        return parent[x]
    
    # union
    def union(x, y):
        # 1. 이미 같은 집합인 지 체크
        x = find_set(x)
        y = find_set(y)
    
        # 대표자가 같으니, 같은 집합이다.
        if x == y:
            print("싸이클 발생")
            return
    
        # 2. 다른 집합이라면, 같은 대표자로 수정
        if x < y:
            parent[y] = x
        else:
            parent[x] = y
    
    union(0, 1)
    
    union(2, 3)
    
    union(1, 3)
    
    # 이미 같은 집합에 속해 있는 원소를 한 번 더 union
    # 싸이클이 발생
    union(0, 2)
    
    # 대표자 검색
    print(find_set(2))
    print(find_set(3))
    
    # 같은 그룹인 지 판별
    t_x = 0
    t_y = 2
    
    if find_set(t_x) == find_set(t_y):
        print(f"{t_x} 와 {t_y} 는 같은 집합에 속해 있습니다.")
    else:
        print(f"{t_x} 와 {t_y} 는 다른 집합에 속해 있습니다.")
    ```
    
    - 연산의 효율을 높이는 방법
        - Rank를 이용한 Union
            - 각 노드는 자신을 루트로 하는 subtree의 높이를 랭크Rank라는 이름으로 저장
            - 두 집합을 합칠 대, rank가 낮은 집합을 rank가 높은 집합에 붙임
            
            ![Untitled 3](https://github.com/yuj1818/TIL/assets/95585314/f1c7caa4-d7ab-4ba3-be57-1d117565a116)
            
            ```python
            # 트리의 rank 도 따로 저장하여 효율적으로 알고리즘을 구현한 방법
            class UnionFind:
                def __init__(self, n):
                    self.parent = [i for i in range(n)]  # 각 원소의 부모를 자신으로 초기화
                    self.rank = [0] * n  # 트리의 깊이(랭크)를   저장
            
                def find_set(self, x):
                    if self.parent[x] == x:
                        return x
            
                    return self.find_set(self.parent[x])
            
                    # 경로 압축 (path compression)을 통해 부모를 루트로 설정
                    # self.parent[x] = self.find_set(self.parent[x])
                    # return self.parent[x]
            
                def union(self, x, y):
                    root_x = self.find_set(x)
                    root_y = self.find_set(y)
            
                    if root_x != root_y:
                        # 랭크를 비교하여 더 높은 트리의 루트를 부모로 설정
                        if self.rank[root_x] < self.rank[root_y]:
                            self.parent[root_x] = root_y
                        elif self.rank[root_x] > self.rank[root_y]:
                            self.parent[root_y] = root_x
                        else:
                            self.parent[root_y] = root_x
                            self.rank[root_x] += 1
            
            # 예제 사용법
            n = 5  # 원소의 개수
            uf = UnionFind(n)
            
            # 원소 0과 원소 1을 합침
            uf.union(0, 1)
            
            # 원소 2와 원소 3을 합침
            uf.union(2, 3)
            
            # uf.union(3, 4)
            
            target_x = 2
            target_y = 4
            
            # 원소 1과 원소 2가 같은 집합에 속해 있는지 확인
            if uf.find_set(target_x) == uf.find_set(target_y):
                print(f"원소 {target_x}과 원소 {target_y}는 같은 집합에 속해 있습니다.")
            else:
                print(f"원소 {target_x}과 원소 {target_y}는 다른 집합에 속해 있습니다.")
            ```
            
        - Path compression
            - Fink-set을 행하는 과정에서 만나는 모든 노드들이 직접 root를 가리키도록 포인터를 바꾸어 줌
            
            ![Untitled 4](https://github.com/yuj1818/TIL/assets/95585314/cd4c1588-a5b5-4808-a109-1702062ab72e)

## 최소 신장 트리(MST, Minimum Spanning Tree)

- 무방향 가중치 그래프에서 신장 트리를 구성하는 간선들의 가중치의 합이 최소인 신장 트리
- 그래프에서 최소 비용 문제
    - 모든 정점을 연결하는 간선들의 가중치의 합이 최소가 되는 트리
    - 두 정점 사이의 최소 비용의 경로 찾기
- 신장 트리
    - n개의 정점으로 이루어진 그래프에서 n개의 정점과 n-1개의 간선으로 이루어진 트리
    - 모든 정점을 연결
    - 사이클이 존재하지 않는 부분 그래프
        - 간선의 개수: n - 1개
    - 한 그래프에서 여러 개의 신장 트리가 나올 수 있음

### Prim 알고리즘

- 하나의 정점에서 연결된 간선들 중에 하나씩 선택하면서 MST를 만들어 가는 방식
    - 임의 정점을 하나 선택해서 시작
    - 선택한 정점과 인접하는 정점들 중의 최소 비용의 간선이 존재하는 정점을 선택
    - 모든 정점이 선택될 때 까지 1, 2 과정을 반복
- 서로소인 2개의 집합(2 disjoint-sets) 정보를 유지
    - 트리 정점들(tree vertices) - MST를 만들기 위해 선택된 정점들
    - 비트리 정점들(nontree vertices) - 선택 되지 않은 정점들

![Untitled](https://github.com/yuj1818/TIL/assets/95585314/935b323b-0ab5-4f48-8621-bf170d59b82f)

```python
'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

import heapq

def prim(start):
    heap = []
    # MST 에 포함되었는 지 여부
    MST = [0] * V

    # 가중치, 정점 정보
    heapq.heappush(heap, (0, start))
    # 누적합 저장
    sum_weight = 0

    while heap:
        # 가장 적은 가중치를 가진 정점을 꺼냄
        weight, v = heapq.heappop(heap)

        # 이미 방문한 노드라면 pass
        if MST[v]:
            continue

        # 방문 체크
        MST[v] = 1
        
        # 누적합 추가
        sum_weight += weight

        # 갈 수 있는 노드들을 체크
        for next in range(V):
            # 갈 수 없거나 이미 방문했다면 pass
            if graph[v][next] == 0 or MST[next]:
                continue

            heapq.heappush(heap, (graph[v][next], next))

    return sum_weight

V, E = map(int, input().split())
# 인접행렬
graph = [[0] * V for _ in range(V)]

for _ in range(E):
    f, t, w = map(int, input().split())
    graph[f][t] = w
    graph[t][f] = w     # 무방향 그래프

result = prim(0)
print(f'최소 비용 = {result}')
```

### KRUSKAL 알고리즘

- 간선을 하나씩 선택해서 MST를 찾는 알고리즘
    - 최초, 모든 간선을 가중치에 따라 오름차순으로 정렬
    - 가중치가 가장 낮은 간선부터 선택하면서 트리를 증가시킴
        - 사이클이 존재하면 다음으로 가중치가 낮은 간선 선택
    - n - 1개의 간선이 선택될 때 까지 두 번째 단계를 반복

```python
'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

# 모든 간선들 중 비용이 가장 적은 걸 우선으로 고르자
V, E = map(int, input().split())
edge = []
for _ in range(E):
    f, t, w = map(int, input().split())
    edge.append([f, t, w])
# w 를 기준으로 정렬
edge.sort(key=lambda x: x[2])

# 사이클 발생 여부를 union find 로 해결
parents = [i for i in range(V)]

def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return

    if x < y:
        parents[y] = x
    else:
        parents[x] = y

# 현재 방문한 정점 수
cnt = 0
sum_weight = 0
for f, t, w in edge:
    # 싸이클이 발생하지 않는다면
    if find_set(f) != find_set(t):
        cnt += 1
        sum_weight += w
        union(f, t)
        # MST 구성이 끝나면
        if cnt == V - 1:
            break
print(f'최소 비용 = {sum_weight}')
```

## 최단 경로

- 간선의 가중치가 있는 그래프에서 두 정점 사이의 경로들 중에 간선의 가중치의 합이 최소인 경로
- 하나의 시작 정점에서 끝 정점까지의 최단 경로
    - 다익스트라(dijkstra) 알고리즘
        - 음의 가중치를 허용하지 않음
    - 벨만-포드(Bellman-Ford) 알고리즘
        - 음의 가중치 허용
- 모든 정점들에 대한 최단 경로
    - 플로이드-워샬(Floyd-Warshall)알고리즘

### Dijkstra 알고리즘

- 시작 정점에서 거리가 최소의 정점을 선택해 나가면서 최단 경로를 구하는 방식
- 시작정점(s)에서 끝정점(t)까지의 최단 경로에 정점 x가 존재
- 이때, 최단 경로는 s에서 x까지의 최단 경로와 x에서 t까지의 최단 경로로 구성됨
- 탐욕 기법을 사용한 알고리즘으로 MST의 프림 알고리즘과 유사

![Untitled 1](https://github.com/yuj1818/TIL/assets/95585314/ccbe56ee-a17b-45f5-946a-8685f2c3bd18)

```python
'''
6 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
'''

# 최단 거리 문제 유형
# 1. 특정 지점 -> 도착 지점까지의 최단 거리 : 다익스트라
# 2. 가중치에 음수가 포함되어 있네 ? : 밸만포드
# 3. 여러 지점 -> 여러 지점까지의 최단 거리
#       - 여러 지점 모두 다익스트라 돌리기 -> 시간 복잡도 계산 잘해야함
#       - 플로이드-워샬

# 내가 갈 수 있는 경로 중 누적거리가 제일 짧은 것부터 고르자!
import heapq

# 입력
n, m = map(int, input().split())
# 인접리스트
graph = [[] for i in range(n)]
for _ in range(m):
    f, t, w = map(int, input().split())
    graph[f].append([t, w])

# 1. 누적 거리를 계속 저장
INF = int(1e9) # 최대값으로 1억 - 대충 엄청 큰 수
distance = [INF] * n

def dijkstra(start):
    # 2. 우선순위 큐
    pq = []
    # 출발점 초기화
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        # 현재 시점에서
        # 누적 거리가 가장 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(pq)

        # 이미 방문한 지점 + 누적 거리가 더 짧게 방문한 적이 있다면 pass
        if distance[now] < dist:
            continue

        # 인접 노드를 확인
        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            # next_node 로 가기 위한 누적 거리
            new_cost = dist + cost

            # 누적 거리가 기존보다 크네 ?
            if distance[next_node] <= new_cost:
                continue

            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))

dijkstra(0)
print(distance)
```

### 플로이드-워셜 알고리즘(**Floyd-Warshall)**

- 모든 지점에서 다른 모든 지점까지의 최단 경로를 구해야 하는 경우 사용
- ‘거쳐가는 노드’ 기준으로 알고리즘 수행
- 점화식

$$
D_{ab}=min(D_{ab},D_{ak}+D_{kb})
$$

- 과정
    - 그래프의 노드와 간선에 따라 최단 거리 테이블 갱신
        
        ![image.png](https://github.com/user-attachments/assets/6a7063bf-07c5-437c-8f74-18f1f35f413f)
        
    - [1, …, n]번 노드를 거쳐 가는 경우의 최단 거리 테이블 갱신
        
        ![1번 노드를 거쳐 가는 경우의 최단 거리 테이블 갱신](https://github.com/user-attachments/assets/fbbf2c25-74ff-4480-8228-2d3f463a5ba9)
        
        | 1번 노드를 거쳐 가는 경우의 최단 거리 테이블 갱신
        
        ![2번 노드를 거쳐 가는 경우의 최단 거리 테이블 갱신(n번까지 계속 갱신)](https://github.com/user-attachments/assets/954057d4-c221-481b-a3a7-419081b7380e)
        
        | 2번 노드를 거쳐 가는 경우의 최단 거리 테이블 갱신(n번까지 계속 갱신)
        

```python
# input 예시
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2

INF = int(1e9)

n = 4  # 노드 개수
m = 7  # 간선 개수

graph = [[INF] * (n - 1) for _ in range(n+1)]

for a in range(1, n + 1):
	for b in range(1, n + 1):
		if a == b:
			graph[a][b] = 0
			
for _ in range(m):
	a, b, c = map(int, input().split())
	graph[a][b] = c
	
for k in range(1, n + 1):
	for a in range(1, n + 1):
		for b in range(1, n + 1):
			graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
```

### 벨만 포드 알고리즘(Bellman-Ford)

- 특정 출발 노드에서 다른 **모든 노드**까지의 최단 경로 탐색
- 음수 가중치가 있을 때 사용
- 음수 사이클 존재의 여부를 알 수 있음
- 과정
    - 시작 정점에서 다른 정점들까지의 거리를 무한대로 초기화
        
        ![image.png](https://github.com/user-attachments/assets/a4a8842c-1653-44b2-bb39-febcd21ef474)
        
    - 시작 정점에서 갈 수 있는 정점들(2 ~ 5)을 탐색하며 최단 거리 갱신(V - 1번 반복)
        
        ![image.png](https://github.com/user-attachments/assets/244b2cb4-8bc2-4cc2-b062-cd364adbe57f)
        
    - V-1번 반복 후에도 거리가 갱신되는 경우가 있다면 음수 사이클이 존재한다는 의미

```python
INF = int(1e9)
# 노드의 개수, 간선의 개수
n, m = map(int, input().split())
# 모든 간선에 대한 정보
edges = []
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

def bf(start):
    distance[start] = 0
    # n - 1번 반복
    for i in range(n):
        모든 간선 확인
        for j in range(m):
		        now, nxt, cost = edges[j]
            if distance[now] != INF and distance[nxt] > distance[now] + cost:
                distance[nxt] = distance[now] + cost
                # n번째에서도 값이 갱신되면 음수 사이클이 존재
                if i == n - 1:
                    return True
    return False

negative_cycle = bf(1)

if negative_cycle:
    print("-1")
else:
    # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리를 출력
    for i in range(2, n + 1):
        # 도달할 수 없는 경우, -1을 출력
        if distance[i] == INF:
            print("-1")
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(distance[i])
```