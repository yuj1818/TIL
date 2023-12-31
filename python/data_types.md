# Data Types

- 값의 종류와 그 값에 적용 가능한 연산과 동작을 결정하는 속성
- 값이 어떤 종류의 데이터인지, 어떻게 해석되고 처리되어야 하는지를 정의
- 값, 값에 적용할 수 있는 연산으로 이루어짐

## | Data Type의 역할

- 값들을 구분하고, 어떻게 다뤄야 하는지 알 수 있음
- 코드를 읽는 사람이 변수의 의도를 더 쉽게 이해할 수 있음
- 잘못된 데이터 타입으로 인한 오류를 미리 예방

## | 종류
- 데이터 타입
    - Numeric Type
        - int
        - float
        - complex
    - Sequence Types
        - list
        - tuple
        - range
    - Text Sequence Type
        - str
    - Set Types
        - set
    - Mapping Types
        - dict
    - 기타
        - None
        - Boolean
        - Functions

### | Numeric Types

- int(정수)
    - 2진수(binary) - 0b
    - 8진수(octal) - 0o
    - 16진수(hexadecimal) - 0x
    
    ```python
    print(bin(12))    # 0b1100
    print(oct(12))    # 0o14
    print(hex(12))    # 0xc
    ```
    
- float(실수)
    - 정확한 실수 값이 아니라 실수에 대한 근삿값을 제공
    
    ```python
    print(2 / 3)    # 0.6666666666666666
    print(5 / 3)    # 1.6666666666666667
    ```
    
    - Floating point rounding error
        - 실수 연산 시, 2진수로 변환되는 과정에서 무한대 숫자를 그대로 저장할 수 없어 사람이 사용하는 10진법의 근삿값만 표시하게 되며 정확히 동일한 값이 아니게 되는 현상
    - Floating point rounding error를 해결하기 위한 방법
        - math 모듈
        
        ```python
        import math
        
        a = 3.2 - 3.1
        b = 1.2 - 1.1
        
        print(math.isclose(a,b))    # True
        ```
        
        - 임의의 작은 수 활용
        
        ```python
        a = 3.2 - 3.1
        b = 1.2 - 1.1
        
        print(abs(a - b) <= 1e-10)    # True
        ```
        
    - 지수 표현 방식
        - e또는 E를 사용하여 표현
        
        ```python
        # 지수(제곱하는 횟수) 표현 10^
        # 314 * 0.01
        number = 314e-2
        
        print(type(number))    # float
        
        print(number)    # 3.14
        ```
- complex

### | Sequence Types❗

- 여러 개의 값들을 **순서대로 나열**하여 저장하는 자료형
- Sequence Types 특징
    - 순서(Sequence)
        - 값들이 순서대로 저장
        - 정렬X
    - 인덱싱(Indexing)
        - 각 값이 고유한 인덱스를 가지고 있음
        - 인덱스를 사용하여 특정 위치의 값을 선택하거나 수정할 수 있음
        
        ```python
        my_str = 'hello'
        
        print(my_str[1])    # e
        ```
        
    - 슬라이싱(Slicing)
        - 인덱스 범위를 조절해 부분적인 값을 추출할 수 있음
        
        ```python
        my_str = 'hello'
        
        print(my_str[2:4])    # ll
        print(my_str[0:5:2])    # hlo
        ```
        
    - 길이(Length)
        - len() 함수를 사용하여 저장된 값의 개수를 구할 수 있음
        
        ```python
        my_str = 'hello'
        
        print(len(my_str))    # 5
        ```
        
    - 반복(iteration)
        - 반복문을 사용하여 저장된 값들을 반복적으로 처리할 수 있음
- str(문자열)
    - 단일 문자나 여러 문자의 조합으로 이루어짐
    - ‘ 또는 “ 로 감싸서 표현
    - 문자열은 immutable
    - 중첩 따옴표
        - 작은 따옴표를 내부에 쓰려면 문자열을 큰 따옴표로 생성
        - 큰 따옴표를 내부에 쓰려면 문자열을 작은 따옴표로 생성
    - Escape sequence
        - \n - 줄바꿈
        - \t - 탭
        - \\ - 백슬래시
        - \’ - 작은 따옴표
        - \” - 큰 따옴표
        
        ```python
        print('철수야 \'안녕\'')
        # 철수야 '안녕'
        
        print('이 다음은 엔터\n입니다.')
        # 이 다음은 엔터
        # 입니다.
        ```
        
- String Interpolation
    - 문자열 내에 변수나 표현식을 삽입하는 방법
    - f-string
        - 문자열에 f 또는 F 접두어를 붙이고 표현식을 {표현식}로 작성하여 문자열에 파이썬 표현식의 값을 삽입 가능케 함
        
        ```python
        print('Debugging roaches 13 living room')
        # Debugging roaches 13 living room
        
        bugs = 'roaches'
        counts = 13
        area = 'living room'
        
        print(f'Debugging {bugs} {counts} {area}')
        print('Debugging {} {} {}'.format(bugs, counts, area))    # 예전 방법
        print('Debugging %s %d %s' % (bugs, counts, area))    # 예전 방법
        # Debugging roaches 13 living room
        
        # f-string 응용
        greeting = 'hi'
        print(f'{greeting:^10}')    # 10칸에서 가운데 정렬
        print(f'{greeting:>10}')    # 10칸에서 우측 정렬
        print(f'{3.141392:.4f}')    # 소숫점 자리 정하기 3.1414 
        ```
        
