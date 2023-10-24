# JavaScript

# Javascript의 역사

## 웹 브라우저와 JavaScript

- 웹의 탄생(1990)
    - 팀 버너스리 경이 WWW, 하이퍼텍스트 시스템 고안
    - URL, HTTP 최초 설계 및 구현
    - 초기의 웹은 정적인 텍스트 페이지만을 지원
- 웹 브라우저의 대중화(1993)
    - Netscape사의 최초 상용 웹 브라우저인 Netscape Navigator 출시
    - 당시 약 90% 이상의 시장 점유율을 가짐
- JavaScript의 탄생(1995)
    - 당시 Netscape 소속 개발자인 Brandon Eich는 웹의 동적 기능 개발이라는 회사의 요구사항을 넘어 스크립트 언어 Mocha를 개발
    - 이후 LiveScript로 이름을 변경했으나 당시 가장 인기 있던 프로그래밍 언어인 Java의 명성에 기대보고자 JavaScript로 이름을 변경
    - JavaScript는 Netscape Navigator 2.0에 탑재되어 웹 페이지에 동적 기능을 추가하는 데 사용됨
- JavaScript 파편화(1996)
    - Microsoft가 자체 웹 브라우저인 인터넷 익스플로러 3.0에 JavaScript와 유사한 언어인 JScript를 도입
    - 이 과정에서 많은 회사들이 자체적으로 JavaScript를 독자적으로 변경하고 이를 자체 브라우저에 탑재
- 1차 브라우저 전쟁(1995-2001)
    - Microsoft는 IE를 자사 윈도우 운영체제에 내장하여 무료로 배포
    - 빌 게이츠를 필두로 한 Microsoft의 공격적인 마케팅, 자금력, 윈도우 운영체제 점유율 앞에 Netscape는 빠르게 몰락하기 시작
    - IE의 시장 점유율은 2002년 약 96%에 달하며 Microsoft가 승리
    - 추후 Brandon Eich와 함께 Netscape에서 나온 핵심 개발진은 모질라 재단을 설립하여 Firefox 브라우저를 출시(2003)
- 1차 브라우저 전쟁의 영향
    - 웹 표준의 부재로 인해 각 기업에서 자체 표준을 확립하려는 상황이 벌어짐
    - 이는 웹 개발자들에게 큰 혼란을 주었으며, 결국 웹 표준의 중요성을 인식하는 계기가 됨
- ECMAScript 출시(1997)
    - JavaScript의 파편화를 막기 위해 1997년 ECMA에서 ECMAScript라는 표준 언어를 정의
    - 이때부터 JavaScript는 ECMAScript 표준에 기반을 두고 발전하기 시작
- 2차 브라우저 전쟁(2004-2017)
    - IE에 독주에 대한 Firefox의 대항
        - 2008년까지 30% 점유율 차지
    - Google의 Chrome 브라우저 출시(2008)
    - Chrome은 출시 3년 만에 Firefox의 점유율을 넘어서고 그로부터 반년 뒤, IE의 점유율을 넘어섬
- 2차 브라우저 전쟁의 영향
    - 웹 표준을 준수하는 Chrome의 등장으로 웹 표준의 중요성이 대두
    - 웹의 기능이 크게 확장되며 웹 애플리케이션의 비약적인 발전을 이끌어 감
    - 웹의 기술적 발전과 웹 표준의 중요성

## ECMAScript

- Ecma International(정보와 통신 시스템을 위한 국제적 표준화 기구)이 정의하고 있는 표준화된 스크립트 프로그래밍 언어 명세
- 스크립트 언어가 준수해야 하는 규칙, 세부 사항 등을 제공
- ECMAScript와 JavaScript
    - JavaScript는 ECMAScript 표준을 구현한 구체적인 프로그래밍 언어
    - ECMAScript의 명세를 기반으로 하여 웹 브라우저나 Node.js와 같은 환경에서 실행됨
    - ECMAScript는 JavaScript의 표준이며, JavaScript는 ECMAScript 표준을 따르는 구체적인 프로그래밍 언어
    - ECMAScript는 언어의 핵심을 정의하고, JavaScript는 ECMAScript 표준을 따라 구현된 언어로 사용됨
