# 변수(Variable)

- 어떠한 "한 값"을 가진 메모리 공간에 붙인 "이름" 또는 공간 "그 자체"
- 값을 참조하는 이름
- ex) a = 1 ⇒ 변수 a에 값 1을 할당
- 변수명 규칙
    - 영문 알파벳, 언더스코어, 숫자로 구성
    - 숫자로 시작 불가능
    - 대소문자 구분
    - 예약어는 사용 불가능
        - ex) True, False, None, and, break, if 등
- 메모리의 모든 위치에는 고유 식별 메모리 주소가 존재
- 변수는 변수가 참조하는 `객체`의 메모리 주소를 가짐
    - id(변수명) 으로 주소 값 알 수 있음

    <img src = "https://github.com/yuj1818/TIL/assets/95585314/1b199939-6b99-45b6-8aa2-86ba7a495cda" width="50%" height="50%">
    <img src = "https://github.com/yuj1818/TIL/assets/95585314/60bf7533-eb77-4f11-9415-16d36e83e630" width="50%" height="50%">
    <img src = "https://github.com/yuj1818/TIL/assets/95585314/ff7af1ab-8f6e-40f0-8d13-1d7ffd5b6cd2" width="50%" height="50%"><br/>
    
    `객체` : 타입을 갖는 메모리 주소 내 값
    
- 변수는 주소를 부르는 닉네임 같은 것
- 할당문
    - 처음 만드는 변수 ⇒ 새 변수 생성
    - 기존에 존재하던 변수 ⇒ 메모리 주소 변경