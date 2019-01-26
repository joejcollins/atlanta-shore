import lxml.etree as ET

dom = ET.parse("./data/raw/quadrats.gpx")
xslt = ET.parse("./data/raw/waypoint.xslt")
transform = ET.XSLT(xslt)
newdom = transform(dom)
print(ET.tostring(newdom, pretty_print=True))