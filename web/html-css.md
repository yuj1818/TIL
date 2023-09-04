# World Wide Web

인터넷으로 연결된 컴퓨터들이 정보를 공유하는 거대한 정보 공간

## Web

Web site, Web application 등을 통해 사용자들이 정보를 검색하고 상호 작용하는 기술

## Web site

인터넷에서 여러 개의 Web page가 모인 것으로, 사용자들에게 정보나 서비스를 제공하는 공간

## Web page

HTML, CSS 등의 웹 기술을 이용하여 만들어진, Web site를 구성하는 하나의 요소

<img src="https://github.com/yuj1818/TIL/assets/95585314/7516c4a4-b5cb-489e-9e3b-ab3afb4b5f2f" width="80%"/>

# 웹 구조화

## HTML(HyperText Markup Language)

웹 페이지의 의미와 구조를 정의하는 언어

`Hypertext`

- 웹 페이지를 다른 페이지로 연결하는 링크
- 참조를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트

`Markup Language`

- 태그 등을 이용하여 데이터의 구조를 명시하는 언어
- HTML, Markdown 등

## HTML 구조

- <!DOCTYPE html>
    - 해당 문서가 html 문서라는 것을 나타냄
- <html></html>
    - 전체 페이지의 콘텐츠를 포함
- <title></title>
    - 브라우저 탭 및 즐겨찾기 시 표시되는 제목으로 사용
- <head></head>
    - HTML 문서에 관련된 설명, 설정 등
    - 사용자에게 보이지 않음
- <body></body>
    - 페이지에 표시되는 모든 콘텐츠

```html
<!DOCTYPE html>
<html lan="en">
    <head>
        <meta charset="UTF-8">
        <title>My Page</title>
    </head>
    <body>
        <p>This is my page</p>
    </body>
</html>
```

### HTML Element

- 하나의 요소는 여는 태그와 닫는 태그 그리고 그 안의 내용으로 구성됨
- 닫는 태그는 태그 이름 앞에 슬래시가 포함되며 닫는 태그가 없는 태그도 존재

<img src="https://github.com/yuj1818/TIL/assets/95585314/b41a79b1-babb-49d3-8ff1-2ec78c43f166" width="80%"/>

### HTML Attributes(속성)

<img src="https://github.com/yuj1818/TIL/assets/95585314/28ecccbc-d5a3-4009-9ca2-a096fc4cd59b" width="80%"/>

- 규칙
    - 속성은 요소 이름과 속성 사이에 공백이 있어야 함
    - 하나 이상의 속성들이 있는 경우엔 속성 사이에 공백으로 구분함
    - 속성 값은 열고 닫는 따옴표로 감싸야 함
- 목적
    - 나타내고 싶지 않지만 추가적인 기능, 내용을 담고 싶을 때 사용
    - CSS에서 해당 요소를 선택하기 위한 값으로 활용됨

### HTML 구조 예시

```html
<!DOCTYPE html>
<html lan="en">
    <head>
        <meta charset="UTF-8">
        <title>My Page</title>
    </head>
    <body>
        <p>This is my page</p>
        <a href="https://www.google.co.kr">Google</a>
        <img src="images/sample.png" alt="sample-img">
        <img src="https://random.imagecdn.app/500/150/" alt="sample-img">
    </body>
</html>
```

<img src="https://github.com/yuj1818/TIL/assets/95585314/f28c0516-e9c3-430a-ba8b-14b7d28b5c72" width="80%">

## Text 구조

### HTML Text structure

- HTML의 주요 목적 중 하나는 텍스트 구조와 의미를 제공하는 것
- 예를 들어, h1 요소는 단순히 텍스트를 크게만 만드는 것이 아닌 현재 문서의 최상위 제목이라는 의미를 부여하는 것

### 대표적인 HTML Text structure

- Heading & Paragraphs
    - h1~h6
    - p
- Lists
    - ol
    - ul
    - li
- Emphasis & Importance
    - em
    - strong

