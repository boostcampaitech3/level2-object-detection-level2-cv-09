

</br>

![image](https://user-images.githubusercontent.com/82289435/161487725-cb433d95-1c59-47eb-b305-218a8c42ea46.png)

### 🚢 Members

[전다운](https://github.com/updaun)|[박정재](https://github.com/jeongjae96)|[김규민](https://github.com/km9mn)|[이융희](https://github.com/yoonghee)|[서경국](https://github.com/tjrudrnr2)|
:-:|:-:|:-:|:-:|:-:|
![image1][image1]|![image2][image2]|![image3][image3]|![image4][image4]|![image5][image5]|

[image1]: https://user-images.githubusercontent.com/82289435/161474965-fde57430-c7d8-4a8b-b042-a60e553cfb4e.png
[image2]: https://user-images.githubusercontent.com/82289435/161475112-33b5e095-c2f1-4ed8-90cb-c3ae9f6296ba.png
[image3]: https://user-images.githubusercontent.com/82289435/161475194-7b2f9f11-98fa-4c10-b3fa-ef986e8775d5.png
[image4]: https://user-images.githubusercontent.com/82289435/161475112-33b5e095-c2f1-4ed8-90cb-c3ae9f6296ba.png
[image5]: https://user-images.githubusercontent.com/82289435/161475256-bc796065-f8f8-4bdc-9d43-05b684a73d7d.png



### 🔥 Contribution  
- `전다운` &nbsp; Data Synthesis • EDA Model Searching • Model Experiment • Git management 
- `박정재` &nbsp; Metrics • 1 stage detector • Model Searching • Model Experiment • Ensemble   
- `김규민` &nbsp; Data Synthesis • Model Searching • Model Experiment • Ensemble  
- `이융희` &nbsp; Model Evaluation • Document • Pre-commit • Recording • Ensemble 
- `서경국` &nbsp; EDA • Modeling • Model Experiment • Ensemble • Pseudo Labeling

</br>

### 🏆 LB Score

- Public LB: 0.7232 mAP(3등/19팀)
- Private LB: 0.7112 mAP(2등/19팀) 

![best scores](https://user-images.githubusercontent.com/82289435/162617030-b7f29809-7cb6-40da-8029-769183e4625a.png)

</br>

## 🔎 Object Detection for sorting recycled items ♻️

</br>

![image](https://user-images.githubusercontent.com/82289435/161470859-3945d5c6-c8f2-4d34-a9e9-316b32a3c801.png)

### 문제 정의 ❓

- 바야흐로 **대량 생산, 대량 소비**의 시대. 우리는 많은 물건이 대량으로 생산되고 소비되는 시대를 삶에 따라 **쓰레기 대란, 매립지 부족**과 같은 사회 문제 발생
- 버려지는 쓰레기 중 잘 분리배출 된 쓰레기는 자원으로서 가치를 인정받아 재활용되지만, 잘못 분리배출 되면 그대로 폐기물로 분류되어 매립 또는 소각되기 때문에 분리수거는 사회적 환경 부담 문제를 줄일 수 있는 방법
- Deep Learning을 통해 쓰레기들을 자동으로 분류할 수 있는 모델 개발 

</br>


### ⚙ Development Environment
- GPU : Nvidia Tesla V100
- OS : Linux Ubuntu 18.04
- Runtime : Python 3.8.5
- Main Dependency : Yolov5, MMdetection, Detectron2, Pytorch 1.7.1, OpenCV 4.5.1

</br>

### 💾 Dataset
![image](https://user-images.githubusercontent.com/82289435/161486061-946f9820-1580-4d0f-a14a-90a9a56181de.png)

- 전체 이미지 개수 : 9754장
- 10 class : General trash, Paper, Paper pack, Metal, Glass, Plastic, Styrofoam, Plastic bag, Battery, Clothing
- 이미지 크기 : (1024, 1024)
- 학습데이터는 4883장, 평가데이터는 4871장으로 무작위 선정
    - 평가데이터: Public 50%, Private 50%

### 📐 Metrics
![image](https://user-images.githubusercontent.com/82289435/161477648-d18e5abc-73f4-478e-b358-ca3ba157ed7c.png)
![image](https://user-images.githubusercontent.com/82289435/161477607-9c6bf2fa-f7bf-473f-8138-e98af5954d83.png)
![image](https://user-images.githubusercontent.com/82289435/161477693-2f92d386-63dd-4329-bd61-3e1a76db3dea.png)

- mAP50 (Mean Average Precision)
    - Object Detection에서 사용하는 대표적인 성능 측정 방법
    - Ground Truth 박스와 Prediction 박스간 IoU(Intersection Over Union, Detector의 정확도를 평가하는 지표)가 50이 넘는 예측에 대해 True라고 판단

</br>

### 🧪 Model Experiments 
### [![Notion](https://img.shields.io/badge/Notion-%23000000.svg?style=for-the-badge&logo=notion&logoColor=white)](https://seemly-newsstand-e49.notion.site/12ea90961aca491ca3a1ff96f26b8717?v=267b6ef3fb264f04934615147e48b912)



### 🔬 Ensemble Experiments
### [![Notion](https://img.shields.io/badge/Notion-%23000000.svg?style=for-the-badge&logo=notion&logoColor=white)](https://seemly-newsstand-e49.notion.site/8ed4c83b48ee403da96211040daf843a?v=d2c1241351ae49f5b3f3f3e2d02d7ad6)

</br>



### Working Directory
```
|-- EDA
|   |-- EDA.ipynb
|   `-- output_visualization.py
|-- dataset
|   |-- test
|   |-- train
|   `-- *.json
|-- models
|   |-- mmdetection
|   |    `--
|   `-- yolo
|       |-- yolor
|       `-- yolov5
|-- src
|   `-- .pre-commit-config.yaml
|-- utils
|   |-- stratified_kfold.ipynb
|   |-- stratified_kfold_group.py
|   |-- submission2json.ipynb
|   `-- readme.md
`-- readme.md
```

### 📢 Presentation
[하이파이프_발표자료.pdf](https://drive.google.com/file/d/1bfRf1bF_aiKwZ2HiWMXdvXdljhdWaMaS/view?usp=sharing)

</br>

<hr>

### 🚩 Pre-Commit Installation Guide (by yoonghee)
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