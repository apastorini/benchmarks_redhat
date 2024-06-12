import pandas as pd
from jinja2 import Environment, FileSystemLoader
from parser.generate_benchmark_rules import (
    check_cramfs_disabled, check_squashfs_disabled, check_udf_disabled,
    check_tmp_configured, check_nodev_on_tmp, dynamic_check, check_service_running
)


def load_rules_from_csv(file_path):
    df = pd.read_csv(file_path)
    return df.to_dict(orient='records')


def render_html(template_path, output_path, context):
    env = Environment(loader=FileSystemLoader(template_path))
    template = env.get_template('report_template.html')
    html_content = template.render(context)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)


def main():
    rules = load_rules_from_csv('../data/benchmark_rules.csv')
    results = []

    for rule in rules:
        rule_id = rule['Rule ID']
        description = rule['Title']
        if rule_id == 'rule_cramfs_disabled':
            result, message = check_cramfs_disabled()
        elif rule_id == 'rule_squashfs_disabled':
            result, message = check_squashfs_disabled()
        elif rule_id == 'rule_udf_disabled':
            result, message = check_udf_disabled()
        elif rule_id == 'rule_tmp_configured':
            result, message = check_tmp_configured()
        elif rule_id == 'rule_nodev_on_tmp':
            result, message = check_nodev_on_tmp()
        elif 'service' in rule_id:
            service_name = rule_id.split('_')[-1]
            result, message = check_service_running(service_name)
        else:
            command = rule.get('Command', '').split()
            check_string = rule.get('Check String', '')
            success_message = rule.get('Success Message', 'Check passed')
            failure_message = rule.get('Failure Message', 'Check failed')
            result, message = dynamic_check(command, check_string, success_message, failure_message)

        results.append((description, result, message))

    context = {'results': results}
    render_html('../templates', 'benchmark_report.html', context)

    print("Benchmark report generated: benchmark_report.html")


if __name__ == "__main__":
    main()
