import lxml.etree as ET
import pandas as pd


#Parece que hay un problema con el archivo XML en la línea 4564, columna 220. El archivo no está bien formado, lo que causa un error de análisis. Vamos a intentar solucionar esto.
#Para proceder, necesitamos limpiar el archivo XML o intentar leerlo ignorando las entidades no válidas. Aquí tienes un enfoque para manejar posibles errores en el XML:
# Parse the XML file with error handling
parser = ET.XMLParser(recover=True)
tree = ET.parse('./data/CIS_Red_Hat_Enterprise_Linux_8_Benchmark_v1.0.1-xccdf.xml', parser)
root = tree.getroot()

# Extract and list all the rule ids and descriptions
rules = []
for rule in root.findall('.//{http://checklists.nist.gov/xccdf/1.2}Rule'):
    rule_id = rule.get('id')
    title = rule.find('{http://checklists.nist.gov/xccdf/1.2}title').text
    description = rule.find('{http://checklists.nist.gov/xccdf/1.2}description').text if rule.find('{http://checklists.nist.gov/xccdf/1.2}description') is not None else "No description"
    rules.append((rule_id, title, description))

# Convert to DataFrame for easier display and handling
df = pd.DataFrame(rules, columns=['Rule ID', 'Title', 'Description'])

# Save to a CSV file for easier review
df.to_csv('./data/benchmark_rules.csv', index=False)

print("Rules have been extracted and saved to 'benchmark_rules.csv'.")
