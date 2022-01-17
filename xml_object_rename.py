import argparse
import os
import glob
from _XML import XML


def rename_xml(xml_file: str, old_name: str, new_name: str):
    tree = XML.parse_tree(xml_file)
    for obj in tree['objects']:
        name = obj['name']
        if name.text == old_name:
            name.text = new_name
    return tree['tree']


def args_input():
    parser = argparse.ArgumentParser(description="Renames object to new name in xml")
    parser.add_argument("-f", "--folder", default="images", help="Specify folder from runnable")
    parser.add_argument("-o", "--old", help="Specify object name")
    parser.add_argument("-n", "--new", help="Specify new object name")
    return parser.parse_args()


def main():
    args = args_input()
    path = os.path.join(os.getcwd(), args.folder)
    old_name = args.old
    new_name = args.new
    xml_files = glob.glob(path + '/*.xml')
    length = len(xml_files)
    if length == 0:
        raise Exception("No files provided")
    print(f'Calling script with for {length} files: ')
    print(f'path = {path}')
    print(f'renaming "{old_name}" to "{new_name}"')

    for xml_file in xml_files:
        rename_xml(xml_file, old_name, new_name).write(xml_file)
    print(f'Successfully renamed objects in xml\'s')


main()
