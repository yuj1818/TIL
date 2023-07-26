# Classes

## 객체 지향 프로그래밍

### 절차 지향 프로그래밍(Procedural Programming)

- 프로그램을 **‘데이터’와 ‘절차’로 구성**하는 방식의 프로그래밍 패러다임
- “데이터”와 해당 데이터를 처리하는 “함수(절차)”가 분리되어 있으며, 함수 호출의 흐름이 중요
- 코드의 순차적인 흐름과 함수 호출에 의해 프로그램이 진행

<img src = "https://github.com/yuj1818/TIL/assets/95585314/819cceb0-bac9-4dbe-8c77-93595ef44620" width="30%" height="30%">

- 데이터를 다시 재사용 하기보다는 처음부터 끝까지 실행되는 결과물이 중요한 방식

### 소프트웨어 위기(Software Crisis)

- 하드웨어의 발전으로 컴퓨터 계산 용량과 문제의 복잡성이 급격히 증가함에 따라 소프트웨어에 발생한 충격

<img src = "https://github.com/yuj1818/TIL/assets/95585314/4e81caa8-ccb4-4043-a65a-4abe6266d669" width="30%" height="30%">

### 객체 지향 프로그래밍(Object Oriented Programming)

- 데이터와 해당 데이터를 조작하는 메서드를 **하나의 객체로 묶어 관리**하는 방식의 프로그래밍 패러다임

### 객체 지향 vs 절차 지향

- **절차 지향과 객체 지향은 대조되는 개념이 아니다**
    - 객체 지향은 기존 절차 지향을 기반으로 두고 보완하기 위해 객체라는 개념을 도입해 상속, 코드 재사용성, 유지보수성 등의 이점을 가지는 패러다임

| 절차 지향 | 객체 지향 |
| --- | --- |
| 데이터와 해당 데이터를 처리하는 함수(절차)가 분리 | 데이터와 해당 데이터를 처리하는 메서드(메시지)를 하나의 객체(클래스)로 묶음 |
| 함수 호출의 흐름이 중요 | 객체 간 상호작용과 메시지 전달이 중요 |

<img src = "https://github.com/yuj1818/TIL/assets/95585314/a6de738a-98f7-49b0-91d2-4e69ecad2a63" width="30%" height="30%">

## 객체(object)

- 클래스와 정의한 것을 토대로 메모리에 할당된 것
- ‘속성’과 ‘행동’으로 구성된 모든 것
    
    <img src = "https://github.com/yuj1818/TIL/assets/95585314/d6ad2f55-f31c-448d-ae33-21e134f33e77" width="30%" height="30%">
    

### 클래스와 객체

- 클래스로 만든 객체를 **인스턴스**라고도 함
- 클래스를 만든다 == 타입을 만든다

```python
name = 'Alice'

print(type(name))    # <class 'str'>
```

⇒ 변수 name의 타입은 str 클래스다.

⇒ 변수 name은 str 클래스의 인스턴스이다.

⇒ 문자열 타입의 변수는 str 클래스로 만든 인스턴스이다.

- **하나의 객체(object)는 특정 타입의 인스턴스(instance)이다.**

### 객체(object)의 특징

- 타입(type)
    - 어떤 연산자(operator)와 조작(method)이 가능한가?
- 속성(attribute)
    - 어떤 상태(데이터)를 가지는가?
- 조작법(method)
    - 어떤 행위(함수)를 할 수 있는가?
- **객체 = 속성 + 기능**

## 클래스(class)

- 파이썬에서 **타입**을 표현하는 방법
- 개체를 생성하기 위한 **설계도(청사진)**
- 데이터와 기능을 함께 묶는 방법을 제공

### 클래스 구조

- 클래스 정의
- 인스턴스 생성
- 메서드 호출
- 속성(변수) 접근

```python
# 클래스 정의
class Person:
	blood_color = 'red'    # 클래스 변수
	
	def __init__(self, name):    # 생성자 함수
		self.name = name    # 인스턴스 변수

	def singing(self):    # 인스턴스 메서드
		return f'{self.name}가 노래합니다.'

# 인스턴스 생성
singer1 = Person('iu')

# 메서드 호출
print(singer1.singing())    # iu가 노래합니다.

# 속성(변수) 접근
print(singer1.blood_color)    # red
```

