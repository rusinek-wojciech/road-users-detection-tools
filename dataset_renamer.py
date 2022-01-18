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
    parser = argparse.ArgumentParser(description="Renames all files in folder")
    parser.add_argument("-f", "--folder", default="images", help="Specify folder from runnable")
    parser.add_argument("-r", "--result", default="", help="Specify result folder")
    parser.add_argument("-n", "--name", default="IMG_", help="Specify folder from runnable")
    return parser.parse_args()


def main():
    args = args_input()
    path = os.path.join(os.getcwd(), args.folder)
    name = args.name
    result = path if args.result == '' else args.result
    xml_files = glob.glob(path + '/*.xml')
    img_files = glob.glob(path + '/*.jpg')

    if len(xml_files) == 0 or len(img_files) == 0 or (len(xml_files) != len(img_files)):
        raise Exception("Invalid data provided")
    print(f'Calling script with for {len(xml_files)} files: ')
    print(f'path = {path} {result}')

    for i in range(len(xml_files)):
        os.rename(img_files[i], result + os.path.sep + name + str(i + 1) + ".jpg")
        os.rename(xml_files[i], result + os.path.sep + name + str(i + 1) + ".xml")

    print(f'Successfully renamed all')

main()
