import lxml.etree as ET


def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    namespaces = {
        'xccdf': 'http://checklists.nist.gov/xccdf/1.2'
    }

    rules = []

    for rule in root.findall('.//xccdf:Rule', namespaces):
        rule_id = rule.get('id')
        description = rule.find('xccdf:description', namespaces).text.strip()
        commands = []
        for check in rule.findall('.//xccdf:check/xccdf:check-content-ref', namespaces):
            command = check.get('name')
            if command:
                commands.append(command)

        rules.append({
            'Check ID': rule_id,
            'Description': description,
            'Commands': ' && '.join(commands)
        })

    return rules


if __name__ == '__main__':
    rules = parse_xml('../data/CIS_Red_Hat_Enterprise_Linux_8_Benchmark_v1.0.1-xccdf.xml')
    for rule in rules:
        print(rule)
