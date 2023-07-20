# 반복문(Loop Statement)

- 주어진 코드 블록을 여러 번 반복해서 실행하는 구문
- 특정 작업을 반복적으로 수행
- 주어진 조건이 참인 동안 반복해서 실행

## for statement

- 반복 횟수가 명확하게 정해져 있는 경우에 유용
- 리스트, 튜플, 문자열 등과 같은 시퀀스 형식의 데이터 처리할 때 유용

```python
# for statement 기본 구조

for 변수 in 반복 가능한 객체:    # 변수는 단수형, iterable은 복수형으로 쓰는 것이 좋음
	코드 블록                     # ex) for book in books:
```

### for

- 임의의 시퀀스의 항목들을 그 시퀀스에 들어있는 순서대로 반복

### 반복 가능한 객체(iterable)

- 반복문에서 순회할 수 있는 객체
- 시퀀스 객체, dict, set 등

### for 문 원리

- 리스트 내 첫 항목이 반복 변수에 할당되고 코드 블록이 실행
- 다음으로 반복 변수에 리스트의 2번째 항목이 할당되고 코드 블록이 다시 실행
- (중략…) 마지막으로 반복 변수에 리스트의 마지막 요소가 할당되고 코드블록이 실행

```python
items = ['apple', 'banana', 'coconut']

for item in items:
	print(item)

"""
apple
banana
coconut
"""
```

### 문자열 순회

```python
country = 'Korea'

for c in country:
	print(c)

"""
K
o
r
e
a
"""
```

### range 순회

```python
for i in range(5):
	print(i)

"""
0
1
2
3
4
"""
```

### 인덱스로 리스트 순회

```python
numbers = [4, 6, 10, -8, 5]

for i in range(len(numbers)):
	number[i] = numbers[i] * 2

print(numbers)    # [8, 12, 20, -16, 10]
```

### 중첩된 반복문

```python
outers = ['A', 'B']
inners = ['c', 'd']

for outer in outers:
	for inner in inners:
		print(outer, inner)

"""
A c
A d
B c
B d
"""
```

### 중첩 리스트 순회

```python
elements = [['A', 'B'], ['c', 'd']]

for el in elements:
	print(el)

"""
['A', 'B']
['c', 'd']
"""
```

```python
elements = [['A', 'B'], ['c', 'd']]

for el in elements:
	for item in el:
		print(item)

"""
A
B
c
d
"""
```

## while statement

- ⚠ 반드시 **종료 조건**이 필요 📙
- 반복 횟수가 불명확하거나 조건에 따라 반복을 종료해야 할 때 유용
- 사용자의 입력을 받아서 특정 조건이 충족될 때까지 반복하는 경우

### while

- 주어진 조건식이 참(True)인 동안 코드를 반복해서 실행
- 조건식이 거짓(False)가 될 때 까지 반복

```python
# while statement 기본 구조

while 조건식:
	코드 블록
```

```python
# while 반복문 예시

a = 0

while a < 3:
	print(a)
	a += 1

print('끝')

"""
0
1
2
끝
"""
```

### 사용자 입력에 따른 반복

```python
number = int(input('양의 정수를 입력해주세요.: '))

while number <= 0:
	if number < 0:
		print('음수를 입력했습니다.')
	else:
		print('0은 양의 정수가 아닙니다.')

	number = int(input('양의 정수를 입력해주세요.: '))

print('잘했습니다!')

"""
양의 정수를 입력해주세요.: 0
0은 양의 정수가 아닙니다.
양의 정수를 입력해주세요.: -1
음수를 입력했습니다.
양의 정수를 입력해주세요.: 1
잘했습니다!
"""
```

## 반복 제어

- for문과 while은 매 반복마다 본문 내 모든 코드를 실행하지만 때때로 일부만 실행하는 것이 필요할 때가 있음

### break

- 반복을 즉시 중지

