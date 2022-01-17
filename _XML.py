import xml.etree.ElementTree as ElementTree
from typing import Optional, Dict


class XML:

    @staticmethod
    def get_box(obj_elem: ElementTree.Element) -> Dict[str, Optional[ElementTree.Element]]:
        bndbox_elem = obj_elem.find("bndbox")
        return {
            "xmin": bndbox_elem.find("xmin"),
            "ymin": bndbox_elem.find("ymin"),
            "xmax": bndbox_elem.find("xmax"),
            "ymax": bndbox_elem.find("ymax"),
            "name": obj_elem.find('name'),
        }

    @staticmethod
    def parse_tree(xml_file: str):
        tree = ElementTree.parse(xml_file)
        root = tree.getroot()
        size = root.find("size")
        return {
            "tree": tree,
            "width": size.find("width"),
            "height": size.find("height"),
            "objects": [XML.get_box(obj_elem) for obj_elem in root.findall("object")],
            "filename": root.find('filename'),
        }