### 클래스 기본 활용

- 생성자 함수
    - 객체를 생성할 때 **자동으로 호출**되는 특별한 메서드
    - __init__이라는 이름의 메서드로 정의되며, 객체의 초기화를 담당
    - 생성자 함수를 통해 인스턴스를 생성하고 필요한 초기값을 설정
- 인스턴스 변수
    - 인스턴스(객체)마다 별도로 유지되는 변수
    - 인스턴스마다 독립적인 값을 가지며, 인스턴스가 생성될 때마다 초기화됨
- 클래스 변수
    - 클래스 내부에 선언된 변수
    - 클래스로 생성된 모든 인스턴스들이 공유하는 변수
- 인스턴스 메서드
    - 각각의 인스턴스에서 호출할 수 있는 메서드
    - 인스턴스 변수에 접근하고 수정하는 등의 작업을 수행

### 인스턴스와 클래스 간의 이름 공간(namespace)

- 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성
- 인스턴스를 만들면, 인스턴스 객체가 생성되고 **독립적인** 이름 공간 생성
- 인스턴스에서 특정 속성에 접근하면, 인스턴스 → 클래스 순으로 탐색

```python
class Person:
	blood_color = 'red' 
	
	def __init__(self, name):    
		self.name = name    

p1 = Person('iu')
p2 = Person('BTS')

print(p1.name)    # iu
p1.address = 'korea'
print(p1.address)    # korea
```

<img src = "https://github.com/yuj1818/TIL/assets/95585314/97c8b0c3-48e8-4366-a940-baa19ab0ea2a" width="30%" height="30%">

- 독립적인 이름 공간을 가지는 이점
    - 각 인스턴스는 독립적인 메모리 공간으로 가지며, 클래스와 다른 인스턴스 간에는 서로의 데이터나 상태에 직접적인 접근이 불가능
    - 객체 지향 프로그래밍의 중요한 특성 중 하나로, 클래스와 인스턴스를 모듈화하고 각각의 객체가 독립적으로 동작하도록 보장
    - 이를 통해 클래스와 인스턴스는 다른 객체들과의 상호작용에서 서로 충돌이나 영향을 주지 않으면서 독립적으로 동작할 수 있음
    
    ⇒ 코드의 가독성, 유지보수성, 재사용성을 높이는데 도움을 줌
    

### 인스턴스 변수와 클래스 변수

- 클래스 변수를 변경할 때는 항상 클래스.클래스변수 형식으로 변경

```python
# 클래스 변수 활용
# 인스턴스가 생성될 때마다 클래스 변수가 늘어나도록 설정할 수 있음

class Person:
	count = 0

	def __init__(self, name):
		self.name = name
		Person.count += 1

person1 = Person('iu')
person2 = Person('BTS')

print(Person.count)    # 2
```

## 메서드(method)

### 인스턴스 메서드(instance method)

- 클래스로부터 생성된 각 인스턴스에서 호출할 수 있는 메서드
- 인스턴스의 상태를 조작하거나 동작을 수행

**인스턴스 메서드 구조**

- 클래스 내부에 정의되는 메서드의 기본
- 반드시 첫 번째 매개변수로 인스턴스 자신(self)을 전달받음

```python
class MyClass:
	def instance_method(self, arg1, ...):    # self가 아닌 다른 이름을 써도 에러가 나지는 않지만 
		pass                                   # self로 쓰기로 약속되어 있음
```

**self 동작 원리**

- upper  메서드를 사용해 문자열 ‘hello’를 대문자로 변경
    
    ```python
    'hello'.upper()    # == str.upper('hello')
    ```
    
- str 클래스가 upper 메서드를 호출했고, 그 첫 번째 인자로 문자열 인스턴스가 들어간 것

⇒ 그러므로 **인스턴스 메서드의 첫 번째 매개변수가 반드시 인스턴스 자기 자신이여야 함**

- ‘hello’라는 문자열 객체가 단순히 어딘가의 함수로 들어가는 인자가 아닌 **객체 스스로 메서드를 호출**하여 코드를 동작하는 객체 지향적 표현이다.

### 생성자 메서드(constructor method)

