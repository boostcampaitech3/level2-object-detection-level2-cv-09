## Overview

YOLOv5을 이용한 모델 훈련입니다.  
Pre-trained Model은 **Yolov5x6**를 사용했습니다. 

|Model|리더보드 mAP| kfold |
|---|:---:|:---:|
|YOLOv5x6|0.5978|ensemble|

## 1. Install

  ```
  $ pip install -r requirements.txt
  ```

## 2. prepare dataset
1. train image 폴더를 상기 프로젝트 yolov5/dataset/train에 복사 or make_yolo_dataset.py 경로를 수정합니다.
2. make_yolo_dataset.py에 사용할 kfold num으로 train, val json 파일 수정 ex) kfold1
```
TRAINJSON = os.path.join(DATAROOT,"train_1.json")
VALIDJSON = os.path.join(DATAROOT,"valid_1.json")
``` 
3. 실행결과 : yolov5/dataset/yolov5 하위 폴더로 yolo format 데이터 생성

## 3. Train

- train.sh 내 인자를 조정하여 HyperParameter와 경로 등을 수정합니다.

```bash
$ ./train.sh
```

## 4. Inference
- train output ex) output/yolov5/exp면 exp_name = 'exp'로 코드 수정
- inference.ipynb를 실행하여 submission.csv를 생성합니다.