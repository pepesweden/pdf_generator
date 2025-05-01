from fpdf import FPDF
import io

def generate_pdf(text: str) -> bytes:
    print("Text som skickas in:", text) #Kontrollerar att text variavlen innegåller något"
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, text)

    # Spara som bytes i minnet
    output = io.BytesIO()
    pdf_string = pdf.output(dest='S').encode('latin1')
    print("📄 PDF-genererad, antal bytes:", len(pdf_string))  # <- kontroll av längden på strängen in i PDF
    return pdf_string

#text = input("Skriv in text som ska sparas i PDF: ")
#filename = input("Skriv in filnamn, glöm inte .pdf: ")

# Testkörning
if __name__ == "__main__":
    pdf_string = generate_pdf(text)
    with open(filename, "wb") as f:
        f.write(pdf_string)
    print("✅ PDF sparad som: " + filename)
