import os
import importlib
from reports.generate_html import generate_html_report
from reports.generate_pdf_report import generate_pdf_report


def main():
    # Directorio del paquete 'checks'
    checks_dir = os.path.join(os.path.dirname(__file__), 'checks')

    checks = []

    # Recorrer archivos .py en el paquete 'checks'
    for filename in os.listdir(checks_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = filename[:-3]  # Eliminar la extensión .py
            module = importlib.import_module(f'checks.{module_name}')

            # Obtener la clase de verificación (suponemos que hay una sola clase por archivo)
            check_class = None
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if isinstance(attr, type) and issubclass(attr, ComplianceCheck) and attr is not ComplianceCheck:
                    check_class = attr
                    break

            if check_class:
                check_instance = check_class()
                checks.append(check_instance)

    # Ordenar los checks por el número
    checks.sort(key=lambda x: x.number)

    # Ejecutar y mostrar los checks
    results = []
    for check in checks:
        result = check.check()
        results.append({
            'TITLE': check.title,
            'NUMBER': check.number,
            'COMMANDS': check.command,
            'PROFILE': check.profile,
            'DESCRIPTION': check.description,
            'PASSED': check.passed
        })
        print(f"Compliance check '{check.title}' ({check.number}) passed: {check.passed}")

    # Generar reporte HTML
    generate_html_report(results)
    # Generate PDF report
    generate_pdf_report(results)


if __name__ == '__main__':
    from classes.compliance_check import ComplianceCheck
    main()
