# Classes

## 객체 지향 프로그래밍

### 절차 지향 프로그래밍(Procedural Programming)

- 프로그램을 **‘데이터’와 ‘절차’로 구성**하는 방식의 프로그래밍 패러다임
- “데이터”와 해당 데이터를 처리하는 “함수(절차)”가 분리되어 있으며, 함수 호출의 흐름이 중요
- 코드의 순차적인 흐름과 함수 호출에 의해 프로그램이 진행

<img src = "https://github.com/yuj1818/TIL/assets/95585314/819cceb0-bac9-4dbe-8c77-93595ef44620" width="50%" height="50%">

- 데이터를 다시 재사용 하기보다는 처음부터 끝까지 실행되는 결과물이 중요한 방식

### 소프트웨어 위기(Software Crisis)

- 하드웨어의 발전으로 컴퓨터 계산 용량과 문제의 복잡성이 급격히 증가함에 따라 소프트웨어에 발생한 충격

<img src = "https://github.com/yuj1818/TIL/assets/95585314/4e81caa8-ccb4-4043-a65a-4abe6266d669" width="50%" height="50%">

### 객체 지향 프로그래밍(Object Oriented Programming)

- 데이터와 해당 데이터를 조작하는 메서드를 **하나의 객체로 묶어 관리**하는 방식의 프로그래밍 패러다임

### 객체 지향 vs 절차 지향

- **절차 지향과 객체 지향은 대조되는 개념이 아니다**
    - 객체 지향은 기존 절차 지향을 기반으로 두고 보완하기 위해 객체라는 개념을 도입해 상속, 코드 재사용성, 유지보수성 등의 이점을 가지는 패러다임

| 절차 지향 | 객체 지향 |
| --- | --- |
| 데이터와 해당 데이터를 처리하는 함수(절차)가 분리 | 데이터와 해당 데이터를 처리하는 메서드(메시지)를 하나의 객체(클래스)로 묶음 |
| 함수 호출의 흐름이 중요 | 객체 간 상호작용과 메시지 전달이 중요 |

<img src = "https://github.com/yuj1818/TIL/assets/95585314/a6de738a-98f7-49b0-91d2-4e69ecad2a63" width="50%" height="50%">

## 객체(object)

- 클래스와 정의한 것을 토대로 메모리에 할당된 것
- ‘속성’과 ‘행동’으로 구성된 모든 것
    
    <img src = "https://github.com/yuj1818/TIL/assets/95585314/d6ad2f55-f31c-448d-ae33-21e134f33e77" width="50%" height="50%">
    

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

<img src = "https://github.com/yuj1818/TIL/assets/95585314/97c8b0c3-48e8-4366-a940-baa19ab0ea2a" width="50%" height="50%">

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
    
# Classes 상속

## 상속(inheritance)

- 기존 클래스의 속성과 메서드를 물려받아 새로운 하위 클래스를 생성하는 것

### 상속이 필요한 이유

1. 코드 재사용
    - 상속을 통해 기존 클래스의 속성과 메서드를 재사용할 수 있음
    - 새로운 클래스를 작성할 때 기존 클래스의 기능을 그대로 활용할 수 있으며, 중복된 코드를 줄일 수 있음
2. 계층 구조
    - 상속을 통해 클래스들 간의 계층 구조를 형성할 수 있음
    - 부모 클래스와 자식 클래스 간의 관계를 표현하고, 더 구체적인 클래스를 만들 수 있음
3. 유지 보수의 용이성
    - 상속을 통해 기존 클래스의 수정이 필요한 경우, 해당 클래스만 수정하면 되므로 유지 보수가 용이해짐
    - 코드의 일관성을 유지하고, 수정이 필요한 범위를 최소화할 수 있음

## 클래스 상속

### **상속 없이 구현 하는 경우**

```python
# 학생/교수 정보를 나타내기 어려움
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')

s1 = Person('김학생', 23)
s1.talk()   # 반갑습니다. 김학생입니다.

p1 = Person('박교수', 59)
p1.talk()   # 반갑습니다. 박교수입니다.
```

```python
# 메서드 중복 정의
class Professor:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def talk(self):    # 중복
        print(f'반갑습니다. {self.name}입니다.')

class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def talk(self):    # 중복
        print(f'반갑습니다. {self.name}입니다.')
```

### 상속을 사용한 계층구조 변경

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):    # 메서드 재사용
        print(f'반갑습니다. {self.name}입니다.')

class Professor(Person):
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

class Student(Person):
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

p1 = Professor('박교수', 49, '컴퓨터공학과')
s1 = Student('김학생', 20, 3.5)

