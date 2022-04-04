```
`-- detection
    |-- baseline
    |   `-- YOLO
    |       `-- yolor
    |           |-- cfg
    |           |   `-- *.cfg
    |           |-- convert2Yolo
    |           |   |-- img_path_format.py
    |           |   |-- img_path_yolo.py
    |           |   |-- object_format.py
    |           |   |-- yolo_img_path.py
    |           |   |-- yolo_object_info.py
    |           |   `-- yolo_train_test_img_path.ipynb
    |           `-- data
    |               |-- coco.names
    |               |-- coco.yaml
    |               |-- image
    |               |   |-- test
    |               |   |   `-- *.jpg
    |               |   `-- train
    |               |       |-- *.jpg
    |               |       `-- *.txt
    |               `-- image_path
    |                   |-- *.txt
    |                   |-- cv5_train0.txt
    |                   |-- cv5_val0.txt
    |                   |-- test.txt
    |                   `-- train.txt
    `-- dataset
        |-- test
        |   `-- *.jpg
        `-- train
            `-- *.jpg
```

## How to Use

1. yolor 폴더를 위의 tree 구조와 맞게 경로를 옮긴다.

2. Pre-Trained Weights를 다운받는다.
```
cd .../yolor
bash scripts/get_pretrain.sh
```
명령어 실행이 안 된다면, 직접 받아서 yolor 폴더 내부에 저장한다.
- https://drive.google.com/uc?export=download&id=1Tdn3yqpZ79X7R1Ql0zNlNScB1Dv9Fp76
- https://drive.google.com/u/0/uc?export=download&confirm=eUux&id=1UflcHlN5ERPdhahMivQYCbWWw7d2wY7U 

3. ```yolor/data/image``` 안의 train, test 폴더에 이미지(*.jpg)를 넣어준다.

4. ```yolor/convert2Yolo/yolo_train_test_img_path.ipynb```를 실행시키면 train과 test 이미지 경로가 ```yolor/data/image_path``` 내부에 ```txt 파일```로 저장된다.

5. train과 validation dataset의 이미지 경로를 ```txt 파일```로 저장하기 위해 다음의 명령문을 실행시킨다.

예시
```
cd convert2Yolo
python yolo_img_path.py --label ../../../../dataset/cv5_train0.json
```

6. 학습을 시작한다. (epoch를 300이상으로 돌려야 한다.)

예시
```
python train.py --batch-size 8 --img 1280 --data coco_fold1.yaml --cfg cfg/yolor_w6.cfg --weights ./yolor_w6.pt --device 0 --name yolor_fold1 --hyp hyp.finetune.1280.yaml --epochs 900
```

7. Inference 및 submit은 추후 작성 예정

### Reference
- https://github.com/WongKinYiu/yolor
- https://github.com/ssaru/convert2Yolo