- 인스턴스 객체가 생성될 때 자동으로 호출되는 메서드
- 인스턴스 변수들의 초기값을 설정

```python
class Person:
	
	def __init__(self, name):
		print(f'인스턴스가 생성됨. {name}')

person1 = Person('으아악')    # 인스턴스가 생성됨. 으아악
```

### 클래스 메서드(class method)

- 클래스가 호출하는 메서드
- 클래스 변수를 조작하거나 클래스 레벨의 동작을 수행

**클래스 메서드 구조**

- @classmethod 데코레이터를 사용하여 정의
- 호출 시, 첫 번째 인자로 호출하는 클래스(cls)가 전달됨

```python
class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def number_of_population(cls):
        print(f'인구수는 {cls.count}입니다.')

person1 = Person('iu')
person2 = Person('BTS')

Person.number_of_population()   # 인구수는 2입니다.
```

### 스태틱(정적) 메서드(static method)

- 클래스와 인스턴스와 상관없이 독립적으로 동작하는 메서드
- 주로 클래스와 관련이 있지만 인스턴스와 상호작용이 필요하지 않은 경우에 사용

**스태틱 메서드 구조**

- @staticmethod  데코레이터를 사용하여 정의
- 호출 시, 필수적으로 작성해야 할 매개변수가 없음
- 즉, 객체 상태나 클래스 상태를 수정할 수 없으며 단지 기능(행동)만을 위한 메서드로 사용

```python
class StringUtils:
    @staticmethod
    def reverse_string(string):
        return string[::-1]
    
    @staticmethod
    def capitalize_string(string):
        return string.capitalize()
    
text = 'hello, world'

reversed_text = StringUtils.reverse_string(text)
print(reversed_text)    # dlrow ,olleh

capitalized_text = StringUtils.capitalize_string(text)
print(capitalized_text)    # Hello, world
```

### 메서드 정리

| 메서드 종류 | 설명 |
| --- | --- |
| 인스턴스 메서드 | 인스턴스의 상태를 변경하거나, 해당 인스턴스의 특정 동작을 수행 |
| 클래스 메서드 | 인스턴스의 상태에 의존하지 않는 기능을 정의 |
|              | 클래스 변수를 조작하거나 클래스 레벨의 동작을 수행 |
| 스태틱 메서드 | 클래스 및 인스턴스와 관련이 없는 일반적인 기능을 수행 |
- 클래스가 사용해야 할 것
    - 클래스 메서드
    - 스태틱 메서드
    - ⚠ 모든 메서드를 호출할 수 있으나 클래스, 스태틱만 사용하도록 한다.
- 인스턴스가 사용해야 할 것
    - 인스턴스 메서드
    - ⚠ 모든 메서드를 호출할 수 있으나 인스턴스만 사용하도록 한다.
    

## 참고

### 매직 메서드

- 특별한 인스턴스 메서드
- **특정 상황에 자동으로 호출**되는 메서드
- Double underscore(__)가 있는 메서드는 특수한 동작을 위해 만들어진 메서드
    - 스페셜 메서드 혹은 매직 메서드라고 불림
- 예시
    - __str__(self), __len__(self), __lt__(self, other), __le__(self, other), __eq__(self, other), __gt__(self, other), __ge__(self, other), __ne__(self, other)
    
    ```python
    class Circle:
        def __init__(self, r):
            self.r = r
        
        def area(self):
            return 3.14 * self.r * self.r
        
        def __str__(self):
            return f'[원] radius: {self.r}'
        
    c1 = Circle(10)
    c2 = Circle(1)
    
    print(c1)   # [원] radius: 10
    print(c2)   # [원] radius: 1
    ```
    

### 데코레이터(Decorator)

- 다른 함수의 코드를 유지한 채로 수정하거나 확장하기 위해 사용되는 함수

```python
# 데코레이터 정의
def my_decorator(func):
    def wrapper():
        # 함수 실행 전에 수행할 작업
        print('함수 실행 전')
        # 원본 함수 호출
        result = func()
        # 함수 실행 후에 수행할 작업
        print('함수 실행 후')
        return result
    return wrapper

# 데코레이터 적용
@my_decorator
def my_function():
    print('원본 함수 실행')

my_function()

"""
함수 실행 전
원본 함수 실행
함수 실행 후
"""
```