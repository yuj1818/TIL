# Functions

- 특정 작업을 수행하기 위한 재사용 가능한 코드 묶음
- 코드의 중복을 방지
- **재사용성**이 높아지고, 코드의 가독성과 **유지 보수성** 향상

## 내장 함수(Built-in function)

- 파이썬이 기본적으로 제공하는 함수
- ex) print(), abs()
- [python 내장함수](https://docs.python.org/ko/3.9/library/functions.html) 

## 함수 구조

<img src = "https://github.com/yuj1818/TIL/assets/95585314/901ed53f-613b-443f-95d5-994fb2e68e31" width="30%" height="30%">

- 함수 정의
    - def 키워드로 시작
    - def 키워드 다음 함수 이름 작성
    - 괄호 안에 parameter 정의
- 함수 body
    - 콜론(:) 다음에 들여쓰기 된 코드 블록
    - 함수가 실행될 때 수행되는 코드 정의
- 함수 반환 값
    - 필요한 경우 결과를 반환할 수 있음
    - return 키워드 이후, 반환할 값 명시
    - return문은 함수의 실행을 종료하고, 결과를 호출 부분으로 변환
- ❗ 함수 호출
    - 함수를 호출하기 위해 함수의 이름과 필요 인자를 전달해야 함
    - 전달된 인자는 함수 정의 시 작성한 매개변수에 대입됨
    
    ```python
    def greet(name):    # 함수 정의
    	message = 'Hello, ' + name    # 함수 body
    	return message                # 반환 값
    
    result = greet('Alice')    # 함수 호출
    print(result)
    ```
    

## 매개변수와 인자

- 매개변수 : 함수를 **정의**할 때, 함수가 받을 값을 나타내는 변수
- 인자: 함수를 **호출**할 때, 실제로 전달되는 값

```python
def add_numbers(x, y):    # x, y는 parameter
	result = x + y
	return result

a = 2
b = 3
sum_result = add_numbers(a, b)    # a, b는 인자(argument)
print(sum_result)
```

### 인자의 종류

- Positional Arguments(위치 인자)
    - 함수  호출 시 인자의 위치에 따라 전달되는 인자
    - ⚠ 함수 호출 시 반드시 값을 전달해야 함
    
    ```python
    def greet(name, age):
    	print(f'안녕하세요, {name}님! {age}살이시군요.')
    
    greet('Alice', 25)    # 안녕하세요, Alice님! 25살이시군요.
    greet(25, 'Alice')    # 안녕하세요, 25님! Alice살이시군요.
    ```
    
- Default Argument Values(기본 인자 값)
    - 함수 정의에서 매개변수에 기본 값을 할당하는 것
    - 함수 호출 시 인자를 전달하지 않으면, 기본 값이 매개변수에 할당됨
    
    ```python
    def greet(name, age=30):
    	print(f'안녕하세요, {name}님! {age}살이시군요.')
    
    greet('Bob')    # 안녕하세요, Bob님! 30살이시군요.
    greet('Charlie', 40)    # 안녕하세요, Charlie님! 40살이시군요.
    ```
    
- Keyword Arguments(키워드 인자)
    - 함수 호출 시 인자의 이름과 함께 값을 전달하는 인자
    - 매개변수와 인자를 일치시키지 않고, 특정 매개변수에 값을 할당할 수 있음
    - 인자의 순서는 중요하지 않으며, 인자의 이름을 명시하여 전달
    - ⚠ 호출 시, 키워드 인자는 위치 인자 뒤에 위치해야 함
    
    ```python
    def greet(name, age):
    	print(f'안녕하세요, {name}님! {age}살이시군요.')
    
    greet(age=35, name='Dave')    # 안녕하세요, Dave님! 35살이시군요.
    greet(age=35, 'Dave')    # positional argument follows keyword argument
    ```
    
- Arbitrary Argument Lists(임의의 인자 목록)
    - 정해지지 않은 개수의 인자를 처리하는 인자
    - 함수 정의 시 매개변수 앞에 ‘*’를 붙여 사용
    - 여러 개의 인자를 tuple로 처리
    
    ```python
    def calculate_sum(*args):
    	print(args)
    	total = sum(args)
    	print(f'합계: {total}')
    
    calculate_sum(1, 2, 3)    # (1, 2, 3)
    												  # 합계: 6
    ```
    
- Arbitrary Keyword Argument Lists(임의의 키워드 인자 목록)
    - 정해지지 않은 개수의 키워드 인자를 처리하는 인자
    - 함수 정의 시 매개변수 앞에 ‘**’를 붙여 사용
    - 여러 개의 인자를 dictionary로 묶어 처리
    
    ```python
    def print_info(**kwargs):
    	print(kwargs)
    
    print_info(name='Eve', age=30)    # {'name': 'Eve', 'age': 30}
    ```
    
- 함수 인자 권장 작성 순서
    - 위치 → 기본 → 가변 → 키워드 → 가변 키워드
    - 모든 상황에 적용되는 절대적인 규칙은 아니며, 상황에 따라 유연하게 조정 가능
    
    ```python
    def func(pos1, pos2, default_arg='default', *args, kwd, **kwargs):
    	...
    ```
    

## 함수와 Scope

- 함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분
- scope
    - global scope : 코드 어디에서나 참조할 수 있는 공간
    - local scope: 함수가 만든 scope(함수 내부에서만 참조 가능)
- variable
    - global variable: global scope에 정의된 변수
    - local variable: local scope에 정의된 변수

```python
def func():
	num = 20
	print('local', num)

func()    # local 20

print('global', num) # NameError: name 'num' is not defined
```

- 변수 수명 주기(lifecycle)
    - 변수의 수명 주기는 변수가 선언되는 위치와 스코프에 따라 결정됨
    1. built-in scope
        
        파이썬이 실행된 이후부터 영원히 유지
        
    2. global scope
        
        모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
        
    3. local scope
        
        함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지
        
- 이름 검색 규칙(Name Resolution)
    - 파이썬에서 사용되는 이름(식별자)들은 특정한 이름 공간(namespace)에 저장되어 있음
    - LEGB Rule 순서로 이름을 찾아 나감 📙
        1. Local scope : 지역 범위(현재 작업 중인 범위)
        2. Enclosed scope : 지역 범위 한 단계 위 범위
        3. Global scope : 최상단에 위치한 범위
        4. Built-in scope : 모든 것을 담고 있는 범위(정의하지 않고 사용할 수 있는 모든 것)
    - ⚠ 함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정은 할 수 없음
    
    ```python
    print(sum)    # <built-in function sum>
    print(sum(range(3)))    # 3
    
    sum = 5
    
    print(sum)    # 5
    print(sum(range(3)))    # TypeError: 'int' object is not callable
    
    # 예약어를 변수명으로 지정함으로써 전역변수 sum이 생겨 built-in의 sum보다 전역 변수 sum이 우선시 됨
    # sum 변수 객체 삭제를 위해 del sum을 입력 후 다시 sum함수 호출하면 가능
    ```
    
    ```python
    a = 1
    b = 2
    
    def enclosed():
    	a = 10
    	c = 3
    	
    	def local(c):
    		print(a, b, c)    # 10 2 500
    
    	local(500)
    	print(a, b, c)    # 10 2 3
    
    enclosed()
    print(a, b)    # 1 2
    ```
    
- ‘global’ 키워드
    - 변수의 스코프를 전역 범위로 지정하기 위해 사용
    - 일반적으로 함수 내에서 전역 변수를 수정하려는 경우에 사용
    
    ```python
    num = 0    # 전역 변수
    
    def increment():
    	global num    # num을 전역 변수로 선언
    	num += 1
    
    print(num)    # 0
    increment()
    print(num)    # 1
    ```
    
    - global 키워드 선언 전에 접근 시
    
    ```python
    num = 0
    
    def increment():
        print(num)    # SyntaxError: name 'num' is used prior to global declaration
        global num
        num += 1
    ```
    
    - 매개변수에 global 사용 불가
    
    ```python
    num = 0
    
    def increment(num):
        global num    # SyntaxError: name 'num' is parameter and global
        num += 1
    ```
    
    - ⚠ global 키워드는 가급적 사용 권장하지 않음

## 재귀 함수

- 함수 내부에서 자기 자신을 호출하는 함수
- 특정 알고리즘 식을 표현할 대 변수의 사용이 줄어들며, 코드의 가독성이 높아짐
- **1개 이상의 base case(종료되는 상황)가 존재**하고, **수렴하도록** 작성
- ex) 팩토리얼, 피보나치 수열

