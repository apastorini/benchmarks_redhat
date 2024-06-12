import os
import importlib
from classes import ComplianceCheck


def main():
    # Directorio del paquete 'checks'
    checks_dir = os.path.join(os.path.dirname(__file__), 'checks')

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
                if check_instance.check():
                    print(f"Compliance check '{check_instance.title}' ({check_instance.number}) passed: {check_instance.passed}")
                else:
                    print(f"Compliance check '{check_instance.title}' ({check_instance.number}) passed: {check_instance.passed}")

if __name__ == '__main__':
    main()
