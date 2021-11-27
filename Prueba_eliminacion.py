from xml.etree.ElementTree import parse, Element

file_name='Alumnos.xml'
doc_xml = parse(files_name)
root = doc_xml.getroot()

root.remove(root.find('Multimedia'))

new_file = 'Alumnos3.xml'
doc_xml.write(new_file, xml_declaration=True)
