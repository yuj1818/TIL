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

## Semantic Web

웹 데이터를 의미론적으로 구조화된 형태로 표현하는 방식

![Untitled 5](https://github.com/yuj1818/TIL/assets/95585314/83855b92-19ed-4814-b2dd-225bcaaba84a)

### HTML Semantic Element

- 기본적인 모양과 기능 이외에 의미를 가지는 HTML 요소
    - 검색엔진 및 개발자가 웹 페이지 콘텐츠를 이해하기 쉽도록
- header, nav, main, article, section, aside, footer

![Untitled 6](https://github.com/yuj1818/TIL/assets/95585314/c14998f1-acf6-4280-bfcb-a96b4fe36ced)

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>

<body>
  <header>
    <h1>Header</h1>
  </header>

  <nav>
    <ul>
      <li><a href="#">Home</a></li>
      <li><a href="#">About Us</a></li>
      <li><a href="#">Contact</a></li>
    </ul>
  </nav>

  <main>
    <article>
      <h2>Article Title</h2>
      <p>Article content goes here...</p>
    </article>
    <aside>
      <h3>Aside</h3>
      <ol>
        <li><a href="#">Lorem, ipsum.</a></li>
        <li><a href="#">Lorem, ipsum.</a></li>
        <li><a href="#">Lorem, ipsum.</a></li>
      </ol>
    </aside>
  </main>

  <footer>
    <p>&copy; All rights reserved.</p>
  </footer>

</body>

</html>
```

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

## CSS Box Model

모든 HTML 요소를 사각형 박스로 표현하는 개념

### 구성 요소

- 내용(content), 안쪽 여백(padding), 테두리(border), 외부 간격(margin)으로 구성

![Untitled 5](https://github.com/yuj1818/TIL/assets/95585314/7c81a3af-a661-4e53-9a25-6c56f7daf351)

- 내용 : 콘텐츠가 표시되는 영역
- 안쪽 여백 : 콘텐츠 주위에 위치하는 공백 영역
- 테두리 : 콘텐츠와 패딩을 감싸는 테두리 영역
- 외부 간격 : 이 박스와 다른 요소 사이의 공백. 가장 바깥쪽 영역

### width & height 속성

- 요소의 너비와 높이를 지정
- 이때 지정되는 요소의 너비와 높이는 콘텐츠 영역을 대상으로 함
- CSS는 border가 아닌 content 크기를 width 값으로 지정
    - box-sizing 속성을 border-box로 하면 border 크기, content-box로 하면 content 크기

### ⭐박스 타입(Block & Inline)⭐

- ⭐Normal flow⭐
    - CSS 를 적용하지 않았을 경우, 웹페이지 요소가 기본적으로 배치되는 방향
- Block 타입 특징
    - 항상 새로운 행으로 나뉨
    - width와 height 속성을 사용하여 너비와 높이를 지정할 수 있음
    - 기본적으로 width 속성을 지정하지 않으면 박스는 inline 방향으로 사용 가능한 공간을 모두 차지함(너비를 사용가능한 공간의 100%로 채우는 것)
    - 대표적인 block 타입 태그
        - h1~6, p, div
    - block 요소의 가운데 정렬
        - margin: 0px auto;
- Inline 타입 특징
    - 새로운 행으로 나뉘지 않음
    - width와 height 속성을 사용할 수 없음
    - 수직 방향
        - padding, margins, borders가 적용되지만 다른 요소를 밀어낼 수는 없음
    - 수평 방향
        - padding, margins, borders가 적용되어 다른요소를 밀어낼 수 있음
    - 대표적인 inline 타입 태그
        - a, img, span
    - inline 요소를 가운데 정렬
        - 요소의 부모에 text-align: center;
- 속성에 따른 수평 정렬
    
    ![Untitled 6](https://github.com/yuj1818/TIL/assets/95585314/1300e2ba-a8c2-4aa6-8716-4d3b52c07cf4)
    
    - margin은 해당 요소에 직접 설정
    - text-align은 해당 요소의 부모에 설정

### 기타 display 속성

- inline-block
    - inline과 block 요소 사이의 중간 지점을 제공하는 display 값
    - block 요소의 특징을 가짐
        - width 및 height 속성 사용 가능
        - padding, margin 및 border로 인해 다른 요소가 밀려남
    - 요소가 줄 바꿈 되는 것을 원하지 않으면서 너비와 높이를 적용하고 싶은 경우에 사용
- ⭐none⭐
    - 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음

## CSS Layout Position

### CSS Layout

- 각 요소의 위치와 크기를 조정하여 웹 페이지의 디자인을 결정하는 것
- Display, Position, Float, Flexbox 등

### CSS Position

- 요소를 Normal Flow에서 제거하여 다른 위치로 배치하는 것
- 다른 요소 위에 올리기, 화면의 특정 위치에 고정시키기 등
- Position 이동 방향
    
    ![Untitled 7](https://github.com/yuj1818/TIL/assets/95585314/d1b1711c-431a-461c-8fa3-afb6364f3dba)
    
- Position 유형
    - static
        - 기본값
        - 요소를 Normal Flow에 따라 배치
    - relative
        - 요소를 Normal Flow에 따라 배치
        - 자기 자신을 기준으로 이동
        - 요소가 차지하는 공간은 static일 때와 같음
    - ⭐absolute⭐
        - 요소를 Normal Flow에서 제거
        - 가장 가까운 relative 부모 요소(**static이 아닌 부모)**를 기준으로 이동
        - 문서에서 요소가 차지하는 공간이 없어짐
        - 예시
        
        ![Untitled 8](https://github.com/yuj1818/TIL/assets/95585314/1915ca4f-aa3f-4b85-bb11-dcdaa571429a)
        
    - fixed
        - 요소를 Normal Flow에서 제거
        - 현재 화면 영역을 기준으로 이동
        - 문서에서 요소가 차지하는 공간이 없어짐
        - 예시
        
        ![Untitled 9](https://github.com/yuj1818/TIL/assets/95585314/e235337b-dad5-4f1f-bbb3-c83ea9380405)
        
    - sticky
        - 요소를 Normal Flow에 따라 배치
        - 요소가 일반적인 문서 흐름에 따라 배치되다가 스크롤이 특정 임계점에 도달하면 그 위치에서 고정됨
        - 만약 다음 sticky 요소가 나오면 다음 sticky 요소가 이전 sticky 요소의 자리를 대체
            - 이전 sticky 요소가 고정되어 있던 위치와 다음 sticky 요소가 고정되어야 할 위치가 겹치게 되기 때문
        
        ![Untitled 10](https://github.com/yuj1818/TIL/assets/95585314/a89d19ab-bbd1-4f8f-b214-54d5783e31f8)
        
    
    ```html
    <!DOCTYPE html>
    <html>
    
    <head>
      <title>CSS Position</title>
      <style>
        * {
          box-sizing: border-box;
        }
    
        body {
          height: 1500px;
        }
    
        .container {
          position: relative;
          height: 300px;
          width: 300px;
          border: 1px solid black;
        }
    
        .box {
          height: 100px;
          width: 100px;
          border: 1px solid black;
        }
    
        .static {
          position: static;
          background-color: lightcoral;
        }
    
        .absolute {
          position: absolute;
          background-color: lightgreen;
          top: 100px;
          left: 100px;
        }
    
        .relative {
          position: relative;
          background-color: lightblue;
          top: 100px;
          left: 100px;
        }
    
        .fixed {
          position: fixed;
          background-color: gray;
          top: 0;
          right: 0;
        }
      </style>
    </head>
    
    <body>
      <div class="container">
        <div class="box static">Static</div>
        <div class="box absolute">Absolute</div>
        <div class="box relative">Relative</div>
        <div class="box fixed">Fixed</div>
      </div>
    </body>
    
    </html>
    ```
    
    ![Untitled 11](https://github.com/yuj1818/TIL/assets/95585314/ea3ec767-d722-42d2-8322-16cdf1ea4774)
    

### z-index

- 요소가 겹쳤을 때 어떤 요소 순으로 위에 나타낼 지 결정
- 정수 값을 사용해 Z축 순서를 지정
- 더 큰 값을 가진 요소가 작은 값의 요소를 덮음

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .container {
      position: relative;
    }

    .box {
      position: absolute;
      width: 100px;
      height: 100px;
    }

    .red {
      background-color: red;
      top: 50px;
      left: 50px;
      z-index: 3;
    }

    .green {
      background-color: green;
      top: 100px;
      left: 100px;
      z-index: 2;
    }

    .blue {
      background-color: blue;
      top: 150px;
      left: 150px;
      z-index: 1;
    }
  </style>
</head>

<body>
  <div class="container">
    <div class="box red"></div>
    <div class="box green"></div>
    <div class="box blue"></div>
  </div>
</body>

</html>
```

![Untitled 12](https://github.com/yuj1818/TIL/assets/95585314/b3bc1f32-3f19-4c71-b84b-8eb7b9c94270)

## CSS Layout Flexbox

### CSS Flexbox

- 요소를 행과 열 형태로 배치하는 1차원 레이아웃 방식
- 공간 배열, 정렬

### 구성 요소

![Untitled 13](https://github.com/yuj1818/TIL/assets/95585314/94a318a2-8b42-48b0-a105-ee841d2a308e)

- main axis(주 축)
    - flex item들이 배치되는 기본 축
    - main start에서 시작하여 main end 방향으로 배치
- cross axis(교차 축)
    - main axis에 수직인 축
    - cross start에서 시작하여 cross end 방향으로 배치
- Flex Container
    - display: flex; 혹은 display: inline-flex; 가 설정된 부모 요소
    - 이 컨테이너의 1차 자식 요소들이 Flex Item이 됨
    - flexbox 속성 값들을 사용하여 자식 요소 Flex Item들을 배치
- Flex Item
    - Flex Container 내부에 레이아웃 되는 항목

### 레이아웃 구성

- Flex Continer 지정
    - flex item은 기본적으로 행으로 나열
    - flex item은 주축의 시작 선에서 시작
    - flex item은 교차축의 크기를 채우기 위해 늘어남
- flex-direction 지정
    - flex item이 나열되는 방향을 지정
    - column으로 지정할 경우 주 축이 변경됨
    - -reverse로 지정하면 시작 선과 끝 선이 서로 바뀜
    
    ![Untitled 14](https://github.com/yuj1818/TIL/assets/95585314/3154bd2a-8492-4f5b-8bec-d07d48f58bee)
    
- flex-wrap
    - flex item 목록이 flex container의 하나의 행에 들어가지 않을 경우, 다른 행에 배치할지 여부 설정
    
    ![Untitled 15](https://github.com/yuj1818/TIL/assets/95585314/bdf503e5-41a6-4879-a2b5-72014d3cdd35)
    
- justify-content
    - 주 축을 따라 flex item과 주위에 공간을 분배
    
    ![Untitled 16](https://github.com/yuj1818/TIL/assets/95585314/3050c43f-d28f-467b-b1b9-6a48e6a6a7eb)
    
- align-content
    - 교차 축을 따라 flex item과 주위에 공간을 분배
        - flex-wrap이 wrap 또는 wrap-reverse로 설정된 여러 행에만 적용됨
        - 한 줄 짜리 행에는 (flex-wrap이 nowrap으로 설정된 경우) 효과 없음
        
        ![Untitled 17](https://github.com/yuj1818/TIL/assets/95585314/bb428798-52af-4e59-ac29-6b81791237a0)
        
- align-items
    - 교차 축을 따라 flex item 행을 정렬
    
    ![Untitled 18](https://github.com/yuj1818/TIL/assets/95585314/bb1ccd25-6cb4-4888-9a81-53e6594d34c5)
    
- align-self
    - 교차 축을 따라 개별 flex item을 정렬
    
    ![Untitled 19](https://github.com/yuj1818/TIL/assets/95585314/b0908dac-0c4f-4698-b5df-5b67cfbc0a3c)
    
- ⭐flex-grow⭐
    - 남는 행 여백을 비율에 따라 각 flex item에 분배
        - 아이템 컨테이너 내에서 확장하는 비율을 지정
    - flex-grow의 반대는 flex-shrink
    
    ![Untitled 20](https://github.com/yuj1818/TIL/assets/95585314/3d40c2b2-87d1-4944-8f6b-21aa33fdca01)
    
- flex-basis
    - flex item의 초기 크기 값을 지정
    - flex-basis와 width 값을 동시에 적용한 경우 flex-basis가 우선

### Flexbox 속성

- Flex Container 관련 속성
    - display, flex-direction, flex-wrap, justify-content, align-items, align-content
- Flex Item 관련 속성
    - align-self, flex-grow, flex-basis, order
- 목적에 따른 분류
    - 배치
        - flex-direction, flex-wrap
    - 공간 분배
        - justify-content
        - align-content
    - 정렬
        - align-items
        - align-self

### flex-wrap 응용

- 반응형 레이아웃
    - 다양한 디바이스와 화면 크기에 자동으로 적응하여 콘텐츠를 최적으로 표시하는 웹 레이아웃 방식
    - flex-wrap 사용하여 반응형 레이아웃 작성
    
    ```html
    <!DOCTYPE html>
    <html lang="en">
    
    <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
      <style>
        .card {
          width: 80%;
          border: 1px solid black;
          display: flex;
          flex-wrap: wrap;
        }
    
        img {
          width: 100%;
        }
    
        .thumbnail {
          flex-basis: 700px;
          flex-grow: 1;
        }
    
        .content {
          flex-basis: 350px;
          flex-grow: 1;
        }
      </style>
    </head>
    
    <body>
      <div class="card">
        <img class="thumbnail" src="images/sample.jpg" alt="sample">
        <div class="content">
          <h2>Heading</h2>
          <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Perspiciatis minus sed expedita ut nihil tempora
            neque autem odio eos, repudiandae blanditiis, molestiae consequatur. Adipisci illo dolor repellat alias
            maiores.
            Aut?</p>
        </div>
      </div>
    </body>
    
    </html>
    ```
    
## Semantic in CSS

### OOCSS(Object Oriented CSS)

- 객체 지향적 접근법을 적용하여 CSS를 구성하는 `방법론`
- 기본 원칙
    - 구조와 스킨을 분리
        - 구조와 스킨을 분리함으로써 재사용 가능성을 높임
        - 예) 버튼
            - 모든 버튼의 공통 구조를 정의 + 각각의 스킨(배경색과 폰트 색상)을 정의
            
            ```css
            .button {
            		border: none;
            		font-size: 1em;
            		padding: 10px 20px;
            }
            
            .button-blue {
            		background-color: blue;
            		color: white;
            }
            
            .button-red {
            		background-color: red;
            		color: white;
            }
            ```
            
    - 컨테이너와 콘텐츠를 분리
        - 객체에 직접 적용하는 대신 객체를 둘러싸는 컨테이너에 스타일을 적용
        - 스타일을 정의할 때 위치에 의존적이 스타일을 사용하지 않도록 함
        - 콘텐츠를 다른 컨테이너로 이동시키거나 재배치할 때 스타일이 깨지는 것을 방지
        - 예) .header와 .footer 클래스가 폰트 크기와 색 둘 다 영향을 줌
            - ⇒ .container .title이 폰트 크기 담당(콘텐츠 스타일)
            - ⇒ .header와 .footer가 폰트 색 담당(컨테이너 스타일)
            
            ```css
            /* bad */
            .header h2 {
            		font-size: 24px;
            		color: white;
            }
            
            .footer h2 {
            		font-size: 24px;
            		color: black;
            }
            
            /* good */
            .container .title {
            	font-size: 24px;
            }
            
            .header {
            		color: white;
            }
            
            .footer {
            		color: black;
            }
            ```
            

`CSS 방법론` : CSS를 효율적이고 유지 보수가 용이하게 작성하기 위한 일련의 가이드라인

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

### Tag

| 태그 | 설명 |
| --- | --- |
| \<strong>\</strong> | 태그 사이 text를 진하게 표시함 |
| \<u>\</u> | 태그 사이 text에 밑줄을 표시함. |
| \<h1>\</h1> ~ \<h6>\</h6> | HTML의 head(제목)를 만든다. 숫자가 작을수록 텍스트 크기는 작아진다. |
| \<br> | 엔터키 한번 누른 것, 줄바꿈 |
| \<p>\</p> | 단락 나눔 태크 |
| \<img src=”경로” width=”크기”> | 이미지를 삽입하는 태그 |
| \<li>\</li> | 목록 표시 |
| \<ul>\</ul> | \<li>태그의 부모 태그, 리스트의 단락을 표시함. 리스트를 그룹핑함 |
| \<ol>\</ol> | \<li>태그의 부모 태그, 리스트에 순서를 부여해서 보여줌 |
| \<title>\</title> | 웹페이지의 제목을 사용자에게 명시적으로 보여준다. |
| \<meta charset=”utf-8”> | HTML 페이지를 UTF-8로 열어라. UTF-8 형태로 저장한다. |
| \<body>\</body> | 본문을 감싸는 태그  |
| \<head>\</head> | 바디를 설명하는 태그 |
| \<html>\</html> | head와 body 전체를 감싸는 가장 상위 태그 |
| \<!doctype html> | ‘이 문서는 HTML파일입니다’ 를 알려줌 |
| \<a href=”주소”></a> | 텍스트에 하이퍼링크를 부여함. 
||● target = “_blank” → 새 창에서 열기 
||●  title   = “설명”     → 커서 올리면 설명 보이기 |
| \<font color=”색상”></font> | text의 색상을 변경해 줌 |
| \<!— —> | 주석 |

[Tag 종류 모음](https://www.notion.so/63c50dd4319e4d8b811d310c19d05191?pvs=21)

### CSS(inline, block, inline-block)

| block | inline |
| --- | --- |
| 줄바꿈 발생 | 줄바꿈 X |
| 너비, 높이 변경 가능 | 너비, 높이 변경 불가 |

### shorthand 속성

- border
    - border-width, border-style, border-color를 한 번에 설정하기 위한 속성
    
    ```css
    border: 2px solid black;
    ```
    
- margin, padding
    - 4방향의 속성을 각각 지정하지 않고 한 번에 지정할 수 있는 속성
    
    ```css
    /* 4개 - 상우하좌 */
    margin: 10px 20px 30px 40px;
    padding: 10px 20px 30px 40px;
    
    /* 3개 - 상/좌우/하 */
    margin: 10px 20px 30px;
    padding: 10px 20px 30px;
    
    /* 2개 - 상하/좌우 */
    margin: 10px 30px;
    padding: 10px 30px;
    
    /* 1개 - 공통 */
    margin: 10x;
    padding: 10px;
    ```
    
- flex-flow
    
    ```css
    .container {
    		flex-flow: flex-direction flex-wrap;
    }
    ```
    

### ⭐Margin collapsing⭐

- 두 block 타입 요소의 margin top과 bottom이 만나 더 큰 margin으로 결합되는 현상
- 웹 개발자가 레이아웃을 더욱 쉽게 관리할 수 있도록 함
    - 각 요소에 대한 상/하 margin을 각각 설정하지 않고 한 요소에 대해서만 설정하기 위함

### 의미론적인 마크업의 이점

- 검색엔진 최적화(SEO)
    - 검색 엔진이 해당 웹 사이트를 분석하기 쉽게 만들어 검색 순위에 영향을 줌
- 웹 접근성(Web Accessibility)
    - 시각 장애 사용자가 스크린 리더기로 웹 페이지를 사용할 때 추가적으로 도움