# Front-end Development

- 웹 사이트와 웹 애플리케이션의 사용자 인터페이스(UI)와 사용자 경험(UX)을 만들고 디자인하는 것
- HTML, CSS, JavaScript 등을 활용하여 사용자가 직접 상호 작용하는 부분을 개발

## Client-side frameworks

- 클라이언트 측에서 UI와 상호작용을 개발하기 위해 사용되는 JavaScript 기반 프레임워크
- ex) Angular.js, Vue.js, React.js

### Client-side frameworks가 필요한 이유

- 웹에서 하는 일이 많아짐
- 단순히 무언가를 읽는 곳 ⇒ 무언가를 하는 곳
    - 웹 에서 문서 만을 읽는 것이 아닌 음악 스트리밍, 영화 시청, 원거리 채팅 및 영상 채팅을 통해 즉시 통신하고 있음
    - 이처럼 현대적이고 복잡한 대화형 웹 사이트를 웹 애플리케이션(Web applications)이라 부름
    - JavaScript 기반의 Client-side frameworks의 출현으로 매우 동적인 대화형 애플리케이션을 훨씬 더 쉽게 구축할 수 있게 됨
- 다루는 데이터가 많아짐
    - SNS를 예로 들면 친구가 이름을 변경하면 친구 목록, 타임라인, 스토리 등 친구 이름이 출력되는 모든 곳이 함께 변경되어야 함
    - 애플리케이션의 기본 데이터를 안정적으로 추적하고 업데이트(렌더링, 추가, 삭제 등)하는 도구가 필요
    - 애플리케이션의 상태를 변경할 때마다 일치하도록 UI를 업데이트해야 한다는 것
- Vanilla JS 만으로 모든 데이터를 조작한다면 불필요한 코드의 반복이 필요

## SPA(Single Page Application)

- 페이지 한 개로 구성된 웹 애플리케이션
- 웹 애플리케이션의 초기 로딩 후 새로운 페이지 요청 없이 동적으로 화면을 갱신하며 사용자와 상호작용하는 웹 애플리케이션
    - CSR(Client Side Rendering) 방식

### SPA 동작 원리

![Untitled](https://github.com/yuj1818/TIL/assets/95585314/4db4c226-d4e5-4e51-8633-073763caf93f)

- 서버로부터 필요한 모든 정적 HTML을 처음에 한 번 가져옴
- 브라우저가 페이지를 로드하면 Vue 프레임워크는 각 HTML 요소에 적절한 JavaScript 코드를 실행(이벤트에 응답, 데이터 요청 후 UI 업데이트 등)
    - ex) 페이지 간 이동 시, 페이지 갱신에 필요한 데이터 만을 JSON으로 전달 받아 페이지 일부 갱신
    - Google Maps, 인스타그램 등의 서비스에서 갱신 시 새로 고침이 없는 이유

### Client-side Rendering

- 클라이언트에서 화면을 렌더링 하는 방식
    - 브라우저는 페이지에 필요한 최소한의 HTML 페이지와 JavaScript를 다운로드
    - 그런 다음 JavaScript를 사용하여 DOM을 업데이트하고 페이지를 렌더링
- Client-side rendering의 장점
    - 빠른 속도
        - 페이지의 일부를 다시 렌더링 할 수 있으므로 동일한 웹 사이트의 다른 페이지로 이동하는 것이 일반적으로 더 빠름
        - 서버로 전송되는 데이터의 양을 최소화
    - 사용자 경험
        - 새로 고침이 발생하지 않아 네이티브 앱과 유사한 사용자 경험을 제공
    - Front-end와 Back-end의 명확한 분리
        - Front-end는 UI 렌더링 및 사용자 상호 작용 처리를 담당 & Back-end는 데이터 및 API 제공을 담당
        - 대규모 애플리케이션을 더 쉽게 개발하고 유지 관리 가능
- Client-side rendering의 단점
    - 초기 구동 속도가 느림
        - 전체 페이지를 보기 전에 약간의 지연을 느낄 수 있음
        - JavaScript가 다운로드, 구문 분석 및 실행될 때까지 페이지가 완전히 렌더링 되지 않기 때문
    - SEO(검색 엔진 최적화) 문제
        - 페이지를 나중에 그려 나가는 것이기 때문에 검색에 잘 노출되지 않을 수 있음

# Vue

