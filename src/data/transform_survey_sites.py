import lxml.etree as ET

dom = ET.parse("./data/raw/quadrats.gpx")
xslt = ET.parse("./data/raw/waypoint.xslt")
transform = ET.XSLT(xslt)
newdom = transform(dom)
infile = ET.tostring(newdom, pretty_print=True)
outfile = open("./data/raw/quadrats-with-descriptions.gpx", 'a')
outfile.write(infile)
