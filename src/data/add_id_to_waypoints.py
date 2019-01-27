""" Transform GPX

View Ranger doesn't read the gpx extensions so in order
to identify sample sites the id element is transformed into
a gpx field. """
import lxml.etree as ET
import os

FILES = ["trial-waypoints.gpx", "spains-hall-waypoints-regular-30m.gpx"]

def main():
    """ Transform all the files """
    for gpx_file in FILES:
        transform(gpx_file)

def transform(gpx_file):
    """ Use an xslt to add put the id in the gpx name element """
    dir_path = os.path.dirname(os.path.realpath(__file__))
    gpx_file_name = os.path.join(dir_path, "../../data/raw/" + gpx_file)
    dom = ET.parse(gpx_file_name)
    xslt_file_name = os.path.join(dir_path, "add_id_to_waypoints.xslt")
    xslt = ET.parse(xslt_file_name)
    xslt_transform = ET.XSLT(xslt)
    newdom = xslt_transform(dom)
    file_transformed = ET.tostring(newdom, pretty_print=True)
    output_file_name = gpx_file.replace(".gpx", "-with-name.gpx")
    output_file = open(output_file_name, 'w+')
    output_file.write(file_transformed)

if __name__ == "__main__":
    main()