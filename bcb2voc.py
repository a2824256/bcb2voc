from xml.dom import minidom
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
from xml.etree.ElementTree import ElementTree
import cv2
import os

XML_PATH = './xml'
IMG_PATH = 'JPEGImages'
LABEL_PATH = 'test.txt'
# img_shape 0:height 1:width 2:channels
def create_xml(img_name, line_arr, path):
    root = Element('annotation')
    node1_folder = SubElement(root, 'folder')
    node1_folder.text = path
    node1_filename = SubElement(root, 'filename')
    node1_filename.text = img_name
    node1_path = SubElement(root, 'path')
    file_path = os.path.join(path, img_name)
    node1_path.text = file_path
    node1_source = SubElement(root, 'source')
    node2_database = SubElement(node1_source, 'database')
    node2_database = 'Unknown'
    node1_size = SubElement(root, 'size')
    img = cv2.imread(file_path)
    node2_width = SubElement(node1_size, 'width')
    node2_width.text = str(img.shape[1])
    node2_height = SubElement(node1_size, 'height')
    node2_height.text = str(img.shape[0])
    node2_depth = SubElement(node1_size, 'depth')
    node2_depth.text = str(img.shape[2])


if __name__ == '__main__':
    # 图片文件夹
    img_path = os.path.join('.', IMG_PATH)
    # label集合
    labels = {}
    # 分类集合
    classes = []
    # 打开标注文件
    with open(LABEL_PATH, 'r') as f:
        # 行迭代
        for line in f:
            # 去换行符
            line_arr = line.replace('\n', '').split(" ")
            # 判断分类是否已添加到classes
            if line_arr[1] not in classes:
                classes.append(line_arr[1])
            # 判断刚文件是否已经存在labels中
            if line_arr[0] in labels:
                labels[line_arr[0]].append(line_arr[1:])
            else:
                labels[line_arr[0]] = []
                labels[line_arr[0]].append(line_arr[1:])
        # 以文件名来进行迭代
        for file in labels:
            print(labels[file])
            create_xml(file, labels[file], img_path)


