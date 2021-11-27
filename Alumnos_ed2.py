import xml.etree.cElementTree as et 

root = et.Element("UTC")
root = et.Element("Alumnosdeledificio2")
se = et.SubElement (root, "RedesInteligentes")
et.SubElement(se, "Nombre").text="Jose Hernando Vazquez Gomez"
et.SubElement(se, "Matricula").text="18040162"

root = et.Element("Alumnosdeledificio2")
se = et.SubElement (root, "RedesInteligentes")
et.SubElement(se, "Nombre").text="Jose Palacios Herrera"
et.SubElement(se, "Matricula").text="18040000"


root = et.Element("Alumnosdeledificio2")
se = et.SubElement (root, "Multimedia")
et.SubElement(se, "Nombre").text="Adriana Carrillo Santamaria"
et.SubElement(se, "Matricula").text="18040189"

root = et.Element("Alumnosdeledificio2")
se = et.SubElement (root, "Multimedia")
et.SubElement(se, "Nombre").text="Rosa Vazquez Gomez"
et.SubElement(se, "Matricula").text="18040677"


root = et.Element("Alumnosdeledificio2")
se = et.SubElement (root, "ProgramacionOP")
et.SubElement(se, "Nombre").text="Claudia Montelongo Garcia"
et.SubElement(se, "Matricula").text="18040006"

root = et.Element("Alumnosdeledificio2")
se = et.SubElement (root, "ProgramacionOP")
et.SubElement(se, "Nombre").text="Jose Hernando Vazquez Gomez"
et.SubElement(se, "Matricula").text="18040020"


tree = et.ElementTree(root)
tree.write("Alumnos.xml", xml_declaration=True)
