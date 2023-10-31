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

### [참조 자료형(Reference type)](#참조-자료형reference-type-종류)

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

# 참조 자료형(Reference Type) 종류

## Function(함수)

- 참조 자료형에 속하며 모든 함수는 Function Object

### 함수 구조

- 함수의 이름
- 함수의 매개변수
- 함수의 body를 구성하는 statement
- return 값이 없다면 undefined를 반환

```jsx
function name ([param[, param, [..., param]]]) {
	statements
	return value
}
```

### 함수 정의 방법

- 선언식(function declaration)

```jsx
function add (num1, num2) {
	return num1 + num2
}

add(1, 2) // 3
```

- 표현식(function expression)

```jsx
const sub = function (num1, num2) {
	return num1 - num2
}

sub(2, 1) // 1
```

- 함수 표현식의 특징
    - 함수 이름이 없는 ‘익명 함수’를 사용할 수 있음
    - 선언식과 달리 표현식으로 정의한 함수는 호이스팅 되지 않으므로 함수를 정의하기 전에 먼저 사용할 수 없음
    
    ```jsx
    // 선언식
    
    add(1, 2) // 3
    
    function add (num1, num2) {
    	return num1 + num2
    }
    
    // 표현식
    
    sub(2, 1) // ReferenceError: Cannot access 'sub' before initialization
    
    const sub = function (num1, num2) {
    	return num1 - num2
    }
    ```
    
- 함수 선언식과 표현식 종합

|  | 선언식 | 표현식 |
| --- | --- | --- |
| 특징 | - 익명 함수 사용 불가능<br>- 호이스팅 있음 | - 익명 함수 사용 가능<br>- 호이스팅 없음 |
| 기타 |  | 사용 권장 |

### 매개변수

- 기본 함수 매개변수(Default function parameter)
    - 값이 없거나 undefined가 전달된 경우 이름 붙은 매개변수를 기본값으로 초기화
    
    ```jsx
    const greeting = function (name = 'Anonymous') {
    	return `Hi ${name}`
    }
    
    greeting() // Hi Anonymous
    ```
    
- 나머지 매개변수(Rest parameters)
    - 임의의 수의 인자를 ‘배열’로 허용하여 가변 인자를 나타내는 방법
    - 작성 규칙
        - 함수 정의 시 나머지 매개변수 하나만 작성할 수 있음
        - 나머지 매개변수는 함수 정의에서 매개변수 마지막에 위치해야 함
    
    ```jsx
    const myFunc = function (param1, param2, ...restParams) {
    	return [param1, param2, restParams]
    }
    
    myFunc(1, 2, 3, 4, 5) // [1, 2, [3, 4, 5]]
    myFunc(1, 2) // [1, 2, []]
    ```
    
- 매개변수와 인자의 개수 불일치
    - 매개변수 개수 > 인자 개수
        - 누락된 인자를 undefined로 할당
        
        ```jsx
        const threeArgs = function (param1, param2, param3) {
        	return [param1, param2, param3]
        }
        
        threeArgs() // [undefined, undefined, undefined]
        threeArgs(1) // [1, undefined, undefined]
        threeArgs(2, 3) // [2, 3, undefined]
        ```
        
    - 매개변수 개수 < 인자 개수
        - 초과 입력한 인자는 사용하지 않음
        
        ```jsx
        const noArgs = function() {
        	return 0
        }
        
        noArgs(1, 2, 3) // 0
        
        const twoArgs = function(param1, param2) {
        	return [param1, param2]
        }
        
        twoArgs(1, 2, 3) // [1, 2]
        ```
        

### Spread syntax(전개 구문, ’…’)

- 배열이나 문자열과 같이 반복 가능한 항목을 펼치는 것(확장, 전개)
- 전개 대상에 따라 역할이 다름
    - 배열이나 객체의 요소를 개별적인 값으로 분리하거나 다른 배열이나 객체의 요소를 현재 배열이나 객체에 추가하는 등
- 함수와의 사용
    - 함수 호출 시 인자 확장
    
    ```jsx
    function myFunc(x, y, z) {
    	return x + y + z
    }
    
    let numbers = [1, 2, 3]
    
    console.log(myFunc(...numbers)) // 6
    ```
    
    - 나머지 매개변수(압축)
    
    ```jsx
    function myFunc2(x, y, ...restArgs) {
    	return [x, y, restArgs]
    }
    
    console.log(myFunc2(1, 2, 3, 4, 5)) // [1, 2, [3, 4, 5]]
    console.log(myFunc2(1, 2)) // [1, 2, []]
    ```
    
- 객체와의 사용
- 배열과의 사용

### ⭐⭐화살표 함수 표현식(Arrow Function Expressions)⭐⭐

- 함수 표현식의 간결한 표현법

```jsx
// 변경 이전
const arrow = function (name) {
	return `Hello, ${name}`
}

//변경 후
const arrow = name => `Hello, ${name}`
```

- 작성 과정

```jsx
const arrow1 = function (name) {
	return `hello, ${name}`
}

// 1. function 키워드 제거 후 매개변수와 중괄호 사이에 화살표(⇒) 작성
const arrow2 = (name) => { return `hello, ${name}` }

// 2. 인자가 1개일 경우에만 () 생략 가능
const arrow2 = name => { return `hello, ${name}` }

// 3. 함수 본문의 표현식이 한 줄이라면, '{}'와 'return' 제거 가능
const arrow2 = name => `hello, ${name}`
```

## 객체(Object)

- 키로 구분된 데이터 집합(data collection)을 저장하는 자료형
- 상태와 행동의 모음

### 객체 구조

- 중괄호를 이용해 작성
- 중괄호 안에는 key:value 쌍으로 구성된 속성(property)를 여러 개 작성 가능
- key는 문자형만 허용
- value는 모든 자료형 허용

```jsx
const user = {
	name: 'Alice',
	'key with space': true,
	greeting: function() {
		return 'hello'	
	}
}
```

### 속성 참조

- 점(’.’, chaining operator) 또는 대괄호([])로 객체 요소 접근
- key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능

```jsx
// 조회
console.log(user.name) // Alice
console.log(user['key with space']) // true

// 추가
user.address = 'korea'
console.log(user) // {name: 'Alice', 'key with space': true, address: 'korea', greeting: f}

// 수정
user.name = 'Bella'
console.log(user.name) // Bella

// 삭제
delete user.name
console.log(user) // {'key with space': true, address: 'korea', greeting: f}
```

### ‘in’ 연산자

- 속성이 객체에 존재하는지 여부를 확인

```jsx
console.log('greeting' in user) // true
console.log('country' in user) // false
```

### Method

- 객체 속성에 정의된 함수
- object.method() 방식으로 호출
- 메서드는 객체를 ‘행동’할 수 있게 함

```jsx
console.log(user.greeting()) // hello
```

### this

- 함수나 메서드를 호출한 객체를 가리키는 키워드
- this 키워드를 사용해 객체에 대한 특정한 작업을 수행할 수 있음
- 함수 내에서 객체의 속성 및 메서드에 접근하기 위해 사용

