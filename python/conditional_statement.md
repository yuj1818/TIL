# 조건문(Conditional Statement)

- 주어진 조건식을 평가하여 해당 조건이 참(True)인 경우에만 코드 블록을 실행하거나 건너뜀
    
### if statement

```python
# if statement 기본 구조

if 표현식:
    코드 블록
elif 표현식:
    코드 블록
else:
    코드 블록
```

```python
# 조건문 예시

a = 5

if a > 3:    # (조건 충족)
    print('3 초과')    # 3 초과
else:
    print('3 이하')

print(a)    # 5
```

```python
# 복수 조건문 예시

dust = 35

if dust > 150:    # pass
    print('매우 나쁨')
elif dust > 80:    # pass
    print('나쁨')
elif dust > 30:    # (조건 충족)
    print('보통')    # 보통
else:
    print('좋음')
```

```python
# 중첩 조건문 예시

dust = 480

if dust > 150:    # (조건 충족)
    print('매우 나쁨')    # 매우 나쁨
    if dust > 300:    # (조건 충족)
        print('위험해요! 나가지 마세요!')     # 위험해요! 나가지 마세요!
elif dust > 80:
    print('나쁨)
elif dust > 30:
    print('보통')
else:
    print('좋음')
```

### pass(참고)

- 아무런 동작도 수행하지 않고 넘어가는 역할
- 문법적으로 문장이 필요하지만 프로그램 실행에는 영향을 주지 않아야 할 때 사용

```python
# 코드 작성 중 미완성 부분

def my_function():
    pass    # 구현 부분을 나중에 추가 가능
        # 컴파일하는 동안 오류 발생하지 않음
```

```python
# 조건문에서 아무런 동작을 수행하지 않아야 할 때

if condition:
    pass    # 아무런 동작도 수행하지 않음
else: 
코드블록    # 다른 동작 수행
```

```python
# 무한 루프에서 조건이 충족되지 않을 때 pass를 사용하여 루프를 계속 진행

while True:
    if condition:
        break
    elif condition:
        pass    # 루프 계속 진행
    else:
        print('..')
```
