import lxml.etree as ET
import pandas as pd

def parse_profiles(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    namespaces = {
        'xccdf': 'http://checklists.nist.gov/xccdf/1.2'
    }

    data = []
    profile_counters = {}

    for profile in root.findall('.//xccdf:Profile', namespaces):
        profile_id = profile.get('id')
        profile_title = profile.find('xccdf:title', namespaces).text.strip() if profile.find('xccdf:title', namespaces) is not None else profile_id

        if profile_id not in profile_counters:
            profile_counters[profile_id] = 0

        for select in profile.findall('.//xccdf:select', namespaces):
            rule_id = select.get('idref')
            selected = select.get('selected') == 'true'

            profile_counters[profile_id] += 1
            data.append({
                'Counter': profile_counters[profile_id],
                'Profile Title': profile_title,
                'Profile ID': profile_id,
                'Rule ID': rule_id,
                'Selected': selected
            })

    return data


