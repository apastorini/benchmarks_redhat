import lxml.etree as ET
import pandas as pd

def extract_values_and_rules(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    namespaces = {
        'xccdf': 'http://checklists.nist.gov/xccdf/1.2'
    }

    data = []
    profile_rules = {}

    # Parse profiles to find rules associated with each profile
    for profile in root.findall('.//xccdf:Profile', namespaces):
        profile_id = profile.get('id')
        profile_title = profile.find('xccdf:title', namespaces).text.strip() if profile.find('xccdf:title', namespaces) is not None else profile_id

        for select in profile.findall('.//xccdf:select', namespaces):
            rule_id = select.get('idref')
            if rule_id not in profile_rules:
                profile_rules[rule_id] = []
            profile_rules[rule_id].append(profile_title)

    # Iterate over each Group element
    for group in root.findall('.//xccdf:Group', namespaces):
        group_id = group.get('id')

        # Iterate over each Rule element within the Group
        for rule in group.findall('.//xccdf:Rule', namespaces):
            rule_id = rule.get('id')

            # Find the title associated with the Rule
            rule_title_elem = rule.find('xccdf:title', namespaces)
            rule_title = rule_title_elem.text.strip() if rule_title_elem is not None else ''

            # Get profiles associated with this rule
            profiles = ', '.join(profile_rules.get(rule_id, []))

            data.append({
                'Title': rule_title,
                'Rule ID': rule_id,
                'Group ID': group_id,
                'Profiles': profiles
            })

    return data

def save_to_csv(data, filename='values_rules_groups_profiles.csv'):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, sep=';')

if __name__ == '__main__':
    file_path = '../data/CIS_Red_Hat_Enterprise_Linux_8_Benchmark_v1.0.1-xccdf.xml'
    data = extract_values_and_rules(file_path)
    save_to_csv(data)
    print(f"Values, rules, groups, and profiles saved to values_rules_groups_profiles.csv")
