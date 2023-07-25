# Data Structure

- 여러 데이터를 효과적으로 사용, 관리하기 위한 구조
- 각 데이터의 효율적인 저장, 관리를 위한 구조를 나눠 놓은 것

## 메서드(Method)

- 객체에 속한 함수
- 함수 > 메서드
- `객체`의 상태를 조작하거나 동작을 수행
- 메서드는 클래스(class) 내부에 정의되는 함수
- 클래스는 파이썬에서 ‘타입을 표현하는 방법’이며 은연중에 사용해왔음
- 메서드는 각 데이터 타입별로 다양한 기능을 가진 메서드가 존재
- `객체` : 객관적인 실체

### 메서드 호출 방법

- 데이터 타입 객체. 메서드()
    
    ```python
    # 문자열 메서드
    'hello'.capitalize()    # Hello
    
    # 리스트 메서드
    numbers = [1, 2, 3]
    numbers.append(4)
    
    print(numbers)    # [1, 2, 3, 4]
    ```
    

## 시퀀스 데이터 구조

### Sequence Types

- 여러 개의 값들을 순서대로 나열하여 저장하는 자료형
- [Sequence Types 특징](./data_types.md#sequence-types❗)

### 문자열

#### 문자열 조회/탐색 및 검증 메서드

| 메서드 | 설명 |
| --- | --- |
| s.find(x) | x의 첫 번째 위치를 반환. 없으면, -1을 반환 |
| s.index(x) | x의 첫 번째 위치를 반환. 없으면, 오류 발생 |
| s.isalpha() | 알파벳 문자 여부
* 단순 알파벳이 아닌 유니코드 상 letter |
| s.isupper() | 대문자 여부 |
| s.islower() | 소문자 여부 |
| s.istitle() | 타이틀 형식 여부 |
- .find(x)
    - x의 첫 번째 위치를 반환. 없으면, -1을 반환
    
    ```python
    print('banana'.find('a'))    # 1
    print('banana'.find('z'))    # -1
    ```
    
- .index(x)
    - x의 첫 번째 위치를 반환. 없으면, 오류 발생
    
    ```python
    print('banana'.index('a'))    # 1
    print('banana'.index('z'))    # ValueError: substring not found
    ```
    
- .isupper(x) / .islower(x)
    - 문자열이 모두 대문자/소문자로 이루어져 있는지 확인
    
    ```python
    string1 = 'HELLO'
    string2 = 'Hello'
    
    print(string1.isupper())    # True
    print(string2.isupper())    # False
    print(string1.islower())    # False
    print(string2.islower())    # False
    ```
    
- .isalpha(x)
    - 문자열이 알파벳으로만 이루어져 있는지 확인
    
    ```python
    string1 = 'Hello'
    string2 = '123'
    print(string1.isalpha())    # True
    print(string2.isalpha())    # False
    ```
    

#### 문자열 조작 메서드 (새 문자열 반환)

| 메서드 | 설명 |
| --- | --- |
| s.replace(old, new[,count]) | 바꿀 대상 글자를 새로운 글자로 바꿔서 반환 |
| s.strip([chars]) | 공백이나 특정 문자를 제거 |
| s.split(sep=None, maxsplit=-1) | 공백이나 특정 문자를 기준으로 분리 |
| ‘separator’.join([iterable]) | 구분자로 iterable을 합침 |
| s.capitalize() | 가장 첫 번째 글자를 대문자로 변경 |
| s.title() | 문자열 내 띄어쓰기 기준으로 각 단어의 첫 글자는 대문자로, 나머지는 소문자로 변환 |
| s.upper() | 모두 대문자로 변경 |
| s.lower() | 모두 소문자로 변경 |
| s.swapcase() | 대 ↔ 소문자 서로 변경 |
- .replace(old, new[,count])
    - 바꿀 대상 글자를 새로운 글자로 바꿔서 반환
    
    ```python
    text = 'Hello, world!'
    new_text = text.replace('world', 'Python')
    print(new_text)    # Hello, Python!
    ```
    
- .strip([chars])
    - 문자열의 시작과 끝에 있는 공백이나 특정 문자를 제거
    
    ```python
    text = '    Hello, world!    '
    new_text = text.strip()
    print(new_text)    # 'Hello, world!'
    ```
    
- .split(sep=None, maxsplit=-1)
    - 지정한 문자를 구분자로 문자열을 분리하여 문자열의 리스트로 반환
    
    ```python
    text = 'Hello, world!'
    words = text.split(',')
    print(words)    # ['Hello', ' world!']
    ```
    
- ‘separator’.join([iterable])
    - iterable 요소들을 원래의 문자열을 구분자로 이용하여 하나의 문자열로 연결
    
    ```python
    words = ['Hello', 'world!']
    text = '-'.join(words)
    print(text)    # Hello-world!
    ```
    
- 그 외
    
    ```python
    text = 'heLLo, woRld!'
    new_text1 = text.capitalize()
    new_text2 = text.title()
    new_text3 = text.upper()
    new_text4 = text.swapcase()
    
    print(new_text1)    # Hello, world!
    print(new_text2)    # Hello, World!
    print(new_text3)    # HELLO, WORLD!
    print(new_text4)    # HEllO, WOrLD!
    ```
    
- 메서드는 이어서 사용 가능
    
    ```python
    text = 'heLLo, woRld!'
    
    new_text = text.swapcase().replace('l', 'z')
    
    print(new_text)    # HELLO, WOrLD! => HEzzO, WOrLD!
    ```
    

### 리스트

#### 리스트 값 추가 및 삭제 메서드

| 메서드 | 설명 |
| --- | --- |
| L.append(x) | 리스트 마지막에 항목 x를 추가 |
| L.extend(m) | iterable m의 모든 항목들을 리스트 끝에 추가 |
| L.insert(i, x) | 리스트 인덱스 i에 항목 x를 삽입 |
| L.remove(x) | 리스트 가장 왼쪽에 있는 항목(첫 번째) x를 제거
항목이 존재하지 않을 경우, ValueError |
| L.pop() | 리스트 가장 오른쪽에 있는 항목(마지막)을 반환 후 제거 |
| L.pop(i) | 리스트의 인덱스 i에 있는 항목을 반환 후 제거 |
| L.clear() | 리스트의 모든 항목 제거 |
- .append(x)
    - 리스트 마지막에 항목 x를 추가
    
    ```python
    my_list = [1, 2, 3]
    my_list.append(4)
    print(my_list)    # [1, 2, 3, 4]
    ```
    
- .extend(iterable)
    - 리스트에 다른 반복 가능한 객체의 모든 항목을 추가
    
    ```python
    my_list = [1, 2, 3]
    my_list.extend([4, 5, 6])
    print(my_list)    # [1, 2, 3, 4, 5, 6]
    ```
    
- .insert(i, x)
    - 리스트의 지정한 인덱스 i 위치에 항목 x를 삽입
    
    ```python
    my_list = [1, 2, 3]
    my_list.insert(1, 5)
    print(my_list)    # [1, 5, 2, 3]
    ```
    
- .remove(x)
    - 리스트에서 첫 번째로 일치하는 항목을 삭제
    
    ```python
    my_list = [1, 2, 3, 2]
    my_list.remove(2)
    print(my_list)    # [1, 3, 2]
    ```
    
- .pop(i)
    - 리스트에서 지정한 인덱스의 항목을 제거하고 반환
    - 작성하지 않을 경우 마지막 항목을 제거
    
    ```python
    my_list = [1, 2, 3, 4, 5]
    
    item1 = my_list.pop()
    item2 = my_list.pop(0)
    
    print(item1)    # 5
    print(item2)    # 1
    print(my_list)    # [2, 3, 4]
    ```
    
- .clear()
    - 리스트의 모든 항목을 삭제
    
    ```python
    my_list = [1, 2, 3]
    my_list.clear()
    prnit(my_list)    # []
    ```
    

#### 리스트 탐색 및 정렬 메서드

| 문법 | 설명 |
| --- | --- |
| L.index(x, start, end) | 리스트에 있는 항목 중 가장 왼쪽에 있는 항목 x의 인덱스를 반환 |
| L.reverse() | 리스트를 거꾸로 나열 |
| L.sort() | 리스트를 정렬(매개 변수 이용 가능) |
| L.count(x) | 리스트에서 항목 x의 개수를 반환 |
- .index(x)
    - 리스트에서 첫 번째로 일치하는 항목의 인덱스를 반환
    
    ```python
    my_list = [1, 2, 3]
    index = my_list.index(2)
    print(index)    # 1
    ```
    
- .count(x)
    - 리스트에서 항목 x가 등장하는 횟수를 반환
    
    ```python
    my_list = [1, 2, 2, 3, 3, 3]
    count = my_list.count(3)
    print(count)    # 3
    ```
    
- .sort()
    - 원본 리스트를 오름차순으로 정렬
    
    ```python
    my_list = [3, 2, 1]
    
    print(sorted(my_list))    # [1, 2, 3]
    print(my_list)    # [3, 2, 1]
    
    my_list.sort()
    
    print(my_list)    # [1, 2, 3]
    print(my_list.sort())    # None
    
    my_list.sort(reverse=True)
    print(my_list)    # [3, 2, 1]
    ```
    
- .reverse()
    - 리스트의 순서를 역순으로 변경(정렬 x)
    
    ```python
    my_list = [1, 3, 2, 8, 1, 9]
    my_list.reverse()
    print(my_list)    # [9, 1, 8, 2, 3, 1]
    ```

## 비시퀀스 데이터 구조

### set

- 고유한 항목들의 **정렬되지 않은** 컬렉션

#### 세트 관련 메서드

| 메서드 | 설명 |
| --- | --- |
| s.add(x) | 세트 s에 항목 x를 추가.
이미 x가 있다면 변화 없음 |
| s.clear() | 세트 s의 모든 항목을 제거 |
| s.remove(x) | 세트 s에서 항목 x를 제거
항목 x가 없을 경우 key error |
| s.pop() | 세트 s에서 랜덤하게 항목을 반환하고, 해당 항목을 제거 |
| s.discard(x) | 세트 s에서 항목 x를 제거 |
| s.update(iterable) | 세트 s에 다른 iterable 요소를 추가 |
- .add(x)
    - 세트에 x를 추가
    
    ```python
    my_set = {1, 2, 3}
    my_set.add(4)
    print(my_set)    # {1, 2, 3, 4}
    
    my_set.add(4)
    print(my_set)    # {1, 2, 3, 4}
    ```
    
- .clear()
    - 세트의 모든 항목을 제거
    
    ```python
    my_set = {1, 2, 3}
    my_set.clear()
    print(my_set)    # set()
    ```
    
- .remove(x)
    - 세트에서 항목 x를 제거
    
    ```python
    my_set = {1, 2, 3}
    my_set.remove(2)
    print(my_set)    # {1, 3}
    
    my_set.remove(10)
    print(my_set)    # KeyError
    ```
    
- .discard(x)
    - 세트 s에서 항목 x를 제거. remove와 달리 에러 없음
    
    ```python
    my_set = {1, 2, 3}
    my_set.discard(2)
    print(my_set)    # {1, 3}
    
    my_set.discard(10)
    ```
    
- .pop()
    - 세트에서 **임의의 요소**를 제거하고 반환
    
    ```python
    my_set = {1, 2, 3}
    element = my_set.pop()
    
    print(element)    # 1
    print(my_set)    # {2, 3}
    ```
    
- .update(iterable)
    - 세트에 다른 iterable 요소를 추가
    
    ```python
    my_set = {1, 2, 3}
    my_set.update([4, 5, 1])
    print(my_set)    # {1, 2, 3, 4, 5}
    ```
    

#### 세트의 집합 메서드

| 메서드 | 설명 | 연산자 |
| --- | --- | --- |
| set1.difference(set2) | set1에는 들어있지만 set2에는 없는 항목으로 세트를 생성 후 반환 | set1 - set2 |
| set1.itersection(set2) | set1과 set2에 모두 들어있는 항목으로 세트를 생성 후 반환 | set1 & set2 |
| set1.issubset(set2) | set1의 항목이 모두 set2에 들어있으면 True를 반환 | set1 ≤ set2 |
| set1.issuperset(set2) | set1가 set2의 항목을 모두 포함하면 True를 반환 | set1 ≥ set2 |
| set1.union(set2) | set1 또는 set2에(혹은 둘 다) 들어있는 항목으로 세트를 생성 후 반환 | set1 | set2 |

```python
set1 = {0, 1, 2, 3, 4}
set2 = {1, 3, 5, 7, 9]

print(set1.difference(set2))    # {0, 2, 4}
print(set1.intersection(set2))    # {1, 3}
print(set1.issubset(set2))    # False
print(set1.issuperset(set2))    # False
print(set1.union(set2))    # {0, 1, 2, 3, 4, 5, 7, 9}
```

### dictionary

- 고유한 항목들의 정렬되지 않은 컬렉션

#### 딕셔너리 메서드

| 메서드 | 설명 |
| --- | --- |
| D.clear() | 딕셔너리 D의 모든 키/값 쌍을 제거 |
| D.get(k) | 키 k에 연결된 값을 반환(키가 없으면 None 반환) |
| D.get(k, v) | 키 k에 연결된 값을 반환하거나 키가 없으면 기본 값으로 v 반환 |
| D.keys() | 딕셔너리 D의 키를 모은 객체를 반환 |
| D.values() | 딕셔너리 D의 값을 모은 객체를 반환 |
| D.items() | 딕셔너리 D의 키/값 쌍을 모은 객체를 반환 |
| D.pop(k) | 딕셔너리 D에서 키 k를 제거하고 연결됐던 값을 반환(없으면 오류) |
| D.pop(k, v) | 딕셔너리 D에서 키 k를 제거하고 연결됐던 값을 반환(없으면 v 반환) |
| D.setdefault(k) | 딕셔너리 D에서 키 k와 연결된 값을 반환 |
| D.setdefault(k, v) | 딕셔너리 D에서 키 k와 연결된 값을 반환
k가 D의 키가 아니면 값 v와 연결한 키 k를 D에 추가하고 v를 반환 |
| D.update(other) | other 내 각 키에 대해 D에 있는 키면 D에 있는 그 키의 값을 other에 있는 값으로 대체.
other에 있는 각 키에 대해 D에 없는 키면 키/값 쌍을 D에 추가 |
- .clear()
    - 딕셔너리 D의 모든 키/값 쌍을 제거
    
    ```python
    person = {'name': 'Alice', 'age': 25}
    person.clear()
    print(person)    # {}
    ```
    
- .get(key[, default])
    - 키 연결된 값을 반환하거나 키가 없으면 None 혹은 기본 값을 반환
    
    ```python
    person = {'name': 'Alice', 'age': 25}
    
    print(person.get('name'))    # Alice
    print(person.get('country'))    # None
    print(person.get('country', 'Unknown'))    # Unknown
    ```
    
- .keys()
    - 딕셔너리 키를 모은 객체를 반환
    
    ```python
    person = {'name': 'Alice', 'age': 25}
    print(person.keys())    # dict_keys(['name', 'age'])
    
    for k in person.keys():
        print(k)
    
    """
    name
    age
    """
    ```
    
- .values()
    - 딕셔너리 값을 모은 객체를 반환
    
    ```python
    person = {'name': 'Alice', 'age': 25}
    print(person.keys())    # dict_keys(['name', 'age'])
    
    for v in person.values():
        print(v)
    
    """
    Alice
    25
    """
    ```
    
- .items()
    - 딕셔너리 키/값 쌍을 모은 객체를 반환
    
    ```python
    person = {'name': 'Alice', 'age': 25}
    
    print(person.items())    # dict_items([('name', 'Alice'), ('age', 25)])
    for k,v in person.items():
        print(k, v)
    """
    name Alice
    age 25
    """
    ```
    
- .pop(key[, default])
    - 키를 제거하고 연결됐던 값을 반환(없으면 에러나 default를 반환)
    
    ```python
    person = {'name': 'Alice', 'age': 25}
    
    print(person.pop('age'))    # 25
    print(person)    # {'name': 'Alice'}
    print(person.pop('country', None))    # None
    print(person.pop('country'))    # KeyError
    ```
    
- .setdefault(key[, default])
    - 키와 연결된 값을 반환
    - 키가 없다면 default와 연결한 키를 딕셔너리에 추가하고 default를 반환
    
    ```python
    person = {'name': 'Alice', 'age': 25}
    
    print(person.setdefault('country', 'KOREA'))    # KOREA
    print(person)    # {'name': 'Alice', 'age': 25, 'country': 'KOREA'}
    ```
    
- .update([other])
    - other가 제공하는 키/값 쌍으로 딕셔너리를 갱신
    - 기존 키는 덮어씀
    
    ```python
    person = {'name': 'Alice', 'age': 25}
    other_person = {'name': 'Jane', 'gender': 'Female'}
    
    person.update(other_person)
    print(person)   # {'name': 'Jane', 'age': 25, 'gender': 'Female'}
    
    person.update(age=50)
    print(person)   # {'name': 'Jane', 'age': 50, 'gender': 'Female'}
    
    person.update(country='KOREA')
    print(person)   # {'name': 'Jane', 'age': 25, 'gender': 'Female', 'country': 'KOREA'}
    ```
    
- key 사용, get() 사용, setdefault() 사용 비교
    
    ```python
    # 혈액형 인원수 세기
    # 결과 => {'A': 3, 'B': 3, 'O': 3, 'AB': 3}
    
    blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
    
    #[]
    new_dict = {}
    
    for blood_type in blood_types:
        if blood_type in new_dict.keys():
            new_dict[blood_type] += 1
        else:
            new_dict[blood_type] = 1
    
    print(new_dict)    # {'A': 3, 'B': 3, 'O': 3, 'AB': 3}
    
    # .get()
    new_get_dict = {}
    
    for blood_type in blood_types:
        new_get_dict[blood_type] = new_get_dict.get(blood_type, 0) + 1
    
    print(new_get_dict)    # {'A': 3, 'B': 3, 'O': 3, 'AB': 3}
    
    # .setdefault()
    new_set_dict = {}
    
    for blood_type in blood_types:
        new_set_dict.setdefault(blood_type, 0)
        new_set_dict[blood_type] += 1
    
    print(new_set_dict)    # {'A': 3, 'B': 3, 'O': 3, 'AB': 3}
    ```
    

## 복사

### 데이터 타입과 복사

- 파이썬에서는 데이터에 분류에 따라 복사가 달라짐
- “변경 가능한 데이터 타입”과 “변경 불가능한 데이터 타입”을 다르게 다룸

#### 변경 가능한 데이터 타입의 복사

```python
a = [1, 2, 3, 4]
b = a
b[0] = 100

print(a)    # [100, 2, 3, 4]
print(b)    # [100, 2, 3, 4]
```

<img src = "https://github.com/yuj1818/TIL/assets/95585314/557cfeb1-965e-4853-a958-66f00d0f9656">

#### 변경 불가능한 데이터 타입의 복사

```python
a = 20
b = a
b = 10

print(a)    # 20
print(b)    # 10
```

<img src = "https://github.com/yuj1818/TIL/assets/95585314/564dcafa-0080-4921-bed4-9c0d7cb09ddc">

### 복사 유형

#### 할당(Assignment)

```python
# 리스트 복사 예시

original_list = [1, 2, 3]
copy_list = original_list
print(original_list, copy_list)    # [1, 2, 3] [1, 2 ,3]

copy_list[0] = 'hi'
print(original_list, copy_list)    # ['hi', 2, 3] ['hi', 2, 3]
```

 > 할당 연산자(=)를 통한 복사는 해당 객체에 대한 객체 참조를 복사

#### 얕은 복사(Shallow Copy)

```python
# 리스트 얕은 복사 예시

a = [1, 2, 3]
b = a[:]
print(a, b)    # [1, 2, 3] [1, 2, 3]

b[0] = 100
print(a, b)    # [1, 2, 3] [100, 2, 3]
```

 > 슬라이싱을 통해 생성된 객체는 원본 객체와 독립적으로 존재

```python
# 얕은 복사의 한계
# 2차원 리스트와 같이 변경가능한 객체 안에 변경 가능한 객체가 있는 경우

g = [1, 2, [3, 4]]
h = g[:]

g[2][0] = 30

print(g, h)    # [1, 2, [30, 4]] [1, 2, [30, 4]]
```

<img src = "https://github.com/yuj1818/TIL/assets/95585314/fdaa2f28-f325-4689-b874-c306318bc9f7" width="50%" height="50%">

 > a와 b의 주소는 다르지만 내부 객체의 주소는 같기 때문에 함께 변경됨

#### 깊은 복사(Deep Copy)

```python
# 리스트 깊은 복사 예시

import copy

original_list = [1, 2, [1, 2]]
deep_copied_list = copy.deepcopy(original_list)

deep_copied_list[2][0] = 100

print(original_list)    # [1, 2, [1, 2]]
print(deep_copied_list)    # [1, 2, [100, 2]]
```

 > 내부에 중첩된 모든 객체까지 새로운 객체 주소를 참조하도록 함

## 참고

### 문자열에 포함된 문자들의 유형을 판별하는 메서드

- isdecimal()
    - 문자열이 모두 숫자 문자(0~9)로만 이루어져 있어야 True
- isdigit()
    - isdecimal()과 비슷하지만, 유니코드 숫자도 인식(’①’도 숫자로 인식)
- isnumeric()
    - isdigit()과 유사하지만, 몇 가지 추가적인 유니코드 문자들을 인식
    - 분수, 지수, 루트 기호도 숫자로 인식

### 해시 테이블 (Hash Table)

- 데이터를 효율적으로 저장하고 검색하기 위해 사용되는 자료 구조

- 키-값 쌍을 연결하여 저장하는 방식

- 키를 해시 함수를 통해 해시 값으로 변환하고, 이 해시 값을 인덱스로 사용하여 데이터를 저장하거나 검색
  - 이렇게 하면 데이터의 검색이 매우 빠르게 이루어짐

- 파이썬에서 세트의 요소와 딕셔너리의 키는 해시 테이블을 이용하여 중복되지 않는 고유한 값을 저장

- 세트 내의 각 요소는 해시 함수를 통해 해시 값으로 변환되고, 이 해시 값을 기반으로 해시 테이블에 저장됨
- 마찬가지로 딕셔너리의 키는 고유해야 하므로, 키를 해시 함수를 통해 해시 값으로 변환하여 해시 테이블에 저장

- 따라서 세트와 딕셔너리의 키는 매우 빠른 탐색 속도를 제공하며, 중복된 값을 허용하지 않음

### 해시(Hash)

- 임의의 크기를 가진 데이터를 고정된 크기의 고유한 값으로 변환하는 것
- 이렇게 생성된 고유한 값은 해당 데이터를 식별하는 데 사용될 수 있음
- 일종의 "지문"과 같은 역할
- 지문은 개인을 고유하게 식별하는 것처럼, 해시 값은 데이터를 고유하게 식별
- 파이썬에서는 해시 함수를 사용하여 데이터를 해시 값으로 변환하며, 이 해시 값은 정수로 표현됨

### set의 pop 메서드 예시

- set에서 임의의 요소를 제거하고 반환

- 실행할 때마다 다른 요소를 얻는다는 의미에서의 "무작위"가 아니라 "임의"라는 의미에서 "무작위"

  > By `"arbitrary"` the docs don't mean `"random"`

- 해시 테이블에 나타나는 순서대로 반환

```python
# 정수

my_set = {1, 2, 3, 9, 100, 4, 87, 39, 10, 52}

print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set)
```

> 정수 값 자체가 곧 해시 값

```python
# 문자열

my_str_set = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'}

print(my_str_set.pop())
print(my_str_set.pop())
print(my_str_set.pop())
print(my_str_set.pop())
print(my_str_set.pop())
```

> 반환 값이 매번 다름


```python
print(hash(1))  # 1
print(hash(1))  # 1
print(hash('a'))  # 실행시마다 다름
print(hash('a'))  # 실행시마다 다름
```

- 파이썬에서 해시 함수의 동작 방식은 객체의 타입에 따라 달라짐
- 정수와 문자열은 서로 다른 타입이며, 이들의 해시 값을 계산하는 방식도 다름
- 정수 타입의 경우, 정수 값 자체가 곧 해시 값이 됨
  - 즉, 같은 정수는 항상 같은 해시 값을 가짐
  - 해시 테이블에 정수를 저장할 때 효율적인 방법
  - 예를 들어, hash(1)과 hash(2)는 항상 서로 다른 해시 값을 갖지만, hash(1)은 항상 동일한 해시 값을 갖게 됨
- 반면에 문자열은 가변적인 길이를 갖고 있고, 문자열에 포함된 각 문자들의 유니코드 코드 포인트 등을 기반으로 해시 값을 계산
  - 이로 인해 문자열의 해시 값은 문자열의 내용에 따라 다르게 계산됨

### 해시 함수

- 주어진 객체의 해시 값을 계산하는 함수

- 해시 값은 객체의 고유한 식별자로 사용될 수 있으며, 해시 테이블과 같은 자료 구조에서 빠른 검색을 위해 사용됨

  ```python
  # TypeError: unhashable type: 'list'
  my_set = {[1, 2, 3], 1, 2, 3, 4, 5}
  
  # TypeError: unhashable type: 'list
  my_dict = {[1, 2, 3]: 'a'}
  ```

  > `해시 가능성(hashable)`은 객체를 "딕셔너리의 키"나 "세트의 요소"로 사용할 수 있게 하는데, 이 자료 구조들이 내부적으로 해시 값을 사용하기 때문

### 참고 문헌

- https://docs.python.org/ko/3.9/library/stdtypes.html#set-types-set-frozenset
- https://docs.python.org/ko/3.9/glossary.html#term-hashable