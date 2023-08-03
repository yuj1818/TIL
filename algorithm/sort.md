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

### 선택 정렬(Selection Sort)

- **인덱스**
    - 인덱스라는 용어는 Database에서 유래
    - 테이블에 대한 동작 속도를 높여주는 자료 구조
    - Loo up table 등의 용어를 사용하기도 함
    - 인덱스를 저장하는데 필요한 디스크 공간은 보통 테이블을 저장하는데 필요한 디스크 공간보다 작음
    - 인덱스는 키-필드만 갖고 있고, 테이블의 다른 세부 항목들은 갖고 있지 않기 때문
    - 배열을 사용한 인덱스
        - 대량의 데이터를 매번 정렬하면, 프로그램의 반응은 느려질 수 밖에 없다
        - 이러한 대량 데이터의 성능 저하 문제를 해결하기 위해 배열 인덱스를 사용
- 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식
- 정렬 과정
    - 주어진 리스트 중에서 최소값을 찾는다
    
    <img src="https://github.com/yuj1818/TIL/assets/95585314/f09b0df0-ac1a-4c19-80e1-7d7d1e02fc87" />
    
    - 그 값을 리스트의 맨 앞에 위치한 값과 교환
    
    <img src="https://github.com/yuj1818/TIL/assets/95585314/3617b860-7acf-4e79-adf0-72bf0c986e5d" />
    
    - 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정 반복
    
    <img src="https://github.com/yuj1818/TIL/assets/95585314/64adb230-e391-463f-8ea4-efb2f00e5d78" />
    
    <img src="https://github.com/yuj1818/TIL/assets/95585314/5d5b9939-a0cc-4c8a-ac6f-949f26647022" />
    
    <img src="https://github.com/yuj1818/TIL/assets/95585314/e2babff9-8551-4631-acae-5fe772a22762" />
    
    - 미정렬원소가 하나 남은 상황에서는 마지막 원소가 가장 큰 값을 갖게 되므로, 실행을 종료하고 선택 정렬이 완료된다.
    
    ```python
    def selectionSort(a, N):
        for i in range(N - 1):
            minIdx = i
            for j in range(i + 1, N):
                if a[minIdx] > a[j]:
                    minIdx = j
            a[i], a[minIdx] = a[minIdx], a[i]
    ```
    
- 시간 복잡도 : O(n^2)

### 셀렉션 알고리즘(Selection Algorithm)

- 저장되어 있는 자료로부터 k번째로 큰 혹은 작은 원소를 찾는 방법을 셀렉션 알고리즘이라 함
    - 최소값, 최대값 혹은 중간값을 찾는 알고리즘
- 선택 과정
    - 정렬 알고리즘을 이용하여 자료 정렬
    - 원하는 순서에 있는 원소 가져오기
- k번째로 작은 원소를 찾는 알고리즘
    
    ```python
    def select(arr, k):
        for i in range(0, k):
            minIdx = i
            for j in range(i + 1, len(arr)):
                if arr[minIdx] > arr[j]:
                    minIdx = j
            arr[i], arr[minIdx] = arr[minIdx], arr[i]
        return arr[k - 1]
    ```