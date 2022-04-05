## Overview

여러 submission.csv를 ensemble한 result.csv를 생성하는 폴더입니다.  

## prepare ensemble
1. ensemble할 csv파일을 submisson_files에 넣어 줍니다.
```
submission_files = ['submission_faster_rcnn.csv', 'submission_yolo']
```
2. 각 모델에 적용할 가중치를 지정합니다 default = 1
```
# 아래의 경우 faster_rcnn에 가중치를 좀 더 주어 WBF를 하게됩니다.
weights = [1.2, 1]
```
3. iou value tunning
- 두 모델의 겹치는 박스의 iou를 계산하여 iou가 iou_thr보다 크면 get_weighted_box (boxes, conf_type = 'avg') 함수를 통해 두 박스가 융합됩니다
- 그러므로 iou값이 낮을수록 많은 box들이 융합되게 됩니다.
```
boxes, scores, labels = weighted_boxes_fusion(boxes_list, scores_list, labels_list, weights=weights, iou_thr=0.65)
``` 