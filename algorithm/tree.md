# 트리

## 트리의 개념

- cycle이 없는 무향 연결 그래프
    - 두 노드 사이에는 유일한 경로가 존재
    - 각 노드는 최대 하나의 부모 노드가 존재
    - 각 노드는 자식 노드가 없거나 하나 이상이 존재
- 비선형 구조
- 원소들 간에 1:n 관계를 가지는 자료 구조
- 원소들 간에 계층 관계를 가지는 계층형 자료 구조
- 상위 원소에서 하위 원소로 내려가면서 확장되는 트리(나무) 모양의 구조

## 트리의 정의

- 한 개 이상의 노드로 이루어진 유한 집합이며 다음 조건을 만족
    - 노드 중 최상위 노드를 루트(root)라 한다.
    - 나머지 노드들은 n(≥ 0)개의 분리 집합 T1, …, TN으로 분리될 수 있다.
- 이들 T1, …, TN은 각각 하나의 트리가 되며(재귀적 정의) 루트의 부 트리(subtree)라 한다.

<img src="https://github.com/yuj1818/TIL/assets/95585314/35cad706-9125-437e-842a-085260b855ca" />

## 트리의 용어 정리

<img src="https://github.com/yuj1818/TIL/assets/95585314/fe4c8fd7-7dbd-4a40-9f75-48e33926a4cb" />

- 노드(node)
    - 트리의 원소
    - 트리 T의 노드
        - A, B, C, D, E, F, G, H, I, J, K
- 간선(edge)
    - 노드를 연결하는 선
    - 부모 노드와 자식 노드를 연결
- 루트 노드(root node)
    - 트리의 시작 노드
    - 트리 T의 루트 노드 - A
- 형제 노드(sibling node)
    - 같은 부모 노드의 자식 노드들
    - B, C, D는 형제 노드
- 조상 노드
    - 간선을 따라 루트 노드까지 이르는 경로에 있는 모든 노드들
    - K의 조상 노드: F, B, A
- 서브 트리(subtree)
    - 부모 노드와 연결된 간선을 끊었을 때 생성되는 트리
- 자손 노드
    - 서브 트리에 있는 하위 레벨의 노드들
    - B의 자손 노드 - E, F, K
- 차수(degree)
    - 노드의 차수 : 노드에 연결된 자식 노드의 수
        - B의 차수 = 2, C의 차수 = 1
    - 트리의 차수 : 트리에 있는 노드의 차수 중에서 가장 큰 값
        - 트리  T의 차수 = 3
    - 단말 노드(리프 노드) : 차수가 0인 노드. 자식 노드가 없는 노드
- 높이
    - 노드의 높이 : 루트에서 노드에 이르는 간선의 수. 노드의 레벨
        - B의 높이 = 1, F의 높이 = 2
    - 트리의 높이: 트리에 있는 노드의 높이 중에서 가장 큰 값. 최대 레벨
        - 트리 T의 높이 = 3

## 이진 트리

- 모든 노드들이 2개의 서브트리를 갖는 특별한 형태의 트리
- 각 노드가 자식 노드를 최대한 2개 까지만 가질 수 있는 트리
    - 왼쪽 자식 노드(left child node)
    - 오른쪽 자식 노드(right child node)
- 이진 트리의 예

<img src="https://github.com/yuj1818/TIL/assets/95585314/83962c52-05be-430a-b185-a83aa70e0f08" />

### 이진 트리의 특성

- 레벨 i에서의 노드의 최대 개수는 2^i개
- 높이가 h인 이진 트리가 가질 수 있는 노드의 최소 개수는 (h + 1)개가 되며, 최대 개수는 (2^(h + 1) - 1)개가 된다.

### 포화 이진 트리(Full Binary Tree)

- 모든 레벨에 노드가 포화상태로 차 있는 이진 트리
- 높이가 h일 때, 최대의 노드 개수인 (2^(h + 1) - 1)의 노드를 가진 이진 트리
- 루트를 1번으로 하여 2^(h + 1) - 1 까지 정해진 위치에 대한 노드 번호를 가짐

<img src="https://github.com/yuj1818/TIL/assets/95585314/ce8c0630-8736-46c1-b9ce-dfb22211973e" />

### 완전 이진 트리(Complete Binary Tree)

- 높이가 h이고 노드 수가 n개일 때(단. 2^h ≤ n ≤ 2^(h + 1) - 1), 포화 이진 트리의 노드 번호 1번부터 n번까지 빈자리가 없는 이진 트리

<img src="https://github.com/yuj1818/TIL/assets/95585314/c2d664b4-9edb-41b4-b2af-d6cb96e35198" />