```python
def factorial(n):
	if n == 1:    # 종료 조건
		return 1                     # 5 * factorial(4)
	return n * factorail(n - 1)    # 5 * 4 * factorial(3)
																 # 5 * 4 * 3 * factorial(2)
result = factorial(5)            # 5 * 4 * 3 * 2 * factorial(1)
print(result)    # 120           # 5 * 4 * 3 * 2 * 1 = 120
```

## 유용한 함수

### map(function, iterable)

- 순회 가능한 데이터 구조의 모든 요소에 함수를 적용하고, 그 결과를 map object로 반환

```python
numbers = [1, 2, 3]
result = map(str, numbers)

print(result)    # <map object at 0x0000025f3ddfe3f8>
print(list(result))    # ['1', '2', '3']
```

### zip(*iterables)

- 임의의 iterable을 모아 튜플을 원소로 하는 zip object를 반환

```python
girls = ['jane', 'ashley']
boys = ['peter', 'jay']
pair = zip(girls, boys)

print(pair)    # <zip object at 0x00000167b357e158>
print(list(pair))    # [('jane', 'peter'), ('ashley', 'jay')]
```

### lambda 함수

- 이름 없이 정의되고 사용되는 **익명 함수** (재사용성 X)

```python
lambda 매개변수: 표현식
```

