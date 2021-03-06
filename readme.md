

</br>

![image](https://user-images.githubusercontent.com/82289435/161487725-cb433d95-1c59-47eb-b305-218a8c42ea46.png)

### π’ Members

[μ λ€μ΄](https://github.com/updaun)|[λ°μ μ¬](https://github.com/jeongjae96)|[κΉκ·λ―Ό](https://github.com/km9mn)|[μ΄μ΅ν¬](https://github.com/yoonghee)|[μκ²½κ΅­](https://github.com/tjrudrnr2)|
:-:|:-:|:-:|:-:|:-:|
![image1][image1]|![image2][image2]|![image3][image3]|![image4][image4]|![image5][image5]|

[image1]: https://user-images.githubusercontent.com/82289435/161474965-fde57430-c7d8-4a8b-b042-a60e553cfb4e.png
[image2]: https://user-images.githubusercontent.com/82289435/161475112-33b5e095-c2f1-4ed8-90cb-c3ae9f6296ba.png
[image3]: https://user-images.githubusercontent.com/82289435/161475194-7b2f9f11-98fa-4c10-b3fa-ef986e8775d5.png
[image4]: https://user-images.githubusercontent.com/82289435/161475112-33b5e095-c2f1-4ed8-90cb-c3ae9f6296ba.png
[image5]: https://user-images.githubusercontent.com/82289435/161475256-bc796065-f8f8-4bdc-9d43-05b684a73d7d.png



### π₯ Contribution  
- `μ λ€μ΄` &nbsp; Data Synthesis β’ EDA Model Searching β’ Model Experiment β’ Git management 
- `λ°μ μ¬` &nbsp; Metrics β’ 1 stage detector β’ Model Searching β’ Model Experiment β’ Ensemble   
- `κΉκ·λ―Ό` &nbsp; Data Synthesis β’ Model Searching β’ Model Experiment β’ Ensemble  
- `μ΄μ΅ν¬` &nbsp; Model Evaluation β’ Document β’ Pre-commit β’ Recording β’ Ensemble 
- `μκ²½κ΅­` &nbsp; EDA β’ Modeling β’ Model Experiment β’ Ensemble β’ Pseudo Labeling

</br>

### π LB Score

- Public LB: 0.7232 mAP(3λ±/19ν)
- Private LB: 0.7112 mAP(2λ±/19ν) 

![object_detection](https://user-images.githubusercontent.com/82289435/164722125-c2ddd619-bc82-4be2-a12d-f00f945f378b.png)

</br>

## π Object Detection for sorting recycled items β»οΈ

</br>

![image](https://user-images.githubusercontent.com/82289435/161470859-3945d5c6-c8f2-4d34-a9e9-316b32a3c801.png)

### λ¬Έμ  μ μ β

- λ°μΌνλ‘ **λλ μμ°, λλ μλΉ**μ μλ. μ°λ¦¬λ λ§μ λ¬Όκ±΄μ΄ λλμΌλ‘ μμ°λκ³  μλΉλλ μλλ₯Ό μΆμ λ°λΌ **μ°λ κΈ° λλ, λ§€λ¦½μ§ λΆμ‘±**κ³Ό κ°μ μ¬ν λ¬Έμ  λ°μ
- λ²λ €μ§λ μ°λ κΈ° μ€ μ λΆλ¦¬λ°°μΆ λ μ°λ κΈ°λ μμμΌλ‘μ κ°μΉλ₯Ό μΈμ λ°μ μ¬νμ©λμ§λ§, μλͺ» λΆλ¦¬λ°°μΆ λλ©΄ κ·Έλλ‘ νκΈ°λ¬Όλ‘ λΆλ₯λμ΄ λ§€λ¦½ λλ μκ°λκΈ° λλ¬Έμ λΆλ¦¬μκ±°λ μ¬νμ  νκ²½ λΆλ΄ λ¬Έμ λ₯Ό μ€μΌ μ μλ λ°©λ²
- Deep Learningμ ν΅ν΄ μ°λ κΈ°λ€μ μλμΌλ‘ λΆλ₯ν  μ μλ λͺ¨λΈ κ°λ° 

</br>


### β Development Environment
- GPU : Nvidia Tesla V100
- OS : Linux Ubuntu 18.04
- Runtime : Python 3.8.5
- Main Dependency : Yolov5, MMdetection, Detectron2, Pytorch 1.7.1, OpenCV 4.5.1

</br>

### πΎ Dataset
![image](https://user-images.githubusercontent.com/82289435/161486061-946f9820-1580-4d0f-a14a-90a9a56181de.png)

- μ μ²΄ μ΄λ―Έμ§ κ°μ : 9754μ₯
- 10 class : General trash, Paper, Paper pack, Metal, Glass, Plastic, Styrofoam, Plastic bag, Battery, Clothing
- μ΄λ―Έμ§ ν¬κΈ° : (1024, 1024)
- νμ΅λ°μ΄ν°λ 4883μ₯, νκ°λ°μ΄ν°λ 4871μ₯μΌλ‘ λ¬΄μμ μ μ 
    - νκ°λ°μ΄ν°: Public 50%, Private 50%

### π Metrics
![image](https://user-images.githubusercontent.com/82289435/161477648-d18e5abc-73f4-478e-b358-ca3ba157ed7c.png)
![image](https://user-images.githubusercontent.com/82289435/161477607-9c6bf2fa-f7bf-473f-8138-e98af5954d83.png)
![image](https://user-images.githubusercontent.com/82289435/161477693-2f92d386-63dd-4329-bd61-3e1a76db3dea.png)

- mAP50 (Mean Average Precision)
    - Object Detectionμμ μ¬μ©νλ λνμ μΈ μ±λ₯ μΈ‘μ  λ°©λ²
    - Ground Truth λ°μ€μ Prediction λ°μ€κ° IoU(Intersection Over Union, Detectorμ μ νλλ₯Ό νκ°νλ μ§ν)κ° 50μ΄ λλ μμΈ‘μ λν΄ TrueλΌκ³  νλ¨

</br>

### π§ͺ Model Experiments 
### [![Notion](https://img.shields.io/badge/Notion-%23000000.svg?style=for-the-badge&logo=notion&logoColor=white)](https://seemly-newsstand-e49.notion.site/12ea90961aca491ca3a1ff96f26b8717?v=267b6ef3fb264f04934615147e48b912)



### π¬ Ensemble Experiments
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

### π’ Presentation
[νμ΄νμ΄ν_λ°νμλ£.pdf](https://drive.google.com/file/d/1bfRf1bF_aiKwZ2HiWMXdvXdljhdWaMaS/view?usp=sharing)

</br>

<hr>

### π© Pre-Commit Installation Guide (by yoonghee)
0. μλ λͺλ Ήμ΄λ₯Ό λ¦¬λμ€ κΈ°λ³Έ shellμμ μ€νν©λλ€.
<br/><br/>

1. pre-commit μ€μΉ
```
$ pip install pre-commit
$ brew install pre-commit
```
<br/>




2. λ²μ  νμΈ
```
$ pre-commit --v
pre-commit 2.17.0
```
<br/>

3. μ€μΉ νμΈ λ° μλ°μ΄νΈ
```
$ pre-commit autoupdate
[WARNING] The 'rev' field.......
```
<br/>

4. μ€μΉ
```
$ pre-commit install
pre-commit installed at .git/hooks/pre-commit
```
<br/>

5. μ΄ν commitλΆν° μ€ν  ν¬λ§€ν λ°μ
- fixλ μ¬ν­ μμ μ git statusλ₯Ό ν΅ν΄ modified νμΈ ν λ€μ add & commit

<br/>