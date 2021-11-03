import os
import glob
import sys
import xml.etree.ElementTree as ET


# changing xml file parameters
def formal_xml(xml_file, scale):
    print(xml_file)
    tree = ET.parse(xml_file)
    root = tree.getroot()
    size = root.find('size')
    object = root.find('object')
    bndbox = object.find('bndbox')
    xmin = bndbox.find('xmin')
    ymin = bndbox.find('ymin')
    xmax = bndbox.find('xmax')
    ymax = bndbox.find('ymax')
    width = size.find('width')
    height = size.find('height')
    xmin.text = str(int(int(xmin.text) * scale))
    ymin.text = str(int(int(ymin.text) * scale))
    xmax.text = str(int(int(xmax.text) * scale))
    ymax.text = str(int(int(ymax.text) * scale))
    width.text = str(int(int(width.text) * scale))
    height.text = str(int(int(height.text) * scale))
    tree.write(xml_file)


def main():
    args = sys.argv
    scale = float(args[1])
    folder = str(args[2])
    image_path = os.path.join(os.getcwd(), folder)
    print('Calling script with: ')
    print(f'scale = {scale}')
    print(f'path = {image_path}')
    for xml_file in glob.glob(image_path + '/*.xml'):
        formal_xml(xml_file, scale)
    print('Successfully scaled all xml')


main()

