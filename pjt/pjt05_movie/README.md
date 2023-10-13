# 05_PJT DB를 활용한 웹 페이지 구현(영화 커뮤니티)

## 프로젝트 목표

- 데이터를 생성, 조회, 수정, 삭제할 수 있는 Web application 제작
- Django Model과 ORM에 대한 이해
- Django Authentication System에 대한 이해
- Many to one relationship에 대한 이해

## 개발 도구

- Visual Studio Code
- Google Chrome
- Django 4.2.6

## 구현 내용

### 게시글

#### Movie 모델 작성

![Untitled](https://github.com/yuj1818/TIL/assets/95585314/4b70ff21-a8ac-4dfe-b18f-79b71e00b1c8)

- title
    - 영화 제목
    - CharField 사용하여 30자로 제한
- description
    - 영화 설명
    - TextField 사용
- genre
    - 영화 장르
    - CharField 사용
- score
    - 영화 평점
    - FloatField 사용
- user
    - 글쓴이
    - Foreign Key - User 모델 참조
    - User 모델의 회원이 탈퇴하면 해당 회원이 작성한 글도 삭제되도록 설정

#### Comment 모델 작성

![Untitled 1](https://github.com/yuj1818/TIL/assets/95585314/072347b5-9b37-4670-ac97-b50ec34cbe23)

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

#### Movie Form 작성

- Movie 모델을 가져와서 사용
- user 필드는 사용자가 직접 작성하지 않으므로 title, description, genre, score 필드만 사용
- genre 필드는 ChoiceField 사용하여 선택지를 주고, Select 폼 사용
- score 필드는 최대값 5, 최소값 0, 간격 0.5로 설정
    - validator를 사용하여 유효성 검사 진행

#### Comment Form 작성

- Comment 모델을 가져와서 사용
- movie, user 필드는 사용자가 직접 작성하지 않으므로 comment 필드만 사용

#### 게시글 조회

![Untitled 2](https://github.com/yuj1818/TIL/assets/95585314/eb0ce796-9378-4aef-8925-2ae57a59544f)

- Movie 모델에 있는 모든 게시글 데이터를 가져와 제목, 내용만 보이도록 작성
- Bootstrap Card 컴포넌트를 사용하여 게시글 표현
- 하나의 행에 2개의 게시글이 보이도록 함

#### 영화 정보 작성

![Untitled 3](https://github.com/yuj1818/TIL/assets/95585314/989a8d52-19b0-4340-a2b4-228a97ce492c)

- login_required 데코레이터를 사용하여 로그인이 되어있지 않으면 게시글을 작성하지 못하도록 작성
- 게시글 작성 후 POST 요청하면, 유효성 검사 후 글쓴이 정보를 추가하고 데이터가 저장되도록 작성
- 게시글 작성 완료 후, 제출하면 상세 페이지로 가도록 작성

#### 영화 상세 정보 조회

![Untitled 4](https://github.com/yuj1818/TIL/assets/95585314/7c4dd700-561f-4719-860d-f597a2e763b7)

- 게시글 pk를 사용하여 상세 페이지 조회가 가능하도록 작성
- 영화 제목, 내용, 장르, 평점을 조회 가능하도록 작성
- 게시글 작성자와 현재 사용자가 일치하지 않으면 update, delete 기능 사용하지 못하도록 작성
- 게시글 pk를 사용하여 해당 게시글에 대한 댓글 목록을 조회 가능하도록 작성
- 댓글 목록을 Bootstrap List Group 컴포넌트를 사용하여 표현
- 댓글 작성자와 댓글 내용이 보이도록 작성
- 댓글이 없으면 ‘작성된 댓글이 없음 :(’이 나오도록 작성
- 로그인 하지 않은 사용자는 댓글 작성이 불가능하도록 댓글 작성 폼이 보이지 않도록 작성
- 댓글 작성자 본인이 아니면 댓글 삭제 기능을 사용하지 못하도록 작성
- 댓글 작성이 가능하도록 댓글 폼을 나타냄
- Back 버튼을 누르면 메인 페이지로 가도록 작성

#### 영화 정보 수정

![Untitled 5](https://github.com/yuj1818/TIL/assets/95585314/ac0b5b98-0a9a-4527-a004-fc9025e7bec7)

- login_required 데코레이터를 사용하여 로그인이 되어있지 않으면 게시글을 작성하지 못하도록 작성
- 게시글 pk를 사용하여 해당 게시글 정보를 수정할 수 있도록 작성
- POST 요청 시, 유효성 검사 후 데이터 저장
- 글 작성자 본인이 아닌데 수정 url로 접속 시도 시, 상세 페이지로 돌아가도록 작성
- 수정 완료 후, 상세 페이지로 가도록 작성

#### 게시글 삭제

- is_authenticated를 사용하여 인증된 사용자만 삭제할 수 있도록 작성
- 게시글 pk를 사용하여 해당 게시글 정보를 삭제할 수 있도록 작성
- 삭제 완료 후, 메인 페이지로 가도록 작성

#### 댓글 작성

![Untitled 6](https://github.com/yuj1818/TIL/assets/95585314/fa3cb52c-d192-41e0-b868-b0fa28872f69)

- is_authenticated를 사용하여 로그인한 사용자가 아니면 댓글을 작성하지 못하도록 작성
- 게시글 작성 후 POST 요청하면, 유효성 검사 후 해당 게시글에 대한 댓글임을 나타낼 수 있도록 게시글 정보를 추가하고 데이터가 저장되도록 작성
- 게시글 작성 완료 후, 제출하면 상세 페이지로 가도록 작성

#### 댓글 삭제

- is_authenticated를 사용하여 인증된 사용자만 댓글을 삭제할 수 있도록 작성
- 댓글 pk를 사용하여 해당 댓글을 삭제할 수 있도록 작성
- 댓글 작성자 본인이 아닐 시, 삭제 기능을 사용하지 못하도록 작성

### 인증

#### User 모델 작성

- AbstractUser 상속받아 사용

#### 커스텀 UserCreationForm 작성

- UserCreationForm 상속 받아 CustomUserCreationForm 작성

#### 회원가입

![Untitled 7](https://github.com/yuj1818/TIL/assets/95585314/239272e6-6043-497a-a68b-8fc0607cd8d3)

- is_authenticated를 사용하여 이미 로그인된 사용자가 로그인 url에 접속 시, 메인 페이지로 돌아가도록 작성
- CustomUserCreationForm을 사용하여 작성
- 회원 가입 완료 시, 로그인이 되도록 하기 위해 유효성 검사 후, form을 저장하고 login 함수 호출하여 로그인 된 상태로 메인 페이지로 가도록 작성

#### 로그인

![Untitled 8](https://github.com/yuj1818/TIL/assets/95585314/89954171-a28b-4749-91d9-624b3af6d623)

- is_authenticated를 사용하여 이미 로그인된 사용자가 로그인 url에 접속 시, 메인 페이지로 돌아가도록 작성
- AuthenticationForm을 사용하여 작성
- login 함수를 호출하여 session 정보 저장
- 로그인 여부에 따라 네비게이션 바에 사용 가능한 기능 바뀌도록 작성

#### 로그아웃

- logout 함수를 호출하여 session 정보 삭제