```python
# break 예시 1

number = int(input('양의 정수를 입력해주세요.: '))    # ① 사용자 입력

while number <= 0:    # ② 조건 만족
	if number == -9999:    # ③ 조건 만족
		print('프로그램을 종료합니다.')    # ④ 출력
		break    # ⑤ break가 있으므로 반복문에서 빠져나감

	if number < 0:
		print('음수를 입력했습니다.')
	else:
		print('0은 양의 정수가 아닙니다.')

	number = int(input('양의 정수를 입력해주세요.: '))

print('잘했습니다!')    # ⑥ 출력

"""
양의 정수를 입력해주세요.: -9999
프로그램을 종료합니다.
잘했습니다!
"""
```

```python
# break 예시 2 

numbers = [1, 3, 5, 6, 7, 9, 10, 11]
found_even = False

for num in numbers:    # ① num = 1 ③ num = 3 ⑤ num = 5 ⑦ num = 6
	if num % 2 == 0:    # ② 1 % 2 != 0, 조건 불만족 ④ 3 % 2 != 0, 조건 불만족
                      # ⑥ 5 % 2 != 0, 조건 불만족 ⑧ 6 % 2 == 0, 조건 만족
    print('첫 번째 짝수를 찾았습니다:', num)    # ⑨ 출력
		found_even = True    # ⑩ found_even = False => True
		break    # ⑪ break를 만났으므로 반복문에서 빠져나감

if not found_even:    # ⑫ 조건 불만족
	print('짝수를 찾지 못했습니다')

"""
첫 번째 짝수를 찾았습니다: 6
"""
```

### continue 📙

- 다음 반복으로 건너뜀

```python
# continue 예시 📙

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:    # (1)num = 1  (4)num = 2  (7)num = 3  (10)num = 4 (13)num = 5 
                       # (16)num = 6 (19)num = 7 (22)num = 8 (25)num = 9 (28)num = 10
	if num % 2 == 0:    # (2)1 % 2 != 0, 조건 불만족 (5)2 % 2 == 0, 조건 만족
											# (8)3 % 2 != 0, 조건 불만족 (11)4 % 2 == 0, 조건 만족
											# (14)5 % 2 != 0, 조건 불만족 (17)6 % 2 == 0, 조건 만족
											# (20)7 % 2 != 0, 조건 불만족 (23)8 % 2 == 0, 조건 만족
											# (26)9 % 2 != 0, 조건 불만족 (29)10 % 2 == 0, 조건 만족
		continue    # (6, 12, 18, 24, 30)continue를 만났으므로 뒷 코드 건너뛰고 다음 반복으로 넘어감
	print(num)    #  (3)1 출력 (9)3 출력 (15)5 출력 (21)7 출력 (27)9 출력

"""
1
3
5
7
9
"""
```

### break와 continue 주의 사항

- break와 continue를 남용하는 것은 가독성을 저하시킴
- 특정한 종료 조건을 만들어 break를 대신하거나, if 문을 사용하여 continue처럼 코드를 건너 뛸 수도 있음
- 약간의 시간이 들더라도 가능한 코드의 가독성을 유지하고 코드의 의도를 명확하게 작성하도록 노력하는 것이 중요

## List Comprehension

- 간결하고 효율적인 리스트 생성 방법
- ⚠ 가독성이 안 좋아질 수 있기 때문에 comprehension을 남용하면 안됨

```python
# list comprehension 구조

[expression for 변수 in iterable]

list(expression for 변수 in iterable)
```

```python
# list comprehension 사용 전

numbers = [1, 2, 3, 4, 5]
squared_numbers = []

for num in numbers:
    squared_numbers.append(num ** 2)
    
print(squred_numbers)    # [1, 4, 9, 16, 25]
```

```python
# list comprehension 사용 후

numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]

print(squred_numbers)    # [1, 4, 9, 16, 25]
```

### List Comprehension과 if 조건문

```python
[expression for 변수 in iterable if 조건식]

list(expression for 변수 in iterable if 조건식)
```

## 참고

### enumerate

- iterable 객체의 각 요소에 대해 **인덱스와 함께 반환**하는 내장함수
- enumerate(iterable, start = 0)

```python
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(f'인덱스 {index}: {fruit}')

"""
인덱스 0: apple
인덱스 1: banana
인덱스 2: cherry
"""
```