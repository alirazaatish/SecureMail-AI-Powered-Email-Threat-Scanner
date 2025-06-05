from fpdf import FPDF

class PDFReport(FPDF):
    def header(self):
        # Add a title with a line below
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Phishing Detection Report", ln=True, align="C")
        self.set_line_width(0.5)
        self.line(10, 22, 200, 22)
        self.ln(10)
    
    def footer(self):
        # Add page number at bottom center
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

def generate_pdf(file_name, keywords, urls):
    pdf = PDFReport()
    pdf.add_page()
    
    # File info
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"Scanned File: {file_name}", ln=True)
    pdf.ln(5)
    
    # Phishing Keywords Section
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Detected Phishing Keywords:", ln=True)
    pdf.set_font("Arial", "", 12)
    if keywords:
        pdf.multi_cell(0, 10, ", ".join(keywords))
    else:
        pdf.cell(0, 10, "None", ln=True)
    pdf.ln(5)
    
    # Suspicious URLs Section
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Suspicious URLs Found:", ln=True)
    pdf.set_font("Arial", "", 12)
    if urls:
        for url in urls:
            pdf.multi_cell(0, 10, url)
    else:
        pdf.cell(0, 10, "None", ln=True)
    
    # Save the PDF
    pdf_file = "phishing_report.pdf"
    pdf.output(pdf_file)
    return pdf_file