### 편향 이진 트리(Skewed Binary Tree)

- 높이 h에 대한 최소 개수의 노드를 가지면서 한쪽 방향의 자식 노드만을 가진 이진 트리
    - 왼쪽 편향 이진 트리
    - 오른쪽 편향 이진 트리

<img src="https://github.com/yuj1818/TIL/assets/95585314/ed157527-8114-4519-a639-3fa89097a75b" />

### 이진트리 - 순회(traversal)

- 순회(traveral) : 트리의 노드들을 체계적으로 방문하는 것
- 순회(traversal)란 트리의 각 노드를 중복되지 않게 전부 방문(visit)하는 것을 말하는데 트리는 비 선형 구조이기 때문에 선형구조에서와 같이 선후 연결 관계를 알 수 없다.
- 따라서 특별한 방법이 필요
- 3가지의 기본적인 순회 방법
    - 전위 순회(preoerder traversal) : VLR
        - 부모 노드 방문 후, 자식 노드를 좌, 우 순서로 방문
    - 중위 순회(inorder traversal) : LVR
        - 왼쪽 자식 노드, 부모 노드, 오른쪽 자식 노드 순으로 방문
    - 후위 순회(postorder traversal) : LRV
        - 자식 노드를 좌, 우 순서로 방문한 후, 부모 노드로 방문

**전위 순회(preordr traversal)**

- 수행 방법
    1. 현재 노드 n을 방문하여 처리 → V
    2. 현재 노드 n의 왼쪽 서브트리로 이동 → L
    3. 현재 노드 n의 오른쪽 서브트리로 이동 → R

```python
def preorder_traverse(T):
		if T:
				visit(T)
				preorder_traverse(T.left)
			  preorder_traverse(T.right)
```

- 전위 순회 예
    - A →  B → D → E → H → I → C → F → G

<img src="https://github.com/yuj1818/TIL/assets/95585314/b0b4d9b4-953e-4f74-9060-e741d89cc744" />

**중위 순회(inorder traversal)**

- 수행 방법
    1. 현재 노드 n의 왼쪽 서브트리로 이동 : L
    2. 현재 노드 n을 방문하여 처리 : V
    3. 현재 노드 n의 오른쪽 서브트리로 이동 : R

```python
def inorder_traversal(T):
		if T:
				inorder_traverse(T.left)
				visit(T)
				inorder_traverse(T.right)
```

- 중위 순회의 예
    - D → B → H → E → I → A → F → C → G

<img src="https://github.com/yuj1818/TIL/assets/95585314/b0b4d9b4-953e-4f74-9060-e741d89cc744" />

**후위 순회(postorder traversal)**

- 수행 방법
    1. 현재 노드 n의 왼쪽 서브트리로 이동 : L
    2. 현재 노드 n의 오른쪽 서브트리로 이동 : R
    3. 현재 노드 n을 방문하여 처리 : V

```python
def postorder_traversal(T):
		if T:
				postorder_traversal(T.left)
				postorder_traversal(T.right)
				visit(T)
```

- 후위 순회의 예
    - D → H → I → E → B → F → G → C → A

<img src="https://github.com/yuj1818/TIL/assets/95585314/b0b4d9b4-953e-4f74-9060-e741d89cc744" />

**순회 연습 문제**

<img src="https://github.com/yuj1818/TIL/assets/95585314/0ae79f2a-15b5-4872-be6e-5da8bef11f74" />

- 전위 순회
    - A B D H I E J C F K G L M
- 중위 순회
    - H D I B J E A F K C L G M
- 후위 순회
    - H I D J E B K F L M G C A

### 이진트리의 표현

- 배열의 이용한 이진 트리의 표현
    - 이진 트리에 각 노드 번호를 다음과 같이 부여
    - 루트의 번호를 1로 함
    - 레벨 n에 있는 노드에 대하여 왼쪽부터 오른쪽으로 2^n 부터 2^(n + 1) - 1 까지 번호를 차례로 부여
    - 노드 번호를 배열의 인덱스로 사용
    - 높이가 h인 이진 트리를 위한 배열의 크기는?
        - 레벨 i의 최대 노드 수: 2 ^ i
        - 따라서 2 ^ (h + 1) - 1

<img src="https://github.com/yuj1818/TIL/assets/95585314/1a9d4f2a-7c75-4206-baa8-bd9ee70762a7" />

- 노드 번호의 성질
    - 노드 번호가 i인 부모 노드 번호? i / 2
    - 노드 번호가 i인 노드의 왼쪽 자식 노드 번호? 2 * i
    - 노드 번호가 i이 노드의 오른쪽 자식 노드 번호? 2 * i + 1
    - 레벨 n의 노드 번호 시작 번호는? 2^n

