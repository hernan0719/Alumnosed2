import xml.etree.cElementTree as et
from xml.etree.ElementTree import SubElement, parse

xml_file = parse('Alumnos_ed2.xml')

root = et.Element("Alumnosdeledificio2")

xmlRoot = xml_file.getroot()

se = et.SubElement (root, "Multimedia")
et.SubElement(se, "Nombre").text="Mario Rodrigues Vallejo"
et.SubElement(se, "Matricula").text="18040188"

xmlRoot.append(se)

xml_file.write("Alumnos2.xml",xml_declaration=True)
