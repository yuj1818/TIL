# 백트래킹

- 여러 가지 선택지들이 존재하는 상황에서 한가지를 선택
- 선택이 이루어지면 새로운 선택지들의 집합이 생성됨
- 이런 선택을 반복하며 최종 상태에 도달
    - 올바른 선택을 계속하면 목표 상태(goal state)에 도달
- 어떤 노드의 유망성을 점검한 후에 유망(promising)하지 않다고 결정되면 그 노드의 부모로 되돌아가(backtracking) 다음 자식 노드로 감
- 어떤 노드를 방문하였을 때 그 노드를 포함한 경로가 해답이 될 수 없으면 그 노드는 유망하지 않다고 하며, 반대로 해답의 가능성이 있으면 유망하다고 함
- 가지치기(Prunning)
    - 유망하지 않는 노드가 포함되는 경로는 더 이상 고려하지 않음

## 백트래킹 알고리즘 절차

1. 상태 공간 트리의 깊이 우선 검색을 실시
2. 각 노드가 유망한지를 점검
3. 만일 그 노드가 유망하지 않으면, 그 노드의 부모 노드로 돌아가서 검색 계속

## 백트래킹과 깊이 우선 탐색과의 차이

- 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않음으로써 시도의 횟수를 줄임
    - Prunning(가지치기)
- 깊이 우선 탐색이 모든 경로를 추적하는데 비해 백트래킹은 불필요한 경로를 미리 차단
- 깊이 우선 탐색을 가하기에는 경우의 수가 너무나 많음. 즉 N!가지의 경우의 수를 가진 문제에 대해 깊이 우선 탐색을 가하면 당연히 처리 불가능
- 백트래킹 알고리즘을 적용하면 일반적으로 경우의 수가 줄어들지만 이 역시 최악의 경우에는 여전히 지수함수 시간(Exponential Time)을 요하므로 처리 불가능

## 백트래킹 예제

### 일반 백트래킹 알고리즘

```python
def checknode(v):
	if promising(v):    # v가 유망한가
		if there is a solution at v:
			wrtie the solution
		else:
			for w in v의 자식 노드:
				checknode(w)
```

### 상태 공간 트리

```python
# {1, 2, 3} 집합에서 3개의 숫자를 선택
# 이미 사용한 숫자는 사용하지 않도록

arr= [1, 2, 3]
path = [0] * 3

def backtracking(cnt):
	# 기저 조건
	# 숫자 3개를 골랐을 때 종료
	if cnt == 3:
		return
	for num in arr:
		# 가지치기 - 중복된 숫자 제거
		if num in path:
			continue
		# 들어가기 전 로직 - 경로 저장 
		path[cnt] = num
		# 다음 재귀 호출
		backtracking(cnt + 1)
		# 돌아와서 할 로직
		path[cnt] = 0

backtracking(0)
```

```python
# {1, 2, 4, 5, 6, 7, 8, 9, 10} 집합에서 합이 10이 되는 부분 집합을 모두 출력

arr= [i for i in range(1, 11)]
stack = []

def backtracking():
	# 기저 조건
	# 합이 10이면 종료
	if sum(stack) == 10:
		print(*stack)
		return
	# 가지치기 - 합이 이미 10보다 크면 검색 종료
	elif sum(stack) > 10:
		return
	for num in arr:
		# 가지치기 - 중복된 숫자 제거
		if num in stack:
			continue
		# 들어가기 전 로직 - 경로 저장
		stack.append(num)
		# 다음 재귀 호출
		backtracking()
		# 돌아와서 할 로직
		stack.pop()

backtracking()
```