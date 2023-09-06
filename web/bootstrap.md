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