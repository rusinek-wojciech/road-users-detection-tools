import argparse
import os
import glob
from _XML import XML


def rename_xml(xml_file: str):
    tree = XML.parse_tree(xml_file)
    file_image = tree['filename'].text
    file_xml = os.path.split(xml_file)[-1]
    file_image_name = file_image.split(".")[0]
    file_xml_name = file_xml.split(".")[0]
    if file_image_name != file_xml_name:
        print(f"{file_xml} has invalid image: {file_image}, renaming...")
        tree['filename'].text = file_xml_name + '.jpg'
    return tree['tree']


def args_input():
    parser = argparse.ArgumentParser(description="Renames incorrect 'filename' section in xml")
    parser.add_argument("-f", "--folder", default="images", help="Specify folder from runnable")
    return parser.parse_args()


def main():
    args = args_input()
    path = os.path.join(os.getcwd(), args.folder)
    xml_files = glob.glob(path + '/*.xml')
    length = len(xml_files)
    if length == 0:
        raise Exception("No files provided")
    print(f'Calling script with for {length} files: ')
    print(f'path = {path}')

    for xml_file in xml_files:
        rename_xml(xml_file).write(xml_file)
    print(f'Successfully renamed xml\'s')


main()