- lambda 키워드
    - 람다 함수를 선언하기 위해 사용되는 키워드
- 매개변수
    - 함수에 전달되는 매개변수들
    - 여러 개의 매개변수가 있을 경우, 쉼표로 구분
- 표현식
    - 함수의 실행되는 코드 블록으로, 결과 값을 반환하는 표현식으로 작성

```python
# 변환 전
def addition(x, y):
    return x + y

result = addition(3, 5)
print(result)    # 8
```

```python
# 변환 후
addition = lambda x, y: x+ y    # 좋지 않은 예시, 굳이 lambda 쓰지 않아도 됨

result = addition(3, 5)
print(result)    # 8
```

```python
# map + lambda
number = [1, 2, 3, 4, 5]
result = map(lambda x: x * 2, number)
print(list(result))
```

## Packing & Unpacking

### Packing

- 여러 개의 값을 하나의 변수에 묶어서 담는 것

```python
packed_values = 1, 2, 3, 4, 5
print(packed_values)    # (1, 2, 3, 4, 5)
```

- ‘*’ 활용하여 packing ⇒ print 함수에 임의의 가변 인자를 작성할 수 있는 이유

```python
numbers = [1, 2, 3, 4, 5]
a, *b, c = numbers

print(a)    # 1
print(b)    # [2, 3, 4]
print(c)    # 5
```

### Unpacking

- 패킹된 변수의 값을 개별적인 변수로 분리하여 할당하는 것

```python
lst = [1, 2, 3]
a, b, c = lst

print(a)    # 1
print(b)    # 2
print(c)    # 3
```

- ‘*’ 활용하여 unpacking

```python
lst = [1, 2, 3]

print(*lst)    # 1 2 3
```

- ‘**’ 활용하여 unpacking

```python
def my_function(x, y, z):
	print(x, y, z)

my_dict = {'x': 1, 'y': 2, 'z': 3}
my_function(**my_dict)    # 1 2 3
```