- list
    - 여러 개의 값을 순서대로 저장하는 **변경 가능한** 시퀀스 자료형
    
    ```python
    l = [1, 2, 3]
    l[0] = 100
    
    print(l)    # [100, 2, 3]
    ```
    
    - 0개 이상의 객체 포함
    - 대괄호([])로 표기
    - 어떤 자료형도 저장할 수 있음
    
    ```python
    l = []
    l1 = [1, 'a', 3, 'b', 5]
    l2 = [1, 2, 3, 'Python', ['hello', 'world', '!']]
    ```
    
    <img src = "https://github.com/yuj1818/TIL/assets/95585314/ac4ce534-cc96-4c21-b8c6-a5cfddb5afc1" width="30%" height="30%">
    
- tuple
    - 리스트와 동일하나 변경 불가능한 시퀀스 자료형
    
    ```python
    t = (1, 'a', 3, 'b', 5)
    
    t[1] = 'z'    # 'tuple' object does not support item assignment
    ```
    
    - 소괄호(())로 표기
    
    ```python
    t = ()
    t1 = (1,)    # 튜플 원소가 하나일 때 ','를 쓰지 않으면 연산 기호로 인식됨
    t2 = (1, 'a', 3, 'b', 5)
    ```
    
- range
    - 연속된 정수 시퀀스를 생성하는 변경 불가능한 자료형
    - range(n)
        - 0부터 n-1 까지의 숫자 시퀀스
        
        ```python
        r = range(5)
        
        print(list(r))    # [0, 1, 2, 3, 4]
        ```
        
    - range(n, m)
        - n부터 m-1 까지의 숫자 시퀀스
        
        ```python
        r = range(1, 10)
        
        print(list(r))    #[1, 2, 3, 4, 5, 6, 7, 8, 9]
        ```
        

### | Non-sequence Types

- dict
    - key-value 쌍으로 이루어진 **순서와 중복이 없는** 변경 가능한 자료형
    - key는 변경 불가능한 자료형만 사용 가능
    - value는 모든 자료형 사용 가능
    - 중괄호({})로 표기
    - key를 통해 value에 접근
    
    ```python
    my_dict = {'apple': 12, 'list': [1, 2, 3]}
    
    print(my_dict['apple'])    # 12
    print(my_dict['list'])    # [1, 2, 3]
    
    my_dict['apple'] = 100
    print(my_dict)    # {'apple': 100, 'list': [1, 2, 3]}
    ```
    
- set
    - 순서와 중복이 없는 변경 가능한 자료형
    - 중괄호({})로 표기
    
    ```python
    s = set()
    s1 = {1, 2, 3}
    s2 = {1, 1, 1}
    
    print(s)    # set()
    print(s1)    # {1, 2, 3}
    print(s2)    # {1} 중복 없음
    ```
    
    - 수학에서의 집합과 동일한 연산 처리 가능
    
    ```python
    s1 = {1, 2, 3}
    s2 = {3, 6, 9}
    
    # 합집합
    print(s1 | s2)    # {1, 2, 3, 6, 9}
    
    # 차집합
    print(s1 - s2)    # {1, 2}
    
    # 교집합
    print(s1 & s2)    # {3}
    ```
    

### | Other Types

- None
    - 파이썬에서 ‘값이 없음’을 표현하는 자료형
- Boolean
    - 참(True), 거짓(False) 표현
    - 비교 / 논리 연산의 평과 결과로 사용
    - 조건 / 반복문과 사용
    
    ```python
    b1 = True
    b2 = False
    
    print(b1)    # True
    print(b2)    # False
    print(3 > 1)    # True
    print('3' != 3)    # True
    ```
    

### | Collection

- 여러 개의 항목 또는 요소를 담는 자료 구조

| 컬렉션 | 변경 가능 여부 | 나열 순서 |
| --- | --- | --- |
| str | X | O |
| list | O | O |
| tuple | X | O |
| set | O | X |
| dict | O | X |
- 컬렉션의 차이점

<img src = "https://github.com/yuj1818/TIL/assets/95585314/740101f0-4e99-4aba-af2f-2823d0db1270" width="50%" height="50%">


## | Type Conversion

### | 암시적 형변환(Implicit Type Conversion)

- 파이썬이 자동으로 형변환을 하는 것

```python
print(3 + 5.0)    # 8.0

print(True + 3)    # 4

print(True + False)    # 1
```

### | 명시적 형변환(Explicit Type Conversion)

- 개발자가 직접 형변환을 하는 것
- 암시적 형변환이 아닌 경우를 모두 포함

