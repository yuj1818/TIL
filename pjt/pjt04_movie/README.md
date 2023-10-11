# 04_PJT 인증 페이지 구현(영화 커뮤니티)

## 프로젝트 목표

- 데이터를 생성, 조회, 수정, 삭제할 수 있는 Web application 제작
- Django Model과 ORM에 대한 이해
- Django Authentication System에 대한 이해

## 개발 도구

- Visual Studio Code
- Google Chrome
- Django 4.2.6

## 구현 내용

### 게시글

#### Movie 모델 작성

![Untitled](https://github.com/yuj1818/TIL/assets/95585314/9b36f017-12be-4e63-8fe9-097125f3a232)

- title
    - 영화 제목
    - CharField 사용하여 20자로 제한
- description
    - 영화 설명
    - TextField 사용
- movie_image
    - 영화 이미지
    - ImageField를 사용하여 영화 대표 이미지를 설정할 수 있도록 작성
    - 사진을 첨부하지 않아도 글이 작성되도록 blank=True로 설정
- author_id
    - 글쓴이
    - User 모델의 pk 참조
    - User 모델의 회원이 탈퇴하면 해당 회원이 작성한 글도 삭제되도록 설정

#### Model Form 작성

- Movie 모델을 가져와서 사용
- author 필드는 사용자가 직접 작성하지 않으므로 exclude 사용하여 form에서 제외

#### 메인 페이지(게시글 조회, READ)

![Untitled 1](https://github.com/yuj1818/TIL/assets/95585314/a5a1955d-b2d4-4986-90d5-07025f4daea5)

- Movie 모델에 있는 모든 게시글 데이터를 가져와 제목, 내용만 보이도록 작성
- Bootstrap Card 컴포넌트를 사용하여 게시글 표현
- 하나의 행에 2개의 게시글이 보이도록 함

#### 영화 정보 작성(CREATE)

![Untitled 2](https://github.com/yuj1818/TIL/assets/95585314/68c7c578-f844-44da-ac8b-48d80a75f142)

- login_required 데코레이터를 사용하여 로그인이 되어있지 않으면 게시글을 작성하지 못하도록 작성
- 게시글 작성 후 POST 요청하면, 유효성 검사 후  글쓴이 정보를 추가하고 데이터가 저장되도록 작성
- 게시글 작성 완료 후에 제출하면 상세 페이지로 가도록 작성

#### 개별 영화 상세 페이지(READ)

![Untitled 3](https://github.com/yuj1818/TIL/assets/95585314/a3928bc5-182c-4cec-8c53-a1d758e8bac0)

- 게시글 pk를 사용하여 상세 페이지 조회 가능하도록 작성
- 영화 이미지, 제목, 내용, 작성자를 조회 가능하도록 작성
- 로그인 하지 않으면 UPDATE, DELETE 기능을 사용하지 못하도록 작성
- Movie 모델의 author와 사용자 정보가 일치하지 않으면 글쓴이 본인이 아니므로 UPDATE, DELETE 기능을 사용하지 못하도록 작성
- Back 버튼을 누르면 메인 페이지로 가도록 작성

#### 영화 정보 수정(UPDATE)

![Untitled 4](https://github.com/yuj1818/TIL/assets/95585314/429ed91a-9873-4bc3-9bbb-ce34f70d9f63)

- login_required 데코레이터를 사용하여 로그인이 되어있지 않으면 게시글을 작성하지 못하도록 작성
- 게시글 pk를 사용하여 해당 게시글 정보를 수정할 수 있도록 작성
- POST 요청 시, 유효성 검사 후 데이터 저장
- 글 작성자 본인이 아닌데 수정 url로 접속 시도 시, 상세 페이지로 돌아가도록 작성
- 수정 완료 후, 상세 페이지로 가도록 작성

#### 게시글 삭제(DELETE)

- is_authenticated를 사용하여 인증된 사용자만 delete 할 수 있도록 작성
- 게시글 pk를 사용하여 해당 게시글 정보를 삭제할 수 있도록 작성
- 삭제 완료 후, 메인 페이지로 가도로 작성

### 인증

#### User 모델 작성

- AbstractUser 상속받아 사용

#### Model Form 작성

- UserCreationForm 상속 받아 CustomUserCreationForm 작성
    - username, email, first_name, last_name, password1, password2 필드 사용
- UserChangeForm 상속 받아 CustomUserChangeForm 작성
    - email, first_name, last_name, username 필드 사용
    - password 변경은 따로 버튼을 사용할 예정이므로 None으로 설정

#### 회원가입(User CREATE)

![Untitled 5](https://github.com/yuj1818/TIL/assets/95585314/a63b2075-615a-42e6-9029-b28ab3096a6c)

- 이미 로그인된 사용자가 로그인 url에 접속 시, 메인 페이지로 돌아가도록 작성
- CustomUserCreationForm을 사용하여 작성
- 회원가입이 되면 로그인이 되도록 하기 위해 유효성 검사 후, form을 저장하고 login 함수 호출하여 로그인 된 상태로 메인 페이지로 가도록 작성

#### 로그인(Session CREATE)

![Untitled 6](https://github.com/yuj1818/TIL/assets/95585314/10242f0f-1637-403b-b677-0a5ea82cec9c)

- 이미 로그인된 사용자가 로그인 url에 접속 시, 메인 페이지로 돌아가도록 작성
- AuthenticationForm을 사용하여 작성
- 유효성 검사 후, 로그인되면 login_required 데코레이터로 인해 로그인 페이지로 강제 이동 되면 next 인자에 원래 가려던 페이지가 저장되어 있으므로 next 인자 값이 존재하면 next 인자에 저장된 페이지로, 없으면 메인 페이지로 가도록 작성
- 로그인 여부에 따라 네비게이션 바에 사용가능한 기능 바뀌도록 작성

#### 로그아웃(Session DELETE)

- logout 함수를 호출하여 session 정보 삭제

#### 회원 정보 수정(User UPDATE)

![Untitled 7](https://github.com/yuj1818/TIL/assets/95585314/416da75f-8ea3-4176-8663-a2b6ce2e3c6b)

- CustomUserChangeForm을 사용하여 작성
- 유효성 검사 후, form 저장하고 메인페이지로 가도록 작성

#### 회원 탈퇴(User DELETE)

- user 데이터를 삭제
- 데이터 삭제 후, logout 함수 호출하여 session 정보도 삭제
- 삭제 후, 메인페이지로 가도록 작성

#### 비밀번호 변경(Session UPDATE)

![Untitled 8](https://github.com/yuj1818/TIL/assets/95585314/b1377366-65f3-4071-886c-d7937fab53d4)

- PasswordChangeForm을 사용
- 유효성 검사 후, form 저장하고 변경된 비밀번호로 다시 session 저장될 수 있게 update_session_auth_hash 함수 사용
- 변경 완료 후 메인페이지로 가도록 작성

### 이슈 사항

- MEDIA_URL, MEDIA_ROOT url 지정할 때, 앱 내의 urls.py에 작성하여 media 경로를 찾지 못해 이미지를 띄우지 못하는 에러 발생
    - project 폴더의 urls.py에 작성함으로써 문제 해결
- help_text가 영어로 설정되어 있어 한글로 모두 바꿔주기 힘든 문제 발생
    - settings.py의 LANGUAGE_CODE를 ‘ko-KR’로 변경하여 문제 해결
- 비밀번호 변경 버튼 작성 중, button 태그의 onclick 속성을 사용하여 location.href로 페이지 이동을 시도했지만 작동하지 않는 문제 발생
    - button 태그 안에 a 태그를 넣어 문제 해결