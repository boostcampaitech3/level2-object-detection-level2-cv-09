## Overview

YOLOv5 학습을 위해 필요한 데이터셋을 생성하는 폴더입니다.  
**COCO datasets** -> **YOLO datasets**로 변환 합니다.

## prepare dataset
1. 학습할 이미지 폴더를 현재 경로로 복사하거나 make_yolo_dataset.py 경로를 수정합니다.
```
cp -r /opt/ml/detection/datasets/train ./
```
2. coco json 파일을 가져옵니다.
```
cp /opt/ml/detection/datasets/train.json ./
cp /opt/ml/detection/datasets/test.json ./
```
3. YOLO format으로 바꿔줄 coco json 으로  파일 수정
```
TRAINJSON = os.path.join(DATAROOT,"train.json")
VALIDJSON = os.path.join(DATAROOT,"test.json")
``` 
4. 실행결과 : yolov5/dataset/yolov5 하위 폴더로 yolo format 데이터 생성