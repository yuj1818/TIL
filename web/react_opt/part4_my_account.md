# React 최적화 Part4 - 금융 서비스

## Next 프로젝트 생성 및 환경 설정

### 프로젝트 생성

[Next 공식 문서](https://nextjs.org/docs/app/getting-started/installation)

```bash
npx create-next-app@latest
```

### 프로젝트 설정

- eslint, prettier 설정
    
    >[!WARNING]
    >설정 후에 꼭 `yarn dlx @yarnpkg/sdks vscode` 실행
    
    ```jsx
    // eslint.config.mjs
    import { dirname } from "path";
    import { fileURLToPath } from "url";
    import { FlatCompat } from "@eslint/eslintrc";
    import prettierPlugin from "eslint-plugin-prettier";
    
    const __filename = fileURLToPath(import.meta.url);
    const __dirname = dirname(__filename);
    
    const compat = new FlatCompat({
      baseDirectory: __dirname,
    });
    
    const eslintConfig = [
      ...compat.extends("next/core-web-vitals", "next/typescript", "plugin:prettier/recommended"),
      {
        plugins: {
          prettier: prettierPlugin,
        },
        rules: {
          "prettier/prettier": "error"
        }
      }
    ];
    
    export default eslintConfig;
    ```
    
    ```json
    // .prettierrc
    {
      "useTabs": false,
      "printWidth": 80,
      "tabWidth": 2,
      "singleQuote": true,
      "trailingComma": "all",
      "endOfLine": "lf",
      "semi": true,
      "arrowParens": "always"
    }
    ```
    

### Emotion 설정

- `@emotion/react` `@emotion/styled` 라이브러리 설치
- `.babelrc` 설정 (Next 15 버전에서는 이제 설정 따로 안 해도 됨)
    
    ```json
    // .babelrc
    {
      "presets": [
        [
          "next/babel",
          {
            "preset-react": {
              "runtime": "automatic",
              "importSource": "@emotion/react"
            }
          }
        ]
      ]
    }
    ```
    
- `tsconfig.json` 설정
    
    ```json
    {
      "compilerOptions": {
        "target": "ES2017",
        "lib": ["dom", "dom.iterable", "esnext"],
        "allowJs": true,
        "skipLibCheck": true,
        "strict": true,
        "noEmit": true,
        "esModuleInterop": true,
        "module": "esnext",
        "moduleResolution": "bundler",
        "resolveJsonModule": true,
        "isolatedModules": true,
        "jsx": "preserve",
        "incremental": true,
        "paths": {
          "@/*": ["./src/*"]
        },
        **"jsxImportSource": "@emotion/react"**
      },
      "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx"],
      "exclude": ["node_modules"]
    }
    
    ```
    

### path alias 설정

```json
{
  "compilerOptions": {
    "target": "ES2017",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "baseUrl": ".",
    **"paths": {
      "@/*": ["src/*"],
      "@components/*": ["src/components/*"],
      "@shared/*": ["src/components/shared/*"],
      "@styles/*": ["src/styles/*"],
      "@pages/*": ["src/pages/*"]
    },**
    "jsxImportSource": "@emotion/react"
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx"],
  "exclude": ["node_modules"]
}

```

### firebase 설정

- `.env` 설정
    - react 프로젝트에서 사용했던 `REACT_APP` 대신 `NEXT_PUBLIC`으로 변경
    
    ```tsx
    import { initializeApp, getApp, getApps } from 'firebase/app';
    import { getAuth } from 'firebase/auth';
    import { getFirestore } from 'firebase/firestore';
    
    const firebaseConfig = {
      apiKey: process.env.NEXT_PUBLIC_API_KEY,
      authDomain: process.env.NEXT_PUBLIC_AUTH_DOMAIN,
      projectId: process.env.NEXT_PUBLIC_PROJECT_ID,
      storageBucket: process.env.NEXT_PUBLIC_STORAGE_BUCKET,
      messagingSenderId: process.env.NEXT_PUBLIC_MESSAGING_SENDER_ID,
      appId: process.env.NEXT_PUBLIC_APP_ID,
      measurementId: process.env.NEXT_PUBLIC_MEASUREMENT_ID,
    };
    
    const app = getApps().length > 0 ? getApp() : initializeApp(firebaseConfig);
    
    export const auth = getAuth(app);
    export const store = getFirestore(app);
    
    ```
    

## 이벤트 배너 데이터 생성 및 디스플레이

### 데이터 생성

- mock 데이터 준비하여 firestore에 저장
    
    ```tsx
    import { collection, writeBatch, doc } from 'firebase/firestore';
    import { store } from '@remote/firebase';
    import Button from '@shared/Button';
    import { EVENT_BANNERS } from '@/mock/banner';
    import { COLLECTIONS } from '@constants/collection';
    
    function EventBannerAddButton() {
      const handleButtonClick = async () => {
        const batch = writeBatch(store);
    
        EVENT_BANNERS.forEach((banner) => {
          const bannerRef = doc(collection(store, COLLECTIONS.EVENT_BANNER));
    
          batch.set(bannerRef, banner);
        });
    
        await batch.commit();
    
        alert('배너 데이터가 추가되었습니다.');
      };
    
      return <Button onClick={handleButtonClick}>이벤트 배너 데이터 추가</Button>;
    }
    export default EventBannerAddButton;
    
    ```
    

### Lazy Loading

- `Suspense`, `lazy` 대신 `dynamic` 사용
    - `loading`
        - fallback 처럼 로딩 중에 보여 줄 컴포넌트 설정
    - `ssr`
        - 서버 사이드 렌더링을 할 건지 말 건지에 대한 여부 판단
    
    ```tsx
    import dynamic from 'next/dynamic';
    
    const EventBanners = dynamic(() => import('@components/home/EventBanners'), {
      loading: () => <div>Loading...</div>,
      ssr: false
    });
    ```
    

## Page Router(Next.js)

- `pages` 폴더 안의 **파일 및 폴더 구조에 따라 자동으로 라우팅**을 설정
    - pages/index.tsx ⇒ /
    - pages/card/index.tsx ⇒ /card
    - pages/card/[id].tsx ⇒ /card/:id

### 페이지 이동

- `react-router-dom` 대신 `next/router`의 `useRouter` 사용
    - navigate.push(’/경로’)
    
    ```tsx
    import { useRouter } from 'next/router';
    
    function CardList() {
    	const navigate = useRouter();
    	
    	...
    	
    	return (
    		...
    		<Button
          full={true}
          weak={true}
          size="medium"
          onClick={() => {
            **navigate.push('/card');**
          }}
        >
          더보기
        </Button>
    	)
    }
    ```
    

## react-query + SSR 카드 리스트

- server 측에서 데이터를 먼저 받아오고, `_app.tsx`가 실행됨
- card 목록을 `prefetchInfiniteQuery`로 가져와 app의 pageProps에 넘기기
    
    ```tsx
    import { dehydrate, QueryClient } from 'react-query';
    import { getCards } from '@remote/card';
    
    function CardListPage() {
      return <div>카드 리스트 페이지</div>;
    }
    
    export async function getServerSideProps() {
      console.log('getServerSideProps');
    
      const client = new QueryClient();
    
      await client.prefetchInfiniteQuery(['cards'], () => getCards());
    
      return {
        props: {
          dehydratedState: JON.parse(JSON.stringify(dehydrate(client))),
        },
      };
    }
    ```
    
- `_app.tsx`에서는 `Hydrate`로 state에 pageProps로 받은를 넘기기
    
    ```tsx
    import { QueryClientProvider, QueryClient, Hydrate } from 'react-query';
    ...
    
    const client = new QueryClient({});
    
    export default function App({
      Component,
      pageProps: { dehydratedState, ...pageProps },
    }: AppProps) {
      return (
        <Layout>
          <Global styles={globalStyles} />
          <QueryClientProvider client={client}>
            <Hydrate state={dehydratedState}>
              <Component {...pageProps} />
            </Hydrate>
          </QueryClientProvider>
        </Layout>
      );
    }
    ```
    
- useInfiniteQuery 사용하여 무한 스크롤 기능 구현
    
    ```
    import { dehydrate, QueryClient, useInfiniteQuery } from 'react-query';
    import { getCards } from '@remote/card';
    import InfiniteScroll from 'react-infinite-scroll-component';
    import { useCallback } from 'react';
    import { useRouter } from 'next/router';
    import ListRow from '@shared/ListRow';
    import Badge from '@shared/Badge';
    
    function CardListPage() {
      const navigate = useRouter();
      const {
        data,
        hasNextPage = false,
        fetchNextPage,
        isFetching,
      } = useInfiniteQuery(['cards'], ({ pageParam }) => getCards(pageParam), {
        getNextPageParam: (snapshot) => {
          return snapshot.lastVisible;
        },
      });
    
      const loadMore = useCallback(() => {
        if (hasNextPage === false || isFetching) {
          return;
        }
    
        fetchNextPage();
      }, [hasNextPage, fetchNextPage, isFetching]);
    
      if (data == null) {
        return null;
      }
    
      const cards = data?.pages.map(({ items }) => items).flat();
    
      return (
        <div>
          <InfiniteScroll
            dataLength={cards.length}
            hasMore={hasNextPage}
            loader={<ListRow.Skeleton />}
            next={loadMore}
            scrollThreshold="100px"
          >
            <ul>
              {cards.map((card, index) => (
                <ListRow
                  key={card.id}
                  contents={
                    <ListRow.Texts title={`${index + 1}위`} subTitle={card.name} />
                  }
                  right={
                    card.payback != null ? <Badge label={card.payback} /> : null
                  }
                  withArrow={true}
                  onClick={() => {
                    navigate.push(`/card/${card.id}`);
                  }}
                />
              ))}
            </ul>
          </InfiniteScroll>
        </div>
      );
    }
    
    export async function getServerSideProps() {
      console.log('getServerSideProps');
    
      const client = new QueryClient();
    
      await client.prefetchInfiniteQuery(['cards'], () => getCards());
    
      return {
        props: {
          dehydratedState: JSON.parse(JSON.stringify(dehydrate(client))),
        },
      };
    }
    
    export default CardListPage;
    
    ```
    

## 카드 검색 기능(Debounce)

- 검색 키워드로 시작하는 모든 카드를 검색 결과로 반환하는 쿼리문
    
    ```tsx
    export async function getSearchCards(keyword: string) {
      // 키워드로 시작하는 모든 카드를 찾기
      const searchQuery = query(
        collection(store, COLLECTIONS.CARD),
        where('name', '>=', keyword),
        where('name', '<=', keyword + '\uf8ff'),
      );
    
      const cardSnapshot = await getDocs(searchQuery);
    
      return cardSnapshot.docs.map((doc) => ({
        id: doc.id,
        ...(doc.data() as Card),
      }));
    }
    ```
    

### Debounce

- 여러가지 액션이 일어날 때, 마지막 액션을 캐치해서 일정한 시간이 지난 후에 액션을 실행해주는 역할
- input 값이 바뀔 때 마다 검색을 하면 효율적이지 않으므로 디바운싱하여 마지막 keyword만 검색하도록 최적화
- 커스텀 훅 `useDebounce` 구현
    
    ```tsx
    import { useEffect, useState } from 'react';
    function useDebounce<T = any>(value: T, delay = 800) {
      const [debouncedValue, setDebouncedValue] = useState<T>(value);
    
      useEffect(() => {
        const timeout = setTimeout(() => {
          setDebouncedValue(value);
        }, delay);
    
    		// 실행하는 중에 value가 바뀌면 clear하고 다시 실행
        return () => {
          clearTimeout(timeout);
        };
      }, [delay, value]);
    
      return debouncedValue;
    }
    
    export default useDebounce;
    ```
    
- debouncedKeyword 사용하여 검색 실행
    
    ```tsx
    const [keyword, setKeyword] = useState('');
    const debouncedKeyword = useDebounce(keyword);
    const { data } = useQuery(
      ['cards', debouncedKeyword],
      () => getSearchCards(debouncedKeyword),
      {
        enabled: debouncedKeyword !== '',
      },
    );
    ```
    

## 카드 상세 정보

### getServerSideProps 함수에서 cardId 값 가져오기

- context에서 query 값 가져와서 id 추출 가능
- id 값 사용하여 서버 사이드로 카드 상세 데이터를 미리 받아올 수 있음

```tsx
export async function getServerSideProps(context: GetServerSidePropsContext) {
  const { query } = context;
  const cardId = query.id as string;

  const card = await getCard(cardId);

  return {
    props: {
      initialCard: card,
    },
  };
}
```

### 카드 상세 정보 불러오기

- `next/navigation`의 `useParams` 사용하여 cardId 값 가져오기
    - initialData에 서버 사이드로 받아 온 initialCard 값을 넣어주면 처음부터 데이터가 비어있지 않게 됨
    
    ```tsx
    function CardDetailPage({ initialCard }: CardDetailPageProps) {
      const { id } = useParams();
    
      const { data } = useQuery(['card'], () => getCard(id as string), {
        **initialData: initialCard**,
      });
    
      ...
    }
    ```
    

### portal에 컴포넌트 띄우는 방법

- 서버 사이드 렌더링 단계에서 window에 접근하는 것이 불가능해서 portal에 띄우는 컴포넌트에서 에러 발생
- `dynamic` 사용하여 클라이언트 사이드 렌더링 될 때만 FixedBottomButton이 생기게 만들고, `_document.tsx`에 portal 추가
    
    ```tsx
    const FixedBottomButton = dynamic(() => import('@shared/FixedBottomButton'), {
      ssr: false,
    });
    ```
    
    ```tsx
    import { Html, Head, Main, NextScript } from 'next/document';
    
    export default function Document() {
      return (
        <Html lang="en">
          <Head>
            <link rel="icon" href="/favicon.ico" />
          </Head>
          <body>
            <Main />
            <NextScript />
            **<div id="root-portal" />**
          </body>
        </Html>
      );
    }
    ```

## Next Auth 인증

### [NextAuth.js](https://next-auth.js.org/)

- Next.js 애플리케이션을 위한 인증 및 세션 관리 라이브러리
    - next 환경에서 회원 데이터를 손쉽게 관리할 수 있도록 하는 라이브러리
- Apple, FaceBook, Google, Email 인증 방식 지원

### 구글 로그인 설정

- pages/api/auth/[…nextauth].tsx 에서 로그인 Provider 설정
    - 구글 API 서비스에서 클라이언트 생성하여 클라이언트 ID, secret `.env`에 설정
    - 어떤 Provider를 사용할 것인지와 callback 함수 설정 가능
    
    ```tsx
    import NextAuth from 'next-auth';
    import GoogleProvider from 'next-auth/providers/google';
    import { User } from '@models/user';
    
    export default NextAuth({
      providers: [
        GoogleProvider({
          clientId: process.env.GOOGLE_ID as string,
          clientSecret: process.env.GOOGLE_SECRET as string,
        }),
      ],
      callbacks: {
        session({ session, token }) {
          console.log('session', session);
          console.log('token', token);
    
          if (session.user) {
            (session.user as User).id = token.sub as string;
          }
    
          return session;
        },
      },
      session: {
        strategy: 'jwt',
      },
      pages: {
        signIn: '/auth/signin',
      },
    });
    ```
    
- _app.tsx에서 SessionProvider로 감싸줘야 사용 가능
    
    ```
    import type { AppProps } from 'next/app';
    import { SessionProvider } from 'next-auth/react';
    import { Global } from '@emotion/react';
    import { QueryClientProvider, QueryClient, Hydrate } from 'react-query';
    import globalStyles from '@styles/globalStyles';
    import Layout from '@shared/Layout';
    
    const client = new QueryClient({});
    
    export default function App({
      Component,
      pageProps: { dehydratedState, session, ...pageProps },
    }: AppProps) {
      return (
        <Layout>
          <Global styles={globalStyles} />
          <SessionProvider session={session}>
            <QueryClientProvider client={client}>
              <Hydrate state={dehydratedState}>
                <Component {...pageProps} />
              </Hydrate>
            </QueryClientProvider>
          </SessionProvider>
        </Layout>
      );
    }
    ```
    
- providers를 서버 사이드로 미리 받아와서 유동적으로 설정한 Provider에 맞게 로그인 버튼을 생성할 수 있음
    - `next-auth/react`의 `signIn` 함수를 onClick 함수와 연결하면 손쉽게 소셜 로그인 기능을 구현할 수 있음.
    - 로그인한 사용자의 정보는 cookie session에 저장됨
    
    ```tsx
    import { BuiltInProviderType } from 'next-auth/providers/index';
    import {
      ClientSafeProvider,
      getProviders,
      LiteralUnion,
      signIn,
    } from 'next-auth/react';
    import Flex from '@shared/Flex';
    import Text from '@shared/Text';
    import Button from '@shared/Button';
    import Spacing from '@shared/Spacing';
    
    function SigninPage({
      providers,
    }: {
      providers: Record<LiteralUnion<BuiltInProviderType>, ClientSafeProvider>;
    }) {
      return (
        <div>
          <Spacing size={100} />
          <Flex direction="column" align="center">
            <Text bold={true}>My Account</Text>
            <Spacing size={80} />
            <ul>
              {Object.values(providers).map((provider) => (
                <li key={provider.id}>
                  <Button onClick={() => signIn(provider.id, { callbackUrl: '/' })}>
                    {provider.name} LOGIN
                  </Button>
                </li>
              ))}
            </ul>
          </Flex>
        </div>
      );
    }
    
    export async function getServerSideProps() {
      const providers = await getProviders();
    
      return {
        props: {
          providers,
        },
      };
    }
    
    export default SigninPage;
    ```
    

### withAuth hoc 컴포넌트로 인증 여부에 따라서 강제 페이지 이동

- window.redirect 대신 useRouter의 replace 를 사용하여 인증이 필요한 페이지에 인증이 안 된 상태로 접근하면 강제로 로그인 페이지로 이동
    
    ```tsx
    import { ComponentType } from 'react';
    import { useSession } from 'next-auth/react';
    import { useRouter } from 'next/router';
    
    function withAuth<Props = Record<string, never>>(
      WrappedComponent: ComponentType<Props>,
    ) {
      return function AuthenticatedComponent(props: Props) {
        const { data, status } = useSession();
        const router = useRouter();
    
        if (status !== 'loading' && data == null) {
          router.replace('/auth/signin');
    
          return null;
        }
    
        return <WrappedComponent {...(props as any)} />;
      };
    }
    
    export default withAuth;
    ```

## CSR, SSR, SSG

### CSR(Client Side Rendering)

- 서버 측에서 HTML, JS 파일을 클라이언트로 전송하여 클라이언트 측에서 JS 파일을 다운로드 받아 화면을 그리는 방식
- 첫 페이지 렌더링 후 후속 탐색이 빠름
    - 페이지 이동 시, 전체 HTML을 다시 로드하지 않기 때문
    - 변경이 필요한 데이터의 경우는 필요한 데이터만 서버로 요청하여 화면 갱신
- 검색 엔진 최적화 대응이 어려움
    - 초기 HTML에 모든 컨텐츠가 포함되어 있지 않아서 SEO 어려움

### SSR(Server Side Rendering)

- 최초의 사용자에게 보여줄 페이지를 서버 측에서 생성하여 클라이언트로 전송
- Layout Shift 줄일 수 있음
- 최초 페이지 진입이 상황에 따라 빠를 수 있음
    - 서버 작업이 지연되는 경우에는 그렇지 않음
- 검색 엔진 최적화에 용이
- 보안에 유리
    - 인증이나 민감한 작업들을 서버 측에서 수행하고, 결과만 클라이언트에 전송되기 때문
- 서버 코드를 고려해야 함

### SSG(Static Site Generator)

- Html 페이지를 사전에 빌드하여 정적 파일로 제공
- 빠른 페이지 로드가 가능
- 쉽게 데이터가 변하지 않는 정적 콘텐츠를 사용하는데 유리
    - 예 ) 사전, 블로그
