import lxml.etree as ET
import pandas as pd
import argparse

def extract_values_and_rules(file_path, profile_filter=None):
    tree = ET.parse(file_path)
    root = tree.getroot()
    namespaces = {
        'xccdf': 'http://checklists.nist.gov/xccdf/1.2'
    }

    data = []
    profile_rules = {}

    # Parse values to find their title and value content
    values_dict = {}
    for value in root.findall('.//xccdf:Value', namespaces):
        value_id = value.get('id')
        title_elem = value.find('xccdf:title', namespaces)
        value_elem = value.find('xccdf:value', namespaces)
        if title_elem is not None and value_elem is not None:
            value_object = {
                'value_elem': value_elem.text.strip(),
                'title_elem': title_elem.text.strip(),
                'rule_titles': []
            }
            values_dict[value_id] = value_object

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

            # Get the value associated with the rule using <check-export>
            value_id = ''
            value_title = ''
            value = ''
            check_export = rule.find('.//xccdf:check-export', namespaces)
            if check_export is not None:
                value_id = check_export.get('value-id')
                if value_id in values_dict:
                    value_title = values_dict[value_id]['title_elem']
                    value = values_dict[value_id]['value_elem']

            # Filter by profile if profile_filter is provided
            if profile_filter:
                if profile_filter in profiles.split(', '):
                    data.append({
                        'Rule Title': rule_title,
                        'Rule ID': rule_id,
                        'Group ID': group_id,
                        'Profiles': profiles,
                        'Value Title': value_title,
                        'Value': value,
                        'Value ID': value_id
                    })
            else:
                data.append({
                    'Rule Title': rule_title,
                    'Rule ID': rule_id,
                    'Group ID': group_id,
                    'Profiles': profiles,
                    'Value Title': value_title,
                    'Value': value,
                    'Value ID': value_id
                })

    return data

def save_to_csv(data, filename='values_rules_groups_profiles.csv', profile_filter=None):
    df = pd.DataFrame(data)
    if profile_filter:
        df = df.reset_index(drop=True)
        df.index += 1
        df.index.name = 'Counter'
    df.to_csv(filename, index=profile_filter is not None, sep=';')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Extract values, rules, and profiles from an XCCDF XML file.")
    parser.add_argument('--profile', type=str, help='Profile name to filter by')
    args = parser.parse_args()

    file_path = '../data/CIS_Red_Hat_Enterprise_Linux_8_Benchmark_v1.0.1-xccdf.xml'
    data = extract_values_and_rules(file_path, profile_filter=args.profile)
    output_filename = 'values_rules_groups_profiles.csv' if not args.profile else f'values_rules_groups_profiles_{args.profile}.csv'
    save_to_csv(data, filename=output_filename, profile_filter=args.profile)
    print(f"Values, rules, groups, and profiles saved to {output_filename}")
