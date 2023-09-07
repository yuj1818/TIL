# Bootstrap

- CSS 프론트엔드 프레임워크(Toolkit)
    - 미리 만들어진 다양한 디자인 요소들을 제공하여 웹 사이트를 빠르고 쉽게 개발할 수 있도록 함

```html
<!-- Bootstrap 사용 기본 코드 -->
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
  </head>
  <body>
    <h1>Hello, world!</h1>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
  </body>
</html>
```

## Bootstrap 기본 사용법

### padding, margin

```html
<p class="mt-5">Hello, world!</p>
```

- mt-5 ⇒ {property}{sides}-{size

![Untitled](https://github.com/yuj1818/TIL/assets/95585314/818aa160-4790-425b-8c66-bead68db0acc)

- Bootstrap에는 특정한 규칙이 있는 클래스 이름으로 이미 스타일 및 레이아웃이 작성되어 있음

### Typography

- 제목, 본문 텍스트, 목록 등
- Display headings
    - 기존 Headings보다 더 눈에 띄는 제목이 필요한 경우(더 크고 약간 다른 스타일)
    
    ```html
    <h1 class="display-1">Display 1</h1>
    <h1 class="display-2">Display 2</h1>
    <h1 class="display-3">Display 3</h1>
    <h1 class="display-4">Display 4</h1>
    <h1 class="display-5">Display 5</h1>
    <h1 class="display-6">Display 6</h1>
    ```
    
- Inline text elements
    - HTML inline 요소에 대한 스타일
    
    ```html
    <p>You can use the mark tag to <mark>highlight</mark> text.</p>
    <p><del>This line of text is meant to be treated as deleted text.</del></p>
    <p><s>This line of text is meant to be treated as no longer accurate.</s></p>
    <p><ins>This line of text is meant to be treated as an addition to the document.</ins></p>
    <p><u>This line of text will render as underlined.</u></p>
    <p><small>This line of text is meant to be treated as fine print.</small></p>
    <p><strong>This line rendered as bold text.</strong></p>
    <p><em>This line rendered as italicized text.</em></p>
    ```
    
- Lists
    - HTML list 요소에 대한 스타일
    
    ```html
    <ul class="list-unstyled">
      <li>This is a list.</li>
      <li>It appears completely unstyled.</li>
      <li>Structurally, it's still a list.</li>
      <li>However, this style only applies to immediate child elements.</li>
      <li>Nested lists:
        <ul>
          <li>are unaffected by this style</li>
          <li>will still show a bullet</li>
          <li>and have appropriate left margin</li>
        </ul>
      </li>
      <li>This may still come in handy in some situations.</li>
    </ul>
    ```
    

### Colors

- Bootstrap이 지정하고 제공하는 색상 시스템
- Text, Border, Background 및 다양한 요소에 사용하는 Bootstrap의 색상 키워드
- Text colors

```html
<p class="text-primary">.text-primary</p>
<p class="text-primary-emphasis">.text-primary-emphasis</p>
<p class="text-secondary">.text-secondary</p>
<p class="text-secondary-emphasis">.text-secondary-emphasis</p>
<p class="text-success">.text-success</p>
<p class="text-success-emphasis">.text-success-emphasis</p>
<p class="text-danger">.text-danger</p>
```

- Background colors

```html
<div class="p-3 mb-2 bg-primary text-white">.bg-primary</div>
<div class="p-3 mb-2 bg-primary-subtle text-emphasis-primary">.bg-primary-subtle</div>
<div class="p-3 mb-2 bg-secondary text-white">.bg-secondary</div>
<div class="p-3 mb-2 bg-secondary-subtle text-emphasis-secondary">.bg-secondary-subtle</div>
<div class="p-3 mb-2 bg-success text-white">.bg-success</div>
<div class="p-3 mb-2 bg-success-subtle text-emphasis-success">.bg-success-subtle</div>
<div class="p-3 mb-2 bg-danger text-white">.bg-danger</div>
```

### Component

- Bootstrap에서 제공하는 UI관련 요소
- 버튼, 네비게이션 바, 카드, 폼, 드롭다운 등
- 일관된 디자인을 제공하여 웹 사이트의 구성 요소를 구축하는 데 유용하게 활용
- 대표 Component
    - Alerts
    - Badges
    - Buttons
    - Cards
    - Navbar

## ⭐Bootstrap Grid system⭐

- 웹 페이지의 레이아웃을 조정하는 데 사용되는 12개의 컬럼으로 구성된 시스템
- 12개의 칸을 각 요소에 나누어 주는 것

### Grid system 목적

- 반응형 디자인을 지원해 웹 페이지를 모바일, 태블릿, 데스크탑 등 다양한 기기에서 적절하게 표시할 수 있도록 도움

### ⭐Grid system 클래스와 기본 구조⭐

- Grid system 기본 요소
    - Container
        - Column들을 담고 있는 공간
    - Column
        - 실제 컨텐츠를 포함하는 부분
    - Gutter
        - 컬럼과 컬럼 사이의 여백 영역
    
    ![Untitled 1](https://github.com/yuj1818/TIL/assets/95585314/bddaf19c-5302-4884-ab68-1da98f6bb4d6)
    
    - 1개의 row안에 12칸의 column 영역이 구성
    - 각 요소는 12칸 중 몇 개를 차지할 것인지 지정됨
- Grid System 실습
    - 기본
    
    ```html
    <h2 class="text-center">Basic</h2>
      <div class="row">
        <div class="row">
          <div class="box col">col</div>
          <div class="box col">col</div>
          <div class="box col">col</div>
        </div>
        <div class="row">
          <div class="box col-4">col-4</div>
          <div class="box col-4">col-4</div>
          <div class="box col-4">col-4</div>
        </div>
        <div class="row">
          <div class="box col-2">col-2</div>
          <div class="box col-8">col-8</div>
          <div class="box col-2">col-2</div>
        </div>
      </div>
    ```
    
    - Nesting
    
    ```html
    <h2 class="text-center">Nesting</h2>
      <div class="container">
        <div class="row">
          <div class="box col-4">col-4</div>
          <div class="box col-8">
            <div class="row">
              <div class="box col-6">col-6</div>
              <div class="box col-6">col-6</div>
              <div class="box col-6">col-6</div>
              <div class="box col-6">col-6</div>
            </div>
          </div>
        </div>
      </div>
    ```
    
    - 상쇄(Offset)
    
    ```html
    <h2 class="text-center">Offset</h2>
      <div class="container">
        <div class="row">
          <div class="box col-4">col-4</div>
          <div class="box col-4 offset-4">col-4 offset-4</div>
        </div>
        <div class="row">
          <div class="box col-3 offset-3">col-3 offset-3</div>
          <div class="box col-3 offset-3">col-3 offset-3</div>
        </div>
        <div class="row">
          <div class="box col-6 offset-3">col-6 offset-3</div>
        </div>
      </div>
    ```
    
    - Gutters
        - Grid system에서 column 사이에 여백 영역
        - x축은 padding, y축은 margin으로 여백 생성
        
        ```html
        <h2 class="text-center">Gutters(gx-0)</h2>
          <div class="container">
            <div class="row gx-0">
              <div class="col">
                <div class="box">col</div>
              </div>
              <div class="col">
                <div class="box">col</div>
              </div>
            </div>
          </div>
        
          <br>
        
          <h2 class="text-center">Gutters(gy-5)</h2>
          <div class="container">
            <div class="row gy-5">
              <div class="col-6">
                <div class="box">col</div>
              </div>
              <div class="col-6">
                <div class="box">col</div>
              </div>
              <div class="col-6">
                <div class="box">col</div>
              </div>
              <div class="col-6">
                <div class="box">col</div>
              </div>
            </div>
          </div>
        
          <br>
        
          <h2 class="text-center">Gutters(g-5)</h2>
          <div class="container">
            <div class="row g-5">
              <div class="col-6">
                <div class="box">col</div>
              </div>
              <div class="col-6">
                <div class="box">col</div>
              </div>
              <div class="col-6">
                <div class="box">col</div>
              </div>
              <div class="col-6">
                <div class="box">col</div>
              </div>
            </div>
          </div>
        ```
        

## Grid system for responsive web

### Responsive Web Design

- 디바이스 종류나 화면 크기에 상관없이, 어디서든 일관된 레이아웃 및 사용자 경험을 제공하는 디자인 기술
- Bootstrap grid system에서는 12개의 column과 6개 breakpoints를 사용하여 반응형 웹 디자인을 구현

### Grid system Breakpoints

- 웹 페이지를 다양한 화면 크기에서 적절하게 배치하기 위한 분기점
    - 화면 너비에 따라 6개의 분기점 제공(xs, sm, md, lg, xl, xxl)
    - 각 breakpoints 마다 설정된 최대 너비 값 “이상으로” 화면이 커지면 grid system 동작이 변경됨
    - medai query로도 작성 가능
    
    ![Untitled 2](https://github.com/yuj1818/TIL/assets/95585314/8251abb8-0f11-49ec-9b44-abf3a7d514bf)
    
    ```html
    <h2 class="text-center">Breakpoints</h2>
    <div class="container">
      <div class="row">
        <div class="col-12 col-sm-6 col-md-2 col-lg-3 col-xl-4 box">
          col
        </div>
        <div class="col-12 col-sm-6 col-md-8 col-lg-3 col-xl-4 box">
          col
        </div>
        <div class="col-12 col-sm-6 col-md-2 col-lg-3 col-xl-4 box">
          col
        </div>
        <div class="col-12 col-sm-6 col-md-12 col-lg-3 col-xl-12 box">
          col
        </div>
      </div>
    
      <hr>
    
      <h2 class="text-center">Breakpoints + offset</h2>
      <div class="row g-4">
        <div class="box col-12 col-sm-4 col-md-6">
          col
        </div>
        <div class="box col-12 col-sm-4 col-md-6">
          col
        </div>
        <div class="box col-12 col-sm-4 col-md-6">
          col
        </div>
        <div class="box col-12 col-sm-4 col-md-6 offset-sm-4 offset-md-0">
          col
        </div>
      </div>
    </div>
    ```

## 참고

### ⭐CDN(Content Delivery Network)⭐

- 지리적 제약 없이 빠르고 안전하게 콘텐츠를 전송할 수 있는 전송 기술
- 서버와 사용자 사이의 물리적인 거리를 줄여 콘텐츠 로딩에 소요되는 시간을 최소화(웹 페이지 로드 속도를 높임)
- 지리적으로 사용자와 가까운 CDN 서버에 콘텐츠를 저장해서 사용자에게 전달
- Bootstrap CDN
    - Bootstrap 홈페이지 - Download - “Compiled CSS and JS” Download
    - CDN을 통해 가져오는 bootstrap css 와 js 파일을 확인
    - bootstrap.css 파일을 참고하여, 현재까지 작성한 클래스에 적용된 스타일을 직접 확인

### ⭐Bootstrap을 사용하는 이유⭐

- 가장 인기 있고 잘 정립된 CSS 프레임워크
- 사전에 디자인된 다양한 컴포넌트 및 기능
    - 빠른 개발과 유지 보수
- 손쉬운 반응형 웹 디자인 구현
- 커스터마이징이 용이
- 크로스 브라우징 지원
    - 모든 주요 브라우저에서 작동하도록 설계되어 있음

### The Grid System

- CSS가 아닌 편집 디자인에서 나온 개념으로 구성 요소를 잘 배치해서 시각적으로 좋은 결과물을 만들기 위함
- 기본적으로 안쪽에 있는 요소들의 오와 열을 맞추는 것에서 기인
- 정보 구조와 배열을 체계적으로 작성하여 정보의 질서를 부여하는 시스템

### Grid cards

- row-cols 클래스를 사용하여 행당 표시할 열 수를 손쉽게 제어할 수 있음

```html
<h2 class="text-center">Grid Cards</h2>
  <div class="container">
    <div class="row">
      <div class="col-12 col-sm-4 col-md-6">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional
              content. This content is a little bit longer.</p>
          </div>
        </div>
      </div>
      <div class="col-12 col-sm-4 col-md-6">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional
              content. This content is a little bit longer.</p>
          </div>
        </div>
      </div>
      <div class="col-12 col-sm-4 col-md-6">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional
              content.</p>
          </div>
        </div>
      </div>
      <div class="col-12 col-sm-4 col-md-6 offset-sm-4 offset-md-0">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional
              content. This content is a little bit longer.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
```