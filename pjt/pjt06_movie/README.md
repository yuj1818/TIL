# 06_PJT 관계형 데이터베이스 설계(영화 커뮤니티)

## 프로젝트 목표

- 데이터를 생성, 조회, 수정, 삭제할 수 있는 Web application 제작
- Django web framework를 사용한 데이터 처리
- Django Model과 ORM에 대한 이해
- Django Authentication System에 대한 이해
- Many to One relationship 및 Many to Many relationship에 대한 이해

## 개발 도구

- Visual Studio Code
- Google Chrome
- Django 4.2.6

## 구현 내용

### ERD(Entity-Relationship Diagram)

![Untitled](https://github.com/yuj1818/TIL/assets/95585314/1422480c-dfe3-45d7-85a4-5b6aad0c56b7)

### 게시글

#### Movie 모델 작성

- title
    - 영화 제목
    - CharField 사용하여 30자로 제한
- description
    - 영화 설명
    - TextField 사용
- created_at
    - 게시글 생성일
    - DateTimeField 사용
        - auto_now_add=True 설정하여 Create 될 때만 생성
- updated_at
    - 게시글 수정일
    - DateTimeField 사용
        - auto_now=True 설정하여 Update 될 때마다 수정
- user
    - 글쓴이
    - Foreign Key - User 모델 참조
    - User 모델의 회원이 탈퇴하면 해당 회원이 작성한 글도 삭제되도록 설정
- like_users
    - 해당 게시글에 좋아요 누른 사용자들
    - ManyToManyField 사용하여 User 모델 참조
    - 역참조 매니저 이름 like_movies로 설정

#### Comment 모델 작성

- content
    - 댓글 내용
    - CharField 사용하여 200자로 제한
- movie
    - 댓글 단 게시글
    - Foreign Key - Movie 모델 참조
    - Movie 모델의 게시글이 지워지면 해당 게시글에 달린 댓글도 삭제되도록 설정
- user
    - 댓글 글쓴이
    - Foreign Key - User 모델 참조
    - User 모델의 회원이 탈퇴하면 해당 회원이 작성한 댓글도 삭제되도록 설정
- org_comment
    - 원 댓글
    - Foreign Key - 자기 자신 참조
    - null=True 설정하여 org_comment가 없으면 원 댓글, org_comment 값이 존재하면 대댓글
    - 역참조 매니저 이름을 re_comments로 설정
    - 원 댓글이 삭제되면 대댓글 또한 삭제되도록 설정

#### Movie Form 작성

- Movie 모델을 가져와서 사용
- user 필드는 사용자가 직접 작성하지 않으므로 title, description 필드만 사용

#### Comment Form 작성

- Comment 모델을 가져와서 사용
- movie, user, org_comment 필드는 사용자가 직접 작성하지 않으므로 content 필드만 사용

#### 메인 페이지

![Untitled 1](https://github.com/yuj1818/TIL/assets/95585314/1838fd15-f164-42e8-8878-00dbc62e8aa0)

- 게시글 조회
    - Movie 모델에 있는 모든 게시글 데이터를 가져와 제목, 생성일, 좋아요 수만 보이도록 작성
    - Bootstrap Card 컴포넌트를 사용하여 게시글 표현
    - 하나의 행에 2개의 게시글이 보이도록 함
- 좋아요 기능 구현
    
    ![Untitled 2](https://github.com/yuj1818/TIL/assets/95585314/b15d1bae-bf26-4e4a-bca6-f58f056a17ec)
    
    - is_authenticated를 사용하여 로그인이 되어있지 않으면 좋아요 기능 사용하지 못하도록 설정
    - 좋아요 버튼을 누르면 좋아요 수 증가하고 좋아요 취소 버튼으로 변경되도록 설정
    - 좋아요 취소 버튼을 누르면 좋아요 수 감소하고 좋아요 버튼으로 변경되도록 설정
    - 자신이 작성한 글은 좋아요를 하지 못하도록 설정

#### 영화 정보 작성 페이지

![Untitled 3](https://github.com/yuj1818/TIL/assets/95585314/fab5b3d8-5256-4ec3-a677-2526504e7253)

- login_required 데코레이터를 사용하여 로그인이 되어있지 않으면 게시글을 작성하지 못하도록 작성
- 게시글 작성 후 POST 요청하면, 유효성 검사 후 글쓴이 정보를 추가하고 데이터가 저장되도록 작성
- 게시글 작성 완료 후, 제출하면 상세 페이지로 가도록 작성

#### 영화 상세 정보 페이지

![Untitled 4](https://github.com/yuj1818/TIL/assets/95585314/95490357-4a8e-4ed7-822a-acec508014ee)

- 상세 정보 조회
    - 게시글 pk를 사용하여 상세 페이지 조회가 가능하도록 작성
    - 영화 제목, 내용, 작성자를 조회 가능하도록 작성
    - 게시글 작성자와 현재 사용자가 일치하지 않으면 update, delete 기능 사용하지 못하도록 작성
    - Back 버튼을 누르면 메인 페이지로 가도록 작성
    - 작성자 링크를 누르면 작성자 프로필 페이지로 가도록 작성
- 영화 게시글 삭제
    - is_authenticated를 사용하여 인증된 사용자만 삭제할 수 있도록 작성
    - 게시글 pk를 사용하여 해당 게시글 정보를 삭제할 수 있도록 작성
    - 삭제 완료 후, 메인 페이지로 가도록 작성
- 댓글 조회
    - 게시글 pk를 사용하여 해당 게시글에 대한 댓글 목록 중, org_comment 필드가 null인 데이터들을 조회 가능하도록 작성
    - 댓글 목록을 Bootstrap List Group 컴포넌트를 사용하여 표현
    - 댓글 작성자와 댓글 내용이 보이도록 작성
    - 댓글이 없으면 ‘작성된 댓글이 없음 :(’이 나오도록 작성
    - 댓글 작성자 링크를 누르면 댓글 작성자 프로필 페이지로 가도록 작성
- 댓글 작성
    - 댓글 작성이 가능하도록 댓글 폼을 나타냄
    - 로그인 하지 않은 사용자는 댓글 작성 폼이 보이지 않도록 작성
    - is_authenticated를 사용하여 로그인한 사용자가 아니면 댓글을 작성하지 못하도록 작성
    - 댓글 작성 후 POST 요청하면, 유효성 검사 후 해당 게시글에 대한 댓글임을 나타낼 수 있도록 게시글 정보를 추가하고 데이터가 저장되도록 작성
    - 댓글 작성 완료 후, 제출하면 상세 페이지로 가도록 작성
- 댓글 삭제
    - is_authenticated를 사용하여 인증된 사용자만 댓글을 삭제할 수 있도록 작성
    - 댓글 pk를 사용하여 해당 댓글을 삭제할 수 있도록 작성
    - 댓글 작성자 본인이 아닐 시, 삭제 기능을 사용하지 못하도록 작성
- 대댓글 조회
    - 원 댓글을 참조하는 대댓글 목록을 불러와 조회 가능하도록 작성
    - 대댓글 내용만 보이도록 작성
- 대댓글 작성
    - 대댓글 작성이 가능하도록 대댓글 폼을 나타냄
    - 로그인 하지 않은 사용자는 대댓글 작성 폼이 보이지 않도록 작성
- 대댓글 삭제
    - 대댓글 작성자 본인이 아니면 대댓글 삭제 기능을 사용하지 못하도록 작성

#### 영화 정보 수정 페이지

![Untitled 5](https://github.com/yuj1818/TIL/assets/95585314/7d50a759-f909-4ed4-a246-a7f8abd55ea7)

- login_required 데코레이터를 사용하여 로그인이 되어있지 않으면 게시글을 수정하지 못하도록 작성
- 게시글 pk를 사용하여 해당 게시글 정보를 수정할 수 있도록 작성
- POST 요청 시, 유효성 검사 후 데이터 저장
- 글 작성자 본인이 아닌데 수정 url로 접속 시도 시, 상세 페이지로 돌아가도록 작성
- 수정 완료 후, 상세 페이지로 가도록 작성

#### 좋아요 누른 영화 목록 페이지

![Untitled 6](https://github.com/yuj1818/TIL/assets/95585314/911582a8-2f66-4ded-b34b-7ca8f7eeb31a)

- 프로필 페이지에서 넘겨 받은 사용자 pk를 사용하여 해당 사용자가 역참조 되는 게시글(좋아요를 누른 게시글) 목록을 조회 가능하도록 작성
- Back 링크 누르면 해당 사용자 프로필로 돌아가도록 작성
- 게시글 제목 링크를 누르면 그 게시글의 상세 페이지로 가도록 작성

### 사용자

#### User 모델 작성

- AbstractUser 상속받아 사용
- followings
    - 사용자가 팔로우 하는 사람
    - ManyToManyField 사용하여 자기 자신을 참조
    - 역참조 매니저 이름을 followers로 설정

#### 커스텀 UserCreationForm, UserChangeForm 작성

- UserCreationForm 상속 받아 CustomUserCreationForm 작성
- UserChangeForm 상속 받아 CustomUserChangeForm 작성

#### 회원가입 페이지

![Untitled 7](https://github.com/yuj1818/TIL/assets/95585314/974aeba0-715f-496b-b486-50d1d69fe7ec)

- is_authenticated를 사용하여 이미 로그인된 사용자가 로그인 url에 접속 시, 메인 페이지로 돌아가도록 작성
- CustomUserCreationForm을 사용하여 작성
- 회원 가입 완료 시, 로그인이 되도록 하기 위해 유효성 검사 후, form을 저장하고 login 함수 호출하여 로그인 된 상태로 메인 페이지로 가도록 작성

#### 로그인 페이지

![Untitled 8](https://github.com/yuj1818/TIL/assets/95585314/43f01062-e026-4881-8dcf-7cd0128a8455)

- is_authenticated를 사용하여 이미 로그인된 사용자가 로그인 url에 접속 시, 메인 페이지로 돌아가도록 작성
- AuthenticationForm을 사용하여 작성
- login 함수를 호출하여 session 정보 저장
- 로그인 여부에 따라 네비게이션 바에 사용 가능한 기능 바뀌도록 작성

#### 로그아웃

- logout 함수를 호출하여 session 정보 삭제

#### 회원 정보 수정 페이지

![Untitled 9](https://github.com/yuj1818/TIL/assets/95585314/d341a06e-88d7-4c86-8051-3e0cb23d4d47)

- login_required 데코레이터를 사용하여 로그인이 되어있지 않으면 회원 정보를 수정하지 못하도록 작성
- CustomUserChangeForm을 사용하여 작성
- 수정 완료 후, 메인 페이지로 가도록 설정

#### 비밀번호 변경 페이지

![Untitled 10](https://github.com/yuj1818/TIL/assets/95585314/b4db1a3b-1055-4c33-9bd6-51957a181995)

- login_required 데코레이터를 사용하여 로그인이 되어있지 않으면 비밀번호를 수정하지 못하도록 작성
- PasswordChangeForm을 사용하여 작성
- 변경 후, 로그인 상태를 유지할 수 있도록 update_session_auth_hash 함수를 사용하여 session 정보를 갱신
- 수정 완료 후, 메인 페이지로 가도록 설정

#### 프로필 페이지

![Untitled 11](https://github.com/yuj1818/TIL/assets/95585314/03130e39-c048-43b3-9be1-dc2e7fa7ba1a)

- 해당 사용자가 작성한 글 조회
    - 해당 사용자를 참조하는 게시글(해당 사용자가 작성한 게시글) 목록을 조회 가능하도록 작성
    - Bootstrap의 Card 컴포넌트를 사용하여 표현
    - 게시글 제목만을 나타내면 제목 링크를 누르면 해당 게시글 상세 페이지로 가도록 작성
- 해당 사용자가 좋아요를 누른 게시글 수, 목록 조회
    - 해당 사용자가 역참조 되는 게시글 수를 count 함수를 사용하여 조회
    - 좋아요 영화 확인 링크를 누르면 좋아요 누른 게시글 목록 페이지로 가도록 작성
- 해당 사용자를 팔로우 하는 사람 수, 목록 조회
    - 해당 사용자가 역참조 되는 사용자 수를 count 함수를 사용하여 조회
    - 팔로워 링크를 누르면 팔로워 목록 페이지로 가도록 작성
- 해당 사용자가 팔로우 하는 사람 수, 목록 조회
    - 해당 사용자가 참조하는 사용자 수를 count 함수를 사용하여 조회
    - 팔로잉 링크를 누르면 팔로잉 목록 페이지로 가도록 작성
- 회원 탈퇴 기능
    - 탈퇴하기 버튼을 누르면 사용자 데이터베이스에서 해당 사용자를 삭제
    - 삭제 후, session 정보 삭제 되도록 auth_logout 함수 사용
    - 회원 탈퇴가 완료되면, 메인 페이지로 가도록 작성

#### 팔로워 목록 페이지

![Untitled 12](https://github.com/yuj1818/TIL/assets/95585314/a02c05dd-952f-413e-a128-9800d2e22c6d)

- 넘겨 받은 사용자 pk를 사용하여 해당 사용자를 팔로우 하는 사람 목록 조회
- Back 링크를 누르면 해당 사용자의 프로필로 돌아가게 작성
- 사용자 아이디 링크를 누르면 그 사용자의 프로필 페이지로 가도록 작성

#### 팔로잉 목록 페이지

![Untitled 13](https://github.com/yuj1818/TIL/assets/95585314/c73c77c7-9292-4fd2-b093-91f102c5a170)

- 넘겨 받은 사용자 pk를 사용하여 해당 사용자가 팔로우 하는 사람 목록 조회
- Back 링크를 누르면 해당 사용자의 프로필로 돌아가게 작성
- 사용자 아이디 링크를 누르면 그 사용자의 프로필 페이지로 가도록 작성