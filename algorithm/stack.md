# ⭐⭐⭐스택(Stack)⭐⭐⭐

- 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조
- 스택에 저장된 자료는 선형 구조를 갖는다.
    - 선형 구조: 자료 간의 관계가 1대 1의 관계를 갖는다.
    - 비선형 구조: 자료 간의 관계가 1대 N의 관계를 갖는다.(ex: 트리)
- 스택에 자료를 삽입하거나 스택에서 자료를 꺼낼 수 있다.
- 마지막에 삽입한 자료를 가장 먼저 꺼낸다.
    - ⭐⭐**후입선출(LIFO, Last In First Out)⭐⭐**

## 스택의 구현

### 스택을 프로그램에서 구현하기 위해서 필요한 자료구조와 연산

- 자료구조:
    - 자료를 선형으로 저장할 저장소
- 배열 사용 가능
- 저장소 자체를 스택이라고 부르기도 한다
- 스택에서 마지막 삽입된 원소의 위치를 top이라 한다.

### 연산

- 삽입
    - 저장소에 자료를 저장. push
- 삭제
    - 저장소에서 자료를 꺼냄
    - 꺼낸 자료는 삽입한 자료의 역순으로 꺼냄. pop
- 스택이 공백인지 아닌지 확인
    - isEmpty
- 스택의 top에 있는 item을 반환
    - peek

### 스택의 삽입/삭제 과정

- 빈 스택에 원소 A, B, C를 차례로 삽입 후 한 번 삭제하는 연산 과정

<img src="https://github.com/yuj1818/TIL/assets/95585314/177a368c-5c86-4234-bc6c-b58f023a7c06" />

### 스택의 push 알고리즘

- append 메소드를 사용하여 리스트의 마지막에 데이터를 삽입

```python
def push(item):
		s.append(item)
```

```python
def push(item, size):
    global top
    top += 1
    if top == size:
        print('overflow!')
    else:
        stack[top] = item

size = 10
stack = [0] * size
top = -1

push(10, size)
top += 1
stack[top] = 20
```

### 스택의 pop 알고리즘

```python
def pop():
		if len(s) == 0:
				# underflow
				return
		else:
				return s.pop()
```

```python
def pop():
    global top
    if top == -1:
        print('underflow!')
        return 0
    else:
        top -= 1
        return stack[top + 1]

top = 9
stack = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10]

for i in range(10):
    if top > -1:
        top -= 1
        print(stack[top + 1])
    else:
        print(pop())
'''
10
9
8
7
6
5
4
3
2
1
'''
```

## 스택 구현 고려 사항

- 1차원 배열을 사용하여 구현할 경우 구현이 용이하다는 장점이 있지만 스택의 크기를 변경하기가 어려움
- 이를 해결하기 위해 저장소를 동적으로 할당하여 스택을 구현하는 방법 존재
    - 동적 연결리스트를 이용하여 구현하는 방법
    - 구현이 복잡하다는 단점이 있지만 메모리를 효율적으로 사용한다는 장점이 있음

## 스택의 응용

### ⭐⭐괄호 검사⭐⭐

- 조건
    1. 왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 같아야 한다
    2. 같은 괄호에서 왼쪽 괄호는 오른쪽 괄호보다 먼저 나와야 한다
    3. 괄호 사이에는 포함 관계만 존재한다
- 문자열에 있는 괄호를 차례대로 조사하면서 왼쪽 괄호를 만나면 스택에 삽입
- 오른쪽 괄호를 만나면 스택에서 top괄호 삭제한 후 오른쪽 괄호와 짝이 맞는지 검사
- 스택이 비어 있다면 조건 1, 조건 2에 위배되고 괄호의 짝이 맞지 않으면 조건 3에 위배
- 마지막 괄호까지 조사한 후에도 스택에 괄호가 남아 있으면 조건 1에 위배

```python
T = int(input())
check = ['()', '{}']
for tc in range(1, T + 1):
    code = input()
    stack = []
    sig = 1
    for c in code:
        if c in list(zip(*check))[0]:
            stack.append(c)
        elif c in list(zip(*check))[1]:
            if len(stack) == 0:
                sig = 0
                break
            if stack[-1] + c in check:
                stack.pop()
            else:
                stack.append(c)
    answer = int(len(stack) == 0 and sig)
    print(f'#{tc} {answer}')
```

### function call

- 프로그램에서 함수 호출과 복귀에 따른 수행 순서를 관리
    - 가장 마지막에 호출된 함수가 가장 먼저 실행을 완료하고 복귀하는 후입선출 구조이므로, 후입선출 구조의 스택을 이용하여 수행 순서 관리
    - 함수 호출이 발생하면 호출한 함수 수행에 필요한 지역변수, 매개변수 및 수행 후 복귀할 주소 등의 정보를 스택 프레임에 저장하여 시스템 스택에 삽입
    - 함수의 실행이 끝나면 시스템 스택의 top원소를 삭제(pop)하면서 프레임에 저장되어 있던 복귀 주소를 확인하고 복귀
    - 함수 호출과 복귀에 따라 이 과정을 반복하여 전체 프로그램 수행이 종료되면 시스템 스택은 공백 스택이 됨
    
    <img src="https://github.com/yuj1818/TIL/assets/95585314/4efa1e71-82c2-4051-9375-a87ae9ff0661" />
    
    <img src="https://github.com/yuj1818/TIL/assets/95585314/ea5b1dfa-9cf8-495d-8424-bbc8b1dec875" />
    

## 재귀 호출

- 자기 자신을 호출하여 순환 수행되는 것
- 함수에서 실행해야 하는 작업의 특성에 따라 일반적인 호출 방식보다 재귀 호출 방식을 사용하여 함수를 만들면 프로그램의 크기를 줄이고 간단하게 작성 가능
    - 예) factorial
    
    <img src="https://github.com/yuj1818/TIL/assets/95585314/eaf309bf-845b-4c03-91b7-b899fd904232" />
    

### 예) 피보나치 수열

- 0과 1로 시작하고 이전의 두 수 합을 다음 항으로 하는 수열을 피보나치라 한다.
- 피보나치 수열의 i번 째 값을 계산하는 함수 F
    - F0 = 0, F1 = 1
    - Fi = Fi-1 + Fi-2 for i ≥ 2
- 위의 정의로부터 피보나치 수열의 i번째 항을 반환하는 함수를 재귀 함수로 구현 가능

```python
def fibo(n):
		if n < 2:
				return n
		else:
				return fibo(n - 1) + fibo(n - 2)
```

## Memoization

- 앞의 예에서 피보나치 수를 구하는 함수를 재귀 함수로 구현한 알고리즘은 엄청난 중복 호출이 존재한다는 문제점이 존재

<img src="https://github.com/yuj1818/TIL/assets/95585314/db60a1ac-b3a5-4107-9600-d981480263b0" />

- 메모이제이션은 컴퓨터 프로그램을 실행할 때 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 전체적인 실행 속도를 빠르게 하는 기술
- 동적 계획법의 핵심이 되는 기술