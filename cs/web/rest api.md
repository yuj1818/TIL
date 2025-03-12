# REST **API**

- REST 원칙을 적용하여 서비스 API를 설계한 것

## REST(**REpresentational State Transfer)** 란?

- 자원을 이름으로 구분하여 해당 자원의 상태를 주고 받는 모든 것
- HTTP URI를 통해 자원을 명시하고 HTTP 메서드(GET, POST, PUT, DELETE)를 통해 해당 자원에 대한 CRUD를 적용하는 것
    
    
    | Method | 의미 |
    | :---: | :---: |
    | GEST | Select |
    | POST | Create |
    | PUT | Update |
    | DELETE | Delete |
- 즉, 자원 기반의 구조 설계의 중심에 자원이 있고, HTTP 메서드를 통해 이를 처리

### REST 구성 요소

- 자원(Resource): HTTP URI
- 자원에 대한 행위(Verb): HTTP Method
- 자원에 대한 행위의 내용(Representations): HTTP Message Pay Load

### REST의 특징

- Server-Client
- Stateless
- Cacheable
- Layered System
- Uniform Interface

## API란?

- 응용 프로그램에서 사용할 수 있도록 운영 체제나 프로그래밍 언어가 제공하는 기능을 제어할 수 있게 만든 인터페이스
- 프로그램끼리 통신할 수 있도록 하는 중개자

## REST API 설계 원칙

### 1. URI는 동사보다는 명사, 대문자보다는 소문자를 사용
    - http://xxxx.com/Running/ ❌
    - http://xxxx.com/run/ ✅
### 2. 마지막에 슬래시(/)를 포함하지 않는다
    - http://xxxx.com/test/ ❌
    - http://xxxx.com/test ✅
### 3. 언더바 대신 하이폰(-)을 사용한다
    - http://xxx.com/test_ex ❌
    - http://xxx.com/test-ex ✅
### 4. 파일 확장자는 URI에 포함하지 않는다
    - http://xxx.com/exImg.jpg ❌
    - http://xxx.com/exImg ✅
### 5. 행위를 포함하지 않는다
    - http://xxx.com/delete-post/1 ❌
    - http://xxx.com/post/1 ✅