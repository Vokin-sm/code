from xml.etree import ElementTree

tree = ElementTree.parse("exercise.xml")
root = tree.getroot()
col = dict()

col[root.attrib["color"]] = 1


def getchild(root,level):
    level += 1
    for el in root:
        if el.attrib["color"] not in col.keys():
            col[el.attrib["color"]] = level
        else:
            col[el.attrib["color"]] += level
        getchild(el, level)


getchild(root, 1)

print(col["red"])
print(col["green"])
print(col["blue"])