```python
# str -> integer: 형식에 맞는 숫자만 가능
# integer -> str: 모두 가능

print(int('1'))    # 1

print(str(1) + '등')    # 1등

print(float('3.5'))    # 3.5

print(int(3.5))    # 3

print(int('3.5'))    # ValueError: invalid literal for int() with base 10: '3.5'
```

|  | str | list | tuple | range | set | dict |
| --- | --- | --- | --- | --- | --- | --- |
| str |  | O | O | X | O | X |
| list | O |  | O | X | O | X |
| tuple | O | O |  | X | O | X |
| range | O | O | O |  | O | X |
| set | O | O | O | X |  | X |
| dict | O | O(key만) | O(key만) | X | O(key만) |  |

## | 연산자

### | 산술 연산자

| 기호 | 연산자 | 우선 순위 |
| --- | --- | --- |
| - | 음수 부호 | 2 |
| + | 덧셈 | 4 |
| - | 뺄셈 | 4 |
| * | 곱셈 | 3 |
| / | 나눗셈 | 3 |
| // | 몫 | 3 |
| % | 나머지 | 3 |
| ** | 지수 | 1 |

### | 복합 연산자

| 기호 |  |  |
| --- | --- | --- |
| += | a += b | a = a + b |
| -= | a -= b | a = a - b |
| *= | a *= b | a = a * b |
| /= | a /= b | a = a / b |
| //= | a //= b | a = a // b |
| %= | a %= b | a = a % b |
| **= | a **= b | a = a ** b |

### | 비교 연산자

| 기호 | 내용 |
| --- | --- |
| < | 미만 |
| ≤ | 이하 |
| > | 초과 |
| ≥ | 이상 |
| == | 같음 |
| ≠ | 같지 않음 |
| is | 같음 |
| is not | 같지 않음 |
- is 비교 연산자 📙
    - 메모리 내에서 같은 객체를 참조하는지 확인
    - ==와 달리 주소를 비교
    - 되도록이면 None, True, False 등을 비교할 때 사용
    
    ```python
    print(2.0 == 2)    # True
    
    print(2.0 is 2)    # False
    ```
    

### | 논리 연산자

| 기호 | 연산자 | 내용 |
| --- | --- | --- |
| and | 논리곱 | 두 피연산자 모두 True인 경우에만 전체 표현식을 True로 평가 |
| or | 논리합 | 두 피연산자 중 하나라도 True인 경우 전체 표현식을 True로 평가 |
| not | 논리부정 | 단일 피연산자를 부정 |
- 단축 평가 📙
    - 논리 연산에서 두 번째 피연산자를 평가하지 않고 결과를 결정하는 동작
    
    ```python
    vowels = 'aeiou'
    
    print(('a' and 'b') in vowels)    # => 'b' in vowels => False
    print(('b' and 'a') in vowels)    # => 'a' in vowels => True
    
    print(3 and 5)    # 5
    print(3 and 0)    # 0
    print(0 and 3)    # 0
    print(0 and 0)    # 0
    
    print(5 or 3)    # 5
    print(3 or 0)    # 3
    print(0 or 3)    # 3
    print(0 or 0)    # 0
    ```
    
    - and
        - 첫 번째 피연산자가 False인 경우, 전체 표현식은 False로 결정
        - 두 번째 피연산자 평가X
        - 첫 번째 피연산자가 True인 경우, 전체 표현식은 두 번째 피연산자에 의해 결정
        - 두 번째 피연산자가 평가되고 그 결과가 전체 표현식의 결과로 반환
    - or
        - 첫 번째 피연산자가 True이면 전체 표현식을 True로 결정
        - 두 번째 피연산자 평가X
        - 첫 번째 피연산자가 Fasle이 경우, 전체 표현식은 두 번째 피연산자에 의해 결정
        - 두 번째 피연산자가 평가되고 그 결과가 전체 표현식의 결과로 반환
    - 코드 실행을 최적화하고, 불필요한 연산을 피할 수 있도록 함

### | 멤버십 연산자

- 특정 값이 시퀀스나 다른 컬렉션에 속하는지 여부를 확인
- in
    - 왼쪽 피연산자가 오른쪽 피연산자의 시퀀스에 속하는지 확인
- not in
    - 왼쪽 피연산자가 오른쪽 피연산자의 시퀀스에 속하지 않는지를 확인

### | 시퀀스형 연산자

- +와 *는 연산에서 산술 연산자일때와 다른 역할을 가짐
- + : 결합 연산자

```python
print('Gildong' + 'Hong')    # Gildong Hong

print([1, 2] + [3, 4])    # [1, 2, 3, 4]
```

- * : 반복 연산자

```python
print([1, 2] * 2)    # [1, 2, 1, 2]
```

### | 연산자 우선순위

| 우선순위 | 연산자 |
| --- | --- |
| 높음 | () |
|  | [] |
|  | ** |
|  | +, - |
|  | *, /, //, % |
|  | +, - |
|  | <, ≤, >, ≥, ==, ≠ |
|  | is, is not |
|  | in, not in |
|  | not |
|  | and |
| 낮음 | or |