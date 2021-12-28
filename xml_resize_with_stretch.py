import argparse
import os
import glob
from _XML import XML


def format_xml(xml_file: str, new_width: int, new_height: int):
    tree = XML.parse_tree(xml_file)
    x_scale = new_width / int(tree["width"].text)
    y_scale = new_height / int(tree["height"].text)
    tree["width"].text = str(new_width)
    tree["height"].text = str(new_height)
    for obj in tree["objects"]:
        obj["xmin"].text = str(int(int(obj["xmin"].text) * x_scale))
        obj["ymin"].text = str(int(int(obj["ymin"].text) * y_scale))
        obj["xmax"].text = str(int(int(obj["xmax"].text) * x_scale))
        obj["ymax"].text = str(int(int(obj["ymax"].text) * y_scale))
    return tree["tree"]


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
