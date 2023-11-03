# 08_PJT_비동기 통신을 이용한 웹 사이트 구현(영화 커뮤니티)

## 프로젝트 목표

- AJAX 통신과 JSON 데이터를 활용하는 커뮤니티 웹 서비스의 구성
- 영화 데이터에 대한 목록 및 단일 조회, 알고리즘을 통한 영화 추천이 가능한 애플리케이션 완성
- 영화 리뷰의 좋아요가 가능한 애플리케이션 완성
- 유저 팔로우가 가능한 애플리케이션 완성

## 개발 도구

- Visual Studio Code
- Google Chrome
- Django 4.2.6

## 구현 내용

### ERD(Entity-Relationship Diagram)

![Untitled](https://github.com/yuj1818/TIL/assets/95585314/00664c57-1793-4e11-a923-4142b0c11a3e)

### 유저 팔로우 기능

![Untitled 1](https://github.com/yuj1818/TIL/assets/95585314/cc89ad2b-1c8a-46f3-9ecf-e3c5ac9717b9)

- is_authenticated를 사용하여 인증된 사용자가 아니면 다른 사용자를 팔로우 할 수 없도록 설정
- 팔로잉 요청한 사용자가 본인이면 팔로우 할 수 없도록 설정
- ManyToManyField followings를 역참조 하는 followers를 사용하여 followers에 팔로잉 요청자가 포함되어 있으면 follower 데이터에서 삭제(unFollow), 그렇지 않으면 follower 데이터에 추가(Follow)되도록 설정
- axios 사용하여 post 요청하면 서버에서 팔로잉 여부, 팔로워 수, 팔로잉 수 데이터를 반환
    - 팔로잉 여부에 따라 버튼 textContent 변경
    - 팔로워, 팔로잉 수에 따라 textContent 변경

### 리뷰 좋아요 기능

![Untitled 2](https://github.com/yuj1818/TIL/assets/95585314/9fb88483-2cdd-47e1-a85f-276d2660aab6)

- 전체 리뷰 목록 조회 페이지에 좋아요 버튼과 좋아요 개수 표시
- is_authenticated를 사용하여 인증된 사용자가 아니면 좋아요 기능 사용하지 못하도록 설정
- 인증되지 않은 사용자가 요청할 시 status Code 302와 함께 login 페이지의 url를 반환
    - window.location.href 를 사용하여 302 코드가 반환되면 로그인 페이지로 이동
- axios 사용하여 post 요청하면 좋아요 여부, 좋아요 수를 반환
    - 좋아요 여부에 따라 좋아요 버튼 textContent 변경
    - 좋아요 수에 따라 textContent 변경

### Movies 앱 기능

1. 전체 영화 목록 조회
    
    ![Untitled 3](https://github.com/yuj1818/TIL/assets/95585314/05a54f84-c654-41dc-ae20-31d0ac21f653)
    
    - 등록 역순으로 조회 되도록 설정
    - BootStrap Card 컴포넌트를 사용하여 영화 목록 구성
    - 카드를 클릭하면 상세 정보 페이지로 갈 수 있도록 click 이벤트 설정
    - 카드에 mouseover 이벤트를 설정하여 어떤 카드를 선택하고 있는지 알 수 있도록 설정
        - style의 box-shadow 사용
    - 카드에 mouseout 이벤트를 설정하여 이전의 box-shadow style 초기화
2. 단일 영화 상세 조회
    
    ![Untitled 4](https://github.com/yuj1818/TIL/assets/95585314/966dc2e5-6281-418a-9819-d7e4f8cf8873)
    
    - 영화의 제목, 줄거리, 상영일, 선호도, 평균 평점, 장르가 조회 되도록 설정
    - BootStrap의 Badge 컴포넌트를 사용하여 장르 목록을 구성
        - Badge에 클릭 이벤트를 추가하여 각 장르 관련 추천 영화 페이지로 갈 수 있도록 설정

### 영화 추천 기능

![Untitled 5](https://github.com/yuj1818/TIL/assets/95585314/1117af65-f1ed-497c-ab93-398999ea07c0)

- 선택한 장르의 영화 리스트 중 popularity가 높은 것 상위 6개 추천하도록 설정
    - query parameter를 사용하여 selectedGenre를 설정
    - 영화 데이터 중 장르에 selectedGenre가 포함되어 있는 영화를 popularity가 높은 순으로 정렬하여 6개 선택

### 리뷰 대댓글 기능

![Untitled 6](https://github.com/yuj1818/TIL/assets/95585314/a89b6585-f993-4b06-806e-3cf1b6015e03)

- 리뷰 상세 조회 페이지에 댓글 좋아요 버튼과 좋아요 개수를 표시
    - is_authenticated를 사용하여 인증된 사용자가 아니면 좋아요 기능 사용하지 못하도록 설정
    - 인증되지 않은 사용자가 요청할 시 status Code 302와 함께 login 페이지 url 반환
        - window.location.href를 사용하여 302 코드가 반환되면 로그인 페이지로 이동
    - 본인의 댓글에 좋아요 기능 사용하지 못하도록 status Code 403 반환
        - alert 사용하여 본인의 댓글은 좋아요 누르지 못한다는 경고창 뜨게 설정
    - axios 사용하여 post 요청하면 좋아요 여부, 좋아요 수를 반환
        - 좋아요 여부에 따라 classList add/remove하여 하트 아이콘 변경
        - 좋아요 수에 따라 textContent 변경
- 각 댓글에 하위 댓글을 작성할 수 있는 대댓글 기능 구현
    - 자기 자신을 참조하는 Foreign Key org_comment를 사용하여 org_comment를 참조하는 대댓글 목록을 불러와 조회 되도록 설정
    - 대댓글 작성이 가능하도록 대댓글 폼을 나타냄
    - is_authenticated를 사용하여 인증된 사용자가 아니면 대댓글을 작성하지 못하도록 설정