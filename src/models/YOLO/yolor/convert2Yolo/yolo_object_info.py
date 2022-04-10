# -*-coding:utf-8-*-

import os
import argparse

from object_format import COCO, YOLO

parser = argparse.ArgumentParser(description='label Converting example.')
parser.add_argument('--img_path', type=str, help='directory of image folder')
parser.add_argument('--label', type=str,
                    help='directory of label folder or label file path')
parser.add_argument('--convert_output_path', type=str,
                    help='directory of label folder')
parser.add_argument('--cls_list_file', type=str,
                    help='directory of *.names file', default="./")


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
            flag, data = yolo.save(data, config["output_path"])

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
        "output_path": args.convert_output_path,
        "cls_list": args.cls_list_file,
    }

    main(config)
