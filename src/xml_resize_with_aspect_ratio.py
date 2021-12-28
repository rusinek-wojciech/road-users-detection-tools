import argparse
import os
import glob
import xml.etree.ElementTree as ET


def formal_xml(xml_file, new_width: int, new_height: int):
    print(xml_file)
    tree = ET.parse(xml_file)
    root = tree.getroot()
    size = root.find('size')
    width = size.find('width')
    height = size.find('height')

    width_num = int(width.text)
    height_num = int(height.text)

    x_scale = width_num / new_width
    y_scale = height_num / new_height

    if x_scale >= y_scale:
        new_width_num = new_width
        new_height_num = int(height_num / x_scale)
        scale = 1.0 / x_scale
    else:
        new_width_num = int(width_num / y_scale)
        new_height_num = new_height_num
        scale = 1.0 / y_scale


    width.text = str(new_width_num)
    height.text = str(new_height_num)
    object = root.findall('object')
    for obj in object:
        bndbox = obj.find('bndbox')
        xmin = bndbox.find('xmin')
        ymin = bndbox.find('ymin')
        xmax = bndbox.find('xmax')
        ymax = bndbox.find('ymax')
        xmin.text = str(int(int(xmin.text) * scale))
        ymin.text = str(int(int(ymin.text) * scale))
        xmax.text = str(int(int(xmax.text) * scale))
        ymax.text = str(int(int(ymax.text) * scale))
    
    tree.write(xml_file)


def args_input():
    parser = argparse.ArgumentParser(description="Give scale and folder to format xml")
    parser.add_argument("-f", "--folder", default="images", help="Specify folder from runnable")
    parser.add_argument("-wi", "--width", help="Specify width")
    parser.add_argument("-he", "--height", help="Specify height")
    return parser.parse_args()


def main():
    args = args_input()
    width = int(args.width)
    height = int(args.height)

    image_path = os.path.join(os.getcwd(), args.folder)
    print('Calling script with: ')
    print(f'width = {width}px')
    print(f'height = {height}px')
    print(f'path = {image_path}')

    xmls = glob.glob(image_path + '/*.xml')
    length = len(xmls)
    if length == 0:
        raise Exception("No files provided")

    for xml_file in xmls:
        formal_xml(xml_file, width, height)
    print(f'Successfully scaled {length} xml')


main()