# 부모 Person 클래스의 talk 메서드를 활용
p1.talk()   # 반갑습니다. 박교수입니다.

# 부모 Person 클래스의 talk 메서드를 활용 
s1.talk()   # 반갑습니다. 김학생입니다.
```

### super()

- 부모 클래스의 메서드를 호출하기 위해 사용되는 내장 함수
- 상속 순서에 맞춰서 자동으로 알맞은 부모 클래스의 메서드를 호출할 수 있음

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')

class Professor(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)    # 부모 클래스의 init 메서드 호출
        self.department = department

class Student(Person):
    def __init__(self, name, age, gpa):
        super().__init__(name, age)    # 부모 클래스의 init 메서드 호출
        self.gpa = gpa

p1 = Professor('박교수', 49, '컴퓨터공학과')
s1 = Student('김학생', 20, 3.5)

p1.talk()   # 반갑습니다. 박교수입니다.

s1.talk()   # 반갑습니다. 김학생입니다.
```

## 다중 상속

- 두 개 이상의 클래스를 상속 받는 경우
- 상속 받은 모든 클래스의 요소를 활용 가능함
- 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정됨

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'안녕, {self.name}'
    
class Mom(Person):
    gene = 'XX'

    def swim(self):
        return '엄마가 수영'
    
class Dad(Person):
    gene = 'XY'

    def walk(self):
        return '아빠가 걷기'
    
class FirstChild(Dad, Mom):
    def swim(self):
        return '첫째가 수영'
    
    def cry(self):
        return '첫째가 응애'
    
baby1 = FirstChild('아가')
print(baby1.cry())  # 첫째가 응애
print(baby1.swim()) # 첫째가 수영
print(baby1.walk()) # 아빠가 걷기
print(baby1.gene)   # XY
```

### 상속 관련 함수와 메서드

- mro()
    - Method Resolution Order
    - 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 메서드
    - 기존의 인스턴스 ⇒ 클래스 순으로 이름 공간을 탐색하는 과정에서 상속 관계에 있으면 인스턴스 ⇒ 자식 클래스 ⇒ 부모 클래스로 확장
    
    ```python
    print(FirstChild.mro())
    """
    [<class '__main__.FirstChild'>, <class '__main__.Dad'>, <class '__main__.Mom'>,
     <class '__main__.Person'>, <class 'object'>]
    """
    ```
    

# 에러와 예외

## 디버깅

### 버그(bug)

- 소프트웨어에서 발생하는 오류 또는 결함
- 프로그램의 예상된 동작과 실제 동작 사이의 불일치

### 버그의 기원

- 최초의 버그는 1945년 프로그래밍 언어의 일종인 코볼 발명자 그레이스 호퍼가 발견
- 역사상 최초의 컴퓨터 버그는 Mark Ⅱ라는 컴퓨터 회로에 벌레인 나방이 들어가 합선을 일으켜 비정상적으로 동작한 것을 기록한 것
- “버그”라는 용어는 이전부터 사용되어 왔지만 이 사건을 계기로 컴퓨터 시스템에서 발생하는 오류 또는 결함을 지칭하는 용어로 널리 사용되기 시작

### 디버깅(Debugging)

- 소프트웨어에서 발생하는 버그를 찾아내고 수정하는 과정
- 프로그램의 오작동 원인을 식별하여 수정하는 작업

### 디버깅 방법

1. print 함수 활용
    - 특정 함수 결과, 반복/조건 결과 등 나눠서 생각, 코드를 bisection으로 나눠서 생각
2. 개발 환경(text editor, IDE) 등에서 제공하는 기능 활용
    - breakpoint, 변수 조회 등
3. Python tutor 활용(단순 파이썬 코드인 경우)
4. 뇌 컴파일, 눈 디버깅 등

## 에러(error)

- 프로그램 실행 중에 발생하는 예외 상황

### 파이썬의 에러 유형

- 문법 에러(Syntax Error)
    - 프로그램의 구문이 올바르지 않은 경우 발생
    - 오타, 괄호 및 콜론 누락 등의 문법적 오류
    - Invalid syntax, assign to literal, EOL, EOF
- 예외(Exception)
    - 프로그램 실행 중에 감지되는 에러

## 예외(Exception)

- 프로그램 실행 중에 감지되는 에러

### 내장 예외(Built-in Exceptions)

- 예외 상황을 나타내는 예외 클래스들
- 파이썬에서 이미 정의되어 있으며, 특정 예외 상황에 대한 처리를 위해 사용
- ZeroDivisionError
    - 나누기 또는 모듈로 연산의 두 번째 인자가 0일 때 발생
- NameError
    - 지역 또는 전역 이름을 찾을 수 없을 때 발생
- TypeError
    - 타입 불일치
    - 인자 누락
    - 인자 초과
    - 인자 타입 불일치
- ValueError
    - 연산이나 함수에 문제가 없지만 부적절한 값을 가진 인자를 받았고, 상황이 IndexError처럼 더 구체적인 예외로 설명되지 않는 경우 발생
- IndexError
    - 시퀀스 인덱스가 범위를 벗어날 때 발생
- KeyError
    - 딕셔너리에 해당 키가 존재하지 않는 경우
- ModuleNotFoundError
    - 모듈을 찾을 수 없을 때 발생
- ImportError
    - 임포트 하려는 이름을 찾을 수 없을 때 발생
- KeboardInterrupt
    - 사용자가 Ctrl+C 또는 Delete를 누를 때 발생
- IndentationError
    - 잘못된 들여쓰기와 관련된 문법 오류

## 예외 처리

### try와 except

- 파이썬에서는 try 문과 except 절을 사용하여 에러 처리
- try 블록 안에는 예외가 발생할 수 있는 코드 작성
- except 블록 안에는 예외가 발생했을 때 처리할 코드를 작성
- 예외가 발생하면 프로그램 흐름은 try 블록을 빠져나와 해당 예외에 대응하는 except 블록으로 이동

```python
try:
	# 예외가 발생할 수 있는 코드
	result = 10 / 0
