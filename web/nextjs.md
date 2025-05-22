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

## NextJS 앱을 만들기 위한 방법

### Pages Router

- 안정적
- 많이 사용됨
- 기능이 다양한 풀스택 앱을 만들 수 있음

### App Router

- Next13과 함께 나온 방식
- 안정적이나 부분적으로 버그 존재
- 리액트 서버 컴포넌트나 Server Actions 같은 다양한 최신 기능 사용 가능

#### 파일 시스템을 사용한 경로 설정

- 프로젝트 폴더의 app 폴더에 폴더(ex. awesome)를 생성하고, 해당 폴더 내에 page.js 파일을 만들면 `loacalhost:{portNum}/awesome`에서 해당 페이지를 볼 수 있음

```markdown
⨽app
	⨽awesome
		⨽page.js
```
