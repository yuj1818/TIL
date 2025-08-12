# NextJS

## NextJS란?

- React 프레임워크
- React에 빌드됨

## NextJS가 필요한 이유

- React로 풀스택 애플리케이션을 구축하는 과정을 단순화할 수 있음
- 최근들어, SPA보다 풀스택 애플리케이션을 구축하는 추세
- React 업데이트 내용을 보면 서버에서 리액트 사용을 더 쉽게 하도록 함
    - ex) 서버에서 컴포넌트를 렌더링 할 수 있게 업데이트

### 풀스택 애플리케이션을 구축하기 위해 필요한 요소

- 라우팅 (Route Setup & handling)
- Form 제출 처리 (Form Submission)
- 데이터 처리 (Data Fetching)
- 인증 (Authentication)
- etc

> [!IMPORTANT]
>⇒ NextJS로 해결할 수 있음

## NextJS의 주요 기능과 장점

- 하나의 언어로 하나의 프로젝트에서 프론트엔드와 백엔드를 다 구현할 수 있음
- 파일 시스템을 사용하여 경로 설정 가능 (File-based Routing)
    - 코드 기반 환경 설정이 추가로 필요하지 않음
- 서버 사이드 렌더링 (Server Side Rendering)
    - 모든 페이지를 서버에서 렌더링
    - SEO 성능 최적화 가능

### NextJS 프로젝트 생성

```bash
npx create-next-app@latest
cd 프로젝트 폴더
npm run dev
```

## Next 핵심 요소

### Pages Router

- 안정적
- 많이 사용됨
- 기능이 다양한 풀스택 앱을 만들 수 있음

### App Router

- Next13과 함께 나온 방식
- 안정적이나 부분적으로 버그 존재
- 리액트 서버 컴포넌트나 Server Actions 같은 다양한 최신 기능 사용 가능

**파일 시스템을 사용한 경로 설정**

- 프로젝트 폴더의 app 폴더에 폴더(ex. awesome)를 생성하고, 해당 폴더 내에 page.js 파일을 만들면 `loacalhost:{portNum}/awesome`에서 해당 페이지를 볼 수 있음

```markdown
├─app
	├─awesome
		├─page.js
```

### 보호된 파일명

- `page.js` => 신규 페이지 생성 (예: `app/about/page.js`은 `<domain_url>/about page`을 생성)
- `layout.js` => 형제 및 중첩 페이지를 감싸는 신규 레이아웃 생성
- `not-found.js` => ‘Not Found’ 오류에 대한 폴백 페이지(형제 또는 중첩 페이지 또는 레이아웃에서 전달된)
- `error.js` => 기타 오류에 대한 폴백 페이지(형제 또는 중첩 페이지 또는 레이아웃에서 전달된)
- `loading.js` => 형제 또는 중첩 페이지(또는 레이아웃)가 데이터를 가져오는 동안 표시되는 폴백 페이지
- `route.js` => API 경로 생성(즉, JSX 코드가 아닌 데이터를 반환하는 페이지, 예: JSON 형식)

### 서버 컴포넌트

- Next 앱에서는 기본적으로 모든 리액트 컴포넌트는 서버에서만 렌더링 됨
- 서버에서 데이터를 가져오고 UI의 일부를 렌더링 가능
- 선택적으로 결과를 캐시하고 클라이언트로 스트리밍 할 수 있음

### 클라이언트 컴포넌트

- 서버에서 미리 렌더링 된 후, 클라이언트 javascript를 통해 브라우저에서 실행할 수 있는 interactive UI를 작성할 수 있음
- 상호작용이나 브라우저 API가 필요한 경우 클라이언트 컴포넌트를 사용
- 파일 상단에 `“use client”` 를 import 위에 추가하면 사용 가능
    - 해당 파일에 import 된 모든 모듈, 자식 컴포넌트를 포함하여 클라이언트 번들의 일부로 간주됨

| **서버 컴포넌트** | **클라이언트 컴포넌트** |
| --- | --- |
| DB나 API에서 데이터를 가져올 때 | 상태 및 이벤트 핸들러가 필요할 때 (onClick, onChange) |
| 클라이언트에게 공개하지 않고 API 키, 토큰 등을 사용할 때 | useEffect 같이 수명 주기 논리가 필요할 때 |
| 브라우저로 전송되는 javascript의 양을 줄이고 싶을 때 | 브라우저 전용 API를 사용해야 할 때(localStorage, window 등) |
| FCP 개선을 위해 | 커스텀 훅을 사용해야 할 때 |

### 서버 액션

- async 함수 내부 상단에 `‘use server’` 추가하여 서버 액션 생성 가능
- 오직 서버에서만  해당 함수가 실행될 수 있게 보장해주는 기능
    - `<form>`의 action 속성에 서버 액션을 넣어 줄 수 있다.
        - 자동으로 요청을 생성하여 웹사이트를 제공하는 서버로 보내 폼 제출을 서버가 제어할 수 있음

### `revalidatePath`

```jsx
revalidatePath(path: string, type?: ‘page’ | ‘layout’): void;
```

- 특정 경로에 대해 캐시된 데이터를 필요에 따라 무효화(≓ 갱신)하는 함수
    - `path(필수)` : 무효화하려는 데이터와 관련된 파일 시스템 경로 또는 실제 경로 세그먼트
    - `type(선택)` : 무효화할 경로의 유형을 변경하기 위한 속성
        - page
            - 해당 **페이지 파일**과 그 **하위 children 페이지**들만 갱신
        - layout
            - 해당 **레이아웃 파일**과 그 **레이아웃을 공유하는 모든 하위 페이지** **전부**를 갱신
- 캐싱된 데이터를 무효화시켜 최신 데이터로 갱신하기 위한 함수