- ECMAScript의 역사
    - ECMAScript 5(ES5)에서 안정성과 생산성을 크게 높임(2009)
    - ECMAScript 2015(ES6)에서 객체지향 프로그래밍 언어로써 많은 발전을 이루어, 역사상 가장 중요한 버전으로 평가됨(2015)

## JavaScript의 현재

- 현재는 Chrome, Firefox, Safari, Microsoft Edge 등 다양한 웹 브라우저가 출시되어 있으며, 웹 브라우저 시장이 다양화 되어있음
- 기존에 JavaScript는 브라우저에서만 웹 페이지의 동적인 기능을 구현하는 데에만 사용되었음
- 이후 브라우저에서 벗어나 Node.js와 같은 서버 사이드 분야 뿐만 아니라, 다양한 프레임워크와 라이브러리들이 개발되면서, 웹 개발 분야에서는 필수적인 언어로 자리 잡게 됨

# JavaScript and DOM

- 웹 브라우저에서의 JavaScript = 웹 페이지의 동적인 기능을 구현
- JavaScript 실행 환경 종류
    - HTML script 태그
    - js 확장자 파일
    - 브라우저 console

## DOM(The Document Object Model)

- 웹 페이지(Document)를 구조화된 객체로 제공하여 프로그래밍 언어가 페이지 구조에 접근할 수 있는 방법을 제공
- 문서 구조, 스타일, 내용 등을 변경할 수 있도록 함

### DOM의 특징

<img src="https://github.com/yuj1818/TIL/assets/95585314/d6bf6c54-7ebe-405e-b5b8-57fd43ac38cf" width="80%">

- DOM에서 모든 요소, 속성, 텍스트는 하나의 객체
- 모두 document 객체의 자식으로 구성됨

### DOM tree