![Untitled 4](https://github.com/yuj1818/TIL/assets/95585314/567a5855-ca0f-459f-bc05-058cb8f991dc)

# 웹 스타일링

## CSS(Cascading Style Sheet)

웹 페이지의 디자인과 레이아웃을 구성하는 언어

### CSS 구문

```css
h1 {    /* 선택자 */
		color: blue;    /* 선언 */
		font-size: 30px;
}  /* 속성 */ /* 값 */
```

### CSS 적용 방법

- 인라인(Inline) 스타일
    - HTML 요소 안에 style 속성 값으로 작성
    
    ```html
    <h1 sylte="color: blue; background-color: yellow;">Hello World!</h1>
    ```
    
- 내부(Internal) 스타일 시트
    - head 태그 안에 style 태그에 작성
    
    ```html
    <style>
    		h1 {
    				color: blue;
    				background-color: yellow;
    		}
    </style>
    ```
    
- 외부(External) 스타일 시트
    - 별도의 CSS 파일 생성 후 HTML link 태그를 사용해 불러오기
    
    ```html
    <head>
    		<link rel="stylesheet" href="style.css">
    </head>
    ```
    

### CSS 선택자

- HTML 요소를 선택하여 스타일을 적용할 수 있도록 하는 선택자

#### 종류

- 기본 선택자
    - 전체(*) 선택자
        - HTML 모든 요소를 선택
    - 요소(tag) 선택자
        - 지정한 모든 태그를 선택
    - 클래스(class) 선택자
        - 주어진 클래스 속성을 가진 모든 요소를 선택
    - 아이디(id) 선택자
        - 주어진 아이디 속성을 가진 요소 선택
        - 문서에는 주어진 아이디를 가진 요소가 하나만 있어야 함
    - 속성(attr) 선택자 등

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    /* 전체 선택자 */
    * {
      color: red;
    }
    /* 타입 선택자 */
    h2 {
      color: orange;
    }

    h3, h4 {
      color: blue;
    }
    /* 클래스 선택자 */
    .green{
      color: green;
    }
    /* id 선택자 */
    #purple {
      color: purple;
    }
  </style>
</head>

<body>
  <h1 class="green">Heading</h1>
  <h2>선택자</h2>
  <h3>연습</h3>
  <h4>반가워요</h4>
  <p id="purple">과목 목록</p>
  <ul>
    <li>파이썬</li>
    <li>알고리즘</li>
    <li>웹
      <ol>
        <li>HTML</li>
        <li>CSS</li>
        <li>PYTHON</li>
      </ol>
    </li>
  </ul>
  <p class="green">Lorem, <span>ipsum</span> dolor.</p>
</body>

</html>
```

- 결합자
    - 자손 결합자(” “ (space))
        - 첫 번째 요소의 자손 요소들 선택
        - 예) p span은 <p> 안에 있는 모든 <span>를 선택(하위 레벨 상관 없이)
    - 자식 결합자(>)
        - 첫 번째 요소의 직계 자식만 선택
        - 예) ul > li은 <ul>안에 있는 모든 <li>를 선택(한 단계 아래 자식들만)

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    /* 전체 선택자 */
    * {
      color: red;
    }
    /* 타입 선택자 */
    h2 {
      color: orange;
    }

    h3, h4 {
      color: blue;
    }
    /* 클래스 선택자 */
    .green{
      color: green;
    }
    /* id 선택자 */
    #purple {
      color: purple;
    }
    /* 자손 결합자 */
    .green span {
      font-size: 50px;
    }
  /* 자식 결합자 */
    .green > li {
      color: brown;
    }
  </style>
</head>

<body>
  <h1 class="green">Heading</h1>
  <h2>선택자</h2>
  <h3>연습</h3>
  <h4>반가워요</h4>
  <p id="purple">과목 목록</p>
  <ul class="green">
    <li>파이썬</li>
    <li>알고리즘</li>
    <li>웹
      <ol>
        <li>HTML</li>
        <li>CSS</li>
        <li>PYTHON</li>
      </ol>
    </li>
  </ul>
  <p class="green">Lorem, <span>ipsum</span> dolor.</p>
</body>

</html>
```

