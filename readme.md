### object detection competition


### Pre-Commit Installation Guide (by yoonghee)
0. 아래 명령어를 리눅스 기본 shell에서 실행합니다.
<br/><br/>

1. pre-commit 설치
```
$ pip install pre-commit
$ brew install pre-commit
```
<br/>




2. 버전 확인
```
$ pre-commit --v
pre-commit 2.17.0
```
<br/>

3. 설치 확인 및 업데이트
```
$ cd src
$ pre-commit autoupdate
[WARNING] The 'rev' field.......
```
<br/>

4. 설치
```
$ pre-commit install
pre-commit installed at .git/hooks/pre-commit
```
<br/>

5. 이후 commit부터 오통 포매팅 자동 반영
- fix된 사항 있을 시 git status를 통해 modified 확인 후 다시 add & commit

