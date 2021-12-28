import argparse
import os
import glob
from _XML import XML


def format_xml(xml_file: str, requested_width: int, requested_height: int):
    tree = XML.parse_tree(xml_file)
    original_width = int(tree["width"].text)
    original_height = int(tree["height"].text)
    x_scale = original_width / requested_width
    y_scale = original_height / requested_height
    if x_scale >= y_scale:
        tree["width"].text = str(requested_width)
        tree["height"].text = str(int(original_height / x_scale))
        scale = 1.0 / x_scale
    else:
        tree["width"].text = str(int(original_width / y_scale))
        tree["height"].text = str(requested_height)
        scale = 1.0 / y_scale
    for obj in tree["objects"]:
        obj["xmin"].text = str(int(int(obj["xmin"].text) * scale))
        obj["ymin"].text = str(int(int(obj["ymin"].text) * scale))
        obj["xmax"].text = str(int(int(obj["xmax"].text) * scale))
        obj["ymax"].text = str(int(int(obj["ymax"].text) * scale))
    return tree["tree"]


def args_input():
    parser = argparse.ArgumentParser(description="Give scale and folder to format xml\'s")
    parser.add_argument("-f", "--folder", default="images", help="Specify folder from runnable")
    parser.add_argument("-wi", "--width", help="Specify width")
    parser.add_argument("-he", "--height", help="Specify height")
    return parser.parse_args()


def main():
    args = args_input()
    width = int(args.width)
    height = int(args.height)
    image_path = os.path.join(os.getcwd(), args.folder)
    xml_files = glob.glob(image_path + '/*.xml')
    length = len(xml_files)
    if length == 0:
        raise Exception("No files provided")
    print(f'Calling script with for {length} files: ')
    print(f'width = {width}px')
    print(f'height = {height}px')
    print(f'path = {image_path}')
    for xml_file in xml_files:
        print(xml_file)
        format_xml(xml_file, width, height).write(xml_file)
    print(f'Successfully scaled xml\'s')


main()