### 우선 순위(Specificity)

- 동일한 요소에 적용 가능한 같은 스타일을 두 가지 이상 작성했을 때, 어떤 규칙이 적용 되는지 결정하는 것

#### Cascade

- 동일한 우선순위를 같은 규칙이 적용될 때, CSS에서 마지막에 나오는 규칙이 사용됨
- 예시
    
    ```css
    h1 {
    		color: red;
    }
    
    h1 {
    		color: purple;
    }
    ```
    
    - h1 태그 내용의 색은 purple이 적용됨

#### Specificity

- 예시
    
    ```css
    .make-red {
    		color: red;
    }
    
    h1 {
    		color: purple;
    }
    ```
    
- 동일한 h1 태그에 다음과 같이 스타일이 작성된다면 h1 태그 내용의 색은 red가 적용됨

#### 우선순위가 높은 순

1. Importance
    - !important
        - 다른 우선순위 규칙보다 우선하여 적용하는 키워드
        - Cascade 구조를 무시하고 강제로 스타일을 적용하는 방식이므로 사용을 권장하지 않음
2. Inline 스타일
3. 선택자
    - id 선택자 > class 선택자 > 요소 선택자
4. 소스 코드 순서
- 예시
    
    ```html
    <!DOCTYPE html>
    <html lang="en">
    
    <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
      <style>
        h2 {
          color: darkviolet !important;
        }
    
        p {
          color: blue;
        }
    
        .orange {
          color: orange;
        }
    
        .green {
          color: green;
        }
    
        #red {
          color: red;
        }
      </style>
    </head>
    
    <body>
      <p>1</p>
      <p class="orange">2</p>
      <p class="green orange">3</p>
      <p class="orange green">4</p>
      <p id="red" class="orange">5</p>
      <h2 id="red" class="orange">6</h2>
      <p id="red" class="orange" style="color: brown;">7</p>
      <h2 id="red" class="orange" style="color: brown;">8</h2>
    </body>
    
    </html>
    ```
    

### 상속

- 기본적으로 CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속해 재사용성을 높임

#### 상속 여부

- CSS 상속 여부는 MDN 문서에서 확인
- 상속되는 속성
    - Text 관련 요소(font, color, text-align), opacity, visibility 등
- 상속되지 않는 속성
    - Box model 관련 요소(width, height, border, box-sizing)
    - position 관련 요소(position, top/right/bottom/left, z-index) 등

#### 상속 예시

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .parent {
      /* 상속 O */
      color: red;

      /* 상속 X */
      border: 1px solid black;
    }
  </style>
</head>

<body>
  <ul class="parent">
    <li class="child">Hello</li>
    <li class="child">Bye</li>
  </ul>
</body>

</html>
```

# 참고

### HTML 관련 사항

- 요소(태그) 이름은 대소문자를 구분하지 않지만 “소문자” 사용을 권장
- 속성의 따옴표는 작은 따옴표와 큰 따옴표를 구분하지 않지만 “큰 따옴표” 권장
- HTML은 프로그래밍 언어와 달리 에어를 반환하지 않기 때문에 작성 시 주의

### CSS 관련 사항

- CSS 인라인(inline) 스타일은 사용하지 말 것
    - CSS와 HTML 구조 정보가 혼합되어 작성되기 때문에 코드를 이해하기 어렵게 만듦
- CSS의 모든 속성을 외우는 것이 아님
    - 자주 사용되는 속성은 그리 많지 않으며 주로 활용하는 속성 위주로 사용하다 보면 자연스럽게 익히게 됨
    - 그 외 속성들은 개발하며 필요할 때마다 검색해서 학습 후 사용할 것
- 속성은 되도록 class만 사용할 것
    - id, 요소 선택자 등 여러 선택자들과 함께 사용할 경우, 우선순위 규칙에 따라 예기치 못한 스타일 규칙이 적용되어 전반적인 유지보수가 어려워지기 때문
    - 문서에서 단 한 번 유일하게 적용될 스타일의 경우에만 id 선택자 사용을 고려