except ZeroDivisionError:
	# 예외 처리 코드
	print('0으로 나눌 수 없습니다.')    # 0으로 나눌 수 없습니다.
```

```python
try:
	# 예외가 발생할 수 있는 코드
	num = int(input('숫자 입력 : '))
except ValueError:
	# 예외 처리 코드
	print('숫자가 아닙니다.')

"""
숫자입력 : a
숫자가 아닙니다.
"""
```

**복수 예외 처리**

```python
try:
    num = int(input('100으로 나눌 값을 입력하시오: '))
    print(100 / num)
except ZeroDivisionError:
    print('0으로는 나눌 수 없습니다.')
except ValueError:
    print('숫자를 입력해주세요')
except:
    print('에러 발생')
```

**내장 예외의 상속 계층 구조 주의**

- 내장 예외 클래스는 상속 계층구조를 가지기 때문에 except 절로 분기 시 반드시 하위 클래스를 먼저 확인할 수 있도록 작성해야 함

<p align='center'><img src = "https://github.com/yuj1818/TIL/assets/95585314/2e034e82-ae10-484e-8d9e-d85015ccad82" ></p>

```python
try:
    num = int(input('100으로 나눌 값을 입력하시오: '))
    print(100 / num)
except BaseException:
    print('숫자를 입력해주세요')
except ZeroDivisionError:   # 2번째 예외처리 부터는 도달할 수 가 없음
    print('0으로는 나눌 수 없습니다.')
except:
    print('에러 발생'
```

## EAFP & LBYL

### EAFP(Easier to Ask for Forgiveness than Permission)

- 예외처리를 중심으로 코드를 작성하는 접근 방식
- try - except

### LBYL(Look Before You Leap)

- 값 검사를 중심으로 코드를 작성하는 접근 방식
- if - else

### 접근 방식 비교

| EAFP | LBYL |
| --- | --- |
| “일단 실행하고 예외 처리” | “실행하기 전에 조건을 검사” |
| 코드를 실행하고 예외가 발생하면 예외처리를 수행 | 코드 실행 전에 조건문 등을 사용하여 예외 상황을 미리 검사하고, 예외 상황을 피하는 방식 |
| 코드에서 예외가 발생할 수 있는 부분을 미리 예측하여 대비하는 것이 아니라, 예외가 발생한 후에 예외를 처리 | 코드가 좀 더 예측 가능한 동작을 하지만, 코드가 더 길고 복잡해질 수 있음 |
| 예외 상황을 예측하기 어려운 경우에 유용 | 예외 상황을 미리 방지하고 싶을 때 유용 |

```python
# EAFP
try:
    result = my_dict['key']
    print(result)
except KeyError:
    print('Key가 존재하지 않습니다.')
```

```python
# LBYL
if 'key' in my_dict:
    result = my_dict['key']
    print(result)
else:
    print('Key가 존재하지 않습니다.')
```

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

### as 키워드

- as 키워드를 활용하여 에러 메시지를 except 블록에서 사용할 수 있음

```python
my_list = []

try:
    number = my_list[1]
except IndexError as error:
    print(f'{error}가 발생했습니다.')

# list index out of range가 발생했습니다.
```