![Untitled 1](https://github.com/yuj1818/TIL/assets/95585314/e43d8b3a-2b78-4d57-a74f-059c1b6ea79d)

- 브라우저는 HTML 문서를 해석하여 DOM tree라는 객체 트리로 구조화
- 객체 간 상속 구조가 존재

브라우저가 웹 페이지를 불러오는 과정

- 웹 페이지는 웹 브라우저를 통해 해석되어 웹 브라우저 화면에 나타남

![Untitled 2](https://github.com/yuj1818/TIL/assets/95585314/5391ec0e-5fce-4476-9d8f-b663acd20f58)

### DOM의 핵심

- 문서의 요소들을 객체로 제공하여 다른 프로그래밍 언어에서 접근하고 조작할 수 있는 방법을 제공하는 API

### document 객체

- 웹 페이지 객체
- DOM Tree의 진입점
- 페이지를 구성하는 모든 객체 요소를 포함
- 예시
    - HTML의 \<title> 변경하기
    
    ![Untitled 3](https://github.com/yuj1818/TIL/assets/95585314/cc1e13fd-a475-44e4-b4d6-53e495b9962c)
    

## DOM 선택

### DOM 조작 시 기억해야 할 것

- 웹 페이지를 동적으로 만들기 == 웹 페이지를 조작하기
- 조작 순서
    - 조작 하고자 하는 요소를 선택(또는 탐색)
    - 선택된 요소의 콘텐츠 또는 속성을 조작

### 선택 메서드

- `document.querySelector()`
    - 제공한 선택자와 일치하는 element 한 개 선택
    - 제공한 CSS selector를 만족하는 첫 번째 element 객체를 반환(없다면 null 반환)
- `document.querySelectorAll()`
    - 제공한 선택자와 일치하는 여러 element를 선택
    - 제공한 CSS selector를 만족하는 NodeList를 반환
- 예시
    
    ```html
    <body>
      <h1 class="heading">DOM 선택</h1>
      <a href="https://www.google.com/">google</a>
      <p class="content">content1</p>
      <p class="content">content2</p>
      <p class="content">content3</p>
      <ul>
        <li>list1</li>
        <li>list2</li>
      </ul>
      <script>
        // heading 클래스를 가지는 element중 첫 번째를 반환
        console.log(document.querySelector('.heading'))
        // content 클래스를 가지는 element 중 첫 번째를 반환
        console.log(document.querySelector('.content'))
        // content 클래스를 가지는 모든 element 반환
        console.log(document.querySelectorAll('.content'))
        // ul 태그 안의 모든 li 태그를 반환
        console.log(document.querySelectorAll('ul > li'))
      </script>
    </body>
    ```
    
    ![Untitled 4](https://github.com/yuj1818/TIL/assets/95585314/ccc11dff-c878-42f1-9527-c97f3be5bf43)
    

## DOM 조작

### 속성 조작

- 클래스 속성 조작
    - ‘classList’ property
    - 요소의 클래스 목록을 DOMTokenList(유사 배열) 형태로 반환
    
    |  |  |
    | --- | --- |
    | element.classList.add() | 지정한 클래스 값을 추가 |
    | element.classList.remove() | 지정한 클래스 값을 제거 |
    | element.classList.toggle() | 클래스가 존재한다면 제거하고 false를 반환<br>(존재하지 않으면 클래스를 추가하고 true 반환) |
    - 예시
    
    ```html
    <body>
      <h1 class="heading">DOM 선택</h1>
      <a href="https://www.google.com/">google</a>
      <p class="content">content1</p>
      <p class="content">content2</p>
      <p class="content">content3</p>
      <ul>
        <li>list1</li>
        <li>list2</li>
      </ul>
      <script>
        const h1Tag = document.querySelector('.heading')
        console.log(h1Tag.classList)
    
        h1Tag.classList.add('red')
        console.log(h1Tag.classList)
    
        h1Tag.classList.remove('red')
        console.log(h1Tag.classList)
    
        h1Tag.classList.toggle('red')
        console.log(h1Tag.classList)
      </script>
    </body>
    ```
    
    ![Untitled 5](https://github.com/yuj1818/TIL/assets/95585314/3363b1af-e0b0-48cc-ac7e-34e9c9ec7839)
    
- 속성 조작
    - 속성 조작 메서드
    
    |  |  |
    | --- | --- |
    | Element.getAttribute() | - 해당 요소에 지정된 값을 반환(조회) |
    | Element.setAttribute(name, value) | - 지정된 요소의 속성 값을 설정<br>- 속성이 이미 있으면 기존 값을 갱신(그렇지 않으면 지정된 이름과 값으로 새 속성이 추가) |
    | Element.removeAttribute() | - 요소에서 지정된 이름을 가진 속성 제거 |
    - 예시
    
    ```html
    <body>
      <h1 class="heading">DOM 선택</h1>
      <a href="https://www.google.com/">google</a>
      <p class="content">content1</p>
      <p class="content">content2</p>
      <p class="content">content3</p>
      <ul>
        <li>list1</li>
        <li>list2</li>
      </ul>
      <script>
        const aTag = document.querySelector('a')
        console.log(aTag.getAttribute('href'))
    
        aTag.setAttribute('href', 'https://www.naver.com/')
        console.log(aTag.getAttribute('href'))
    
        aTag.removeAttribute('href')
        console.log(aTag.getAttribute('href'))
      </script>
    </body>
    ```
    
    ![Untitled 6](https://github.com/yuj1818/TIL/assets/95585314/e2dc60f6-6850-4335-8eea-44a31b8f3888)
    

## HTML 콘텐츠 조작

- ‘textContent’ property
- 요소의 텍스트 콘텐츠를 표현

```html
<body>
  <h1 class="heading">DOM 조작</h1>
  <a href="https://www.google.com/">google</a>
  <p class="content">content1</p>
  <p class="content">content2</p>
  <p class="content">content3</p>
  <ul>
    <li>list1</li>
    <li>list2</li>
  </ul>
  <script>
    const h1Tag = document.querySelector('.heading')
    console.log(h1Tag.textContent)

    h1Tag.textContent = '내용 수정'
    console.log(h1Tag.textContent)
  </script>
</body>
```

![Untitled 7](https://github.com/yuj1818/TIL/assets/95585314/acd1ef35-4262-4c2b-b432-ab59bb233361)

## DOM 요소 조작

### DOM 요소 조작 메서드

|  |  |
| --- | --- |
| document.createElement(tagName) | - 작성한 tagName의 HTML 요소를 생성하여 반환 |
| Node.appendChild() | - 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입<br>- 추가된 Node 객체를 반환 |
| Node.removeChild() | - DOM에서 자식 Node를 제거<br>- 제거된 Node를 반환 |
- 예시

```html
<body>
  <div></div>
  <script>
    const h1Tag = document.createElement('h1')
    h1Tag.textContent = '제목'
    console.log(h1Tag)
		// <h1>제목</h1>

    const divTag = document.querySelector('div')
    divTag.appendChild(h1Tag)
    console.log(divTag)
		// <h1>제목</h1>
		// <div><h1>제목</h1></div>

    divTag.removeChild(h1Tag)
		// <h1>제목</h1>
		// <div></div>
  </script>
</body>
```

## style 조작

- ‘style’ property
- 해당 요소의 모든 style 속성 목록을 포함하는 속성
- 예시
    
    ```html
    <body>
      <p>Lorem, ipsum dolor.</p>
      <script>
        const pTag = document.querySelector('p')
    
        pTag.style.color = 'crimson'
        pTag.style.fontSize = '2rem'
        pTag.style.border = '1px solid black'
        console.log(pTag.style)
      </script>
    </body>
    ```
    
    ![Untitled 8](https://github.com/yuj1818/TIL/assets/95585314/811cb5e1-d31b-4b16-baa8-bd8b82c22525)
    

# JavaScript 기본 문법

## 변수

- ECMAScript 2015(ES6) 이후의 명제를 따름
- 권장 스타일 가이드
    - [https://standardjs.com/rules-kokr.html](https://standardjs.com/rules-kokr.html)

### 식별자(변수명) 작성 규칙

- 반드시 문자, 달러($) 또는 밑줄(_)로 시작
- 대소문자를 구분
- 예약어 사용 불가
    - for, if, function 등
- 카멜 케이스(camelCase)
    - 변수, 객체, 함수에 사용
- 파스칼 케이스(PascalCase)
    - 클래스, 생성자에 사용
- 대문자 스네이크 케이스(SNAKE_CASE)
    - 상수(constants)에 사용

### 변수 선언 키워드

- let
    - 블록 스코프(block scope)를 갖는 지역 변수를 선언
    - 재할당 가능
    - 재선언 불가능
    - ES6에서 추가
- const
    - 기본적으로 권장
    - 블록 스코프를 갖는 지역 변수를 선언
    - 재할당 불가능
    - 재선언 불가능
    - ES6에서 추가
    - 선언 시, 반드시 초기값 설정 필요
    
    `블록 스코프(block scope)` 
    
    - if, for, 함수 등의 중괄호 내부를 가리킴
    - 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능
- var

## 데이터 타입

### 원시 자료형(Primitive type)

- Number, String, Boolean, undefined, null
- 변수에 값이 직접 저장되는 자료형(불변, 값이 복사)
- 변수에 할당될 때 값이 복사 되어 변수 간에 서로 영향을 미치지 않음

```jsx
const bar = 'bar'
console.log(bar) // bar

bar.toUpperCase()
console.log(bar) // bar

let a = 10
let b = a
b = 20
console.log(a) // 10
console.log(b) // 20
```

- Number
    - 정수 또는 실수형 숫자를 표현하는 자료형
    
    ```jsx
    const a = 13
    const b = -5
    const c = 3.14 // float - 숫자 표현
    const d = 2.998e8 // 2.998 * 10^8
    const e = Infinity
    const f = -Infinity
    const g = NaN // Not a Number
    ```
    
- String
    - 텍스트 데이터를 표현하는 자료형
    - ‘+’ 연산자를 사용해 문자열끼리 결합
    - 곱셈, 나눗셈, 뺄셈 불가능
    
    ```jsx
    const firstName = 'Tony'
    const lastName = 'Stark'
    const fullName = firstName + lastName
    
    console.log(fullName) // TonyStark
    ```
    
- null
    - 변수의 값이 없음을 의도적으로 표현할 때 사용
    
    ```jsx
    let a = null
    console.log(a) // null
    ```
    
- undefined
    - 변수 선언 이후 직접 값을 할당하지 않으며 자동으로 할당됨
    
    ```jsx
    let b
    console.log(b) // undefined
    ```
    
- Boolean
    - true/false
    - 조건문 또는 반복문에서 Boolean이 아닌 데이터 타입은 “자동 형변환 규칙”에 따라 true 또는 false로 변환됨
    
    | 데이터 타입 | false | true |
    | --- | --- | --- |
    | undefined | 항상 false | X |
    | null | 항상 false | X |
    | Number | 0, -0, NaN | 나머지 모든 경우 |
    | String | 빈 문자열 | 나머지 모든 경우 |

### 참조 자료형(Reference type)

- Objects(Object, Array, Function)
- 객체의 주소가 저장되는 자료형(가변, 주소가 복사)

```jsx
const obj1 = { name: 'Alice', age: 30}
const obj2 = obj1
obj2.age = 40

console.log(obj1.age) // 40
console.log(obj2.age) // 40
```

## 연산자

### 할당 연산자

- 오른쪽에 있는 피연산자의 평가 결과를 왼쪽 피연산자에 할당하는 연산자
- 단축 연산자 지원

```jsx
let a = 0
a += 10
console.log(a) // 10

a -= 3
console.log(a) // 7

a *= 10
console.log(a) // 70

a %= 7
console.log(a) // 0
```

### 증가&감소 연산자

- 증가 연산자(++)
    - 피연산자를 증가(1을 더함)시키고 연산자의 위치에 따라 증가하기 전이나 후의 값을 반환
- 감소 연산자(—)
    - 피연산자를 감소(1을 뺌)시키고 연산자의 위치에 따라 감소하기 전이나 후의 값을 반환
- += 또는 -=와 같이 더 명시적인 표현으로 작성하는 것을 권장

```jsx
let x = 3
const y = x++
console.log(x, y) // 4 3

let a = 3
const b = ++a
console.log(a, b) // 4 4
```

### 비교 연산자

- 피연산자들(숫자, 문자, Boolean 등)을 비교하고 결과 값을 boolean으로 반환하는 연산자

```jsx
3 > 2 // true
3 < 2 // false
'A' < 'B' // true
'Z' < 'a' // true
'가' < '나' // true
```

### 동등 연산자(==)

- 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
- ‘암묵적 타입 변환’ 통해 타입을 일치시킨 후 같은 값인지 비교
- 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별

```jsx
console.log(1 == 1) // true
console.log('hello' == 'hello') // true
console.log('1' == 1) // true
console.log(0 == false) // true
```

### 일치 연산자(===)

- 두 피연산자의 값과 타입이 모두 같은 경우 true를 반환
- 같은 객체를 가리키거나, 같은 타입이면서 같은 값인지를 비교
- 엄격한 비교가 이뤄지며 암묵적 타입 변환이 발생하지 않음
- 특수한 경우를 제외하고는 동등 연산자가 아닌 일치 연산자 사용 권장

```jsx
console.log(1 === 1) // true
console.log('1' === 1) // false
console.log('hello' === 'hello') // true
console.log(0 === false) //false
```

### 논리 연산자

- and 연산(&&)
- or 연산(||)
- not 연산(!)
- 단축 평가 지원

```jsx
true && false // false
true && true // true

false || false // false
false || true // true

!true // false

1 && 0 // 0
0 && 1 // 0
4 && 7 // 7
1 || 0 // 1
0 || 1 // 1
4 || 7 // 4
```

## 조건문

### if

- 조건 표현식의 결과값을 boolean 타입으로 변환 후 참/거짓을 판단

```jsx
const name = 'customer'

if (name === 'admin') {
	console.log('관리자님 환영해요')
} else if (name === 'customer') {
	console.log('고객님 환영해요')
} else {
	console.log(`반갑습니다. ${name}님`)
}
```

### 조건 (삼항) 연산자

- 세 개의 피연산자를 받는 유일한 연산자
- 앞에서부터 조건문, 물음표(?), 조건문이 참일 경우 실행할 표현식, 콜론(:), 조건문이 거짓일 경우 실행할 표현식이 배치

```jsx
// 기본 if 문
const func1 = function (person) {
	if (person > 17) {
		return 'Yes'
	} else {
		return 'No'
	}
}
```

```jsx
// 삼항 연산자 사용한 조건문
const func2 = function (person) {
	return person > 17 ? 'Yes' : 'No'
}
```

## 반복문

### while

- 조건문이 참이면 문장을 계속해서 수행

```jsx
let i = 0

while (i < 6) {
	console.log(i)
	i += 1
}
```

### for

- 특정한 조건이 거짓으로 판별 될 때까지 반복

```jsx
//      변수  | 조건문|i값 증가
for (let i = 0; i < 6; i++) {
	console.log(i)
}
```

- for 동작 원리
    1. 반복문 진입 및 변수 i 선언
    2. 조건문 평가 후 코드 블록 실행
    3. 코드 블록 실행 이후 i값 증가

### for … in

- 객체의 열거 가능한 속성(property)에 대해 반복

```jsx
const fruits = { a: 'apple', b: 'banana' }

for (const property in object) {
	console.log(property) // a, b
	console.log(object[property]) // apple, banana
}
```

### for … of

- 반복 가능한 객체(배열, 문자열 등)에 대해 반복

```jsx
const numbers = [0, 1, 2, 3]

for (const number of numbers) {
	console.log(number) // 0, 1, 2, 3
}
```

### 배열 반복과 for … in

- 배열의 인덱스는 정수 이름을 가진 열거 가능한 속성
- for … in은 정수가 아닌 이름과 속성을 포함하여 열거 가능한 모든 속성을 반환
- 내부적으로 for … in은 배열의 반복자 대신 속성 열거를 사용하기 때문에 특정 순서에 따라 인덱스를 반환하는 것을 보장할 수 없음
- 인덱스의 순서가 중요한 **배열에서는 사용하지 않음**
- 배열에서는 **for 반복, for … of 반복을 사용**

```jsx
const arr = ['a', 'b', 'c']

for (const i in arr) {
	console.log(i) // 0, 1, 2
}

for (const i of arr) {
	console.log(i) // a, b, c
}
```

### for … in 과 for … of 의 차이 예시

```jsx
// for ... in
const capitals = {
	korea: '서울',
	japan: '도쿄',
	china: '베이징',
}
for (const capital in capitals) {
	console.log(capital) // korea, japan, china
}

// for ... of
for (const capital of capitals) {
	console.log(capital) // TypeError: capitals is not iterable
}
```

### 반복문 총정리

| 키워드 | 연관 키워드 | 스코프 |
| --- | --- | --- |
| while | break, continue | 블록 스코프 |
| for | break, continue | 블록 스코프 |
| for … in | object 순회 | 블록 스코프 |
| for … of | Iterable 순회 | 블록 스코프 |

# 참고

## DOM 관련

### Node

- DOM의 기본 구성 단위
- DOM 트리의 각 부분은 Node라는 객체로 표현됨
    - Document Node ⇒ HTML 문서 전체를 나타내는 노드
    - Element Node ⇒ HTML 요소를 나타내는 노드 ex) \<p>
    - Text Node ⇒ HTML 텍스트, Element Node 내의 텍스트 컨텐츠를 나타냄
    - Attribute Node ⇒ HTML 요소의 속성을 나타내는 노드

### NodeList

- DOM 메서드를 사용해 선택한 Node의 목록
- 배열과 유사한 구조를 가짐
- Index로만 각 항목에 접근 가능
- 다양한 배열 메서드 사용 가능
- querySelectorAll()에 의해 반환되는 NodeList는 DOM의 변경사항을 실시간으로 반영하지 않음

### Element

- Node의 하위 유형
- Element는 DOM 트리에서 HTML 요소를 나타내는 특별한 유형의 Node
- 예를 들어, \<p>, \<div>, \<span>, \<body> 등의 HTML 태그들이 Element 노드를 생성
- Node의 속성과 메서드를 모두 가지고 있으며 추가적으로 요소 특화된 기능(className, innerHTML, id 등)을 가지고 있음
- 모든 Element는 Node이지만, 모든 Node가 Element인 것은 아님

### DOM 속성 확인 Tip

- 개발자 도구 - Elements - Properties
- 해당 요소의 모든 DOM 속성 확인 가능

### Parsing

- 구문 분석, 해석
- 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정

## 문법 관련

### ‘값이 없음’에 대한 표현이 null과 undefined 2가지인 이유

- JavaScript의 설계 실수
- null이 원시 자료형임에도 불구하고 object로 출력되는 이유는 JavaScript  설계 당시의 버그를 해결하지 않은 것
- 해결하지 못하는 이유는 이미 null 타입에 의존성을 띄고 있는 수 많은 프로그램들이 망가질 수 있기 때문

### Template literals(템플릿 리터럴)

- 내장된 표현식을 허용하는 문자열 작성 방식
- Backtick(``)을 이용하며, 여러 줄에 걸쳐 문자열을 정의할 수도 있고 JavaScript의 변수를 문자열 안에 바로 연결할 수 있음
- 표현식은 ‘\$’와 중괄호(${expression})로 표기
- ES6+부터 지원

```jsx
const age = 100
const message = `홍길동은 ${age}세 입니다`
console.log(message) // 홍길동은 100세 입니다.
```

### 반복문 사용 시 const 사용 여부

- for 문
    - for (let i = 0; i < arr.length; i++) { … }의 경우에는 최초 정의한 i를 “재할당”하면서 사용하기 때문에 const를 사용하면 에러 발생
- for … in, for … of
    - 재할당이 아니라, 매 반복마다 다른 속성 이름이 변수에 지정되는 것이므로 const를 사용해도 에러가 발생하지 않음
    - 단 const의 특징에 따라 블록 내부에서 변수를 수정할 수 없음

### 세미콜론(semicolon)

- 자바스크립트는 세미콜론을 선택적으로 사용 가능
- 세미콜론이 없으면 ASI에 의해 자동으로 세미콜론이 삽입됨
    - ASI(Automatic Semicolon Insertion, 자동 세미콜론 삽입 규칙)
- JavaScript를 만든 Brendan Eich 또한 세미콜론 작성을 반대

### 변수 선언 키워드 - ‘var’

- ES6 이전에 변수 선언에 사용했던 키워드
- 재할당 가능 & 재선언 가능
- “호이스팅” 되는 특성으로 인해 예기치 못한 문제 발생 가능
    - 따라서 ES6 이후부터는 var 대신 const와 let을 사용하는 것을 권장
- 함수 스코프(function scope)를 가짐
- 변수 선어 시 var, const, let 키워드 중 하나를 사용하지 않으면 자동으로 var로 선언됨

### 함수 스코프(function scope)

- 함수의 중괄호 내부를 가리킴
- 함수 스코프를 가지는 변수는 함수 바깥에서 접근 불가능

```jsx
function foo() {
	var x = 1
	console.log(x) // 1
}

console.log(x) // ReferenceError: x is not defined
```

### 호이스팅(hoisting)

- 변수를 선언 이전에 참조할 수 있는 현상
- 변수 선언 이전의 위치에서 접근 시 undefined를 반환

```jsx
console.log(name) // undefined => 선언 이전에 참조

var name = '홍길동' // 선언
```

- 위 코드를 아래와 같이 이해함

```jsx
var name // undefined으로 초기화
console.log(name)

var name = '홍길동' // 재할당
```

- JavaScript에서 변수들은 실제 실행 시에 코드의 최상단으로 끌어 올려지게 되며 (hoisted) 이러한 이유 때문에 var로 선언된 변수는 선언 시에 undefined로 값이 초기화되는 과정이 동시에 발생

### NaN을 반환하는 경우 예시

- 숫자로서 읽을 수 없음 (Number(undefined))
- 결과가 허수인 수학 계산식 (Math.sqrt(-1))
- 피연산자가 NaN (7 ** NaN)
- 정의할 수 없는 계산식 (0 * Infinity)
- 문자열을 포함하면서 덧셈이 아닌 계산식 (’가’ / 3)