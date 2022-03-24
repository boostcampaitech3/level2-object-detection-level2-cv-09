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

5. 이후 commit부터 오토 포매팅 반영
- fix된 사항 있을 시 git status를 통해 modified 확인 후 다시 add & commit

<br/>


### Train Data Visualization Guide (by updaun) - 토론 게시판 공유 코드 

- 패키지 설치
```
apt-get install curl
apt-get install libcurl3
apt-get install libcurl4-openssl-dev
```
- 파이썬 fiftyone 라이브러리 설치
```
pip install fiftyone
```
- 사용 방법
```
python [python 파일명] -d [Data Directory] -a [Annotation File Directory(JSON file)] -p [서버 외부 포트 번호]
```
- 사용 예시(포트 번호만 변경해서 사용하세요.)
```
python src/visualization/output_visualization.py -d ../dataset/ -a ../dataset/train.json -p 30006
```

### Stratified K-fold (by JJ)

- 파이썬 라이브러리 설치
```
pip install funcy
```

- 사용 방법
```
python coco_cv.py -n [Number of Splits (default=5)] [Data Directory]
```


- 사용 예시
```
python coco_cv.py -n 5 ../../detection/dataset/
```

#### Reference
- https://github.com/akarazniewicz/cocosplit