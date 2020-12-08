from xml.etree import ElementTree

tree = ElementTree.parse("example.modified.xml")
root = tree.getroot()

greg = root[0]
#certificate = greg[2]
#certificate.set("type", "with distinction")

#tree.write("example.modified.xml")

#description = ElementTree.Element("description")
#description.text = "Showed excellent skills during the course"
#greg.append(description)

#tree.write("example.modified.xml")

description = greg.find("description")
greg.remove(description)
tree.write("example.modified.xml")