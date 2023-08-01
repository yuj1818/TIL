# 정렬

- 2개 이상의 자료를 특정 기준에 의해 작은 값부터 큰 값, 혹은 그 반대의 순서대로 재배열하는 것
- 키
    - 자료를 정렬하는 기준이 되는 특정 값

## 정렬의 종류

- 버블 정렬
- 카운팅 정렬
- 선택 정렬
- **퀵 정렬** ❗
- 삽입 정렬
- 병합 정렬

### 버블 정렬

- 인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식
- 과정
    - 첫 번째 원소부터 인접한 원소끼리 계속 자리를 교환하면서 맨 마지막 자리까지 이동
    - 한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬 됨
    - 교환하며 자리를 이동하는 모습이 물 위에 올라오는 거품 모양과 같다고 하여 버블 정렬이라고 한다.
- 시간 복잡도
    - O(n^2)
- 배열을 활용한 버블 정렬

```python
def BuubleSort(a, N):
	for i in range(N-1, 0, -1):
		for j in range(0, i):
			if a[j] > a[j + 1]:
				a[j], a[j + 1] = a[j + 1], a[j]
```

### 카운팅 정렬(Counting Sort)

- 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여, 선형 시간에 정렬하는 효율적인 알고리즘
- 제한 사항
    - 정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능
        - 각 항목의 발생 회수를 기록하기 위해, 정수 항목으로 인덱스 되는 카운트들의 배열을 사용하기 때문
    - 카운트들을 위한 충분한 공간을 할당하려면 집합 내의 가장 큰 정수를 알아야 함
- 시간 복잡도
    - O(n + k) (n: 리스트 길이, k: 정수의 최대값)
- 카운팅 정렬 과정
    1. Data에서 각 항목들의 발생 회수를 세고, 정수 항목들로 직접 인덱스 되는 카운트 배열 counts에 저장
    
    <img src="https://github.com/yuj1818/TIL/assets/95585314/2a89e875-8879-4791-b133-05c866f4c48b" />
    
    1. 정렬된 집합에서 각 항목의 앞에 위치할 항목의 개수를 반영하기 위해 counts의 원소를 조정
    
    <img src="https://github.com/yuj1818/TIL/assets/95585314/0c97a1d5-323e-484f-8509-707df02307ea" />
    
    1. counts[1]을 감소시키고 Temp에 1을 삽입
    
    <img src="https://github.com/yuj1818/TIL/assets/95585314/6b745bb5-c105-45d8-94e2-84ea81b9b5ce" />
    
    1. counts[4]를 감소시키고 temp에 4를 삽입
    
    <img src="https://github.com/yuj1818/TIL/assets/95585314/5c71af47-e526-4b01-a524-bc540298d5cb" />
    
    1. counts[2]를 감소시키고 temp에 2를 삽입
    
    <img src="https://github.com/yuj1818/TIL/assets/95585314/d8fc4eee-ac6a-4127-8507-dbce6d32a254" />
    
    1. (중략)
    2. counts[0]을 감소시키고 temp에 0을 삽입
    
    <img src="https://github.com/yuj1818/TIL/assets/95585314/f9664639-57b9-432a-aeee-2ed88b074ece" />
    
    1. Temp 업데이트 완료하고 정렬 작업 종료
- 카운팅 정렬 알고리즘

```python
def Counting_Sort(A, B, k):
    # A [] -- 입력 배열
    # B [] -- 정렬된 배열
    # C [] -- 카운트 배열
    C = [0] * (k + 1)

    for i in range(0, len(A)):
        C[A[i]] += 1

    for i in range(1, len(C)):
        C[i] += C[i - 1]

    for i in range(len(B)-1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]
```