### [참고] 이진 트리의 저장

- 부모 번호를 인덱스로 자식 번호를 저장

```python
N = 4    # 간선 개수
l = [1, 2, 1, 3, 3, 4, 3, 5]   # 부모 자식 순
c1 = [0] * 6
c2 = [0] * 6
for i in range(N):
		p, c = l[i * 2], l[i * 2 + 1]
		if c1[p] == 0:
				c1[p] = c
		else:
				c2[p] = c
```

- 자식 번호를 인덱스로 부모 번호를 저장

```python
N = 4    # 간선 개수
l = [1, 2, 1, 3, 3, 4, 3, 5]   # 부모 자식 순
par = [0] * 6
for i in range(N):
		p, c = l[i * 2], l[i * 2 + 1]
		par[c] = p
```

- 루트 찾기, 조상 찾기

<img src="https://github.com/yuj1818/TIL/assets/95585314/693024bd-9d73-44f7-9048-c77ad99e56f8" />

```python
c = 5
while a[c] != 0:
		c = a[c]
		anc.append(c)
root = c
```

### 이진트리의 표현 - 배열

- 배열을 이용한 이진 트리의 표현의 단점
    - 편향 이진 트리의 경우에 사용하지 않는 배열 원소에 대한 메모리 공간 낭비 발생
    - 트리의 중간에 새로운 노드를 삽입하거나 기존의 노드를 삭제할 경우 배열 크기 변경 어려워 비효율적
```python
        # 문제 풀이용
        arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6]
        # arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]
        
        # 이진 트리 생성
        nodes = [[] for _ in range(14)]
        for i in range(0, len(arr), 2):
            parentNode = arr[i]
            childNode = arr[i + 1]
            nodes[parentNode].append(childNode)
        
        # 자식이 없다는 걸 표현하기 위해 None 을 삽입
        for li in nodes:
            for _ in range(len(li), 2):
                li.append(None)
        
        # 전위 순회
        def preorder(nodeNum):
            if nodeNum == None:
                return
            # print(nodeNum, end=' ')
            preorder(nodes[nodeNum][0])
            # print(nodeNum, end=' ')
            preorder(nodes[nodeNum][1])
            # print(nodeNum, end=' ')
        
        preorder(1)
        ```

### 트리의 표현 - 연결리스트

- 배열을 이용한 이진 트리의 표현의 단점을 보완하기 위해 연결리스트를 이용하여 트리를 표현할 수 있다.
- 연결 자료구조를 이용한 이진트리의 표현
    - 이진 트리의 모든 노드는 최대 2개의 자식 노드를 가지므로 일정ㅎ나 구조의 단순 연결 리스트 노드를 사용하여 구현

<img src="https://github.com/yuj1818/TIL/assets/95585314/5af0f791-0e6a-4eb9-89c8-5e67649748f6" />

- 완전 이진 트리의 연결 리스트 표현

<img src="https://github.com/yuj1818/TIL/assets/95585314/7de59e87-699d-4ce8-aab9-8b2910c74294" />

```python
        # 정석 개발
        arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]
        
        class TreeNode:
            def __init__(self, value):
                self.value = value
                self.left = None
                self.right = None
        
            def insert(self, child):
                if(not self.left):
                    self.left = child
                    return
                if(not self.right):
                    self.right = child
                    return
                return
        
            def preorder(self):
                if self != None:
                    print(self.value, end=' ')
                    if self.left:
                        self.left.preorder()
                    if self.right:
                        self.right.preorder()
        
            # 중위 순회
            def inorder(self):
                if self != None:
                    if self.left:
                        self.left.inorder()
                    print(self.value, end=' ')
                    if self.right:
                        self.right.inorder()
        
            # 후위 순회
            def postorder(self):
                if self != None:
                    if self.left:
                        self.left.postorder()
                    if self.right:
                        self.right.postorder()
                    print(self.value, end=' ')
        
        # 이진 트리 만들기
        nodes = [TreeNode(i) for i in range(0, 14)]
        for i in range(0, len(arr), 2):
            parentNode = arr[i]
            childNode = arr[i + 1]
            nodes[parentNode].insert(nodes[childNode])
        
        nodes[1].preorder()
        print()
        nodes[1].inorder()
        print()
        nodes[1].postorder()
        ```

### 연습 문제