```jsx
const person = {
	name: 'Alice',
	greeting: function () {
		return `Hello my name is ${this.name}`
	},
}

console.log(person.greeting()) // Hello my name is Alce
```

- JavaScript에서 this는 함수를 "**호출하는 방법**"에 따라 가리키는 대상이 다름
    - 단순 호출 시 this
        - 가리키는 대상 ⇒ 전역 객체
        
        ```jsx
        const myFunc = function() {
        	return this
        }
        
        console.log(myFunc()) // window
        ```
        
    - 메서드 호출 시 this
        - 가리키는 대상 ⇒ 메서드를 호출한 객체
        
        ```jsx
        const myObj = {
        	data: 1,
        	myFunc: function() {
        		return this
        	}
        }
        
        console.log(myObj.myFunc()) // myObj
        ```
        
    - 중첩된 함수에서의 this 문제점과 해결책
    
    ```jsx
    /* 
    forEach의 인자로 작성된 콜백 함수는 일반적인 함수 호출이기 때문에 this가 전역 객체를 가리킴
    */
    
    const myObj2 = {
    	numbers: [1, 2, 3],
    	myFunc: function() {
    		this.numbers.forEach(function(number) {
    			console.log(this) // window
    		})
    	}
    }
    
    console.log(myObj2.myFunc())
    ```
    
    ```jsx
    /*
    화살표 함수는 자신만의 this를 가지지 않기 때문에 외부 함수에서의 this 값을 가져옴
    화살표 함수의 this는 렉시컬 this이므로 "바로 위"의 this를 따라간다.
    */
    
    const myObj3 = {
    	numbers: [1, 2, 3],
    	myFunc: function() {
    		this.numbers.forEach((number) => {
    			console.log(this) // myObj3
    		})
    	}
    }
    
    console.log(myObj3.myFunc())
    ```
    
- JavaScript의 함수는 호출될 때 this를 암묵적으로 전달 받음
- Python의 self와 Java의 this가 선언 시 값이 이미 정해지는 것에 비해 JavaScript의 this는 **함수가 호출되기 전까지 값이 할당되지 않고 호출 시에 결정**됨(동적 할당)

### 단축 속성

- 키 이름과 값으로 쓰이는 변수의 이름이 같은 경우 단축 구문을 사용할 수 있음

```jsx
const name = 'Alice'
const age = 30

// 변경 전
const user = {
	name: name,
	age: age,
}

// 변경 후
const user = {
	user,
	name,
}
```

### 단축 메서드

- 메서드 선언 시 function 키워드 생략 가능

```jsx
const myObj1 = {
	myFunc: function () {
		return 'Hello'
	}
}

// 단축 메서드
const myObj2 = {
	myFunc() {
		return 'Hello'
	}
}
```

### 계산된 속성(computed property name)

- 키가 대괄호([])로 둘러싸여 있는 속성
- 고정된 값이 아닌 변수 값을 사용할 수 있음

```jsx
const product = prompt('물건 이름을 입력해주세요')
const prefix = 'my'
const suffix = 'property'

const bag = {
	[product]: 5,
	[prefix + suffix]: 'value',
}

console.log(bag) // {연필: 5, myproperty: 'value'}
```

### 구조 분해 할당(destructing assignment)

- 배열 또는 객체를 분해하여 속성을 변수에 쉽게 할당할 수 있는 문법

```jsx
const userInfo = {
	firstName: 'Alice',
	userId: 'alice123',
	email: 'alice123@gmail.com'
}

// const { firstName } = userInfo
// const { firstName, userId } = userInfo
const { firstName, userId, email } = userInfo

// Alice alice123 alice123@gmail.com
console.log(firstName, userId, email)
```

- 함수의 매개변수로 객체 구조 분해 할당 활용 가능

```jsx
function printInfo({name, age, city}) {
	console.log(`이름: ${name}, 나이: ${age}, 도시: ${city}`)
}

const person = {
	name: 'Bob',
	age: 35,
	city: 'London',
}

// 함수 호출 시, 객체를 구조 분해하여 함수의 매개변수로 전달
printInfo(person) // 이름: Bob, 나이: 35, 도시: London
```

### Object with ‘전개 구문’

- 객체 복사
    - 객체 내부에서 객체 전개
- 얕은 복사에 활용 가능

```jsx
const obj = {b: 2, c: 3, d: 4}
const newObj = {a: 1, ...obj, e: 5}

console.log(newObj) // {a: 1, b: 2, c: 3, d: 4, e: 5}
```

### 유용한 객체 메서드

- Object.keys()
- Object.values()

```jsx
const profile = {
	name: 'Alice',
	age: 30,
}

console.log(Object.keys(profile)) // ['name', 'age']

console.log(Object.values(profile)) // ['Alice', 30]
```

### Optional chaining(’?.’)

- 속성이 없는 중첩 객체를 에러 없이 접근할 수 있음
- 만약 참조 대상이 null 또는 undefined라면 에러가 발생하는 것 대신 평가를 멈추고 undefined를 반환

```jsx
const user = {
	name: 'Alice',
	greeting: function () {
		return 'hello'
	}
}

console.log(user.address.street) // Uncaught TypeError
console.log(user.address?.street) // undefined

console.log(user.nonMethod()) // Uncaught TypeError
console.log(user.nonMethod?.()) // undefined

```

- Optional chaining이 없다면 다음과 같이 ‘&&’ 연산자를 사용해야 함

```jsx
console.log(user.address && user.address.street) // undefined
```

- Optional chaining 장점
    - 참조가 누락될 가능성이 있는 경우 연결된 속성으로 접근할 때 더 짧고 간단한 표현식을 작성할 수 있음
    - 어떤 속성이 필요한지에 대한 보증이 확실하지 않는 경우에 객체의 내용을 보다 편리하게 탐색할 수 있음
- Optional chaining 주의사항
    - Optional chaining은 존재하지 않아도 괜찮은 대상에만 사용해야 함(남용 X)
        - 왼쪽 평가대상이 없어도 괜찮은 경우에만 선택적으로 사용
        
        ```jsx
        // user 객체는 값이 할당되어 있지 않으면 바로 알아낼 수 있어야 해서
        // 논리상 반드시 있어야 하지만 address는 필수 값이 아님
        
        // 잘못된 예시
        user?.address?.street
        ```
        
    - Optional chaining 앞의 변수는 반드시 선언되어 있어야 함
    
    ```jsx
    console.log(myObj?.address) // Uncaught ReferenceErorr: myObj is not defined
    ```
    
- Optional chaining 요약
    - obj?.prop
        - obj가 존재하면 obj.prop을 반환하고, 그렇지 않으면 undefined 반환
    - obj?.[prop]
        - obj가 존재하면 obj[prop]을 반환하고, 그렇지 않으면 undefined 반환
    - obj?.method()
        - obj가 존재하면 obj.method()를 호출하고, 그렇지 않으면 undefined 반환

### JSON(JavaScript Object Notation)

- Key-Value 형태로 이루어진 자료 표기법
- JavaScript의 Object와 유사한 구조를 가지고 있지만 JSON은 형식이 있는 **“문자열”**
- JavaScript에서 JSON을 사용하기 위해서는 Object 자료형으로 변경해야 함