- 예시
    - `getStaticProps()` 함수를 정의하여 미리 faq 데이터를 가져온다.
        
        ```tsx
        import { collection, getDocs } from 'firebase/firestore';
        import { store } from '@remote/firebase';
        import { COLLECTIONS } from '@constants/collection';
        import ListRow from '@shared/ListRow';
        
        interface FAQ {
          id: string;
          question: string;
          answer: string;
        }
        
        function FAQPage({ faqs }: { faqs: FAQ[] }) {
          return (
            <div>
              {faqs.map((faq) => (
                <ListRow
                  key={faq.id}
                  contents={
                    <ListRow.Texts title={faq.question} subTitle={faq.answer} />
                  }
                />
              ))}
            </div>
          );
        }
        
        export async function getStaticProps() {
          const snapshot = await getDocs(collection(store, COLLECTIONS.FAQ));
        
          const faqs = snapshot.docs.map((doc) => ({
            id: doc.id,
            ...doc.data(),
          }));
        
          return {
            props: { faqs },
          };
        }
        
        export default FAQPage;
        
        ```
        
        - build 하면, 정적인 페이지가 바로 제공되는 것을 확인할 수 있음
            
            ![image.png](https://github.com/user-attachments/assets/ff303f8c-c58e-4698-9b3b-0c9564d21aa0)
            

## 프로젝트 최적화

### Next Image, Link

- `Next Image`
    - 별도의 서버 도움 없이 그릴 사이즈에 맞게 이미지의 크기를 자동 조절 가능
    - Lazy Load
    - Layout Shift 방지
- `Next Link`
    - 사용자가 경로를 방문하기 전에, 백그라운드에서 다음 이동할 페이지에 대한 정보를 미리 로드(Prefetch)

### SEO(Search Engine Optimization)

- 검색 엔진 결과 페이지에서 상위에 노출될 수 있도록 최적화하는 프로세스
- 상세 페이지 같은 곳에서 meta 태그를 설정하여 링크를 공유하였을 때, 내부 컨텐츠가 무엇인지 알 수 있게 설정 가능
    
    ```tsx
    <SEO
      title={`${corpName} ${name}`}
      description={subTitle}
      image="https://gl.chiikawa-pocket.com/ko/_astro/kv_sp.Cs2DsXBt.png"
    />
    ```
    

### 에러 관리

- 404 페이지
    - pages/404.tsx
    
    ![image.png](https://github.com/user-attachments/assets/1bccd05b-e39f-4ee3-b998-234ad3e3a9c2)
    
- error 페이지
    - pages/_error.tsx
    
    ![image.png](https://github.com/user-attachments/assets/3846257d-2f4a-40ea-a74d-78c1893af40f)
    
- ErrorBoundary
    
    ```tsx
    import React, { ErrorInfo } from 'react';
    
    interface Props {
      children: React.ReactNode;
      fallbackComponent?: React.ReactNode;
    }
    
    interface State {
      hasError: boolean;
    }
    
    class ErrorBoundary extends React.Component<Props, State> {
      constructor(props: Props) {
        super(props);
    
        // 오류가 있는지 여부를 추적하는 상태 변수 정의
        this.state = { hasError: false };
      }
      static getDerivedStateFromError(error: Error) {
        // 다음 렌더링에서 폴백 UI를 표시하도록 상태 업데이트
    
        return { hasError: true };
      }
      componentDidCatch(error: Error, errorInfo: ErrorInfo) {
        // 여기에서 자체 오류 로깅 서비스를 사용할 수 있습니다
        console.log({ error, errorInfo });
      }
      render() {
        // 오류가 발생했는지 확인
        if (this.state.hasError) {
          // 사용자 정의 폴백 UI를 렌더링할 수 있습니다
          if (this.props.fallbackComponent != null) {
            return <>{this.props.fallbackComponent}</>;
          }
          return (
            <div>
              <h2>알 수 없는 문제가 발생했어요</h2>
              <button
                type="button"
                onClick={() => this.setState({ hasError: false })}
              >
                재시도
              </button>
            </div>
          );
        }
    
        // 오류가 없는 경우 자식 컴포넌트를 반환
    
        return this.props.children;
      }
    }
    
    export default ErrorBoundary;
    ```
    

## 최적화를 위한 3가지 핵심 요소

### WebVital

- 유저의 경험을 측정하기 위한 웹 성능 지표
- 로딩 속도, 상호작용 시간, 페이지의 안정성 등을 측정하여 웹사이트 성능을 평가
- 코어 웹 바이탈(LCP, INP, CLS)은 사용자 환경의 고유한 측면을 나타내며, 현장에서 측정 가능하며, 중요한 사용자 중심 결과의 실제 환경을 반영
    - 측정 항목은 시간이 지남에 따라 진화
    
    ![image.png](https://github.com/user-attachments/assets/0f369261-260a-45a1-abb2-1248a8ad9e28)
    

### LCP(Largest Contentful Paint)

- 로드 성능 측정
- 최대 컨텐츠 렌더링 시간 2.5초 이내

### INP(Interaction to Next Paint)

- 상호작용 측정
- 다음 페인트에 대한 상호작용 반응시간 200ms 이내

### CLS(Cumulative Layout Shift)

- 시각적 안정성 측정
- 시각적 안정성 0.1 이하

### `useReportWebVitals`

- 웹 바이탈 리포트를 쉽게 만들 수 있는 함수
  ```tsx
  import type { AppProps } from 'next/app';
  import { SessionProvider } from 'next-auth/react';
  import { Global } from '@emotion/react';
  import { QueryClientProvider, QueryClient, Hydrate } from 'react-query';
  import globalStyles from '@styles/globalStyles';
  import Layout from '@shared/Layout';
  import Navbar from '@shared/Navbar';
  import { AlertContextProvider } from '@contexts/AlertContext';
  import ErrorBoundary from '@shared/ErrorBoundary';
  import { useReportWebVitals } from 'next/web-vitals';

  const client = new QueryClient({});

  export default function App({
    Component,
    pageProps: { dehydratedState, session, ...pageProps },
  }: AppProps) {
    useReportWebVitals((metric) => {
      console.log(metric);
    });

    return (
      <Layout>
        <Global styles={globalStyles} />
        <SessionProvider session={session}>
          <QueryClientProvider client={client}>
            <Hydrate state={dehydratedState}>
              <ErrorBoundary>
                <AlertContextProvider>
                  <Navbar />
                  <Component {...pageProps} />
                </AlertContextProvider>
              </ErrorBoundary>
            </Hydrate>
          </QueryClientProvider>
        </SessionProvider>
      </Layout>
    );
  }
  ```