- 첫 줄에는 트리의 정점의 총 수 V가 주어진다. 그 다음 줄에는 V - 1개 간선이 나열된다. 간선은 그것을 이루는 두 정점으로 표기된다. 간선은 항상 “부모 자식” 순서로 표기된다. 아래 예에서 두 번째 줄 처음 1 과 2는 정점 1과 2를 잇는 간선을 의미하며, 1이 부모, 2가 자식을 의미한다. 간선은 부모 정점 번화 작은 것부터 나열되고, 부모 정점이 동일하다면 자식 정점 번호가 작은 것부터 나열된다.
- 다음 이진 트리 표현에 대하여 전위 순회하여 정점의 번호를 출력하시오.
    - 정점 개수 : 13
    - 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

```python
def preorder_traversal(s):
    print(s)
    if ch1[s]:
        preorder_traversal(ch1[s])
    if ch2[s]:
        preorder_traversal(ch2[s])

V = int(input())
E = V - 1
arr = list(map(int, input().split()))
# 부모를 인덱스로 자식 저장
ch1 = [0] * (V + 1)
ch2 = [0] * (V + 1)
for i in range(E):
    p, c = arr[i * 2], arr[i * 2 + 1]
    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c
preorder_traversal(1)
```

## 수식 트리

- 수식을 표현하는 이진 트리
- 수식 이진 트리(Expression Binary Tree)라고 부르기도 함
- 연산자는 루트 노드이거나 가지 노드
- 피연산자는 모두 잎 노드

### 수식 트리의 순회

- 중위 순회
    - A / B * C * D + E
- 후위 순회
    - A B / C * D * E +
- 전위 순회
    - \+ * * / A B C D E

<img src="https://github.com/yuj1818/TIL/assets/95585314/f8c366bd-95af-4168-bb6d-1638b4531429" />

## 이진 탐색 트리

- 탐색작업을 효율적으로 하기 위한 자료 구조
- 모든 원소는 서로 다른 유일한 키를 갖는다
- key(왼쪽 서브트리) < key(루트 노드) < key(오른쪽 서브트리)
- 왼쪽 서브트리와 오른쪽 서브트리도 이진 탐색 트리다
- 중위 순회하면 오름차순으로 정렬된 값을 얻을 수 있다.
    
    <img src="https://github.com/yuj1818/TIL/assets/95585314/eede4c08-ad5a-47c1-bedc-b61d24b2e2d2" />
    

### 이진 탐색 트리 - 연산

- 탐색 연산
    - 루트에서 시작
    - 탐색할 키 값 x를 루트 노드의 키 값과 비교
        - (키 값 x = 루트 노드의 키 값)인 경우 : 원하는 원소를 찾았으므로 탐색 연산 성공
        - (키 값 x < 루트 노드의 키 값)인 경우 : 루트 노드의 왼쪽 서브트리에 대해서 탐색연산 수행
        - (키 값 x > 루트 노드의 키 값)인 경우 : 루트 노드의 오른쪽 서브트리에 대해서 탐색연산 수행
    - 서브트리에 대해서 순환적으로 탐색 연산을 반복
    - 예) 13 탐색
    
    <img src="https://github.com/yuj1818/TIL/assets/95585314/d718f797-0c14-4544-8bde-fd4f27082c82" />
    
- 삽입 연산
    - 먼저 탐색 연산을 수행
        - 삽입할 원소와 같은 원소가 트리에 있으면 삽입할 수 없으므로, 같은 원소가 트리에 있는지 탐색하여 확인
        - 탐색에서 탐색 실패가 결정되는 위치가 삽입 위치가 됨
    - 탐색 실패한 위치에 원소를 삽입
    - 예) 5 삽입
    
    <img src="https://github.com/yuj1818/TIL/assets/95585314/0e01a6f0-fcda-4570-a3a5-aa0b3789b76d" />
    

### 이진 탐색 트리 - 성능

- 탐색, 삽입, 삭제 시간은 트리의 높이 만큼 시간이 걸린다.
    - O(h), h : BST의 깊이
- 평균의 경우
    - 이진 트리가 균형적으로 생성되어 있는 경우
    - O(log n)
- 최악의 경우
    - 한쪽으로 치우친 경사 이진트리의 경우
    - O(n)
    - 순차탐색과 시간복잡도가 같다.
- 검색 알고리즘의 비교
    - 배열에서의 순차 검색 : O(N)
    - 정렬된 배열에서의 순차 검색 : O(N)
    - 정렬된 배열에서의 이진 탐색 : O(logN)
        - 고정 배열 크기와 삽입, 삭제 시 추가 연산 필요
    - 이진 탐색트리에서의 평균 : O(logN)
        - 최악의 경우 : O(N)
        - 완전 이진 트리 또는 균형 트리로 바꿀 수 있다면 최악의 경우를 없앨 수 있음
            - 새로운 원소를 삽입할 때 삽입 시간을 줄임
            - 평균과 최악의 시간이 같다. O(logn)
    - 해쉬 검색 : O(1)
        - 추가 저장 공간 필요