- 사용자 인터페이스를 구축하기 위한 JavaScript 프레임워크
- 2014년 발표 - Evan You
- 2023년 기준 최신 버전은 Vue3
    - [https://vuejs.org](https://vuejs.org)

## Vue를 학습하는 이유

- 쉬운 학습 곡선 및 간편한 문법
    - 새로운 개발자들도 빠르게 학습할 수 있음
- 반응성 시스템
    - 데이터 변경에 따라 자동으로 화면이 업데이트 되는 기능을 제공
- 모듈화 및 유연한 구조
    - 애플리케이션을 컴포넌트 조각으로 나눌 수 있음
    - 코드의 재사용성을 높이고 유지 보수를 용이하게 함
- 거대하고 활발한 커뮤니티를 가지고 있어 풍부한 문서, 튜토리얼 예제 및 다양한 리소스를 공유 받을 수 있음
    - 최신 업데이트 및 트렌드를 공유함으로써 지속적인 학습을 촉진

## Vue의 핵심 기능

- 선언적 렌더링(Declarative Rendering)
    - HTML을 확장하는 템플릿 구문을 사용하여 HTML이 JavaScript 데이터를 기반으로 어떻게 보이는지 설명할 수 있음
    
    ```html
    <body>
    	<div id="app">
    		<h1>{{ message }}</h1>
    		<button @click="count++">
    			Count is: {{ count }}
    		</button>
    	</div>
    	<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
    	<script>
    		const { createApp, ref } = Vue
    	
    		const app = createApp({
    			setup() {
    				const message = ref('Hello vue!')
    				const count = ref(0)
    		
    				return {
    					message,
    					count
    				}
    			}
    		})
    		app.mount('#app')
    	</script>
    </body>
    ```
    
- 반응형(Reactivity)
    - JavaScript 상태 변경 사항을 자동으로 추적하고 변경 사항이 발생할 때 DOM을 효율적으로 업데이트

## Vue 사용 방법

- CDN 방식

```html
<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
```

- NPM 설치 방식

### Application instance 생성

- 모든 Vue 애플리케이션을 createApp 함수로 새 Application instance를 생성하는 것으로 시작

```html
<script>
	const { createApp } = Vue

	const app = createApp({})
</script>
```

### app.mount()

- 컨테이너 요소에 애플리케이션 인스턴스를 탑재(연결)
- 각 앱 인스턴스에 대해 mount()는 한 번만 호출할 수 있음

```html
<div id="app"></div>
<script>
	...
	app.mount('#app')
</script>
```

### ref()

- 반응형 상태(데이터)를 선언하는 함수
    - 반응형을 가지는 참조 변수를 만드는 것
    - ref === reactive reference
- Declaring Reactive State
- 인자를 받아 .value 속성이 있는 ref 객체로 래핑(wrapping)하여 반환
- const로 선언해도 값을 재할당 할 수 있는 이유는 ref는 객체이므로 속성의 값을 바꾸는 것과 같기 때문
- ref로 선언된 변수의 값이 변경되면, 해당 값을 사용하는 템플릿에서 자동으로 업데이트
- 인자는 어떠한 타입도 가능

```html
<script>
	const { createApp } = Vue

	const app = createApp({
		setup(){
			const message = ref('Hello vue!')
			console.log(message) // ref 객체
			console.log(message.value) // Hello vue!
		}
	})
</script>
```

- 템플릿의 참조에 접근하려면 setup 함수에서 선언 및 반환 필요
- 템플릿에서 ref를 사용할 때는 .value를 작성할 필요 없음(automatically unwrapped)

```html
<div id="app">
	<h1>{{ message }}</h1>
</div>
<script>
	const { createApp } = Vue

	const app = createApp({
		setup(){
			const message = ref('Hello vue!')
			return {
				message
			}
		}
	})
</script>
```

## Vue 기본 구조

- createApp()에 전달되는 객체는 Vue 컴포넌트(Component)
- 컴포넌트의 상태는 setup() 함수 내에서 선언되어야 하며 **객체를 반환해야 함**

### 템플릿 렌더링

- 반환된 객체의 속성은 템플릿에서 사용할 수 있음
- Mustache syntax(콧수염 구문)를 사용하여 메시지 값을 기반으로 동적 텍스트를 렌더링
- 콘텐츠는 식별자나 경로에만 국한되지 않으며 유효현 JavaScript 표현식을 사용할 수 ㅇ있음

```html
<h1>{{ message.split('').reverse().join('') }}</h1>
```

### Event Listeners in Vue

- ‘v-on’ directive를 사용하여 DOM 이벤트를 수신할 수 있음
- 함수 내에서 refs를 변경하여 구성 요소 상태를 업데이트

```html
<div id="app">
  <button v-on:click="increment">{{ count }}</button>
</div>
<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
<script>
  const { createApp, ref } = Vue

  const app = createApp({
    setup() {
      const count = ref(0)
      const increment = function() {
        count.value++
      }
      return {
        count,
        increment
      }
    }
  })
  
  app.mount('#app')
</script>
```

# Basic Syntax

## Template Syntax

- DOM을 기본 구성 요소 인스턴스의 데이터에 선언적으로 바인딩(Vue Instance와 DOM을 연결)할 수 있는 HTML 기반 템플릿 구문(확장된 문법 제공)을 사용

### Text Interpolation

```html
<p>Message: {{ msg }}</p>
```

- 데이터 바인딩의 가장 기본적인 형태
- 이중 중괄호 구문(콧수염 구문)을 사용
- 콧수염 구문은 해당 구성 요소 인스턴스의 msg 속성 값으로 대체
- msg 속성이 변경될 때마다 업데이트 됨

### Raw HTML

```html
<div v-html="rawHtml"></div>
<script>
	...
	const rawHtml = ref('<span style="color:red">This should be red.</span>')
	...
</script>
```

- 콧수염 구문은 데이터를 일반 텍스트로 해석하기 때문에 실제 HTML을 출력하려면 v-html을 사용해야 함

### Attribute Bindings

```html
<div v-bind:id="dynamicId"></div>
<script>
	...
	const dynamicId = ref('my-id')
	...
</script>
```

- 콧수염 구문은 HTML 속성 내에서 사용할 수 없기 때문에 v-bind를 사용
- HTML의 id 속성 값을 vue의 dynamicId 속성과 동기화 되도록 함
- 바인딩 값이 null이나 undefined인 경우 렌더링 요소에서 제거됨

### JavaScript Expressions

```html
{{ number + 1 }}

{{ ok ? 'YES' : 'NO' }}

{{ msg.split('').reverse().join('') }}

<div :id="`list-${id}`"></div>

<script>
	...
	const msg = ref('Hello')
  const number = ref(1)
  const ok = ref(false)
  const id = ref(100)
	...
</script>
```

- Vue는 모든 데이터 바인딩 내에서 JavaScript 표현식의 모든 기능을 지원
- Vue 템플릿에서 JavaScript 표현식을 사용할 수 있는 위치
    - 콧수염 구문 내부
    - 모든 directive의 속성 값(v-로 시작하는 특수 속성)
- Expressions 주의사항
    - 각 바인딩에는 하나의 단일 표현식만 포함될 수 있음
        - 표현식은 값으로 평가할 수 있는 코드 조각(return 뒤에 사용할 수 있는 코드여야 함)
    - 작동하지 않는 경우
    
    ```html
    <!-- 표현식이 아닌 선언식 -->
    {{ const number = 1 }}
    
    <!-- 흐름제어도 작동하지 않음. 삼항 표현식을 사용 -->
    {{ if (ok) { return message } }}
    ```
    

### Directive

- ‘v-' 접두사가 있는 특수 속성
- Directive의 속성 값은 단일 JavaScript 표현식이어야 함(v-for, v-on 제외)
- 표현식 값이 변경될 때 DOM에 반응적으로 업데이트를 적용
- 예시
    - v-if는 seen 표현식 값의 T/F를 기반으로 <p> 요소를 제거/삽입
    
    ```html
    <p v-if="seen">Hi There</p>
    ```
    

#### Directive 전체 구문

![Untitled 1](https://github.com/yuj1818/TIL/assets/95585314/7bca624d-952d-4071-94b2-08086ec93f3b)


- Arguments
    - 일부 directive는 directive 뒤에 콜론(:)으로 표시되는 인자를 사용할 수 있음
    - 아래 예시는 href는 HTML a 요소의 href 속성 값을 myUrl 값에 바인딩하도록 하는 v-bind의 인자
    
    ```html
    <a :href="myUrl">Link</a>
    ```
    
    - 아래 예시의 click은 이벤트 수신할 이벤트 이름을 작성하는 v-on의 인자
    
    ```html
    <button v-on:click="doSomething">Button</button>
    ```
    
- Modifiers
    - .(dot)로 표시되는 특수 접미사로, directive가 특별한 방식으로 바인딩되어야 함을 나타냄
    - 예를 들어 .prevent는 발생한 이벤트에서 event.preventDefault()를 호출하도록 v-on에 지시하는 modifier
    
    ```html
    <form @submit.prevent="onSubmit">...</form>
    ```
    

#### Built-in Directives

- v-text
- v-show
- v-if
- v-for
- …
- [https://vuejs.org/api/built-in-directives.html](https://vuejs.org/api/built-in-directives.html)

## Dynamically data binding

### v-bind

- 하나 이상의 속성 또는 컴포넌트 데이터를 표현식에 동적으로 바인딩

### Attribute Bindings

- HTML의 속성 값을 Vue의 상태 속성 값과 동기화 되도록 함

```html
<img v-bind:src="imageSrc">
<a v-bind:href="myUrl">Move to Url</a>
```

- v-bind shorthand(약어)
    - ‘:’ (colon)
    
    ```html
    <img :src="imageSrc">
    <a :href="myUrl">Move to Url</a>
    ```
    
- Dynamic attribute name(동적 인자 이름)
    - 대괄호로 감싸서 directive argument에 JavaScript 표현식을 사용할 수도 있음
    - JavaScript 표현식에 따라 동적으로 평가된 값이 최종 argument 값으로 사용됨
    
    ```html
    <button :[key]="myValue"></button>
    <!-- 대괄호 안에 작성하는 이름은 반드시 소문자로만 구성 가능 -->
    ```
    
    ```html
    <!-- 예시 -->
    <p :[dynamicattr]="dynamicValue">...</p>
    
    <script>
      ...
      const dynamicattr = ref('title')
      const dynamicValue = ref('Hello Vue.js')
      ...
    </script>
    ```
    

### Class and Style Bindings

- 클래스와 스타일은 모두 속성이므로 v-bind를 사용하여 다른 속성과 마찬가지로 동적으로 문자열 값을 할당할 수 잇음
- 그러나 단순히 문자열 연결을 사용하여 이러한 값을 생성하는 것을 번거롭고 오류가 발생하기가 쉬움
- Vue는 클래스 및 스타일과 함께 v-bind를 사용할 때 객체 또는 배열을 활용한 개선 사항을 제공

#### Binding HTML Classes - Binding to Objects

- 객체를 :class에 전달하여 클래스를 동적으로 전환할 수 있음

```html
<div :class="{active: isActive}">Text</div>
<script>
	...
	const isActive = ref(false)
	...
</script>
```

- 객체에 더 많은 필드를 포함하여 여러 클래스를 전환할 수 있음

```html
<div class="static" :class="{active: isActive, 'text-primary': hasInfo}">Text</div>
<script>
	...
	const isActive = ref(false)
	const hasInfo = ref(true)
	...
</script>
```

- 반드시 inline 방식으로 작성하지 않아도 됨

```html
<div class="static" :class="classObj">Text</div>
<script>
	...
	const isActive = ref(false)
	const hasInfo = ref(true)
	const classObj = ref({
    active: isActive,
    'text-primary': hasInfo
  })
	...
</script>
```

#### Binding HTML classes - Binding to Arrays

- :class를 배열에 바인딩하여 클래스 목록을 적용할 수 있음

```html
<div :class="[activeClass, infoClass]">Text</div>
<script>
	...
	const activeClass = ref('active')
  const infoClass = ref('text-primary')
	...
</script>
```

- 배열 구문 내에서 객체 구문 사용

```html
<div :class="[{active: isActive}, infoClass]">Text</div>
<script>
	...
	const isActive = ref(false)
	const infoClass = ref('text-primary')
	...
</script>
```

#### Binding Inline Styles - Binding to Objects

- :style은 JavaScript 객체 값에 대한 바인딩을 지원(HTML style 속성에 해당)

```html
<div :style="{color: activeColor, fontSize: fontSize + 'px'}">Text</div>
<script>
	...
	const activeColor = ref('crimson')
	const fontSize = ref(50)
	...
</script>
```

- 실제 CSS에서 사용하는 것처럼 :style은 kebab-cased 키 문자열도 지원
    - 단, camelCase 작성을 권장

```html
<div :style="{'font-size': fontSize + 'px'}">Text</div>
```

- 템플릿을 더 깔끔하게 작성하려면 스타일 객체에 직접 바인딩하는 것을 권장

```html
<div :style="styleObj">Text</div>
<script>
	...
	const activeColor = ref('crimson')
  const fontSize = ref(50)
  const styleObj = ref({
    color: activeColor,
    fontSize: fontSize.value + 'px'
  })
	...
</script>
```

#### Binding Inline Styles - Binding to Arrays

- 여러 스타일 객체의 배열에 :style을 바인딩할 수 있음
- 작성한 객체는 병합되어 동일한 요소에 적용

```html
<div :style="[styleObj, styleObj2]">Text</div>
<script>
	...
	const activeColor = ref('crimson')
  const fontSize = ref(50)
  const styleObj = ref({
    color: activeColor,
    fontSize: fontSize.value + 'px'
  })
  const styleObj2 = ref({
    color: 'blue',
    border: '1px solid black'
  })
	...
</script>
```

## Event Handling

### v-on

- DOM 요소에 이벤트 리스너를 연결 및 수신

```html
v-on:event="handler"
```

- handler 종류
    - Inline handlers
        - 이벤트가 트리거 될 때 실행 될 JavaScript 코드
    - Method handlers
        - 컴포넌트에 정의된 메서드 이름
- v-on shorthand(약어)
    - ‘@’
    
    ```html
    @event="handler"
    ```
    

### Inline Handlers

- Inline handlers는 주로 간단한 상황에 사용

```html
<button @click="count++">Add 1</button>
<p>Count: {{ count }}</p>
<script>
	...
	const count = ref(0)
	...
</script>
```

### Method Handlers

- Inline handlers로는 불가능한 대부분의 상황에서 사용
- Method Handlers는 이를 트리거하는 기본 DOM Event 객체를 자동으로 수신

```html
<button @click="myFunc">Hello</button>
<script>
	...
	const name = ref('Alice')
  const myFunc = function(event) {
    console.log(event) // PointerEvent {...}
    console.log(event.currentTarget) // <button>Hello</button>
    console.log(`Hello ${name.value}!`) // Hello Alice!
  }
	...
</script>
```

### Inline Handlers에서의 메서드 호출

- 메서드 이름에 직접 바인딩하는 대신 Inline Handlers에서 메서드를 호출할 수도 있음
- 이렇게 하면 기본 이벤트 대신 사용자 지정 인자를 전달할 수 있음

```html
<button @click="greeting('hello')">Say hello</button>
<button @click="greeting('bye')">Say bye</button>
<script>
	...
	const greeting = function (message) {
    console.log(message)
  }
	...
</script>
```

### Inline Handlers에서의 event 인자에 접근하기

- Inline Handlers에서 원래 DOM 이벤트에 접근하기
- $event 변수를 사용하여 메서드에 전달

```html
<button @click="warning('경고입니다.', $event)">Submit</button>
<script>
	...
	const warning = function(message, event) {
    console.log(message)
    console.log(event)
  }
	...
</script>
```

### Event Modifiers

- Vue는 v-on에 대한 Event Modifiers를 제공해 event.preventDefault()와 같은 구문을 메서드에서 작성하지 않도록 함
- stop, prevent, self 등 다양한 modifires를 제공
- 메서드는 DOM 이벤트에 대한 처리보다는 데이터에 관한 논리를 작성하는 것에 집중할 것

```html
<form @submit.prevent="onSubmit">
  <input type="submit">
</form>
<a @click.stop.prevent="onLink">Link</a>
<!-- Modifiers는 chained 되게끔 작성할 수 있으며 이때는 작성된 순서로 실행되기 때문에 작성 순서에 유의 -->
```

### Key Modifiers

- Vue는 키보드 이벤트를 수신할 때 특정 키에 관한 별도 modifiers를 사용할 수 있음

```html
<!-- key가 Enter일 때만 onSubmit 이벤트 호출하기 -->
<input @keyup.enter="onSumbit">
```

## Form Input Bindings

- form을 처리할 때 사용자가 input에 입력하는 값을 실시간으로 JavaScript 상태에 동기화해야 하는 경우(양방향 바인딩)
- 양방향 바인딩 방법
    - v-bind와 v-on을 함께 사용
    - v-model 사용

### v-bind와 v-on 함께 사용하여 양방향 바인딩

- v-bind를 사용하여 input 요소의 value 속성 값을 입력 값으로 사용
- v-on을 사용하여 input 이벤트가 발생할 때마다 input 요소의 value 값을 별도 반응형 변수에 저장하는 핸들러를 호출

```html
<p>{{ inputText1 }}</p>
<input :value="inputText1" @input="onInput">
<script>
	...
	const inputText1 = ref('')
  const onInput = function(event) {
    inputText1.value = event.currentTarget.value
  }
	...
</script>
```

### v-model 사용하여 양방향 바인딩

- `v-model` : form input 요소 또는 컴포넌트에서 양방향 바인딩을 만듦
- v-model을 사용하여 사용자 입력 데이터와 반응형 변수를 실시간 동기화

```html
<p>{{ inputText2 }}</p>
<input v-model="inputText2">
<script>
	...
	const inputText2 = ref('')
	...
</script>
```

- [IME](#imeinput-method-editor)가 필요한 언어(한국어, 중국어, 일본어 등)의 경우 v-model이 제대로 업데이트되지 않음
- 해당 언어에 대해 올바르게 응답하려면 v-bind와 v-on 방법을 사용해야 함

### v-model 활용

- v-model은 단순 text input 뿐만 아니라 Checkbox, Radio, Select 등 다양한 타입의 사용자 입력 방식과 함께 사용 가능

#### Checkbox 활용

- 단일 체크박스와 boolean 값 활용

```html
<input type="checkbox" id="checkbox" v-model="checked">
<label for="checkbox">{{ checked }}</label>
<script>
	...
	const checked = ref(false)
	...
</script>
```

- 여러 체크박스와 배열 활용

```html
<div>Checked names: {{ checkedNames }}</div>

<input type="checkbox" id="alice" value="Alice" v-model="checkedNames">
<label for="alice">Alice</label>

<input type="checkbox" id="bella" value="Bella" v-model="checkedNames">
<label for="bella">Bella</label>

<script>
	...
	const checkedNames = ref([])
	...
</script>
```

#### Select 활용

- select에서 v-model 표현식의 초기 값이 어떤 option과도 일치하지 않는 경우 select 요소는 “선택되지 않은(unselected)” 상태로 렌더링 됨

```html
<div>Selected: {{ selected }}</div>

<select v-model="selected">
  <option disabled value="">Please select one</option>
  <option>Alice</option>
  <option>Bella</option>
  <option>Cathy</option>
</select>

<script>
	...
	const selected = ref('')
	...
</script>
```

## Computed Property

### computed()

- 계산된 속성의 정의하는 함수
- 미리 계산된 속성을 사용하여 템플릿에서 표현식을 단순하게 하고 불필요한 반복 연산을 줄임

```html
<h2>남은 할 일</h2>
<p>{{ restOfTodos }}</p>
<script>
  const { createApp, ref, computed } = Vue

  const app = createApp({
	  setup() {
	    const todos = ref([
	      { text: 'Vue 실습' },
	      { text: '자격증 공부' },
	      { text: 'TIL 작성' }
	    ])

      const restOfTodos = computed(() => {
        return todos.value.length > 0 ? '아직 남았다' : '퇴근!'
      })

      return {
        todos,
        restOfTodos
      }
    }
  })

  app.mount('#app')
</script>
```

- computed 특징
    - 반환되는 값을 computed ref이며 일반 refs와 유사하게 계산된 결과를 .value로 참조할 수 있음
    - computed 속성은 의존된 반응형 데이터를 자동으로 추적
    - 의존하는 데이터가 변경될 때만 재평가
        - restOfTodos의 계산은 todos에 의존하고 있음
        - 따라서 todos가 변경될 때만 restOfTods가 업데이트 됨

### Method

- computed 속성 대신 method로도 동일한 기능을 정의할 수 있음
- 두 가지 접근 방식은 실제로 완전히 동일

```html
<p>{{ getRestOfTodos() }}</p>
<script>
	...
	const getRestOfTodos = function() {
    return todos.value.length > 0 ? '아직 남았다' : '퇴근!'
  }
	...
</script>
```

### computed와 method 차이

- computed 속성은 의존된 반응형 데이터를 기반으로 캐시(cached)됨
- 의존하는 데이터가 변경된 경우에만 재평가됨
- 즉, 의존된 반응형 데이터가 변경되지 않는 한 이미 계산된 결과에 대한 여러 참조는 다시 평가할 필요 없이 이전에 계산된 결과를 즉시 반환
- 반면, method 호출은 다시 렌더링이 발생할 때마다 항상 함수를 실행
    - 호출해야만 실행됨

`Cache(캐시)`

- 데이터나 결과를 일시적으로 저장해두는 임시 저장소
- 이후에 같은 데이터나 결과를 다시 계산하지 않고 빠르게 접근할 수 있도록 함

### computed와 method의 적절한 사용처

- computed
    - 의존하는 데이터에 따라 결과가 바뀌는 계산된 속성을 만들 때 유용
    - 동일한 의존성을 가진 여러 곳에서 사용할 때 계산 결과를 캐싱하여 중복 계산 방지
- method
    - 단순히 특정 동작을 수행하는 함수를 정의할 때 사용
    - 데이터에 의존하는지 여부와 관계없이 항상 동일한 결과를 반환하는 함수
    - 무조건 computed만 사용하는 것이 아니라 사용 목적과 상황에 맞게 computed와 method를 적절히 조합하여 사용

## Conditional Rendering

### v-if

- 표현식 값의 T/F를 기반으로 요소를 조건부로 렌더링
- ‘v-else’ directive를 사용하여 v-if에 대한 else 블록을 나타낼 수 있음

```html
<p v-if="isSeen">true일때 보여요</p>
<p v-else>false일때 보여요</p>
<button @click="isSeen = !isSeen">토글</button>
<script>
	...
	const isSeen = ref(true)
	...
</script>
```

- ‘v-else-if’ directive를 사용하여 v-if에 대한 else if 블록을 나타낼 수 있음

```html
<div v-if="name === 'Alice'">Alice입니다</div>
<div v-else-if="name === 'Bella'">Bella입니다</div>
<div v-else-if="name === 'Cathy'">Cathy입니다</div>
<div v-else>아무도 아닙니다.</div>
<script>
	...
	const name = ref('Cathy')
	...
</script>
```

- v-if는 directive이기 때문에 단일 요소에만 연결 가능
- 이 경우 template 요소에 v-if를 사용하여 하나 이상의 요소에 대해 적용할 수 있음
    - v-else, v-else-if 모두 적용 가능
    
    ```html
    <template v-if="name === 'Cathy'">
    	<div>Cathy 입니다.</div>
    	<div>나이는 30살입니다.</div>
    </template>
    ```
    

`HTML <template> element`

- 페이지가 로드 될 때 렌더링 되지 않지만 JavaScript를 사용하여 나중에 문서에서 사용할 수 있도록 하는 HTML을 보유하기 위한 메커니즘
- 보이지 않는 wrapper 역할

### v-show

- 표현식의 값의 T/F를 기반으로 요소의 가시성을 전환
- v-show 요소는 항상 렌더링 되어 DOM에 남아있음
- CSS display 속성만 전환하기 때문

```html
<div v-show="isShow">v-show</div>
<script>
	...
	const isShow = ref(false)
	...
</script>
```

### v-if vs v-show

| v-if(Cheap initial load, expensive toggle) | v-show(Expensive initial load, cheap toggle) |
| --- | --- |
| 초기 조건이 false인 경우 아무 작업도 수행하지 않음 | 초기 조건에 관계 없이 항상 렌더링 |
| 토글 비용이 높음 | 초기 렌더링 비용이 더 높음 |
- 무언가를 매우 자주 전환해야 하는 경우에는 v-show를, 실행 중에 조건이 변경되지 않는 경우에는 v-if를 권장

## List Rendering

### v-for

- 소스 데이터(Array, Object, number, string, Iterable)를 기반으로 요소 또는 템플릿 블록을 여러 번 렌더링
- v-for는 alias in expresssion 형식의 특수 구문을 사용하여 반복되는 현재 요소에 대한 별칭(alias)을 제공

```html
<div v-for="item in items">
    {{ item.text }}
</div>
```

- 인덱스(객체에서는 키)에 대한 별칭을 지정할 수 있음

```html
<div v-for="(item, index) in items"></div>

<div v-for="value in object"></div>
<div v-for="(value, key) in object"></div>
<div v-for="(value, key, index) in object"></div>
```

- 배열 반복

```html
<div v-for="(item, index) in myArr">
    {{ index }} / {{ item }}
</div>
<script>
	...
	const myArr = ref([
    { name: 'Alice', age: 20 },
    { name: 'Bella', age: 21 }
  ])
	...
</script>
```

- 객체 반복

```html
<div v-for="(value, key, index) in myObj">
  {{ index }} / {{ key }} / {{ value }}
</div>
<script>
	...
	const myObj = ref({
    name: 'Cathy',
    age: 30
  })
	...
</script>
```

- 여러 요소에 대한 v-for 적용
    - template 요소에 v-for를 사용하여 하나 이상의 요소에 대해 반복 렌더링 할 수 있음
    
    ```html
    <ul>
      <template v-for="item in myArr">
        <li>{{ item.name }}</li>
        <li>{{ item.age }}</li>
        <hr>
      </template>
    </ul>
    <script>
    	...
    	const myArr = ref([
        { name: 'Alice', age: 20 },
        { name: 'Bella', age: 21 }
      ])
    	...
    </script>
    ```
    
- 중첩된 v-for
    - 각 v-for 범위는 상위 범위에 접근할 수 있음
    
    ```html
    <ul v-for="item in myInfo">
      <li v-for="friend in item.friends">
        {{ item.name }} - {{ friend}}
      </li>
    </ul>
    <script>
    	...
    	const myInfo = ref([
        { name: 'Alice', age: 20, friends: ['Bella', 'Cathy', 'Dan'] },
        { name: 'Bella', age: 21, friends: ['Alice', 'Cathy'] }
      ])
    	...
    </script>
    ```
    

### v-for with key

- 반드시 v-for와 key를 함께 사용한다
- 내부 컴포넌트의 상태를 일관되게 유지
- 데이터의 예측 가능한 해동을 유지(Vue 내부 동작 관련)
- key는 반드시 각 요소에 대한 고유한 값을 나타낼 수 있는 식별자여야 함

```html
<div v-for="item in items" :key="item.id">
  <!-- content -->
</div>
<script>
	...
	let id = 0

  const items = ref([
    { id: id++, name: 'Alice' },
    { id: id++, name: 'Bella' },
  ])
	...
</script>
```

### v-for with v-if

- 동일 요소에 v-for와 v-if를 함께 사용하지 않는다
- 동일한 요소에서 v-if가 v-for보다 우선순위가 더 높기 때문
- v-if 조건은 v-for 범위의 변수에 접근할 수 없음
- 예시
    - todo 데이터 중 이미 처리 한(isComplete === true) todo만 출력하기
        - v-if가 더 높은 우선순위를 가지므로 v-for의 todo 요소를 v-if에서 사용할 수 없음
    
    ```html
    <ul>
      <li v-for="todo in todos" v-if="!todo.isComplete" :key="todo.id">
        {{ todo.name }}
      </li>
    </ul>
    <script>
    	...
    	let id = 0
    
      const todos = ref([
        { id: id++, name: '복습', isComplete: true },
        { id: id++, name: '예습', isComplete: false },
        { id: id++, name: '저녁식사', isComplete: true },
        { id: id++, name: '노래방', isComplete: false }
      ])
    	...
    </script>
    ```
    
    - 해결 1 - computed를 활용해 필터링 된 목록을 반환하여 반복하도록 설정
    
    ```html
    <ul>
      <li v-for="todo in complteTodos" :key="todo.id">
        {{ todo.name }}
      </li>
    </ul>
    <script>
    	...
    	const completeTodos = computed(() => {
        return todos.value.filter((todo) => todo.isComplete)
      })
    	...
    </script>
    ```
    
    - 해결 2 - v-for와 template 요소를 사용하여 v-if를 이동
    
    ```html
    <ul>
      <template v-for="todo in todos" :key="todo.id">
        <li v-if="!todo.isComplete">
          {{ todo.name }}
        </li>
      </template>
    </ul>
    <script>
    	...
    	//위와 동일
    	...
    </script>
    ```
    

## Watchers

### watch()

- 반응형 데이터를 감시하고 감시하는 데이터가 변경되면 콜백 함수를 호출

```jsx
watch(variable, (newValue, oldValue) => {
	//do something
})
```

- variable
    - 감시하는 변수
- newValue
    - 감시하는 변수가 변화된 값
    - 콜백 함수의 첫번째 인자
- oldValue
    - 콜백 함수의 두번째 인자
- 예시
    - 감시하는 변수에 변화가 생겼을 때 기본 동작 확인하기
    
    ```html
    <button @click="count++">Add 1</button>
    <p>Count: {{ count }}</p>
    <script>
      const { createApp, ref, watch } = Vue
    
      const app = createApp({
        setup() {
          const count = ref(0)
    
          const countWatch = watch(count, (newValue, oldValue) => {
            console.log(`newValue: ${newValue}, oldValue: ${oldValue}`)
          })
    
          return {
            count,
            countWatch
          }
        }
      })
    
      app.mount('#app')
    </script>
    ```
    
    ![Untitled 2](https://github.com/yuj1818/TIL/assets/95585314/06140bc3-b8e2-422a-a1b1-794b48a1ec8d)
    
    - 감시하는 변수에 변화가 생겼을 때 연관 데이터 업데이트하기
    
    ```html
    <input v-model="message">
    <p>Message length: {{ messageLength }}</p>
    <script>
    	const message = ref('')
      const messageLength = ref(0)
    
      const messageWatch = watch(message, (newValue, oldValue) => {
        messageLength.value = newValue.length
      })
    </script>
    ```
    

### Computed와 Watchers

|  | Computed | Watchers |
| --- | --- | --- |
| 공통점 | 데이터의 변화를 감지하고 처리 | “” |
| 동작 | 의존하는 데이터 속성의 계산된 값을 반환 | 특정 데이터 속성의 변화를 감시하고 작업을 수행 |
| 사용 목적 | 템플릿 내에서 사용되는 데이터 연산용 | 데이터 변경에 따른 특정 작업 처리용 |
| 사용 예시 | 연산 된 길이, 필터링 된 목록 계산 등 | 비동기 API 요청, 연관 데이터 업데이트 등 |
- computed와 watch 모두 의존(감시)하는 원본 데이터를 직접 변경하지 않음

## Lifecycle Hooks

- Vue 인스턴스의 생애주기 동안 특정 시점에 실행되는 함수
- 개발자가 특정 단계에서 의도하는 로직이 실행될 수 있도록 함
- 예시
    - Vue 컴포넌트 인스턴스가 초기 렌더링 및 DOM 요소 생성이 완료된 후 특정 로직을 수행하기
    
    ```html
    <script>
    	const { createApp, ref, onMounted } = Vue
    
      const app = createApp({
        setup() {
          onMounted(() => {
            console.log('mounted')
          })
    
    	app.mount('#app')
    </script>
    ```
    
    - 반응형  데이터의 변경으로 인해 컴포넌트의 DOM이 업데이트 된 후 특정 로직을 수행하기
    
    ```html
    <button @click="count++">Add 1</button>
    <p>Count: {{ count }}</p>
    <p>{{ message }}</p>
    <script>
    	const { createApp, ref, onMounted, onUpdated } = Vue
    
      const app = createApp({
        setup() {
          const count = ref(0)
          const message = ref(null)
    
          onUpdated(() => {
            message.value = 'updated!'
          })
    
          return {
            count,
            message
          }
        },
      })
    
      app.mount('#app')
    </script>
    ```
    

### Lifecycle Hooks 특징

- Vue는 Lifecycle Hooks에 등록된 콜백 함수들을 인스턴스와 자동으로 연결함
- 이렇게 동작하려면 hooks 함수들은 반드시 동기적으로 작성되어야 함
- 인스턴스 생애 주기의 여러 단계에서 호출되는 다른 hooks도 있으며, 가장 일반적으로 사용되는 것은 onMounted, onUpdated, onUnmounted
- [https://vuejs.org/api/composition-api-lifecycle.html](https://vuejs.org/api/composition-api-lifecycle.html)

### Lifecycle Hooks Diagram

- [https://vuejs.org/guide/essentials/lifecycle.html#lifecycle-diagram](https://vuejs.org/guide/essentials/lifecycle.html#lifecycle-diagram)

<img src="https://github.com/yuj1818/TIL/assets/95585314/f27f6df2-59a2-4238-a250-1fcf661bf13a" width="40%">

## Vue Style Guide

- Vue의 스타일 가이드 규칙은 우선순위에 따라 4가지 범주로 나눔
- [https://vuejs.org/style-guide/](https://vuejs.org/style-guide/)
- 규칙 범주
    - 우선순위 A : 필수 (Essential)
        - 오류를 방지하는 데 도움이 되므로 어떤 경우에도 규칙을 학습하고 준수
    - 우선순위 B : 적극 권장 (Strongly Recommended)
        - 가독성 및 개발자 경험을 향상시킴
        - 규칙을 어겨도 코드는 여전히 실행되겠지만, 정당한 사유가 있어야 규칙을 위반할 수 있음
    - 우선순위 C : 권장 (Recommended)
        - 일관성을 보장하도록 임의의 선택을 할 수 있음
    - 우선순위 D : 주의 필요 (Use with Caution)
        - 잠재적 위험 특성을 고려함
- 우선 순위 A
    - v-for에 key 작성하기
    - 동일 요소에 v-if와 v-for 함께 사용하지 않기

# Single-File Components

## Component

- 재사용 가능한 코드 블록

### Component 특징

- UI를 독립적이고 재사용 가능한 일부분으로 분할하고 각 부분을 개별적으로 다룰 수 있음
- 그러면 자연스럽게 앱은 중첩된 Component의 트리로 구성됨

## SFC(Single-File Components)

- 컴포넌트의 템플릿, 로직 및 스타일을 하나의 파일로 묶어낸 특수한 파일 형식(*.vue 파일)
- Vue SFC는 HTML, CSS 및 JavaScript 3개를 하나로 합친 것
- \<template>, \<script> 및 \<style> 블록은 하나의 파일에서 컴포넌트의 뷰, 로직 및 스타일을 캡슐화하고 배치

```html
<template>
    <div class="greeting">{{ msg }}</div>
</template>

<script setup>
    import {ref} from 'vue'

    const msg = ref('Hello World!')
</script>

<style scoped>
    .greeting {
        color: red;
    }
</style>
```

### SFC 문법

- 각 *.vue 파일은 세 가지 유형의 최상위 언어 블록 \<template>, \<script>, \<style>으로 구성됨
- 언어 블록의 작성 순서는 상관 없으나 일반적으로 template → script → style 순서로 작성
- 언어 블록 - \<template>
    - 각 *.vue 파일은 최상위 \<template> 블록을 하나만 포함할 수 있음
- 언어 블록 - \<script setup>
    - 각 *.vue 파일은 하나의 \<script setup> 블록만 포함할 수 있음
        - 일반 \<script> 제외
    - 컴포넌트의 setup() 함수로 사용되며 컴포넌트의 각 인스턴스에 대해 실행
- 언어 블록 - \<style scope>
    - *.vue 파일에는 여러 \<style> 태그가 포함될 수 있음
    - scoped가 지정되면 CSS는 현재 컴포넌트에만 적용

### 컴포넌트 사용하기

- [https://play.vuejs.org/](https://play.vuejs.org/) 에서 Vue 컴포넌트 코드 작성 및 미리보기
- Vue SFC는 컴파일러를 통해 컴파일 된 후 빌드 되어야 함
- 실제 프로젝트에서는 일반적으로 SFC 컴파일러를 Vite와 같은 공식 빌드 도구를 사용해 사용

## SFC build tool(Vite)

- 프론트엔드 개발 도구
- 빠른 개발 환경을 위한 빌드 도구와 개발 서버를 제공
- [https://vitejs.dev/](https://vitejs.dev/)

### Vite 튜토리얼

- vite 프로젝트 생성

```bash
npm create vue@latest
```

- 프로젝트 설정 관련 절차 진행
- 프로젝트 폴더 이동 및 패키지 설치

```bash
cd pjt_name
npm install
```

- Vue 프로젝트 서버 실행

```bash
npm run dev
```

## NPM(Node Package Manager)

- Node.js의 기본 패키지 관리자
- Chrome의 V8 JavaScript 엔진을 기반으로 하는 Server-Side 실행 환경

### Node.js의 영향

- 기존에 브라우저 안에서만 동작할 수 있었던 JavaScript를 브라우저가 아닌 서버 측에서도 실행할 수 있게 함
    - 프론트엔드와 백엔드에서 동일한 언어로 개발할 수 있게 됨
- NPM을 활용해 수많은 오픈 소스 패키지와 라이브러리를 제공하여 개발자들이 손쉽게 코드를 공유하고 재사용할 수 있게 함

## Vite 프로젝트 구조

### node_modules

- Node.js 프로젝트에서 사용되는 외부 패키지들이 저장되는 디렉토리
- 프로젝트의 의존성 모듈을 저장하고 관리하는 공간
- 프로젝트가 실행될 때 필요한 라이브러리와 패키지들을 포함
- .gitignore에 작성됨

### package-lock.json

- 패키지들의 실제 설치 버전, 의존성 관계, 하위 패키지 등을 포함하여 패키지 설치에 필요한 모든 정보를 포함
- 패키지들의 정확한 버전을 보장하여, 여러 개발자가 협업하거나 서버 환경에서 일관성 있는 의존성을 유지하는 데 도움을 줌
- npm install 명령을 통해 패키지를 설치할 때, 명시된 버전과 의존성을 기반으로 설치

### package.json

- 프로젝트의 메타 정보와 의존성 패키지 목록을 포함
- 프로젝트의 이름, 버전, 작성자, 라이선스 등과 같은 메타 정보를 정의
- package-lock.json과 함께 프로젝트의 의존성을 관리하고, 버전 충돌 및 일관성을 유지하는 역할

### public 디렉토리

- 주로 다음 정적 파일을 위치 시킴
    - 소스코드에서 참조되지 않는
    - 항상 같은 이름을 갖는
    - import 할 필요 없는
- 항상 root 절대 경로를 사용하여 참조
    - public/icon.png는 소스코드에서 /icon.png로 참조할 수 있음
- [https://vitejs.dev/guide/assets.html#the-public-directory](https://vitejs.dev/guide/assets.html#the-public-directory)

### src 디렉토리

- 프로젝트의 주요 소스 코드를 포함하는 곳
- 컴포넌트, 스타일, 라우팅 등 프로젝트의 핵심 코드를 관리

### src/assets

- 프로젝트 내에서 사용되는 자원(이미지, 폰트, 스타일 시트 등)을 관리
- 컴포넌트 자체에서 참조하는 내부 파일을 저장하는데 사용
- 컴포넌트가 아닌 곳에서는 public 디렉토리에 위치한 파일을 사용

### src/components

- Vue 컴포넌트들을 작성하는 곳

### src/App.vue

- Vue 앱의 최상위 Root 컴포넌트
- 다른 하위 컴포넌트들을 포함
- 애플리케이션 전체의 레이아웃과 공통적인 요소를 정의

### src/main.js

- Vue 인스턴스를 생성하고, 애플리케이션을 초기화하는 역할
- 필요한 라이브러리를 import하고 전역 설정을 수행

### index.html

- Vue 앱의 기본 HTML 파일
- 앱의 진입점(entry point)
- Root 컴포넌트인 App.vue가 해당 페이지에 마운트(mount) 됨
    - Vue 앱이 SPA인 이유
- 필욯한 스타일 시트, 스크립트 등의 외부 리소스를 로드 할 수 있음

### 모듈과 번들러

- Module
    - 프로그램을 구성하는 독립적인 코드 블록(*.js 파일)
    - 개발하는 애플리케이션의 크기가 커지고 복잡해지면서 파일 하나에 모든 기능을 담기가 어려워 짐
    - 따라서 자연스럽게 파일을 여러 개로 분리하여 관리를 하게 되었고, 이때 분리된 파일 각각이 모듈(module). 즉, js 파일 하나가 하나의 모듈
    - 모듈의 수가 많아지고 라이브러리 혹은 모듈 간의 의존성(연결성)이 깊어지면서 특정한 곳에서 발생한 문제가 어떤 모듈 간의 문제인지 파악하기 어려워 짐
    - 복잡하고 깊은 모듈의 의존성 문제를 해결하기 위한 도구가 필요
        - Bundler
- Bundler
    - 여러 모듈과 파일을 하나(혹은 여러 개)의 번들로 묶어 최적화하여 애플리케이션에서 사용할 수 있게 만들어 주는 도구
    - 의존성 관리, 코드 최적화, 리소스 관리 등의 역할
    - Bundler가 하는 작업을 Bundling이라 함
    - Vite는 Rollup이라는 Bundler를 사용하며 개발자가 별도로 기타 환경설정에 신경 쓰지 않도록 모두 설정해두고 있음

## Vue Component

### Component 활용

- 사전 준비
    - 초기에 생성된 모든 컴포넌트 삭제(App.vue 제외)
    - App.vue 코드 초기화
- 컴포넌트 파일 생성
    - MyComponent.vue 생성
    
    ```html
    <template>
        <div class="greeting">{{ msg }}</div>
    </template>
    
    <script setup>
        import {ref} from 'vue'
    
        const msg = ref('Hello World!')
    </script>
    
    <style scoped>
        .greeting {
            color: red;
        }
    </style>
    ```
    
    - App 컴포넌트에 MyComponent를 등록
        - App(부모) - MyComponent(자식) 관계 형성
        - @ - ‘src/’ 경로를 뜻하는 약어
    
    ```html
    <script setup>
      import MyComponent from '@/components/MyComponent.vue';
    </script>
    
    <template>
      <h1>App.vue</h1>
      <MyComponent />
    </template>
    
    <style scoped>
    
    </style>
    ```
    
    - MyComponentItem 컴포넌트 등록 후 활용
        - 컴포넌트의 재사용성 확인
        
        ```html
        <!-- MyComponentItem.vue -->
        <template>
            <p>MyComponentItem</p>
        </template>
        ```
        
        ```html
        <!-- MyComponent.vue -->
        
        <template>
            <div>
                <h2>MyComponent</h2>
                <MyComponentItem />
                <MyComponentItem />
                <MyComponentItem />
            </div>
        </template>
        
        <script setup>
            import MyComponentItem from './MyComponentItem.vue';
        </script>
        ```
        

### component 이름 관련 스타일 가이드

- [https://vuejs.org/style-guide/rules-strongly-recommended.html](https://vuejs.org/style-guide/rules-strongly-recommended.html)

## Virtual DOM

- 가상의 DOM을 메모리에 저장하고 실제 DOM과 동기화하는 프로그래밍 개념
- 실제 DOM과의 변경 사항 비교를 통해 변경된 부분만 실제 DOM에 적용하는 방식
- 웹 애플리케이션의 성능을 향상시키기 위한 Vue의 내부 렌더링 기술

### 내부 렌더링 과정

![Untitled 4](https://github.com/yuj1818/TIL/assets/95585314/cf4e8d70-f6b1-4abb-9615-954fda22b33a)

### Virtual DOM 패턴의 장점

- 효율성
    - 실제 DOM 조작을 최소화하고, 변경된 부분만 업데이트하여 성능을 향상
- 반응성
    - 데이터의 변경을 감지하고, Virtual DOM을 효율적으로 갱신하여 UI를 자동으로 업데이트
- 추상화
    - 개발자는 실제 DOM 조작을 Vue에게 맡기고 컴포넌트와 템플릿을 활용하는 추상화된 프로그래밍 방식으로 원하는 UI 구조를 구성하고 관리할 수 있음

### Virtual DOM 주의사항

- 실제 DOM에 직접 접근하지 말 것
    - JavaScript에서 사용하는 DOM 접근 관련 메서드 사용 금지
        - querySelector, createElement, addEventListener 등
- Vue의 ref와 Lifecycle Hooks 함수를 사용해 간접적으로 접근하여 조작할 것

### 직접 DOM 엘리먼트에 접근해야 하는 경우

- ref 속성을 사용하여 특정 DOM 엘리먼트에 직접적인 참조를 얻을 수 있음

```html
<template>
	<input ref="input">
</template>

<script setup>
	import { ref, onMounted } from 'vue'
	
	const input = ref(null)

	onMounted(() => {
		console.log(input.value) //<input>
	})
</script>
```

## Composition API & Option API

### Composition API

- import해서 가져온 API 함수들을 사용하여 컴포넌트의 로직을 정의
- Vue3에서의 권장 방식

```html
<template>
    <button @click="increment">{{ count }}</button>
</template>

<script setup>
    import { ref, onMounted } from 'vue'
    
    const count = ref(0)

    const increment = () => {
        count.value++
    }

    onMounted(() => {
        console.log(`숫자 세기의 초기값은 ${ count.value }`)
    })
</script>
```

### Option API

- data, methods 및 mounted 같은 객체를 사용하여 컴포넌트의 로직을 정의
- Vue2에서의 작성 방식

```html
<template>
	<button @click="increment">{{ count }}</button>
</template>
<script>
	export default {
		data() {
			return {
				count: 0
			}
		},
		methods: {
			increment() {
				this.count++
			}
		},
		mounted() {
			console.log(`숫자 세기의 초기값은 ${this.count}`)
		}
	}
</script>
```

### API 별 권장 사항

- Composition API + SFC
    - 규모가 있는 앱의 전체를 구축하려는 경우
- Option API
    - 빌드 도구를 사용하지 않거나 복잡성이 낮은 프로젝트에서 사용하려는 경우
- [https://vuejs.org/guide/extras/composition-api-faq.html](https://vuejs.org/guide/extras/composition-api-faq.html)

# Passing Props

- 한 화면의 다양한 컴포넌트에서 동일한 데이터를 다루고 있다면 데이터 변경 시, 모든 컴포넌트에 대해 변경 요청이 필요
    - 공통된 부모 컴포넌트에서 관리하는 것이 효율적
- 부모는 자식에게 데이터를 전달(Pass Props)하며, 자식은 자신에게 일어난 일을 부모에게 알림(Emit event)

![Untitled 5](https://github.com/yuj1818/TIL/assets/95585314/4fbd88fc-def6-4871-bf06-1fa1ad8130ae)

## Props

- 부모 컴포넌트로부터 자식 컴포넌트로 데이터를 전달하는데 사용되는 속성

### One-way Data Flow

- 모든 props는 자식 속성과 부모 속성 사이에 하향식 단방향 바인딩을 형성(one-way-down binding)
- 하위 컴포넌트가 실수로 상위 컴포넌트의 상태를 변경하여 앱에서의 데이터 흐름을 이해하기 어렵게 만드는 것을 방지하기 위해 단방향임

### Props 특징

- 부모 속성이 업데이트 되면 자식으로 흐르지만 그 반대는 안됨
- 즉, 자식 컴포넌트 내부에서 props를 변경하려고 시도해서는 안되며 불가능
- 또한 부모 컴포넌트가 업데이트 될 때마다 자식 컴포넌트의 모든 props가 최신 값으로 업데이트 됨
- 부모 컴포넌트에서만 변경하고 이를 내려 받는 자식 컴포넌트는 자연스럽게 갱신

### App > Parent > ParentChild 컴포넌트 관계 작성

- App 컴포넌트 작성

```html
<template>
  <div>
    <Parent />
  </div>
</template>

<script setup>
  import Parent from '@/components/Parent.vue'
</script>
```

- Parent 컴포넌트 작성

```html
<template>
  <div>
    <ParentChild />
  </div>
</template>

<script setup>
  import ParentChild from '@/components/ParentChild.vue'
</script>
```

- ParentChild 컴포넌트 작성

```html
<template>
  <div>
  </div>
</template>

<script setup>
</script>
```

## Props 선언

- 부모 컴포넌트에서 보낸 props를 사용하기 위해서는 자식 컴포넌트에서 명시적인 props 선언이 필요

### Props 작성

- 부모 컴포넌트 Parent에서 자식 컴포넌트 ParentChild에 보낼 props 작성

```html
<template>
  <div>
    <ParentChild my-msg="message"/>
  </div>
</template>
```

### Props 선언 2가지 방식

- 문자열 배열을 사용한 선언
    - defineProps()를 사용하여 props를 선언
    
    ```html
    <!-- ParentChild.vue -->
    
    <script setup>
      defineProps(['myMsg'])
    </script>
    ```
    
- 객체를 사용한 선언
    - 객체 선언 문법의 각 객체 속성의 키는 props의 이름이 되며, 객체 속성의 값은 값이 될 데이터의 타입에 해당하는 생성자 함수(Number, String)여야 함
    - **객체 선언 문법 사용 권장**
    
    ```html
    <script setup>
      defineProps({
        myMsg:String
      })
    </script>
    ```
    

### Prop 데이터 사용

- 템플릿에서 반응형 변수와 같은 방식으로 활용

```html
<!-- ParentChild.vue -->

<template>
  <div>
    <p>{{ myMsg }}</p>
  </div>
</template>
```

- props를 객체로 반환하므로 필요한 경우 JavaScript에서 접근 가능

```html
<script setup>
  const props = defineProps({
    myMsg:String
  })
  console.log(props)
  console.log(props.myMsg)
</script>
```

### 한 단계 더 prop 내려 보내기

- ParentChild 컴포넌트를 부모로 갖는 ParentGrandChild 컴포넌트 생성 및 등록

```html
<!-- ParentChild.vue -->
<template>
  <div>
    <p>{{ myMsg }}</p>
    <ParentGrandChild />
  </div>
</template>

<script setup>
  import ParentGrandChild from '@/components/ParentGrandChild.vue'
  // defineProps(['myMsg'])
  const props = defineProps({
    myMsg:String
  })
  console.log(props)
  console.log(props.myMsg)
</script>
```

- ParentChild 컴포넌트에서 Parent로 부터 받은 prop인 myMsg를 ParentGrandChild에게 전달

```html
<!-- ParentChild.vue -->
<template>
  <div>
    <p>{{ myMsg }}</p>
    <ParentGrandChild :my-msg="myMsg"/>
  </div>
</template>
```

```html
<!-- ParentGrandChild.vue -->
<template>
  <div>
    <p>{{ myMsg }}</p>
  </div>
</template>

<script setup>
  defineProps({
    myMsg: String
  })
</script>
```

## Props 세부사항

### Props Name Casing (Props 이름 컨벤션)

- 선언 및 템플릿 참조 시 (→ camelCase)

```html
<p>{{ myMsg }}</p>
<script>
	defineProps({
		myMsg: String
	})
</script>
```

- 자식 컴포넌트로 전달 시(→ kebab-case)
    - **기술적으로 camelCase도 가능하나 HTML 속성 표기법과 동일하게 kebab-case로 표기할 것을 권장**

```html
<ParentChild my-msg="message" />
```

### Static Props & Dynamic Props

- 지금까지 작성한 것은 Static(정적) props
- v-bind를 사용하여 동적으로 할당된 props를 사용할 수 있음
- Dynamic props 정의

```html
<template>
  <div>
    <ParentChild my-msg="message" :dynamic-props="name"/>
  </div>
</template>

<script setup>
  import ParentChild from '@/components/ParentChild.vue'
  import { ref } from 'vue'
  const name = ref('Alice')
</script>
```

- Dynamic props 선언 및  출력

```html
<template>
  <div>
    <p>{{ myMsg }}</p>
    <p>{{ dynamicProps}}</p>
  </div>
</template>

<script setup>
  const props = defineProps({
    myMsg:String,
    dynamicProps: String
  })
</script>
```

# Component Events

- 부모는 자식에게 데이터를 전달(Pass Props)하며, 자식은 자신에게 일어난 일을 부모에게 알림(Emit event)
- **부모가 prop 데이터를 변경하도록 말해야 함**

## $emit()

- 자식 컴포넌트가 이벤트를 발생시켜 부모 컴포넌트로 데이터를 전달하는 역할의 메서드
- ‘$’표기는 Vue 인스턴스나 컴포넌트 내에서 제공되는 전역 속성이나 메서드를 식별하기 위한 접두어

### emit 메서드 구조

- `$emit(event, ...args)`
    - event
        - 커스텀 이벤트 이름
    - args
        - 추가 인자

## Event 발신 및 수신

- $emit을 사용하여 템플릿 표현식에서 직접 사용자 정의 이벤트를 발신

```html
<button @click="$emit('someEvent')">클릭</button>
```

- 그러면 부모는 v-on을 사용하여 수신할 수 있음

```html
<ParentComp @some-event="someCallback" />
```

### 이벤트 발신 및 수신하기

- ParentChild에서 someEvent라는 이름의 사용자 정의 이벤트를 발신

```html
<button @click="$emit('someEvent')">클릭</button>
```

- ParentChild의 부모 Parent는 v-on을 사용하여 발신된 이벤트를 수신
- 수신 후 처리할 로직 및 콜백 함수 호출

```html
<!-- Parent.vue -->
<template>
  <div>
    <ParentChild @some-event="someCallback" my-msg="message" :dynamic-props="name"/>
  </div>
</template>

<script setup>
  import ParentChild from '@/components/ParentChild.vue'
  import { ref } from 'vue'
  const name = ref('Alice')
  const someCallback = function() {
      console.log('ParentChild가 발신한 이벤트를 수신했어요.')
  }
</script>  
```

## ‘emit’ Event 선언

- defineEmits()를 사용하여 명시적으로 발신할 이벤트를 선언할 수 있음
- script에서 $emit 메서드를 접근할 수 없기 때문에 defineEmits()는 $emit 대신 사용할 수 있는 동등한 함수를 반환
- 이벤트 선언 방식으로 추가 버튼 작성 및 결과 확인

```html
<!-- ParentChild.vue -->
<template>
  <div>
		...
    <button @click="buttonClick">클릭</button>
  </div>
</template>

<script setup>
  ...
  const emit = defineEmits(['someEvent', 'myFocus'])
  const buttonClick = function() {
    emit('someEvent')
  }
</script>
```

## Event 인자(Event Arguments)

- 이벤트 발신 시 추가 인자를 전달하여 값을 제공할 수 있음

### 이벤트 인자 전달하기

- ParentChild에서 이벤트를 발신하여 Parent로 추가 인자 전달하기

```html
<template>
  <div>
    ...
    <button @click="emitArgs">추가 인자 전달</button>
  </div>
</template>

<script setup>
  ...
  const emit = defineEmits(['someEvent', 'emitArgs'])
  const emitArgs = function() {
    emit('emitArgs', 1, 2, 3)
  }
</script>
```

- ParentChild에서 발신한 이벤트를 Parent에서 수신

```html
<template>
  <div>
    <ParentChild 
      @some-event="someCallback" 
      @emit-args="getNumbers"
      my-msg="message" 
      :dynamic-props="name"
    />
  </div>
</template>

<script setup>
  ...
  const getNumbers = function(...args) {
    console.log(args)
    console.log(`ParentChild가 전달한 추가인자 ${args}를 수신했어요`)
  }
</script>
```

## Event 세부사항

### Event Name Casing

- 선언 및 발신 시 (→ cameCalse)

```html
<button @click="$emit('someEvent')">클릭</button>
<script setup>
	const emit = defineEmits(['someEvent'])
	emit('someEvent')
</script>
```

- 부모 컴포넌트에서 수신 시 (→ kebab-case)

```html
<ParentChild @some-event="..." />
```

## emit Event 실습

- 최하단 컴포넌트 ParentGrandChild에서 Parent 컴포넌트의 name 변수 변경 요청하기

### ParentGrandChild에서 이름 변경을 요청하는 이벤트 발신

```html
<template>
  <div>
    <button @click="updateName">이름 변경</button>
  </div>
</template>

<script setup>
  const emit = defineEmits(['updateName'])
  const updateName = function() {
    emit('updateName')
  }
</script>
```

### ParentChild에서 이벤트 수신 후 이름 변경 요청하는 이벤트 발신

```html
<template>
  <div>
    <p>{{ myMsg }}</p>
    <p>{{ dynamicProps}}</p>
    <ParentGrandChild :my-msg="myMsg" @update-name="updateName"/>
    ...
  </div>
</template>

<script setup>
  ...
  const emit = defineEmits(['updateName'])
  const updateName = function() {
    emit('updateName')
  }
</script>
```

### Parent에서 이벤트 수신 후 이름 변수 변경 메서드 호출

- 해당 변수를 prop으로 받는 모든 곳에서 자동 업데이트

```html
<template>
    <div>
        <ParentChild @update-name="updateName" />
    </div>
</template>

<script setup>
    ...
    const updateName = function() {
        name.value = 'Bella'
    }
</script>
```

# 참고

### Ref Unwrap 주의 사항

- 템플릿에서의 unwrap은 ref 최상위 속성인 경우에만 적용 가능
    
    ```html
    <h1>{{object.id + 1}}</h1> <!-- [object Object]1 로 출력 됨 -->
    <script>
    	...
    	const object = { id : ref(0) }
    	...
    </script>
    ```
    
    - object는 최상위 속성이지만 object.id는 그렇지 않음
    - 표현식을 평가할 때 object.id가 unwrap 되지 않고 ref 객체로 남아 있기 때문
- 이 문제를 해결하기 위해서는 id를 최상위 속성으로 분해해야 함
    
    ```html
    <h1>{{ id + 1 }}</h1>
    <script>
    	...
    	const { id } = object
    	...
    </script>
    ```
    
- 단, ref가 {{}}의 최종 평가 값이 경우는 unwrap 가능
    
    ```html
    <h1>{{ object.id }}</h1> <!-- {{ object.id.value }}와 동일 -->
    ```
    

### Why Refs?

- 일반 변수 대신 굳이 .value가 포함된 ref가 필요한 이유는?
- Vue는 템플릿에서 ref를 사용하고 나중에 ref의 값을 변경하면 자동으로 변경 사항을 감지하고 그에 따라 DOM을 업데이트 함
    - 의존성 추적 기반의 반응형 시스템
- Vue는 렌더링 중에 사용된 모든 ref를 추적하며, 나중에 ref가 변경되면 이를 추적하는 구성 요소에 대해 다시 렌더링
- JavaScript에서는 일반 변수의 접근 또는 변형을 감지할 방법이 없기 때문
- [https://vuejs.org/guide/essentials/reactivity-fundamentals.html#why-refs](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#why-refs)

### SEO(Search Engine Optimization)

- google, bing과 같은 검색 엔진 등에 내 서비스나 제품 등이 효율적으로 검색 엔진에 노출되도록 개선하는 과정을 일컫는 작업
- 정보의 대상은 주로 HTML에 작성된 내용
- 검색
    - 각 사이트가 운영하는 검색 엔진에 의해 이루어지는 작업
- 검색 엔진
    - 웹 상에 존재하는 가능한 모든 정보들을 긁어 모으는 방식으로 동작
- 최근에는 SPA, 즉 CSR로 구성된 서비스의 비중이 증가
- SPA 서비스도 검색 대상으로 넓히기 위해 JS를 지원하는 방식으로 발전하는 중

### CSR & SSR

- CSR과 SSR은 흑과 백이 아님
    - 내 서비스에 적합한 렌더링 방식을 적절하게 활용할 수 있어야 함
- SPA 서비스에서도 SSR을 지원하는 Framework가 발전하고 있음
    - Vue의 Nuxt.js
    - React의 Next.js
    - Angular Universal

## 문법 관련

### v-bind 참고 문서

- [https://vuejs.org/api/built-in-directives.html#v-bind](https://vuejs.org/api/built-in-directives.html#v-bind)

### v-on 참고 문서

- [https://vuejs.org/api/built-in-directives.html#v-on](https://vuejs.org/api/built-in-directives.html#v-on)

### v-model 참고 문서

- [https://vuejs.org/api/built-in-directives.html#v-model](https://vuejs.org/api/built-in-directives.html#v-model)

### IME(Input Method Editor)

- 사용자가 입력 장치에서 기본적으로 사용할 수 없는 문자(비영어권 언어)를 입력할 수 있도록 하는 운영 체제 구성 프로그램
- 일반적으로 키보드 키보다 자모가 더 많은 언어에서 사용해야 함
- IME가 동작하는 방식과 Vue의 양방향 바인딩(v-model) 동작 방식이 상충하기 때문에 한국어 입력 시 예상대로 동작하지 않았던 것

### [주의] computed의 반환 값은 변경하지 말 것

- computed의 반환 값은 의존하는 데이터의 파생된 값
- 일종의 snapshot이며 의존하는 데이터가 변경될 때 마다 새 snapshot이 생성됨
- snapshot을 변경하는 것은 의미가 없으므로 계산된 반환 값은 읽기 전용으로 취급되어야 하며 변경되어서는 안됨
- 대신 새 값을 얻기 위해서는 의존하는 데이터를 업데이트 해야 함

### [주의] computed 사용 시, 원본 배열 변경하지 말 것

- computed에서 reverse() 및 sort() 사용 시 원본 배열을 변경하기 때문에 복사본을 만들어서 진행 해야 함

```html
// 원본 변경
return numbers.reverse()
// 원본 변경하지 않도록 복사본 생성하여 진행
return [...numbers].reverse() 
```

### [주의] 배열의 인덱스를 v-for의 key로 사용하지 말 것

- 인덱스는 식별자가 아닌 배열의 항목 위치만 나타내기 때문에 Vue가 DOM을 변경할 때 (끝이 아닌 위치에 새 항목이 배열에 삽입되면) 여러 컴포넌트 간 데이터 공유 시 문제가 발생
- 직접 고유한 값을 만들어내는 메서드를 만들거나 외부 라이브러리 등을 활용하는 등 식별자 역할을 할 수 있는 값을 만들어 사용

### v-for와 배열 - “배열 변경 감지”

- 수정 메서드(원본 배열 수정)
    - Vue는 반응형 배열의 변경 메소드가 호출되는 것을 감지하여, 필요한 업데이트를 발생시킴
    - push(), pop(), shift(), unshift(), splice(), sort(), reverse()
- 배열 교체
    - 원본 배열을 수정하지 않고 항상 새 배열의 반환
    - filter(), concat(), slice()

### v-for와 배열 - “필터링/정렬 결과 표시”

- 원본 데이터를 수정하거나 교체하지 않고 필터링 되거나 정렬된 결과를 표시
    - computed 활용
    
    ```html
    <li v-for="num in evenNumbers">{{ num }}</li>
    <script>
    	...
    	const numbers = ref([1, 2, 3, 4, 5])
    
    	const evenNumbers = computed(() => {
    		return numbers.value.filter((number) => number % 2 === 0)
    	})
    	...
    </script>
    ```
    
    - method 활용 (computed가 불가능한 중첩된 v-for의 경우)
    
    ```html
    <ul v-for="numbers in numberSets">
      <li v-for="num in evenNumbers(numbers)">
        {{num}}
      </li>
    </ul>
    <script>
    	...
      const numberSets = ref([
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
      ])
    
    	const evenNumbers = function(numbers) {
        return numbers.filter((number) => number % 2 === 0)
      }
    	...
    </script>
    ```

## SFC 관련

### Scaffolding(스캐폴딩)

- 새로운 프로젝트나 모듈을 시작하기 위해 초기 구조와 기본 코드를 자동으로 생성하는 과정
- 개발자들이 프로젝트를 시작하는 데 도움을 주는 틀이나 기반을 제공하는 작업
- 초기 설정, 폴더 구조, 파일 템플릿, 기본 코드 등을 자동으로 생성하여 개발자가 시작할 때 시간과 노력을 절약하고 일관된 구조를 유지할 수 있도록 도와줌

### SFC의 CSS 기능 -scoped

- scoped를 사용하면 부모 컴포넌트의 스타일이 자식 컴포넌트로 유출되지 않음
- 단, 자식 컴포넌트의 최상위 요소(root element)는 부모와 자식의 CSS 모두의 영향을 받음
- 부모가 레이아웃 목적으로 자식 컴포넌트 최상위 요소의 스타일을 지정할 수 있도록 의도적으로 설계된 것
- 다음과 같이 App(부모) 컴포넌트에 적용한 스타일은 scoped가 작성되어 있지만, MyComponent(자식)의 최상위 요소는 부모와 본인의 CSS 모두의 영향을 받기 때문에 부모의 스타일이 적용됨

```html
<!-- App.vue -->

<template>
	<h1>App.vue</h1>
	<MyComponent />
</template>

<style scoped>
	div {
		color: red;
	}
</style>

<!-- MyComponent.vue -->

<template>
	<div>
		<h2>MyComponent</h2>
	</div>
</template>
```

### 모든 컴포넌트에는 최상단 HTML 요소가 작성되는 것이 권장

- 가독성, 스타일링, 명확한 컴포넌트 구조를 위해 각 컴포넌트에는 최상단 HTML 요소를 작성해야 함(Single Root Element)

```html
<template>
	<div> <!-- 최상단 요소 -->
		<h2>Heading</h2>
		<p>Paragraph</p>
		<p>Paragraph</p>
	</div>
</template>
```

### 관심사항의 분리가 파일 유형의 분리와 동일한 것이 아니다

- HTML/CSS/JS를 한 파일에 혼합하는 게 괜찮을까?
- 프론트엔드 앱의 사용 목적이 점점 더 복잡해짐에 따라, 단순 파일 유형으로만 분리하게 될 경우 프로젝트의 목표를 달성 하는데 도움이 되지 않게 됨

## Component State Flow 관련

### 정적 & 동적 props 주의 사항

- 첫 번째는 정적 props로 문자열로써의 “1”을 전달
- 두 번째는 동적 props로 숫자로써의 1을 전달

```html
<SomeComponent num-props="1" />
<SomeComponent :num-props="1" />
```

### Prop 선언을 객체 선언 문법으로 권장하는 이유

- prop에 타입을 지정하는 것은 컴포넌트를 가독성이 좋게 문서화하는데 도움이 되며, 다른 개발자가 잘못된 유형을 전달할 때에 브라우저 콘솔에 경고를 출력하도록 함
- 추가로 prop에 대한 **유효성 검사**로써 활용 가능
- [https://vuejs.org/guide/components/props.html#prop-validation](https://vuejs.org/guide/components/props.html#prop-validation)

### emit 이벤트도 객체 선언 문법으로 작성 가능

- props 타입 유효성 검사와 유사하게 emit 이벤트 또한 객체 구문으로 선언 된 경우 유효성을 검사할 수 있음
- [https://vuejs.org/guide/components/events.html#events-validation](https://vuejs.org/guide/components/events.html#events-validation)

```jsx
const emit = defineEmits({
	//유효성 검사 없음
	click: null,
	submit: ({ email, password }) => {
		if (email && password) {
			return true
		} else {
			console.warn('submit 이벤트가 옳지 않음')
			return false
		}
	}
})
const submitForm = function(email, password) {
	emit('submit', { email, password })
}
```