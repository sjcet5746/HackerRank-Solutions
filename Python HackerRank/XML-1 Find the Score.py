#Written by Gskd
import sys
import xml.etree.ElementTree as etree
def get_attr_number(node):
    total = 0
    for elem in node.iter():
        score = len(elem.attrib)
        total += score
    return total
if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
