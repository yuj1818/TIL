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

#### 파일 시스템을 사용한 경로 설정

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

- Next 앱에서는 <u>기본적으로 모든 리액트 컴포넌트는 서버에서만 렌더링</u> 됨
- 서버에서 데이터를 가져오고 UI의 일부를 렌더링 가능
- 선택적으로 결과를 캐시하고 클라이언트로 스트리밍 할 수 있음

#### 주의 사항
- 서버 컴포넌트에는 브라우저에서 실행될 코드가 포함되면 안됨
- 클라이언트 컴포넌트는 클라이언트에서만 실행되지 않음
    - 사전 렌더링(서버) + 하이드레이션(브라우저) ⇒ 서버, 클라이언트 모두에서 실행
- 클라이언트 컴포넌트에서 서버 컴포넌트를 import 할 수 없음
- 서버 컴포넌트에서 클라이언트 컴포넌트에게 직렬화 되지 않는 Props는 전달 불가

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

## 라우팅 & 페이지 렌더링

### 병렬 라우트 & 중첩 라우트

![image.png](https://github.com/user-attachments/assets/874a6903-eeec-455b-8e0a-9229210c4048)

- 동일한 레이아웃 내에서 하나 이상의 페이지를 동시/조건부로 렌더링 가능
    - 동일한 url이나, 분리된 코드
- 위 이미지처럼 `@folder` 로 정의하며, `slots` 이라고 부름
    - 각 slot은 하나의 layout을 공유하며 layout의 props로 전달됨
- 각 slot에 대해 독립적인 오류 및 로드 상태를 정의할 수 있음
- A slot에서 중첩 라우팅을 사용하는데, B slot에서는 해당 중첩 라우팅이 필요 없는 경우에는 `default.js`를 사용
    - `/settings`로 이동하면, `team` slot에서는 `settings`의 page가 렌더링 되며, `analytics` slot에서는 `default.js`를 렌더링
    
    ![image.png](https://github.com/user-attachments/assets/87ed743c-4683-426e-86dc-bb3edc7a52cf)
    

### Catch-all 세그먼트

- 동적 세그먼트는 대괄호 안에 줄임표를 추가하여, 모든 후속 세그먼트를 포괄하도록 확장 가능
    - `[…folderName]`
    - 예시
        
        
        | Route | URL | params |
        | --- | --- | --- |
        | app/archive/[…filter]/page.js | /archive/year | { filter: [’year’] } |
        |  | /archive/year/month | { filter: [’year’, ‘month’] } |
- 선택적 Catch-all 세그먼트
    - 이중 대괄호를 포함하여 **선택 사항**으로 만들 수 있음
        - `[[…filter]]`
            - 일반적인 catch-all과 선택적 catch-all의 차이점은 **매개변수가 없어도 경로는 일치한다**는 점
            
            | Route | URL | params |
            | --- | --- | --- |
            | app/archive/[…filter]/page.js | /archive | {} |
            |  | /archive/year | { filter: [’year’] } |
            |  | /archive/year/month | { filter: [’year’, ‘month’] } |
            

### Intercepting 라우트

- 현재 레이아웃 내에서 애플리케이션의 다른 부분의 라우트를 로드할 수 있음
    - Modal을 띄울 때 자주 사용
- 컨벤션
    - 상대 경로 규칙과 비슷하게 `(경로)가로챌 페이지` 로 디렉토리를 생성
        
        ![image.png](https://github.com/user-attachments/assets/09271112-6371-4ebf-a3f6-e12282afe1c5)
        
- 병렬 라우트와 같이 사용하는 예시
    
    ![image.png](https://github.com/user-attachments/assets/ce92dafc-850d-47a3-acbc-99dd78c690b5)
    
    - `news/[slug]/image` 로 바로 접속할 경우(url 공유를 통해 접속할 때)에는 전체 사진 페이지가 렌더링
    - `news/[slug]` 에서 이미지를 클릭하여 `news/[slug]/image` 로 접근하는 경우는 해당 라우트를 가로채서 `news/[slug]` 위에 오버레이하여 모달로 사진을 띄울 수 있음

### 라우트 그룹

- **URL 경로에 영향을 주지 않고** 경로를 그룹화하기 위해 사용
- 같은 세그먼트에서 **일부 경로에만** layout을 주고 싶을 때 유용
- 컨벤션
    - 폴더 이름을 괄호로 묶어 생성
    - 최상위 `layout.js` 파일 없이 그룹 별 루트 레이아웃을 사용하는 경우, 홈 `page.js`는 그룹 중 하나에 정의되어야 함
        - 다만, 여러 루트 레이아웃 간의 내비게이션은 전체 페이지 로드를 유발


>[!NOTE]
>다른 그룹이더라도 같은 URL 경로를 가지면 안됨
>예) `(content)/about/page.js` , `(marketing)/about/page.js` 이렇게 사용하면 X

## Data Mutation

### Server Action

- `useFormStatus`
    - ReactJS에서 제공하는 마지막 폼 제출의 상태 정보를 제공하는 Hook
        - pending, data, method, action을 반환
    - 반드시 form 내부의 컴포넌트에서 호출해야 함
    - 동일한 컴포넌트나 자식 컴포넌트에서 렌더링한 form의 상태 정보는 반환하지 않으면 **오직 상위 form의 상태 정보만 반환**
    - form을 제출하는 동안 대기 중인 상태를 표시하기 위해 많이 사용
- `useActionState`
    - ReactJS에서 제공하는 폼 액션 결과를 기반으로 State를 업데이트할 수 있도록 제공하는 Hook
    - 폼 액션 함수와 초기 State를 전달 받고, 폼에서 사용할 새로운 액션과 최신 폼 State, isPending 여부를 반환
        - `useActionState(action, initialState, permalink?)`

>[!WARNING]
>“use server”는 **코드가 서버에서만 실행된다는 것을 의미하거나 보장하지 않음**
>클라이언트 측에서 절대 실행되어서는 안 되는 코드가 있다면 server-only 패키지를 사용해야 함
⚠️

- 추가 인수 전달
    
    `bind`
    
    - bind를 사용하여 서버 함수에 추가 인수를 전달할 수 있음
        - 예로, postId를 인수로 받는 서버 함수에 `togglePostLike(null, postId)` 로 postId를 전달할 수 있음

### 낙관적 업데이트

- `useOptimistic`
    - UI를 낙관적으로 업데이트 할 수 있게 해주는 React Hook
    - 비동기 작업이 진행 중일 때 다른 상태를 보여줄 수 있게 함
        - 예를 들어, 좋아요 api를 요청하고 대기 중일 때, UI는 이미 좋아요가 눌러진 상태로 보여지게 만들 수 있음

## 데이터 캐싱

### [NextJS 캐싱 유형](https://nextjs-ko.org/docs/app/building-your-application/caching)

### Request Memoization

- 동일한 설정을 가진 데이터 요청을 저장하여 <u>중복 요청을 방지</u>
    - 하나의 페이지를 렌더링 하는 동안에 중복된 API 요청을 캐싱하기 위함
- Next JS 서버에서 처리되는 단일 요청 동안에만 발생
- 렌더링이 종료되면 모든 캐시가 소멸됨

### Data Cache

- fetch 메서드를 활용해 불러온 데이터를 Next 서버에 보관하는 기능
- 데이터 소스에서 변경되지 않은 경우, 데이터를 저장하고 재사용
- 데이터가 변경되지 않는 한, 데이터 소스로의 불필요한 요청을 방지함으로써 애플리케이션 속도를 더 빠르게 함
- 사용자가 수동으로 재검증 할 때 까지 혹은 사용자가 설정한 특정 시간이 지나면 지속됨
- 옵션
    - `no-store`
        - 데이터 페칭의 결과를 저장하지 않는 옵션
        - 캐싱을 아예 하지 않도록 설정하는 옵션
    - `force-cache`
        - 요청의 결과를 무조건 캐싱
        - 한 번 호출 된 이후에는 다시는 호출되지 않음
    - `revalidate`
        - 특정 시간을 주기로 캐시를 업데이트
        - ≒ ISR(Page Router)
    - `tags`
        - On-Demand Revalidate
        - 요청이 들어왔을 때 데이터를 최신화 함

### Full Route Cache

- Static Page에서만 적용 가능
- Next 서버측에서 빌드 타임에 특정 페이지의 렌더링 결과를 캐싱하는 기능
- 페이지에서 사용될 수 있는 데이터를 캐싱/저장/재사용 할 뿐만 아니라 전체 페이지/HTML 코드 및 React 서버 컴포넌트 페이로드를 내부적으로 관리
- 전체 HTML 페이지가 리렌더링 되는 것을 방지
    - 기존 페이지를 재사용할 수 있기 때문에 페이지 더 빠르게 만듦
- 데이터 캐시가 재검증 될 때 까지 지속됨
    - 업데이트 된 데이터가 있으면 페이지가 리렌더링
- 동적 경로에 적용하는 방법
    - `generateStaticParams`(≒ `getStaticProps`) 사용
        
        ```tsx
        export function generateStaticParams() {
          return [{ id: '1' }, { id: '2' }, { id: '3' }];
        }
        ```
        
- 참고
    - Dynamic Page로 설정되는 기준
        - 특정 페이지가 접속 요청을 받을 때 마다 매번 변화가 생기거나, 데이터가 달라질 경우
        1. 캐시되지 않는 Data Fetching을 사용할 경우
        2. 동적 함수(쿠키, 헤더, 쿼리스트링)을 사용하는 컴포넌트가 있을 때

### Router Cache

- 브라우저의 메모리에 일부 React 서버 컴포넌트 페이로드를 저장하여 페이지 간의 이동이 더 빠르게 일어날 수 있도록 함
- 캐시된 페이지를 가져오기 위해 NextJS 서버에 요청을 보낼 때, 요청을 더 빠르게 처리하거나 페이지 데이터가 클라이언트 측에서 이미 관리되고 있는 경우 요청 자체를 방지할 수 있도록 함
- 서버에 의해 새로운 페이지가 렌더링되거나 웹 사이트를 벗어났다가 다시 돌아올 때 무효화 됨

## NextJS 앱 최적화

- [참고](https://nextjs-ko.org/docs/app/building-your-application/optimizing)

### Image

- <img> 요소를 확장하여 자동 이미지 최적화 기능을 제공
    - 크기 최적화
    - 시각적 안정성
    - 빠른 페이지 로드
    - Asset 유연성
- `loaders`
    - 이미지의 URL을 생성하는 함수
    - 제공된 src를 수정하여 이미지를 다른 크기로 요청하는 여러 URL을 생성
- `priority`
    - 각 페이지의 Larget Contentful Pain 요소가 될 이미지에 추가하는 속성
    - 이미지를 로드할 때 특별히 우선시하여 LCP를 의미 있게 향상 시킬 수 있음

### Metadata

- 정적 메타데이터 설정
    
    ```jsx
    export const metadata = {
      title: 'Latest Posts',
      description: 'Browse our latest posts!',
    };
    
    ...
    
    export default async function Home() {
      return (
        ...
      );
    }
    ```
    
- 동적 메타데이터 설정
    
    ```jsx
    import { getPosts } from '@/lib/posts';
    
    export async function generateMetadata() {
      const posts = await getPosts();
      const numberOfPosts = posts.length;
      return {
        title: `Browse all our ${numberOfPosts} posts.`,
        description: 'Browse all our posts.',
      };
    }
    
    export default async function FeedPage() {
      ...
    }
    ```
    
- 레이아웃 메타데이터 설정
    - metadata가 설정되어 있는 페이지는 레이아웃의 메타데이터와 병합되고 설정되어 있지 않은 페이지는 레이아웃 메타데이터로 설정됨

## 사용자 인증(Authentication)

### 사용자 인증 방식

1. 사용자 로그인
    - 클라이언트(사용자)는 서버에 credential 정보(아이디 + 비밀번호)를 전송
    - 서버는 credential 정보가 유효한지 확인
    - 인증 세션을 발급하고 저장
    - 세션 ID를 쿠키 형태로 사용자에게 다시 전송
    - 클라이언트 측에서도 세션 쿠키를 저장
2. 보호된 리소스에 접근
    - 클라이언트 측에서 보호되어야 하는 경로에 요청을 보냄
        - 이때, 저장되어 있던 세션 쿠키를 자동으로 요청에 추가하여 전송
    - 서버는 쿠키의 유효성을 확인
        - 쿠키가 유효하다면 요청 받은 리소스를 클라이언트로 전송
        - 유효하지 않다면 에러를 전송

### [Lucia Auth](https://lucia-auth.com/) 사용하여 인증 구현

>[!NOTE]
>`@lucia-auth/adapter-sqlite` 설치할 때, `better-sqlite3` 버전 충돌 나면 node 버전을 20으로 다운그레이드 하면 된다(nvm 사용)

- Lucia 인증 인스턴스 생성
    
    ```jsx
    import { Lucia } from 'lucia';
    import { BetterSqlite3Adapter } from '@lucia-auth/adapter-sqlite';
    import db from './db';
    
    const adapter = new BetterSqlite3Adapter(db, {
      user: 'users',
      session: 'sessions',
    });
    
    const lucia = new Lucia(adapter, {
      sessionCookie: {
        expires: false,
        attributes: {
          secure: process.env.NODE_ENV === 'production',
        },
      },
    });
    ```
    
- 세션 및 세션 쿠키 생성 및 저장
    - `next/headers`의 `cookies` 로 세션 쿠키를 저장
    
    ```jsx
    export async function createAuthSession(userId) {
      const session = await lucia.createSession(userId, {});
      const sessionCookie = lucia.createSessionCookie(session.id);
      cookies().set(
        sessionCookie.name,
        sessionCookie.value,
        sessionCookie.attributes,
      );
    }
    ```
    
- 활성 인증 세션 확인
    
    ```jsx
    export async function verifyAuth() {
      const sessionCookie = cookies().get(lucia.sessionCookieName);
    
      if (!sessionCookie) {
        return {
          user: null,
          session: null,
        };
      }
    
      const sessionId = sessionCookie.value;
    
      if (!sessionId) {
        return {
          user: null,
          session: null,
        };
      }
    
      const result = await lucia.validateSession(sessionId);
    
      try {
        if (result.session && result.session.fresh) {
          const sessionCookie = lucia.createSessionCookie(result.session.id);
          cookies().set(
            sessionCookie.name,
            sessionCookie.value,
            sessionCookie.attributes,
          );
        }
    
        if (!result.session) {
          const sessionCookie = lucia.createBlankSessionCookie();
          cookies().set(
            sessionCookie.name,
            sessionCookie.value,
            sessionCookie.attributes,
          );
        }
      } catch (error) {}
    
      return result;
    }
    ```
    
- 로그인 액션 추가
    - email 기반으로 유저 정보 가져오기
        
        ```jsx
        export function getUserByEmail(email) {
          return db.prepare('SELECT * FROM users WHERE email = ?').get(email);
        }
        ```
        
    - 가져온 유저 정보와 사용자가 입력한 formData를 대조하여 올바른 정보인지 확인
        
        ```jsx
        export async function login(prevState, formData) {
          const email = formData.get('email');
          const password = formData.get('password');
        
          const existingUser = getUserByEmail(email);
        
          if (!existingUser) {
            return {
              errors: {
                email: 'Could not authenticate user, please check your credentials.',
              },
            };
          }
        
          const isValidPassword = verifyPassword(existingUser.password, password);
        
          if (!isValidPassword) {
            return {
              errors: {
                password: 'Could not authenticate user, please check your credentials.',
              },
            };
          }
        
          await createAuthSession(existingUser.id);
          redirect('/training');
        }
        ```

## 페이지 & 파일 기반 라우팅

### 파일 기반 라우팅

- 설정된 폴더 구조로부터 프로젝트의 라우트를 도출하는 라우팅 방식
    - /pages
        - index.js ⇒ (’/’ 시작 페이지)
        - about.js ⇒ (’/about’)
        - /products
            - index.js ⇒ (’/products’)
            - [id].js ⇒ (’/products/:id’)

### 동적 경로 세그먼트 데이터 추출하기

- `next/router`의 `useRouter` 훅을 사용하여 router 정보(pathname, query 등)를 가져올 수 있음
- `router.query` 속성을 통해 세그먼트 데이터를 가져올 수 있음
    - 예) [projectId].js 페이지에서 router.query.projectId로 값을 가져올 수 있음

### 중첩된 동적 라우트 & 경로 구축

![image.png](https://github.com/user-attachments/assets/24df77b0-7d15-4cda-b5ef-8e0eba445a4a)

- `/clients/1/2` 페이지에서 useRouter를 통해 query 값을 가져오면 id, clientProejctId 값을 모두 가져올 수 있음
    
    ```json
    {
    	id: '1', 
    	clientProjectId: '2'
    }
    ```
    

### Catch-All 라우트

![image.png](https://github.com/user-attachments/assets/bc112cff-4c2d-41b3-a072-35e22a2a6f1c)

- 파일명을 대괄호 안에 줄임표를 추가하여 […name].js 으로 명명하면 모든 후속 세그먼트를 포괄하도록 확장 가능
- useRouter를 통해 query 값을 가져오면 ‘/’를 구분자로 split 한 배열로 모든 query 값을 가져올 수 있음
    
    ```json
    slug: ['2020', '12']
    ```
    

### Link

- `next/link`의 `Link`를 통해 페이지 이동 가능
    - `<a>` 태그는 페이지 이동 시, 전체 페이지를 로드하는 반면, Link는 부분적인 업데이트
- 동적 라우팅 시, href 설정 방법
    - 이동할 페이지 url 문자열로 입력
    - pathname, query 로 이루어진 URL 객체 형태로 설정

## 페이지 사전 렌더링 & 데이터 페칭(페이지 라우터)

### 사전 렌더링(Pre Rendering)

- 브라우저의 요청에 사전에 렌더링이 완료된 HTML을 응답하는 렌더링 방식
- Client Side Rendering의 단점을 효율적으로 해결하는 기술
    - **`CSR(Client Side Rendering)`**
        - React.js 앱의 기본적인 렌더링 방식
        - 클라이언트(브라우저)에서 직접 화면을 렌더링 하는 방식
        - <mark>페이지 이동이 매우 빠르고 쾌적</mark>
        - <mark>FCP(초기 접속 속도)가 느림</mark>

#### 과정

  1. 서버가 서버측에서 JS를 실행하여 모든 React 컴포넌트들을 HTML로 변환(사전 렌더링)
  2. 렌더링 된 HTML을 브라우저로 전송
  3. 전달 받은 HTML 파일을 화면에 렌더링
      - 사용자 측에서 바로 화면이 보임
          ⇒ FCP 단축
      - 사용자 인터랙션 불가능
  4. 서버가 React 앱을 JS로 번들링하여 브라우저로 전송
  5. 서버로부터 받은 JS 코드를 실행하여 HTML 요소들과 연결(Hydration)
      - 사용자 인터랙션 가능
  6. 페이지 이동 요청이 들어오면 JS 실행(컴포넌트 교체)하여 페이지를 교체하여 클라이언트에게 보여줄 수 있음(CSR 방식)

  <mark>**⇒ 빠른 FCP 달성 + 빠른 페이지 이동**</mark>

### 정적 생성(getStaticProps / getStaticPaths)

- 빌드하는 동안 페이지 사전 생성
    - <u>최신 데이터 반영은 어려움</u>
- 사전 생성된 페이지는 서버나 앱을 실행시키는 CDN을 통해 캐시로 저장됨
- pages 폴더의 내의 컴포넌트에서 특수 비동기 함수 `getStaticProps` 를 통해 가져올 수 있음
    - 클라이언트는 볼 수 없는 코드
- `getStaticProps`
    - 페이지 **컨텐츠**가 외부 데이터에 연동될 때 주로 사용
    
    ```jsx
    import path from 'path';
    import fs from 'fs/promises';
    import { redirect } from 'next/dist/server/api-utils';
    
    function HomePage(props) {
      const { products } = props;
    
      return (
        <ul>
          {products.map((product) => (
            <li key={product.id}>{product.title}</li>
          ))}
        </ul>
      );
    }
    
    export async function getStaticProps() {
      const filePath = path.join(process.cwd(), 'data', 'dummy-backend.json');
      const jsonData = await fs.readFile(filePath);
      const data = JSON.parse(jsonData);
    
      if (!data) {
        return {
          redirect: {
            destination: '/no-data',
          },
        };
      }
    
      if (data.products.length === 0) {
        return { notFound: true };
      }
    
      return {
        props: {
          products: data.products,
        },
      };
    }
    
    export default HomePage;
    
    ```
    
- `getStaticPaths`
    - 페이지 **경로**가 외부데이터에 연동될 때 주로 사용
    - `fallback` (없는 경로로 요청시 옵션)
        - false ⇒ 404 Not Found 반환
        - blocking ⇒ 즉시 생성 (≒SSR)
        - true ⇒ props 없는 페이지만 미리 반환 + 즉시 생성 + props 따로 반환
    
    ```jsx
    export async function getStaticPaths() {
      return {
        paths: [
          { params: { pid: 'p1' } },
          { params: { pid: 'p2' } },
          { params: { pid: 'p3' } },
        ],
        fallback: false,
      };
    }
    
    ```
    
### 증분 정적 재생성(ISR, Incremental Static Regeneration)

- SSG 방식으로 생성된 정적 페이지를 일정 시간을 주기로 다시 생성하는 기술
- `getStaticProps` 반환값에 revalidate를 설정하여 데이터의 유효기간 설정
    
    ```tsx
    export const getStaticProps = async () => {
      const [allBooks, recoBooks] = await Promise.all([
        fetchBooks(),
        fetchRandomBooks(),
      ]);
    
      return {
        props: {
          allBooks,
          recoBooks,
        },
        revalidate: 3,
      };
    };
    ```
    

#### `주문형 재검증(On-Demand ISR)`

- 요청을 받을 때 마다 페이지를 다시 생성하는 기술
    - 시간과 관계없이 사용자의 행동에 따라 데이터가 업데이트 되는 페이지(사건 기반 -  게시글 수정/삭제)는 ISR을 적용하기 어렵기 때문에 요청에 따라 재생성되도록 함
- 데이터 revalidate할 API route handler 함수를 설정하고, 실행해보면 api 요청이 들어올 때 마다 페이지가 재생성 되는 것을 알 수 있음
    
    ```tsx
    import { NextApiRequest, NextApiResponse } from 'next';
    
    export default async function handler(
      req: NextApiRequest,
      res: NextApiResponse,
    ) {
      try {
        await res.revalidate('/');
        return res.json({ revalidate: true });
      } catch (err) {
        console.error(err);
        res.status(500).send('Revalidation Failed');
      }
    }
    
    ```

### 서버사이드 렌더링(SSR)
- 가장 기본적인 사전 렌더링 방식
- 요청이 들어올 때 마다 사전 렌더링을 진행
- `getServerSideProps`
    - 모든 요청에 대한 페이지를 사전 렌더링하거나 서버에 도달하는 특정 요청 객체(예: 쿠키)에 접근할 필요가 있을 때 사용
    - getStaticProps와 함께 사용할 수 없음. 둘 중 하나만 사용해야 함.
    - 동적 페이지에서 context를 통해 params, res, req를 가져올 수 있음
        - getStaticPaths를 사용할 필요 없음
        
        ```jsx
        function UserIdPage(props) {
          return <h1>{props.id}</h1>;
        }
        
        export default UserIdPage;
        
        export async function getServerSideProps(context) {
          const { params } = context;
        
          const userId = params.uid;
        
          return {
            props: {
              id: 'userid-' + userId,
            },
          };
        }
        
        ```
    - getServerSide에서 미리 받아온 데이터를 prop으로 받을 때, 타입은 `InferGetServerSidePropsType`을 사용하여 지정
    
        ```tsx
        export default function Home({
          data,
        }: InferGetServerSidePropsType<typeof getServerSideProps>) {
          console.log(data);
        
          return (
            ...
          );
        }
        ```

### Client-side 데이터 페칭

- 사용하는 경우
    - 갱신 주기가 잦은 데이터(예: 주가 데이터)
    - 특정 유저에만 한정되는 데이터(예: 최근 주문 내역)
    - 데이터의 일부분만 표시하는 경우(예: 대시보드)
    
    ```jsx
    useEffect(() => {
        setIsLoading(true);
        fetch('api url')
          .then((res) => res.json())
          .then((data) => {
            const transformedSales = [];
    
            for (const key in data) {
              transformedSales.push({
                id: key,
                username: data[key].username,
                volume: data[key].volume,
              });
            }
    
            setSales(transformedSales);
            setIsLoading(false);
          });
      }, []);
    
    ```
    
- [`useSWR(Stale While Revalidate)`](https://swr.vercel.app/ko)
    - 캐시된 데이터(Stale)를 우선적으로 사용하면서 fetch 요청(revalidate)을 하고, 최종적으로 최신화된 데이터를 가져오는 방식
    - HTTP 요청을 보낼 때, fetch 코드를 간결히 사용할 수 있음
    - 로컬 캐싱을 통해 데이터를 빠르게 로딩
    - 데이터 가져오기를 실패하는 경우에 자동으로 재시도 요청
    
    ```jsx
    const { data, error } = useSWR(
        'api url',
        (url) => fetch(url).then((res) => res.json()),
      );
    ```

## API 라우트(페이지 라우터)

>[!NOTE]
>클라이언트 사이드에서 서버에서 데이터를 사져와야 할 때 사용
>`getStaticProps`/`getServerSideProps`에서는 API route를 거치지 않음
>=> 결국 같은 서버 안에서 실행되기 때문에 직접 접근하는 것이 더 효율적

### API Route란?

- 특수한 형태의 URL으로 Next.js 앱에 추가하여 데이터를 수집/사용하고 데이터베이스에 저장한 뒤 원하는 형태의 데이터를 반환하는 역할
- API를 구축하여 REST API 같은 API를 Next.js 앱에 포함함으로써 도메인 뒤에 붙는 URL이나 경로를 통해 여러 가지 HTTP 요청을 받을 수 있게 해주는 역할
- pages 폴더 안에 api 라는 이름의 폴더로 지정하여 작성해야 함
    
    ```jsx
    import fs from 'fs';
    import path from 'path';
    
    function buildFeedbackPath() {
      return path.join(process.cwd(), 'data', 'feedback.json');
    }
    
    function extractFeedback(filePath) {
      const fileData = fs.readFileSync(filePath);
      const data = JSON.parse(fileData);
      return data;
    }
    
    function handler(req, res) {
      if (req.method === 'POST') {
        const email = req.body.email;
        const feedbackText = req.body.text;
    
        const newFeedback = {
          id: new Date().toISOString(),
          email,
          text: feedbackText,
        };
    
        const filePath = buildFeedbackPath();
        const data = extractFeedback(filePath);
        data.push(newFeedback);
        fs.writeFileSync(filePath, JSON.stringify(data));
    
        res.status(201).json({ message: 'Success!', feedback: newFeedback });
      } else {
        const filePath = buildFeedbackPath();
        const data = extractFeedback(filePath);
        res.status(200).json({ feedback: data });
      }
    }
    export default handler;
    ```
    
- 컴포넌트 내에서 fetch(’/api/feedback’)과 같이 요청하면 서버측에서 CRUD 가능(클라이언트에 데이터 저장 로직 노출 X)