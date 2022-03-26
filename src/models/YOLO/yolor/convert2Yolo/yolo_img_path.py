# -*-coding:utf-8-*-

import os
import argparse

from img_path_format import COCO, YOLO

parser = argparse.ArgumentParser(description='label Converting example.')
parser.add_argument('--img_path', type=str, help='directory of image folder',
                    default='../data/image/train')
parser.add_argument('--label', type=str,
                    help='directory of label folder or label file path')
parser.add_argument('--img_type', type=str, help='type of image', default=".jpg")
parser.add_argument('--output_path', type=str,
                    help='directory of manifest file', default="../data/image_path")
parser.add_argument('--cls_list_file', type=str, default="../data/coco.names",
                    help='directory of *.names file')


args = parser.parse_args()


def main(config):

    coco = COCO()

    flag, data, cls_hierarchy = coco.parse(
        config["label"], config["img_path"])

    yolo = YOLO(os.path.abspath(
        config["cls_list"]), cls_hierarchy=cls_hierarchy)

    if flag == True:
        flag, data = yolo.generate(data)

        if flag == True:
            flag, data = yolo.save(data, config["img_path"],
                                    config["img_type"], config["output_path"], config["file_name"])

            if flag == False:
                print("Saving Result : {}, msg : {}".format(flag, data))

        else:
            print("YOLO Generating Result : {}, msg : {}".format(flag, data))

    else:
        print("COCO Parsing Result : {}, msg : {}".format(flag, data))

if __name__ == '__main__':

    config = {
        "img_path": args.img_path,
        "label": args.label,
        "img_type": args.img_type,
        "output_path": args.output_path,
        "cls_list": args.cls_list_file,
        "file_name": args.label.split('/')[-1].split('.')[0]
    }

    main(config)