```jsx
const jsObject = {
	coffee: 'Americano',
	iceCream: 'Cookie and cream',
}

// Object => JSON
const objToJson = JSON.stringify(jsObject)
console.log(objToJson) // {"coffee":"Americano", "iceCream":"Cookie and cream"}
console.log(typeof objToJson) // string

// JSON => Object
const jsonToObj = JSON.parse(objToJson)
console.log(jsonToObj) // { coffee: 'Americano', iceCream: 'Cookie and cream'}
console.log(typeof jsonToObj) // object
```

## 배열(Array)

- 순서가 있는 데이터 집합을 저장하는 자료구조

### 배열 구조

- 대괄호([])를 이용해 작성
- 배열 요소 자료형: 제약 없음
- length 속성을 사용해 배열에 담긴 요소가 몇 개인지 알 수 있음

```jsx
const names = ['Alice', 'Bella', 'Cathy',]

console.log(names[0]) // Alice
console.log(names[1]) // Bella
console.log(names[2]) // Cathy

console.log(names.length) // 3
```

### 배열 메서드

- pop()
    - 배열 끝 요소를 제거하고, 제거한 요소를 반환
    
    ```jsx
    const names = ['Alice', 'Bella', 'Cathy']
    
    console.log(names.pop()) // Cathy
    console.log(names) // ['Alice', 'Bella']
    ```
    
- push()
    - 배열 끝에 요소를 추가
    
    ```jsx
    names.push('Dan')
    console.log(names) // ['Alice', 'Bella', 'Dan']
    ```
    
- shift()
    - 배열 앞 요소를 제거하고, 제거한 요소를 반환
    
    ```jsx
    console.log(names.shift()) // Alice
    console.log(names) // ['Bella', 'Dan']
    ```
    
- unshift()
    - 배열 앞에 요소를 추가
    
    ```jsx
    names.unshift('Eric')
    console.log(names) // ['Eric', 'Bella', 'Dan']
    ```
    

### ⭐⭐Array helper method⭐⭐

- 배열을 순회하며 특정 로직을 수행하는 메서드
- 메서드 호출 시 인자로 함수(콜백 함수)를 받는 것이 특징
- forEach()
    
    ```jsx
    arr.forEach(callback(item[, index[, array]]))
    ```
    
    - 인자로 주어진 함수(콜백 함수)를 배열 요소 각각에 대해 실행
    - 매개변수
        - item: 처리할 배열의 요소
        - index: 처리할 배열 요소의 인덱스(선택 인자)
        - array: forEach를 호출한 배열(선택 인자)
    - 반환 값 ⇒ undefined
    
    ```jsx
    const names = ['Alice', 'Bella', 'Cathy']
    
    // 일반 함수 표기
    names.forEach(function (item, index, array) {
    	console.log(`${item} / ${index} / ${arary}`)
    })
    
    // 화살표 함수 표기
    names.forEach((item, index, array) => {
    	console.log(`${item} / ${index} / ${arary}`)
    })
    ```
    
- 콜백함수
    - 다른 함수에 인자로 전달되는 함수
    - 외부 함수내에서 호출되어 일종의 루틴이나 특정 작업을 진행
    
    ```jsx
    const numbers = [1, 2, 3,]
    
    const callBackFunction = function (num) {
    	console.log(num ** 2)
    }
    
    numbers2.forEach(callBackFunction)
    // 1
    // 4
    // 9
    ```
    
- map()
    - 배열 내의 모든 요소 각각에 대해 함수(콜백 함수)를 호출하고, 함수 호출 결과를 모아 **새로운 배열을 반환**
    
    ```jsx
    arr.map(callback(item[, index[, array]]))
    ```
    
    - 매개변수
        - item: 처리할 배열의 요소
        - index: 처리할 배열 요소의 인덱스 (선택 인자)
        - array: map을 호출한 배열 (선택 인자)
    - 반환 값
        - 배열의 각 요소에 대해 실행한 “callback의 결과를 모은 새로운 배열”
        - 기본적으로 forEach 동작 원리와 같지만 forEach와 달리 새로운 배열을 반환함
    
    ```jsx
    const names = ['Alice', 'Bella', 'Cathy',]
    
    const result1 = names.map(function (name) {
    	return name.length
    })
    
    const result2 = names.map((name) => {
    	return name.length
    })
    
    console.log(result1) // [5, 5, 5]
    console.log(result2) // [5, 5, 5]
    ```
    
    - python의 map 함수와 비교
        - python의 map에 square 함수를 인자로 넘겨 numbers 배열의 각 요소를 square 함수의 인자로 사용하였음
        
        ```python
        numbers = [1, 2, 3]
        
        def square(num):
        	return num ** 2
        
        new_numbers = list(map(square, numbers))
        ```
        
        - map 메서드에 callBackFunc 함수를 인자로 넘겨 numbers 배열의 각 요소를 callBackFunc 함수의 인자로 사용하였음
        
        ```jsx
        const numbers = [1, 2, 3]
        
        const callBackFunction = function (number) {
        	return number ** 2
        }
        
        const newNumbers = numbers.map(callBackFunction)
        ```
        
- 배열 순회 종합

| 방식 | 특징 | 비고 |
| --- | --- | --- |
| for loop | - 배열의 인덱스를 이용하여 각 요소에 접근<br>- break, continue 사용 가능 |  |
| for … of  | - 배열 요소에 바로 접근 가능<br>- break, continue 사용 가능 |  |
| forEach | - 간결하고 가독성이 높음<br>- callback 함수를 이용하여 각 요소를 조작하기 용이<br>- break, continue 사용 불가능 | 사용 권장 |

# Event

- 무언가 일어났다는 신호, 사건
- 모든 DOM 요소는 이러한 event를 만들어 냄
- 웹 에서의 이벤트
    - 버튼을 클릭했을 때 팝업 창이 출력되는 것
    - 마우스 커서의 위치에 따라 드래그 앤 드롭하는 것
    - 사용자의 키보드 입력 값에 따라 새로운 요소를 생성하는 것
    - **이벤트를 통해 특정 동작을 수행**

## event object

