import lxml.etree as ET
import pandas as pd


def parse_profiles_and_values(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    namespaces = {
        'xccdf': 'http://checklists.nist.gov/xccdf/1.2'
    }

    data = []
    profile_counters = {}

    # Parse values
    values = {}
    for value in root.findall('.//xccdf:Value', namespaces):
        value_id = value.get('id')
        title_elem = value.find('xccdf:title', namespaces)
        value_elem = value.find('xccdf:value', namespaces)
        desc_elem = value.find('xccdf:description', namespaces)

        values[value_id] = {
            'Value Title': title_elem.text.strip() if title_elem is not None else "",
            'Value': value_elem.text.strip() if value_elem is not None else "",
            'Value Description': desc_elem.text.strip() if desc_elem is not None else ""
        }

    # Parse profiles and rules
    for profile in root.findall('.//xccdf:Profile', namespaces):
        profile_id = profile.get('id')
        profile_title = profile.find('xccdf:title', namespaces).text.strip() if profile.find('xccdf:title',
                                                                                             namespaces) is not None else profile_id

        if profile_id not in profile_counters:
            profile_counters[profile_id] = 0

        for select in profile.findall('.//xccdf:select', namespaces):
            rule_id = select.get('idref')
            selected = select.get('selected') == 'true'

            profile_counters[profile_id] += 1

            # Find the rule by ID and extract associated values
            rule = root.find(f".//xccdf:Rule[@id='{rule_id}']", namespaces)
            rule_values = {'Value Title': '', 'Value': '', 'Value Description': ''}

            if rule is not None:
                for set_value in rule.findall('.//xccdf:set-value', namespaces):
                    value_id = set_value.get('idref')
                    if value_id in values:
                        rule_values = values[value_id]
                        break

            data.append({
                'Counter': profile_counters[profile_id],
                'Profile Title': profile_title,
                'Profile ID': profile_id,
                'Rule ID': rule_id,
                'Selected': selected,
                'Value Title': rule_values['Value Title'],
                'Value': rule_values['Value'],
                'Value Description': rule_values['Value Description']
            })

    return data


def save_to_csv(data, filename='profile_rules.csv'):
    df = pd.DataFrame(data)
    df = df.sort_values(by=['Profile Title', 'Counter'])
    df.to_csv(filename, index=False)


if __name__ == '__main__':
    file_path = '../data/CIS_Red_Hat_Enterprise_Linux_8_Benchmark_v1.0.1-xccdf.xml'
    data = parse_profiles_and_values(file_path)
    save_to_csv(data)
    print(f"Profile rules saved to profile_rules.csv")
