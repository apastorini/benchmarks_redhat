import pandas as pd

from parser.parse_xml2 import parse_profiles


def save_to_csv(data, filename='profile_rules.csv'):
    df = pd.DataFrame(data)
    df = df.sort_values(by=['Profile Title', 'Counter'])
    df.to_csv(filename, index=False)

if __name__ == '__main__':
    file_path = '../data/CIS_Red_Hat_Enterprise_Linux_8_Benchmark_v1.0.1-xccdf.xml'
    data = parse_profiles(file_path)
    save_to_csv(data)
    print(f"Profile rules saved to profile_rules.csv")
