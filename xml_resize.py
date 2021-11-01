import os
import glob
import xml.etree.ElementTree as ET


def xml(path, scale):
    for xml_file in glob.glob(path + '/*.xml'):
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
        xmin.text = str(int(xmin.text) * scale)
        ymin.text = str(int(ymin.text) * scale)
        xmax.text = str(int(xmax.text) * scale)
        ymax.text = str(int(ymax.text) * scale)
        width.text = str(int(width.text) * scale)
        height.text = str(int(height.text) * scale)
        tree.write(xml_file)


def main():
    image_path = os.path.join(os.getcwd(), 'images')
    xml(image_path, 0.5)


main()
print('Successfully scaled xml')
