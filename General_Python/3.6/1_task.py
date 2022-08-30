from xml.etree import ElementTree

root = ElementTree.fromstring(input())
dictcolor = {'red': 0, 'green': 0, 'blue': 0}
dictcolor[root.attrib['color']] = 1
elements = []


def treeway(elem, level=1):
    if len(elem):
        level += 1
        for child in elem:
            dictcolor[child.attrib['color']] += level
            elements.remove(child)
            treeway(child, level)


for _ in root.iter():
    elements.append(_)
treeway(elements[0])

for value in dictcolor.values():
    print(value, end=' ')
