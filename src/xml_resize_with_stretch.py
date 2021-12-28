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
    x_scale = new_width / int(width.text)
    y_scale = new_height / int(height.text)
    width.text = str(new_width)
    height.text = str(new_height)
    object = root.findall('object')
    for obj in object:
        bndbox = obj.find('bndbox')
        xmin = bndbox.find('xmin')
        ymin = bndbox.find('ymin')
        xmax = bndbox.find('xmax')
        ymax = bndbox.find('ymax')
        xmin.text = str(int(int(xmin.text) * x_scale))
        ymin.text = str(int(int(ymin.text) * y_scale))
        xmax.text = str(int(int(xmax.text) * x_scale))
        ymax.text = str(int(int(ymax.text) * y_scale))
    
    tree.write(xml_file)


def args_input():
    parser = argparse.ArgumentParser(description="Give scale and folder to format xml with stretch")
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

