# Day5_20230807

생성일: 2023년 8월 7일 오후 2:05

# 문자열(String)

## 문자의 표현

- 네트워크가 발전되기 전 미국의 각 지역 별로 코드 체계가 존재
- 네트워크가 발전하면서 서로 간에 정보를 주고 받을 때, 정보를 달리 해석한다는 문제가 발생
- 혼동을 피하기 위해 표준안 ASCII(American Standard Code for Information Interchange) 제정
- ASCII
    - 7bit 인코딩으로 128문자를 표현하며, 3개의 출력 불가능한 제어 문자들과 공백을 비롯한 95개의 출력 가능한 문자들로 이루어져 있음
    
    <img src="https://github.com/yuj1818/TIL/assets/95585314/3ef96f80-b498-41d1-a1ae-003edab5e784" />
    
- 확장 아스키
    - 표준 문자 이외의 악센트 문자, 도형 문자, 특수 문자, 특수 기호 등 부가적인 문자를 128개 추가할 수 있게 하는 부호
    - 1B 내의 8bit를 모두 사용함으로써 추가적인 문자 표현 가능
    - 표준 아스키는 마이크로컴퓨터 하드웨어 및 소프트웨어 사이에서 세계적으로 통용되는 데 비해, 확장 아스키는 프로그램이나 컴퓨터 또는 프린터가 그것을 해독할 수 있도록 설계되어 있어야만 올바로 해독 가능
    
    <img src="https://github.com/yuj1818/TIL/assets/95585314/3b562896-9888-41de-8581-1cb494e9bad4" />
    
- 오늘날 대부분의 컴퓨터는 문자를 읽고 쓰는데 ASCII 형식을 사용
- 컴퓨터가 발전하며 각 국가들은 자국의 문자를 표현하기 위해 코드 체계를 만들어서 사용
- 자국의 코드 체계를 타 국가가 가지고 있지 않으면 정보 해석이 올바르지 못하기 때문에 다국어 처리를 위해 유니코드라는 표준을 마련
- 유니코드
    - Character Set으로 분류
        - UCS-2
        - UCS-4
    - 유니코드를 저장하는 변수의 크기를 정의
    - 바이트 순서에 대해서 표준화 하지 못함
    - 파일을 인식 시, 이 파일이 UCS-2, UCS-4인지 인식하고 각 경우를 구분해서 모두 다르게 구현해야 하는 문제 발생
    - 유니 코드의 적당한 외부 인코딩이 필요해짐
    - 유니코드 인코딩(UTF: Unicode Transformation Format)
        - UTF-8(in web)
            - MIN: 8bit, MAX: 32bit
        - UTF-16(in windows, java)
            - MIN: 16bit, MAX: 32bit
        - UTF-32(in unix)
            - MIN: 32bit, MAX: 32bit
- Python 인코딩
    - 2.X 버전
        - ASCII → #-*- coding: utf-8 -*-
    - 3.X 버전
        - 유니코드 UTF-8 → 생략 가능
    - 다른 인코딩 방식으로 처리 시 첫 줄에 작성하는 위 항목에 원하는 인코딩 방식을 지정해주면 됨

## 문자열의 분류

<img src="https://github.com/yuj1818/TIL/assets/95585314/fc9458a5-8f44-4193-9f6a-b7ad905ea733" />

### java에서의 문자열

- 기본적인 메타 데이터 외에도 네 가지 필드들이 포함
    - hash값, 문자열의 길이, 문자열 데이터의 시작점, 문자열 배열에 대한 참조
- 문자열 데이터를 저장, 처리해주는 클래스를 제공
- String 클래스를 사용

```java
String str = "abc";
String str = new String("abc");
```

- 문자열 처리에 필요한 연산을 연산자, 메소드 형태로 제공
    - +, length(), replace(), spilt(), substring() 등

### C언어에서의 문자열

- 문자열은 문자들의 배열 형태로 구현된 응용 자료형
- 문자배열에 문자열을 저장할 때는 항상 마지막에 끝을 표시하는 널문자(’\0’)를 넣어줘야 함

```c
char ary[]={'a', 'b', 'c', '\0'};
char ary[]="abc";
```

- 문자열 처리에 필요한 연산을 함수 형태로 제공
    - strlen(), strcpy(), strcmp() 등

### Python에서의 문자열 처리

- char 타입 없음
- 텍스트 데이터의 취급 방법이 통일되어 있음
- 문자열 기호
    - ‘, “, ‘’’, ‘’’’’’
    - + 연결(Concatenation)
    - * 반복
- 문자열은 시퀀스 자료형으로 분류되고, 시퀀스 자료형에서 사용할 수 있는 인덱싱, 슬라이싱 연산들을 사용할 수 있음
- 문자열 클래스에서 제공되는 메소드
    - replace(), split(), isalpha(), find()
- 문자열은 튜플과 같이 요소값을 변경할 수 없음(immutable)

| c | java | python |
| --- | --- | --- |
| 아스키 코드로 저장 | 유니코드(UTF16)로 저장 | 유니코드(UTF8)로 저장 |

## 문자열 뒤집기

- 자기 문자열에서 뒤집는 방법이 있고 새로운 빈 문자열을 만들어 소스의 뒤에서부터 읽어서 타겟에 쓰는 방법 2가지 존재
- 자기 문자열을 이용할 경우는 swap을 위한 임시 변수가 필요하며 반복 수행을 문자열 길이의 반만을 수행해야 함

### python에서 문자열 뒤집기

```python
s = 'abcd'
print(s[::-1])    # dcba
s = list(s)
s.reverse()
s = ''.join(s)
print(s)    # dcba
```

```python
s = 'abcd'
s = list(s)
for i in range(len(s) // 2):
	s[i], s[-i - 1] = s[-i - 1], s[i]
print(''.join(s))    # dcba
```

## 문자열 비교

- c
    - strcmp() 함수 제공
- java
    - equals() 메소드 제공
- python
    - == 연산자, is 연산자 제공
    - == 연산자는 내부적으로 특수 메서드 ‘__eq__()’ 호출

```python
s1 = 'abc'
s_list = ['abc', 'def', s1, s1[:2] + 'c']
for s in s_list:
	print(s1 == s)
	print(s1 is s)
'''
True
True
False
False
True
True
True
False
'''
```

## 문자열 숫자를 정수로 변환하기

- c
    - atoi() 함수 제공
    - 역 함수 itoa()
- java
    - 숫자 클래스의 parse 메소드 제공
    - Integer.parseInt(String)
    - 역함수 toString()
- python
    - 숫자와 문자변환 함수 제공
    - int, float, str, repr
    
    ```python
    def atoi(s):
        i = 0
        for x in s:
            i = i * 10 + ord(x) - ord('0')
        return i
    ```
    
    ```python
    def itoa(n):
        i = ''
        sig = ''
        if n < 0:
            sig = '-'
            n *= -1
        while n > 9:
            i = chr(n % 10 + ord('0')) + i
            n = n // 10
        return sig + chr(n + ord('0')) + i
    ```