- DOM에서 이벤트가 발생했을 때 생성되는 객체
- 이벤트 종류
    - mouse, input, keyboard, touch 등
    - [https://developer.mozilla.org/en-US/docs/Web/API/Event](https://developer.mozilla.org/en-US/docs/Web/API/Event)

## Event handler(이벤트 처리기)

- 이벤트가 발생했을 때 실행되는 함수
- 사용자의 행동에 어떻게 반응할지를 JavaScript 코드로 표현한 것
- DOM 요소는 event를 받고 받은 event를 ‘처리’ 할 수 있음

### .addEventListener()

- 대표적인 이벤트 핸들러 중 하나
- 특정 이벤트를 DOM  요소가 수신할 때마다 콜백 함수를 호출

![Untitled 9](https://github.com/yuj1818/TIL/assets/95585314/39023393-66c0-473c-a096-791e9514b68b)

- “대상에 특정 Event가 발생하면, 지정한 이벤트를 받아 할 일을 등록한다”
- type
    - 수신할 이벤트 이름
    - 문자열로 작성
- handler
    - 발생한 이벤트 객체를 수신하는 콜백 함수
    - 콜백 함수는 발생한 Event Object를 유일한 매개변수로 받음
- addEventListener의 콜백 함수 특징
    - 발생한 이벤트를 나타내는 Event 객체를 유일한 매개변수로 받음
    - 아무것도 반환하지 않음
    
    ```jsx
    const btn = document.querySelector('#btn')
    
    const detectClick = function (event) {
    	console.log(event)
    	console.log(event.currentTarget)
    	console.log(this)
    }
    
    btn.addEventListener('click', detectClick)
    ```
    

## 버블링(Bubbling)

- 한 요소에 이벤트가 발생하면, 이 요소에 할당된 핸들러가 동작하고, 이어서 부모 요소의 핸들러가 동작하는 현상
- 가장 최상단의 조상 요소(document)를 만날 때까지 이 과정이 반복되면서 요소 각각에 할당된 핸들러가 동작
- 이벤트가 제일 깊은 곳에 있는 요소에서 시작해 부모 요소를 거슬러 올라가며 발생하는 것이 마치 물속 거품과 닮았기 때문
- 예시
    - 가장 안쪽의 <p>요소를 클릭하면 p ⇒ div ⇒ form 순서로 3개의 이벤트 핸들러가 동작
    
    ![Untitled 10](https://github.com/yuj1818/TIL/assets/95585314/1ff2b996-e6b6-43a0-8bb1-c082755ceadc)
    
    ```html
    <body>
      <form id="form">
        form
        <div id="div">
          div
          <p id="p">p</p>
        </div>
      </form>
    
      <script>
        const formElement = document.querySelector('#form')
        const divElement = document.querySelector('#div')
        const pElement = document.querySelector('#p')
    
        const clickHandler1 = function (event) {
          console.log('form이 클릭되었습니다.')
        }
        const clickHandler2 = function (event) {
          console.log('div가 클릭되었습니다.')
        }
        const clickHandler3 = function (event) {
          console.log('p가 클릭되었습니다.')
        }
    
        formElement.addEventListener('click', clickHandler1)
        divElement.addEventListener('click', clickHandler2)
        pElement.addEventListener('click', clickHandler3)
      </script>
    </body>
    ```
    

### ‘target’ & ‘currentTarget’ 속성

- target
    - 이벤트가 발생한 가장 안쪽의 요소(target)를 참조하는 속성
    - **실제 이벤트가 시작된 target 요소**
    - 버블링이 진행 되어도 변하지 않음
- currentTarget
    - 현재 요소
    - 항상 **이벤트 핸들러가 연결된 요소만을 참조**하는 속성
    - this와 같음
    - 주의사항
        - console.log()로 event 객체를 출력할 경우 currentTarget 키의 값을 null을 가짐
        - currentTarget은 이벤트가 처리되는 동안에만 사용할 수 있기 때문
        - 대신 console.log(event.currentTarget)을 사용하여 콘솔에서 확인 가능
        - currentTarget 이후의 속성 값들은 **‘target’을 참고해서 사용하기**
- 예시
    - 세 요소 중 가장 최상위 요소인 outerouter 요소에만 이벤트 핸들러가 부착
    - 각 요소를 클릭했을 때, event의 target과 currentTarget의 차이 비교
    
    ```html
    <body>
      <div id="outerouter">
        outerouter
        <div id="outer">
          outer
          <div id="inner">inner</div>
        </div>
      </div>
    
      <script>
        const outerOuterElement = document.querySelector('#outerouter')
    
        const clickHandler = function (event) {
          console.log('currentTarget:', event.currentTarget.id)
          console.log('target:', event.target.id)
        }
    
        outerOuterElement.addEventListener('click', clickHandler)
      </script>
    </body>
    ```
    
    ![Untitled 11](https://github.com/yuj1818/TIL/assets/95585314/c1117f17-a28b-4608-b77b-1b1a37386962)

    

### 캡쳐링

```jsx
const btn = document.querySelector('#btn')
btn.addEventListener('click', () => {}, {capture: true})
```

## event handler 활용

### 버튼을 클릭하면 숫자를 1씩 증가해서 출력하기

```html
<body>
    <button class="btn">버튼</button>
    <p>클릭 횟수 : <span class="counter">0</span></p>
    <script>
        const btn = document.querySelector('.btn')
        const counter = document.querySelector('.counter')
        let count = 0
        const onClick = () => {
            count += 1
            counter.textContent = count
        }
        btn.addEventListener('click', onClick)
    </script>
</body>
```

### 사용자의 입력 값을 실시간으로 출력하기

```html
<body>
    <input type="text" class="input">
    <p class="result"></p>
    <script>
        const input = document.querySelector('.input')
        const result = document.querySelector('.result')

        const printResult = (event) => {
            console.log(event.target.value)
            result.textContent = event.target.value
        }

        input.addEventListener('input', printResult)
    </script>
</body>
```

### 사용자의 입력 값을 실시간으로 출력 + 버튼 클릭 시, 출력값 CSS 변경

```html
<body>
    <h1 class="result"></h1>
    <button class="btn">클릭</button>
    <input type="text" class="input-text">
    <script>
        const result = document.querySelector('.result')
        const btn = document.querySelector('.btn')
        const inputText = document.querySelector('.input-text')

        const changeColor = () => {
            result.classList.toggle('blue')
        }

        const printResult = event => {
            result.textContent = event.target.value
        }

        btn.addEventListener('click', changeColor)
        inputText.addEventListener('input', printResult)
    </script>
</body>
```

### todo 실습

```html
<body>
    <input type="text" class="text-input">
    <button class="btn">+</button>
    <ul class="todo-list">
    </ul>
    <script>
        const textInput = document.querySelector('.text-input')
        const btn = document.querySelector('.btn')
        const todoList = document.querySelector('.todo-list')

        const onSubmit = () => {
            const todo = document.createElement('li')
            const inputText = textInput.value
            if (inputText.trim()) {
                todo.textContent = textInput.value
                todoList.appendChild(todo)
                textInput.value = ''
            } else {
                alert('할 일을 입력하세요.')
            }
        }

        btn.addEventListener('click', onSubmit)
    </script>
</body>
```

### 로또 번호 생성기

```html
<body>
    <h1>로또 추천 번호</h1>
    <button class="btn">행운 번호 받기</button>
    <div class="content"></div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.21/lodash.min.js" integrity="sha512-WFN04846sdKMIP5LKNphMaWzU7YpMyCU245etK3g/2ARYbPK9Ub18eG+ljU96qKRCWh+quCY7yefSmlkQw1ANQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <script>
        const btn = document.querySelector('.btn')
        const content = document.querySelector('.content')

        const onClick = () => {
            const numbers = _.range(1, 46)
            const chosenNumbers = _.sampleSize(numbers, 6)

            const ulTag = document.createElement('ul')
            for (number of chosenNumbers) {
                const liTag = document.createElement('li')
                liTag.textContent = number
                ulTag.appendChild(liTag)
            }

            content.appendChild(ulTag)
        }

        btn.addEventListener('click', onClick)
    </script>
</body>
```

## 이벤트 기본 동작 취소

### .preventDefault()

- 해당 이벤트에 대한 기본 동작을 실행하지 않도록 지정
- 예시
    - copy 이벤트 동작 취소
    
    ```html
    <body>
        <h1 class="content">중요한 내용</h1>
        <script>
            const content = document.querySelector('.content')
            content.addEventListener('copy', (event) => {
                event.preventDefault()
                alert('복사 안됨')
            })
        </script>
    </body>
    ```
    
    - form 제출 시 새로 고침 동작 취소
    
    ```html
    <body>
        <form id="my-form">
            <input type="text" name="username">
            <button type="submit">Submit</button>
        </form>
        <script>
            const formTag = document.querySelector('form')
    
            const handleSubmit = (event) => {
                event.preventDefault()
            }
    
            formTag.addEventListener('submit', handleSubmit)
        </script>
    </body>
    ```
    

# Asynchronous JavaScript

## 비동기

### Synchronous(동기)

- 순서가 보장되는 방식
- 프로그램의 실행 흐름이 순차적으로 실행
- 하나의 작업이 완료된 후에 다음 작업이 실행되는 방식
- 예시
    - 메인 작업이 모두 수행되어야 마지막 작업이 수행됨
    
    ```python
    print('첫번째 작업')
    for i in range(10):
    	print('메인 작업')
    print('마지막 작업')
    ```
    
    - 함수의 작업이 완료될 때까지 기다렸다가 값을 반환해야 계속 진행할 수 있음(동기 함수)
    
    ```jsx
    const makeGreeting = function(name) {
    	return `Hello, my name is ${name}!`
    }
    
    const name = 'Alice'
    const greeting = makeGreeting(name)
    console.log(greeting)
    ```
    

### Asynchronous(비동기)

- 프로그램의 실행 흐름이 순차적이지 않으며, 작업이 완료되기를 기다리지 않고 다음 작업이 실행되는 방식
- 순서가 보장되지 않음
- 동시에 여러 일을 수행하는 것은 아님. JavaScript는 싱글 스레드 언어라 동시에 일을 처리할 수 없음
- 병렬적 수행
- 당장 처리를 완료할 수 없고 시간이 필요한 작업들은 별도로 요청을 보낸 뒤 응답이 빨리 오는 작업부터 처리
- 예시
    - Gmail에서 메일 전송을 누르면 목록 화면으로 전환되지만 실제로 메일을 보내는 작업은 병렬적으로 별도로 처리됨
    - 브라우저는 웹페이지를 먼저 처리되는 요소부터 그려 나가며 처리가 오래 걸리는 것들은 별도로 처리가 완료 되는 대로 병렬적으로 처리
    
    ```jsx
    const slowRequest = function (callBack) {
    	console.log('1. 오래 걸리는 작업 시작 ...')
    	setTimeout(function () {
    		callBack()
    	}, 3000)
    }
    
    const myCallBack = function () {
    	console.log('2. 콜백 함수 실행됨')
    }
    
    slowRequest(myCallBack)
    
    console.log('3. 다른 작업 실행')
    
    // 출력 결과
    // 1. 오래 걸리는 작업 시작 ...
    // 3. 다른 작업 실행
    // 2. 콜백 함수 실행됨
    ```
    

## JavaScript와 비동기

- JavaScript는 Single Thread 언어
    - `Thread` : 작업을 처리할 때 실제로 작업을 수행하는 주체
- JavaScript는 한번에 여러 일을 수행할 수 없고 하나의 작업을 요청한 순서대로 처리할 수 밖에 없음

### JavaScript Runtime

- JavaScript가 동작할 수 있는 환경(Runtime)
- JavaScript 자체는 Single Thread이므로 비동기 처리를 할 수 있도록 도와주는 환경이 필요
- JavaScript에서 비동기와 관련한 작업은 “브라우저” 또는 “Node”와 같은 환경에서 처리

### 브라우저 환경에서의 JavaScript 비동기 처리 관련 요소

- JavaScript Engine의 **Call Stack**
    - 요청이 들어올 때 마다 순차적으로 처리하는 Stack(LIFO)
    - 기본적인 JavaScript의 Single Thread 작업 처리
- **Web API**
    - JavaScript 엔진이 아닌 브라우저에서 제공하는 runtime 환경
    - 시간이 소요되는 작업을 처리 (setTimeout, DOM Event, AJAX 요청 등)
- **Task Queue**
    - 비동기 처리된 Callback 함수가 대기하는 Queue(FIFO)
- **Event Loop**
    - 태스크(작업)가 들어오길 기다렸다가 태스크가 들어오면 이를 처리하고, 처리할 태스크가 없는 경우엔 잠드는, 끊임없이 돌아가는 JavaScript 내 루프
    - Call Stack과 Task Queue를 지속적으로 모니터링
    - Call Stack이 비어 있는지 확인 후 비어 있다면 Task Queue에서 대기 중인 오래된 작업을 Call Stack으로 Push
    
    ![Untitled 12](https://github.com/yuj1818/TIL/assets/95585314/3af24d55-31be-465d-a30f-56b5e7ad4d9c)
    

### 브라우저 환경에서의 JavaScript 비동기 처리 동작 방식

1. 모든 작업은 Call Stack(LIFO)으로 들어간 후 처리됨
2. 오래 걸리는 작업이 Call Stack으로 들어오면 Web API로 보내 별도로 처리하도록 함
3. Web API에서 처리가 끝난 작업들은 곧바로 Call Stack으로 들어가지 못하고 Task Queue(FIFO)에 순서대로 들어감
4. Event Loop가 Call Stack이 비어 있는 것을 계속 체크하고 Call Stack이 빈다면 Task Queue에서 가장 오래된 (가장 먼저 처리되어 들어온) 작업을 Call Stack으로 보냄

![javascript_runtime](https://github.com/yuj1818/TIL/assets/95585314/2e32741c-9c38-4a4b-a679-a3ea35d42135)

## AJAX(Asynchronous JavaScript + XML)

- JavaScript의 비동기 구조와 XML 객체를 활용해 비동기적으로 서버와 통신하여 웹 페이지의 일부분만을 업데이트하는 웹 개발 기술
    - ‘X’가 XML을 의미하긴 하지만, 요즘은 더 가벼운 용량과 JavaScript의 일부라는 장점 때문에 ‘JSON’을 더 많이 사용

### XMLHttpRequest 객체

- 서버와 상호작용할 때 사용하며 페이지의 새로고침 없이도 URL에서 데이터를 가져올 수 있음
- 사용자의 작업을 방해하지 않고 페이지의 일부를 업데이트
- 주로 AJAX 프로그래밍에 많이 사용됨

### 이벤트 핸들러는 비동기 프로그래밍의 한 형태

- 이벤트가 발생할 때마다 호출되는 함수(콜백 함수)를 제공하는 것
- XMLHttpRequest(XHR)는 JavaScript를 사용하여 서버에 HTTP 요청을 할 수 있는 객체
- HTTP 요청은 응답이 올 때 까지의 시간이 걸릴 수 있는 작업이라 비동기 API이며, 이벤트 핸들러를 XHR 객체에 연결해 요청의 진행 상태 및 최종 완료에 대한 응답을 받음

### Axios

- JavaScript에서 사용되는 Promise 기반 HTTP 클라이언트 라이브러리
- 서버와의 HTTP 요청과 응답을 간편하게 처리할 수 있도록 도와주는 도구
- 브라우저에서 비동기로 데이터 통신을 가능하게 하는 라이브러리
    - 브라우저를 위해 XMLHttpRequest 생성
- 같은 방식으로 DRF로 만든 API 서버로 요청을 보내서 데이터를 받아온 후 처리할 수 있도록 함

```html
<!-- axios CDN -->
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
```

- Axios 구조
    - get, post 등 여러 request method 사용 가능
    - then 메서드를 사용해서 “성공하면 수행할 로직”을 작성
    - catch 메서드를 사용해서 “실패하면 수행할 로직”을 작성
    
    ```jsx
    axios({
    	method: 'post',
    	url: '/user/12345',
    	data: {
    		firstName: 'Fred',
    		lastName: 'Flintstone'
    	}
    })
    	.then(/*요청에 성공하면 수행할 콜백 함수*/)
    	.catch(/*요청에 실패하면 수행할 콜백 함수*/)
    ```
    
- 예시(고양이 사진 가져오기)

```jsx
<body>
  <button>냥냥펀치</button>
  <script script src="https://unpkg.com/axios/dist/axios.min.js"></script>
  <script>
    const URL = 'https://api.thecatapi.com/v1/images/search/'
    const btn = document.querySelector('button')

    function getCatImg() {
      axios({
        method: 'get',
        url: URL,
      })
        .then(response => {
          const imgTag = document.createElement('img')
          imgTag.src = response.data[0].url
          const bodyTag = document.querySelector('body')
          bodyTag.appendChild(imgTag)
        })
        .catch(error => {
          console.log(error)
          console.log('실패')
        })
    }

    btn.addEventListener('click', getCatImg)

  </script>
</body>
```

## Callback과 Promise

### 비동기 처리의 단점

- 비동기 처리의 핵심은 Web API로 들어오는 순서가 아니라 **작업이 완료되는 순서에 따라 처리**한다는 것
- 그런데 이는 개발자 입장에서 **코드의 실행 순서가 불명확**하다는 단점 존재
- 이와 같은 단점은 실행 결과를 예상하면서 코드를 작성할 수 없게 함
    
    ⇒ 콜백 함수를 사용해야 함
    

### 비동기 콜백

- 비동기적으로 처리되는 작업이 완료되었을 때 실행되는 함수
- 연쇄적으로 발생하는 비동기 작업을 순차적으로 동작할 수 있게 함
- 작업의 순서와 동작을 제어하거나 결과를 처리하는 데 사용

```jsx
const asyncTask = function (callBack) {
	setTimeout(function () {
		console.log('비동기 작업 완료')
		callBack() // 작업 완료 후 콜백 호출
	}, 3000) // 3초 후에 작업 완료
}

// 비동기 작업 수행 후 콜백 실행
asyncTask(function () {
	console.log('작업 완료 후 콜백 실행')
})

// 출력 결과
// 비동기 작업 완료
// 작업 완료 후 콜백 실행

```

### 비동기 콜백의 한계

- 비동기 콜백 함수는 보통 어떤 기능의 실행 결과를 받아서 다른 기능을 수행하기 위해 많이 사용됨
- 이 과정을 작성하다 보면 비슷한 패턴이 계속 발생
    - **콜백 지옥** 발생
    - 가독성을 해치고 유지보수가 어려워짐
- `콜백 지옥(Callback Hell)`
    - 비동기 처리를 위한 콜백을 작성할 때 마주하는 문제
    - 코드 작성 형태가 마치 “피라미드와 같다”고 해서 “Pyramid of doom”라고도 부름

### 프로미스(Promise)

- JavaScript에서 비동기 작업의 결과를 나타내는 객체
- 비동기 작업이 완료되었을 때 결과 값을 반환하거나, 실패 시 에러를 처리할 수 있는 기능을 제공
- 콜백 지옥 문제를 해결하기 위해 등장한 비동기 처리를 위한 객체
- “작업이 끝나면 실행하겠다”라는 약속(promise)
- 비동기 작업의 완료 또는 실패를 나타내는 객체
- Promise 기반의 클라이언트가 바로 이전에 사용한 Axios 라이브러리
    - 성공에 대한 약속 then()
        - 요청한 작업이 성공하면 callback 실행
        - callback은 이전 작업의 성공 결과를 인자로 전달 받음
    - 실패에 대한 약속 catch()
        - then()이 하나라도 실패하면 callback 실행
        - callback은 이전 작업의 실패 객체를 인자로 전달 받음
    - then과 catch는 모두 항상 promise 객체를 반환
        
        ⇒ 계속해서 **chaining**을 할 수 있음
        
    - axios로 처리한 비동기 로직이 항상 promise 객체를 반환
    - then을 계속 이어 나가면서 작성할 수 있게 됨
- Promise가 보장하는 것
    - 콜백 함수는 JavaScript의 Event Loop가 현재 실행 중인 Call Stack을 완료하기 이전에는 절대 호출되지 않음
        - 반면, Promise Callback 함수는 Event Queue에 배치되는 엄격한 순서로 호출됨
    - 비동기 작업이 성공하거나 실패한 뒤에 .then() 메서드를 이용하여 추가한 경우에도 호출 순서를 보장하며 동작
    - .then()을 여러 번 사용하여 여러 개의 callback 함수를 추가할 수 있음
        - 각각의 callback은 주어진 순서대로 하나하나 실행하게 됨
        - Chaining은 Promise의 가장 뛰어난 장점

### 비동기 콜백 vs Promise

```jsx
// 비동기 콜백 방식
work1(function() {
	// 첫번째 작업 ...
	work2(result1, function(result2) {
		// 두번째 작업 ...
		work3(result2, function(result3) {
			console.log('최종 결과 :' + result3)
		})
	})
})
```

```jsx
// promise 방식
work1()
	.then(result1 => {
		// work2
		return result2
	})
	.then(result2 => {
		// work3
		return result3
	})
	.catch(error => {
		// error handling
	})
```

# Ajax with Django

## Ajax와 서버

### Ajax를 활용한 클라이언트 서버 간 동작

![Untitled 13](https://github.com/yuj1818/TIL/assets/95585314/404f5a73-42af-41b4-9c96-7211dc760777)

- 클라이언트 / 서버
- 이벤트 발생 ⇒ XML 객체 생성 및 요청 ⇒ Ajax 요청 처리  ⇒ 응답 데이터 생성 ⇒ JSON 데이터 응답 ⇒ 응답 데이터를 활용해 DOM 조작(웹 페이지 일부분 만을 다시 로딩)

## Ajax with follow(follow 기능 구현)

### Ajax 적용

- 프로필 페이지에 axios CDN 작성

```html
<body>
	<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
	<script></script>
</body>
```

- form 요소 선택을 위해 id 속성 지정 및 선택

```html
<form id="follow-form">
  ...
</form>
<script>
	const formTag = document.querySelector('#follow-form')
</script>
```

- form 요소에 이벤트 핸들러 작성 및 submit 이벤트의 기본 동작 취소

```html
<script>
	...
	formTag.addEventListener('submit', function(e) {
		e.preventDefault()
	})
</script>
```

- axios 요청 작성

```html
<form id="follow-form" data-user-id="{{ person.pk }}">
  ...
</form>
<script>
	...
	formTag.addEventListener('submit', function(e) {
		e.preventDefault()

		const userId = formTag.dataset.userId		

		axios({
			method: 'post',
			url: `/accounts/${userId}/follow/`,
		})
	})
</script>
```

- **‘data-*’ 속성**
    - 사용자 지정 데이터 특성을 만들어 임의의 데이터를 HTML과 DOM 사이에서 교환할 수 있는 방법
    - 모든 사용자 지정 데이터는 JavaScript에서 **dataset** 속성을 통해 사용
    - 주의사항
        - 대소문자 여부에 상관없이 ‘xml’ 문자로 시작 불가
        - 세미콜론 포함 불가
        - 대문자 포함 불가
- 문서상 hidden 타입으로 존재하는 csrf 데이터를 이제는 axios로 전송해야 함
    - csrf 값을 가진 input 요소를 직접 선택 후 axios에 작성하기

```html
<script>
	...
	const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
	
	formTag.addEventListener('submit', function(e) {
		e.preventDefault()
		
		const userId = formTag.dataset.userId

		axios({
			method: 'post',
			url: `/accounts/${userId}/follow/`,
			headers: {'X-CSRFToken': csrftoken,},
		})
	})
</script>
```

- 팔로우 버튼을 토글하기 위해서는 현재 팔로우 상태인지 언팔로우 상태인지에 대한 상태 확인이 필요
    - django의 view 함수에서 팔로우 여부를 파악할 수 있는 변수를 추가로 생성해 JSON 타입으로 응답하기
    - 응답은 더 이상 HTML 문서가 아닌 JSON 데이터로 응답

```python
# accounts/views.py

from django.http import JsonResponse

@login_required
def follow(request, user_pk):
	User = get_user_model()
	person = User.objects.get(pk=user_pk)
	if person != request.user:
		if person.followers.filter(pk=request.user.pk).exists():
			person.followers.remove(request.user)
			is_followed = False
		else:
			person.followers.add(request.user)
			if_followed = True
		context = {
			'is_followed': is_followed,
		}
		return JsonResponse(context)
	return redirect('accounts:profile', person.username)
```

- 팔로우 요청 후 Django 서버로 부터 받은 데이터 확인하기

```html
<script>
	...
	formTag.addEventListener('submit', function(e) {
	  e.preventDefault()
	
	  const userId = formTag.dataset.userId
	
	  axios({
	    method: 'post',
	    url: `/accounts/${userId}/follow/`,
	    headers: {'X-CSRFToken': csrftoken}
	  })
	    .then(response => {
	      console.log(response)
	      console.log(response.data)
	    })
	})
</script>
```

- 응답 데이터 is_followed에 따라 팔로우 버튼 토글

```html
<script>
	...
	axios({
    method: 'post',
    url: `/accounts/${userId}/follow/`,
    headers: {'X-CSRFToken': csrftoken}
  })
    .then(response => {
      //console.log(response.data)
      const isFollowed = response.data.is_Followed
      const followBtn = document.querySelector('input[type=submit]')
      if (isFollowed === true){
        followBtn.value = 'Unfollow'
      } else{
        followBtn.value = 'Follow'
      }
    })
</script>
```

- 팔로잉 수와 팔로워 수 비동기 적용
    - 해당 요소를 선택할 수 있도록 span 태그와 id 속성 작성
    
    ```html
    <body>
    	...
    	<div>
    		팔로잉 : <span id="following-count">{{ person.followings.all|length }}</span> /
        팔로워 : <span id="followers-count">{{ person.followers.all|length }}</span>
    	</div>
    	...
    </body>
    ```
    
    - 각 span 태그를 선택
    
    ```html
    <script>
    	.then(response => {
    		...
    		const followingsCountTag = document.querySelector('#followings-count')
        const followersCountTag = document.querySelector('#followers-count')
    	})
    </script>
    ```
    
    - Django view 함수에서 팔로워, 팔로잉 인원 수 연산을 진행하여 결과를 응답으로 전달
    
    ```python
    # accounts/views.py
    
    def follow(request, user_pk):
    	...
    		context = {
    	      'is_Followed': is_Followed,
    	      'followings_count': you.followings.count(),
    	      'followers_count': you.followers.count(),
    	  }
    		return JsonResponse(context)
    
    ```
    
    - 응답 데이터의 연산 결과를 각 태그의 인원수 값 변경에 적용
    
    ```html
    <script>
    		.then(response => {
          ...
          const followingsCountTag = document.querySelector('#followings-count')
          const followersCountTag = document.querySelector('#followers-count')
    
          followingsCountTag.textContent = response.data.followings_count
          followersCountTag.textContent = response.data.followers_count
        })
    </script>
    ```
    

## Ajax with likes(좋아요 기능 구현)

### Ajax 좋아요 적용 시 유의사항

- Ajax 적용은 팔로우와 모두 동일
- 단, 팔로우와 달리 좋아요 버튼은 한 페이지에 여러 개가 존재
    - forEach
    - querySelectorAll

### Ajax 적용

- HTML 완성 부분

```html
...
<form class="like-forms" data-article-id="{{ article.pk }}">
  {% csrf_token %}
  {% if request.user in article.like_users.all %}
    <input type="submit" value="좋아요 취소" id="like-{{ article.pk }}">
  {% else %}
    <input type="submit" value="좋아요" id="like-{{ article.pk }}">
  {% endif %}
</form>
...
```

- view 함수 완성 부분

```python
from django.http import JsonResponse

def likes(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.user in article.like_users.all():
        article.like_users.remove(request.user)
        is_liked = False
    else:
        article.like_users.add(request.user)
        is_liked = True
    context = {
        'is_liked': is_liked,
    }
    return JsonResponse(context)
```

- JavaScript 완성 부분

```html
<script>
	const formTags = document.querySelectorAll('.like-forms')
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

  formTags.forEach((formTag) => {
    formTag.addEventListener('submit', function(e) {
      e.preventDefault()

      const articleId = formTag.dataset.articleId

      axios({
        method: 'post',
        url: `/articles/${articleId}/likes/`,
        headers: {'X-CSRFToken': csrftoken,},
        mode: 'same-origin',
      })
        .then(response => {
          const isLiked = response.data.is_liked
          const likeBtn = document.querySelector(`#like-${articleId}`)
          if (isLiked === true) {
            likeBtn.value = '좋아요 취소'
          } else {
            likeBtn.value = '좋아요'
          }
        })
    })
  })
</script>
```

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

## 참조 자료형 관련

### 화살표 함수 심화

```jsx
// 1. 인자가 없다면 () or _ 로 표시 가능
const noArgs1 = () => 'No args'
const noArgs2 = _ => 'No args'

// 2-1. object를 return 한다면 return을 명시적으로 작성해야 함
const returnObject1 = () => { return { key: 'value' }}

// 2-2. return을 작성하지 않으려면 객체를 소괄호로 감싸야 함
const returnObject2 = () => ({ key: 'value'})
```

### new 연산자

- JS에서 객체를 하나 생성한다면 하나의 객체를 선언하여 생성
- 동일한 형태의 객체를 또 만들려면 또 다른 객체를 선언하여 생성해야 함
- new 연산자는 사용자 정의 객체 타입을 생성

```jsx
new constructor[([arguments])]
```

- 매개변수
    - constructor: 객체 인스턴스의 타입을 기술(명세)하는 함수
    - arguments: constructor와 함께 호출될 값 목록

```jsx
function Member(name, age, sId) {
	this.name = name
	this.age = age
	this.sId = sId
}

const member3 = new Member('Bella', 21, 20226543)

console.log(member3) // Member { name: 'Bella', age: 211111, sId: 20226543 }
console.log(member3.name) // Bella
```

### JavaScript ‘this’ 장단점

- 장점
    - 함수(메서드)를 하나만 만들어 여러 객체에서 재사용할 수 있다는 것
- 단점
    - 이런 유연함이 실수로 이어질 수 있다는 것
- 개발자는 this의 동작 방식을 충분히 이해하고 장점을 취하면서 실수를 피하는 데에 집중

### 추가 배열 문법

- Array with 전개 구문
    - 배열 복사
    
    ```jsx
    let parts = ['어깨', '무릎']
    let lyrics = ['머리', ...parts, '발']
    
    console.log(lyrics) // ['머리', '어깨', '무릎', '발']
    ```
    
- 기타 Array Helper Methods

| 메서드 | 역할 |
| --- | --- |
| filter | 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열을 반환 |
| find | 콜백 함수의 반환 값이 참이면 해당 요소를 반환 |
| some | 배열의 요소 중 하나라도 판별 함수를 통과하면 참을 반환 |
| every | 배열의 모든 요소가 판별 함수를 통과하면 참을 반환 |

### 콜백함수 구조를 사용하는 이유

- 함수의 재사용성 측면
    - 함수를 호출하는 코드에서 콜백 함수의 동작을 자유롭게 변경할 수 있음
    - 예를 들어, map 함수는 콜백 함수를 인자로 받아 배열의 각 요소를 순회하며 콜백 함수를 실행
    - 이때, 콜백 함수는 각 요소를 변환하는 로직을 담당하므로, map 함수를 호출하는 코드는 간결하고 가독성이 높아짐
- 비동기적 처리 측면
    
    ```jsx
    console.log('a')
    
    setTimeout(() => {
    	console.log('b')
    ], 3000)
    
    console.log('c')
    
    // a
    // c
    // b
    ```
    
    - setTimeout 함수는 콜백 함수를 인자로 받아 일정 시간이 지난 후에 실행됨
    - 이때, setTimeout 함수는 비동기적으로 콜백 함수를 실행하므로 다른 코드의 실행을 방해하지 않음

### 배열은 객체다

- 배열은 키와 속성들을 담고 있는 참조 타입의 객체
- 배열은 인덱스를 키로 가지며 length 프로퍼티를 갖는 특수한 객체
- 배열의 요소를 대괄호 접근법을 사용해 접근하는 건 객체 문법과 같음
- 다만 배열의 키는 숫자라는 점
- 숫자형 키를 사용함으로써 배열은 객체 기본 기능 이외에도 순서가 있는 컬렉션을 제어하게 해주는 특별한 메서드를 제공

## 이벤트 관련

### lodash

- 모듈성, 성능 및 추가 기능을 제공하는 JavaScript 유틸리티 라이브러리
- array, object 등 자료구조를 다룰 때 사용하는 유용하고 간편한 함수들을 제공
- [https://lodash](https://lodash).com

```html
<!-- lodash cdn -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.21/lodash.min.js" integrity="sha512-WFN04846sdKMIP5LKNphMaWzU7YpMyCU245etK3g/2ARYbPK9Ub18eG+ljU96qKRCWh+quCY7yefSmlkQw1ANQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
```

### addEventListener에서의 화살표 함수 주의사항

- 화살표 함수는 자신만의 this를 가지지 않기 때문에 자신을 포함하고 있는 함수의 this를 상속받음

```html
<body>
  <button id="function">function</button>
  <button id="arrow">arrow function</button>

  <script>
    const functionButton = document.querySelector('#function')
    const arrowButton = document.querySelector('#arrow')

    functionButton.addEventListener('click', function () {
      console.log(this) // <button id="function">function</button>
    })

    arrowButton.addEventListener('click', () => {
      console.log(this) // window
    })
  </script>
</body>
```

## 비동기 관련

### then 메서드 chaining

- 비동기 작업의 “**순차적인**” 처리 가능
- 코드를 보다 직관적이고 가독성 좋게 작성할 수 있도록 도움
- 장점
    - 가독성
        - 비동기 작업의 순서와 의존 관계를 명확히 표현할 수 있어 코드의 가독성이 향상
    - 에러 처리
        - 각각의 비동기 작업 단계에서 발생하는 에러를 분할에서 처리 가능
    - 유연성
        - 각 단계마다 필요한 데이터를 가공하거나 다른 비동기 작업을 수행할 수 있어서 더 복잡한 비동기 흐름을 구성할 수 있음
    - 코드 관리
        - 비동기 작업을 분리하여 구성하면 코드를 관리하기 용이
- 예시
    
    ```jsx
    const URL = 'https://api.thecatapi.com/v1/images/search/'
    const btn = document.querySelector('button')
    
    function getCatImg() {
      axios({
        method: 'get',
        url: URL,
      })
        // .then(response => {
        //   const imgTag = document.createElement('img')
        //   imgTag.src = response.data[0].url
        //   const bodyTag = document.querySelector('body')
        //   bodyTag.appendChild(imgTag)
        // })
        .then(response => {
          imgUrl = response.data[0].url
          return imgUrl
        })
        .then(imgData => {
          imgTag = document.createElement('img')
          imgTag.setAttribute('src', imgData)
          document.body.appendChild(imgTag)
        })
        .catch(error => {
          console.log(error)
          console.log('실패')
        })
    }
    
    btn.addEventListener('click', getCatImg)
    ```
    

### 비동기를 사용하는 이유 - “사용자 경험”

- 예를 들어 아주 큰 데이터를 불러온 뒤 실행되는 앱이 있을 때, 동기식으로 처리된다면 데이터를 모두 불러온 뒤에서야 앱의 실행 로직이 수행되므로 사용자들은 마치 앱이 멈춘 것과 같은 경험을 겪게 됨
- 즉, 동기식 처리는 특정 로직이 실행되는 동안 다른 로직 실행을 차단하기 때문에 마치 프로그램이 응답하지 않는 듯한 사용자 경험을 만듦
- 비동기로 처리한다면 먼저 처리되는 부분부터 보여줄 수 있으므로, 사용자 경험에 긍정적인 효과를 볼 수 있음
- 이와 같은 이유로 많은 웹 기능은 비동기 로직을 사용해서 구현됨

### Ajax의 필요성

- human-centered design with UX(인간 중심으로 설계된 사용자 경험)