### 이진 탐색 트리 - 연산 연습

- 삭제 연산
    - 다음 트리에 대하여 13, 12, 9를 차례로 삭제해 보자
    
    <img src="https://github.com/yuj1818/TIL/assets/95585314/4de70c39-fad5-4270-9267-8e673dbd6767" />
```python
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if key < root.value:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.value == key:
        return root
    if root.value < key:
        return search(root.right, key)
    return search(root.left, key)

def inorder_traversal(root):
    if root:
        print(root.value, end=" ")
        inorder_traversal(root.left)
        inorder_traversal(root.right)

def find_min_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete_node(root, key):
    if root is None:
        return root

    if key < root.value:
        root.left = delete_node(root.left, key)
    elif key > root.value:
        root.right = delete_node(root.right, key)
    else:
        # 삭제하려는 노드가 리프 노드이거나 하나의 자식만 가지는 경우
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # 삭제하려는 노드가 두 개의 자식을 가지는 경우
        # 1. 왼쪽 서브 트리의 가장 큰 값
        # 2. 오른쪽 서브 트리의 가장 작은 값
        # 두 가지가 가능한 후보
        temp = find_min_node(root.right)
        root.value = temp.value
        root.right = delete_node(root.right, temp.value)

    return root

# 이진 탐색 트리 생성 및 사용 예제
arr = [8, 3, 10, 2, 5, 14]
root = insert(None, arr[0])
for el in arr[1:]:
    insert(root, el)

# 특정 값 검색 예제
key_to_search = 10
result = search(root, key_to_search)
if result:
    print(f"{key_to_search}를 찾았습니다.")
else:
    print(f"{key_to_search}를 찾을 수 없습니다.")

# 노드 삭제 예제
key_to_delete = 5
inorder_traversal(root)
print()
root = delete_node(root, key_to_delete)
inorder_traversal(root)

test = 1
```
    

## [참고] 힙(heap)

- 완전 이진 트리에 있는 노드 중에서 키 값이 가장 큰 노드나 키 값이 가장 작은 노드를 찾기 위해서 만든 자료 구조
- 최대 힙(max heap)
    - 키 값이 가장 큰 노드를 찾기 위한 완전 이진 트리
    - {부모 노드의 키 값 > 자식 노드의 키 값}
    - 루트 노드 : 키 값이 가장 큰 노드
- 최소 힙(min heap)
    - 키 값이 가장 작은 노드를 찾기 위한 완전 이진 트리
    - {부모 노드의 키 값 < 자식 노드의 키 값}
    - 루트 노드 : 키 값이 가장 작은 노드
- 힙의 예
    - 최대 힙
    
    <img src="https://github.com/yuj1818/TIL/assets/95585314/3a5e578d-65de-4370-9e52-3a084478e3b4" />
    
    - 최소 힙
    
    <img src="https://github.com/yuj1818/TIL/assets/95585314/738743df-5a52-4f0a-b4e8-d25232306e53" />
    

### 힙 연산 - 삽입

예) 23 삽입

<img src="https://github.com/yuj1818/TIL/assets/95585314/d74810b4-cd4f-4eb7-88ce-2b0394e54021" />

### 힙 연산 - 삭제

- 힙에서는 루트 노드의 원소만을 삭제할 수 있다.
- 루트 노드의 원소를 삭제하여 반환
- 힙의 종류에 따라 최대값 또는 최소값을 구할 수 있다.

<img src="https://github.com/yuj1818/TIL/assets/95585314/1dc8bc86-3f98-4a64-8d9a-23d9fd49cf6a" />

```python
from heapq import heappush, heappop

arr = [20, 15, 19, 4, 13, 11]

# 최소힙
min_heap = []

for el in arr:
    heappush(min_heap, el)

print(min_heap)  # [4, 13, 11, 20, 15, 19] 출력

while len(min_heap) > 0:
    print(heappop(min_heap), end=' ')
print()

# 최대힙
max_heap = []
for el in arr:
    heappush(max_heap, -el)

print(max_heap)  # [-20, -15, -19, -4, -13, -11] 출력

while len(max_heap) > 0:
    print(-heappop(max_heap), end=' ')
```

- 힙의 활용
    - 특별한 큐의 구현
        - 우선 순위 큐를 구현하는 가장 효율적인 방법
        - 노드 하나의 추가/삭제가 시간 복잡도가 O(logN)이고 최대값/최소값을 O(1)에 구할 수 있음
    - 정렬