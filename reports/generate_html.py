import os
import pandas as pd
from jinja2 import Environment, FileSystemLoader
import traceback

def generate_html_report(results, output_file='./generados/report.html', template_file='html_report_template.html'):
    try:
        # Crear un DataFrame de los resultados
        df = pd.DataFrame(results)

        # Obtener el directorio del paquete reports
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Configurar Jinja2 Environment con el directorio del paquete reports
        env = Environment(loader=FileSystemLoader(current_dir))
        template = env.get_template(template_file)

        # Renderizar la plantilla con los datos
        html_content = template.render(results=df.to_dict(orient='records'))

        # Crear directorio de salida si no existe
        output_dir = os.path.dirname(output_file)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Guardar el contenido HTML en un archivo
        with open(output_file, 'w') as file:
            file.write(html_content)
        print(f"Reporte HTML generado: {output_file}")
    except Exception as e:
        print(f"Error generando el reporte HTML: {e}")
        traceback.print_exc()

