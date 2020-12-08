from xml.etree import ElementTree

tree = ElementTree.parse("example.xml")
root = tree.getroot()
# use root = ElementTree.fromstring(string_xml_data) to parse from str

#print(root)
#print(root.tag, root.attrib)

#for child in root:
    #print(child.tag, child.attrib)

#print(root[0][0].text)

#for element in root.iter("scores"):
#    scores_sum = 0
#    for child in element:
#        scores_sum += float(child.text)
#    print(scores_sum)

#tree.write("example_cope.xml")

greg = root[0]
module1 = next(greg.iter("module1"))
print(module1, module1.text)
module1.text = str(float(module1.text) + 30)
print(module1, module1.text)

tree.write("example.modified.xml")

