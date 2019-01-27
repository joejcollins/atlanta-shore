
import lxml.etree as ET


def transform(file_path_in):
    dom = ET.parse("file_path_in")
    xslt = ET.parse("add_id_to_waypoints.xslt")
    transform = ET.XSLT(xslt)
    newdom = transform(dom)
    file_transformed = ET.tostring(newdom, pretty_print=True)
    outfile = open("./data/raw/quadrats-with-descriptions.gpx", 'a')
    outfile.write(file_transformed)
