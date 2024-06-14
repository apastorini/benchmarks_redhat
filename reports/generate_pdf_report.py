import os
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Image, Spacer
from reportlab.lib import colors


def generate_pdf_report(results, output_dir='./generados'):
    # Get the current date
    current_date = datetime.now().strftime('%Y-%m-%d')

    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Create the output file path with the current date suffix
    output_file = os.path.join(output_dir, f'reporte_{current_date}.pdf')

    # Create the document
    doc = SimpleDocTemplate(output_file, pagesize=letter,
                            leftMargin=2 * cm, rightMargin=2 * cm,
                            topMargin=2 * cm, bottomMargin=2 * cm)
    elements = []

    # Add logo
    logo_path = 'ivera.png'  # Ensure this path is correct and the file exists
    if os.path.exists(logo_path):
        logo = Image(logo_path)
        logo.drawHeight = 1 * inch
        logo.drawWidth = 2 * inch
        elements.append(logo)

    # Add the title and date
    styles = getSampleStyleSheet()
    title_style = styles['Heading1']
    title = Paragraph("Compliance Report", title_style)
    elements.append(title)

    date_style = styles['Normal']
    execution_date = Paragraph(f"Execution Date: {current_date}", date_style)
    elements.append(execution_date)

    # Calculate scoring
    passed_count = sum(1 for result in results if result['PASSED'] is True)
    total_count = len(results)
    score = (passed_count / total_count * 100) if total_count > 0 else 0
    scoring = Paragraph(f"Scoring: {score:.2f}%", date_style)
    elements.append(scoring)

    # Add space
    elements.append(Spacer(1, 0.5 * cm))

    # Create the table data
    table_data = [['TITLE', 'NUMBER', 'PROFILE', 'DESCRIPTION', 'PASSED']]
    for i, result in enumerate(results):
        table_data.append([
            Paragraph(result['TITLE'], styles['BodyText']),
            result['NUMBER'],
            Paragraph(', '.join(result['PROFILE']), styles['BodyText']),
            Paragraph(result['DESCRIPTION'], styles['BodyText']),
            'Yes' if result['PASSED'] else 'No'
        ])

    # Create the table
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkcyan),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
    ])

    # Apply alternating row background colors
    for row_index in range(1, len(table_data)):
        bg_color = colors.beige if row_index % 2 == 0 else colors.lightcyan
        table_style.add('BACKGROUND', (0, row_index), (-1, row_index), bg_color)

    table = Table(table_data, colWidths=[2 * inch, 1 * inch, 1.5 * inch, 3 * inch, 0.5 * inch])
    table.setStyle(table_style)
    elements.append(table)

    # Build the PDF
    doc.build(elements)
    print(f"PDF report generated: {output_file}")

