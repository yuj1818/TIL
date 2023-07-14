# Git
## 용어 정리
- Working Directory: 내 컴퓨터
- Staging Area: 임시 공간
- Repository: 외부 컴퓨터
<br><br>
## git 사용 방법
```bash
#이 폴더에서 git을 사용하겠다는 의미(초기에 한 번만)
git init

#숨긴 파일까지 다 볼 수 있음
#ls -al

#현재 branch에 commit된 파일들, 추가되지 않은 파일 알려줌
git status

#임시공간에 파일 추가
#git add . -> 현재 디렉토리의 모든 파일 업로드
git add [파일명]

#commit 작성자 설정
git config --global user.email "[메일 주소]"
git config --global user.name "[유저 네임]"

#commit
git commit -m "[commit 메시지]"

#commit 잘 되었는지 로그 확인
git log

#push 과정
git remote add origin [repository 주소]
git push -u origin master

#git repository clone
git clone [repository 주소]

#수정사항 pull
git pull origin master

#저장할 곳 주소 별칭 확인
git remote -v
```
<br><br>
## branch
```bash
#branch 생성
git branch [branch 이름]

#branch 리스트 확인
git branch

#branch 위치 바꾸기
git checkout [branch 이름]

#branch upstream 설정
git push --set-upstream origin [branch 이름]

```
<br><br>
## gitignore
- push 할 때 push하지 않을 파일은 commit되지 않도록 함
- [gitignore 생성 사이트](https://www.toptal.com/developers/gitignore)
<br><br>
## 참고
- pull request 하고 나서 conflict 난 후 수정하면, main이랑 내용이 달라질 수 있음
    - main인 repository remote add해서 다시 pull 해오면 sync 맞출 수 있음
    - github에 있는 sync fork 사용할 수도 있음
