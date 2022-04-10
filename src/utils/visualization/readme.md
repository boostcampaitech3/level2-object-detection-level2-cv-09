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

