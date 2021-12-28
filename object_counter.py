import argparse
import os
import glob
import xml.etree.ElementTree as ET


def get_classes(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    object = root.findall('object')
    names = []
    for obj in object:
        names.append(obj.find('name').text)
    return names


def args_input():
    parser = argparse.ArgumentParser(description="Count classes from xml")
    parser.add_argument("-f", "--folder", default="images", help="Specify folder from runnable")
    return parser.parse_args()


def main():
    args = args_input()

    image_path = os.path.join(os.getcwd(), args.folder)
    print('Calling script with: ')
    print(f'path = {image_path}')

    xmls = glob.glob(image_path + '/*.xml')
    length = len(xmls)
    if length == 0:
        raise Exception("No files provided")

    names = []
    for xml_file in xmls:
        names = names + get_classes(xml_file)

    set_names = set(names)
    for set_name in set_names:
        print(f"{set_name}: {names.count(set_name)}")
    print(f'Successfully printed {length} xml')


main()

