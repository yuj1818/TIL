# 검색

- 저장되어 있는 자료 중에서 원하는 항목을 찾는 작업
- 목적하는 탐색 키를 가진 항목을 찾는 것
    - 탐색 키(search key): 자료를 구별하여 인식할 수 있는 키

## 검색의 종류

- 순차 검색(sequential search)
- 이진 검색(binary search)
- 해쉬(hash)

### 순차 검색(Sequential Search)

- 일렬로 되어 있는 자료를 순서대로 검색하는 방법
    - 가장 간단하고 직관적인 검색 방법
    - 배열이나 연결 리스트 등 순차 구조로 구현된 자료 구조에서 원하는 항목을 찾을 때 유용
    - 알고리즘이 단순하여 구현이 쉽지만, 검색 대상의 수가 많은 경우에는 수행 시간이 급격히 증가하여 비효율적
- 2가지 경우의 검색 과정
    - 정렬되어 있지 않은 경우
        - 첫 번째 원소부터 순서대로 검색 대상과 키 값이 같은 원소가 있는지 비교하며 검색
        - 키 값이 동일한 원소를 찾으면 그 원소의 인덱스를 반환
        - 자료 구조의 마지막에 이를 때까지 검색 대상을 찾지 못하면 검색 실패
        - 예) 2를 검색하는 경우
        
        <img src="https://github.com/yuj1818/TIL/assets/95585314/0741b11f-8879-468c-a43d-3829cd2f0add" />
        
        - 예) 8을 검색하는 경우
        
        <img src="https://github.com/yuj1818/TIL/assets/95585314/b36db2c7-8fdc-412d-b411-1c609092cb97" />
        
        - 찾고자 하는 원소의 순서에 따라 비교 회수가 결정됨
        - 시간 복잡도 : O(n)
        
        ```python
        def sequentialSearch(a, n, key):
            i = 0
            while i < n and a[i] != key:
                i += 1
            if i < n:
                return i
            else:
                return -1
        
        arr = [4, 9, 11, 23, 2, 19, 7]
        
        print(sequentialSearch(arr, len(arr), 2))   # 검색 성공, 2의 인덱스 4를 반환
        print(sequentialSearch(arr, len(arr), 8))   # 검색 실패, -1 반환
        ```
        
    - 정렬되어 있는 경우
        - 자료가 오름차순으로 정렬된 상태에서 검색을 실시한다고 가정
        - 자료를 순차적으로 검색하며 키 값을 비교하여, 원소의 키 값이 검색 대상의 키 값보다 크면 찾는 원소가 없다는 것이므로 더 이상 검색하지 않고 검색을 종료
        - 예) 11을 검색하는 경우
        
        <img src="https://github.com/yuj1818/TIL/assets/95585314/af5cd603-3b51-4d5c-8ae1-68ce85688af1" />
        
        - 예) 10을 검색하는 경우
        
        <img src="https://github.com/yuj1818/TIL/assets/95585314/52a83cfc-8ea8-4507-b733-7af573e0b877" />
        
        - 찾고자 하는 원소의 순서에 따라 비교 회수가 결정
            - 정렬되어 있으므로, 검색 실패를 반환하는 경우, 평균 비교 회수가 반으로 줄어듦
        - 시간 복잡도 : O(n)
        
        ```python
        def sequentialSearch2(a, n, key):
            i = 0
            while i < n and a[i] < key:     # 찾고자 하는 값보다 작은 경우만 탐색
                i += 1
            if i < n and a[i] == key:
                return i
            else:
                return -1
        
        arr = [4, 9, 11, 23, 2, 19, 7]
        print(sequentialSearch2(arr, len(arr), 11))   # 검색 성공, 11의 인덱스 2를 반환
        print(sequentialSearch2(arr, len(arr), 10))   # 검색 실패, -1 반환
        ```
        

### ⭐⭐이진 검색(Binary Search)⭐⭐

- 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행
    - 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위를 반으로 줄여가면서 보다 빠르게 검색 수행
- 이진 검색을 하기 위해서는 자료가 **정렬된 상태**여야 함
- 검색 과정
    - 자료의 중앙에 있는 원소를 고른다
    - 중앙 원소의 값과 찾고자 하는 목표 값을 비교
    - 목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서 새로 검색 수행
    - 크다면 자료의 오른쪽 반에 대해서 새로 검색 수행
    - 찾고자 하는 값을 찾을 때까지 1 ~ 3 과정 반복
    - 예) 이진 검색으로 7을 찾는 경우
    
    <img src="https://github.com/yuj1818/TIL/assets/95585314/63832b2e-859f-4a54-aaaf-c5e7a0d69f0c" />

    - 예) 이진 검색으로 20을 찾는 경우
    
    <img src="https://github.com/yuj1818/TIL/assets/95585314/8810e2df-6444-4545-8ded-9ab8885352f5" />
    
- 구현
    - 검색 범위의 시작점과 종료점을 이용하여 검색을 반복 수행
    - 이진 검색의 경우, 자료에 삽입이나 삭제가 발생했을 때 배열의 상태를 항상 정렬 상태로 유지하는 추가 작업이 필요
    
    ```python
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
    
    - 재귀 함수 이용
    
    ```python
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