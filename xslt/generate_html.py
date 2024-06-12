import lxml.etree as ET

# Cargar el archivo XML
xml_path = '../data/CIS_Red_Hat_Enterprise_Linux_8_Benchmark_v1.0.1-xccdf.xml'
xslt_path = 'benchmark_final.xslt'
output_html = 'output.html'

# Parsear el archivo XML y XSLT
xml_tree = ET.parse(xml_path)
xslt_tree = ET.parse(xslt_path)

# Crear un transformador XSLT
transform = ET.XSLT(xslt_tree)

# Aplicar la transformación
result_tree = transform(xml_tree)

# Guardar el resultado en un archivo HTML
with open(output_html, 'wb') as f:
    f.write(ET.tostring(result_tree, pretty_print=True, method='html'))

print(f'Transformación completada. Archivo HTML guardado como {output_html}')
