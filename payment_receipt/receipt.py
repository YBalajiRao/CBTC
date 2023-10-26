from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet

# Create a PDF receipt
def create_payment_receipt(pdf_filename, customer_name, transaction_details):
    # Create a PDF document
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)

    # Create a flowable object to store the elements of the PDF
    elements = []

    # Add a title
    title = "Payment Receipt"
    elements.append(Paragraph(title, getSampleStyleSheet()['Title']))

    # Add a spacer
    elements.append(Spacer(1, 12))

    # Add customer name
    elements.append(Paragraph(f"Customer: {customer_name}", getSampleStyleSheet()['Normal']))

    # Add transaction details in a table
    data = [["Description", "Amount"]]
    for description, amount in transaction_details:
        data.append([description, amount])

    table = Table(data, colWidths=[350, 100])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    elements.append(table)

    # Build the PDF document
    doc.build(elements)

if __name__ == "__main__":
    # Sample data
    receipt_data = [
        ("Product 1", "$50.00"),
        ("Product 2", "$30.00"),
        ("Tax", "$7.00"),
        ("Total", "$87.00"),
    ]

    create_payment_receipt("payment_receipt.pdf", "John Doe", receipt_data)
