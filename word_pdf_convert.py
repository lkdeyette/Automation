import os
from docx import Document
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        pass

    def footer(self):
        pass

def sanitize_text(text):
    # Replace special characters with ASCII equivalents
    replacements = {
        '\u2018': "'",  # Left single quotation mark
        '\u2019': "'",  # Right single quotation mark
        '\u201C': '"',  # Left double quotation mark
        '\u201D': '"',  # Right double quotation mark
    }
    for original, replacement in replacements.items():
        text = text.replace(original, replacement)
    return text

def convert_word_to_pdf(word_file, output_folder, pdf_file_name):
    print(f"Loading Word document from: {word_file}")
    doc = Document(word_file)
    print("Word document loaded successfully.")

    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=11)

    line_height = 5
    max_page_height = 270
    current_height = 10

    for para in doc.paragraphs:
        text_lines = para.text.split('\n')
        for line in text_lines:
            sanitized_line = sanitize_text(line)
            if current_height + line_height > max_page_height:
                print("Content exceeds one page height. Trimming the text.")
                break

            pdf.multi_cell(0, line_height, sanitized_line)
            current_height += line_height
            print("Added line to PDF.")

    pdf_file_path = os.path.join(output_folder, f"{pdf_file_name}.pdf")
    if os.path.exists(pdf_file_path):
        os.remove(pdf_file_path)
        print(f"Removed existing PDF file: {pdf_file_path}")

    pdf.output(pdf_file_path)
    print(f"PDF saved successfully at: {pdf_file_path}")

if __name__ == "__main__":
    word_file_name = "Lincoln K D Cover Letter.docx"
    word_file_path = os.path.join(r"C:\Users\Meanie\Desktop\Lincoln\Resume & CL", word_file_name)
    output_folder_path = r"C:\Users\Meanie\Desktop\Lincoln\Resume & CL"
    pdf_file_name = "Lincoln K D Cover Letter"

    print("Starting the conversion process...")
    convert_word_to_pdf(word_file_path, output_folder_path, pdf_file_name)
    print("Conversion process completed.")
