from datetime import datetime
from fpdf import FPDF

def calculate_birth_year(yosh):
    hozir = datetime.now().year
    t_yil = hozir - yosh
    return t_yil

# Function to generate PDF file
def generate_pdf(ism, familiya, yosh, tel):
    pdf = FPDF()
    pdf.add_page()

    # Set font and text size
    pdf.set_font("Arial", size=16)

    # Write PDF content
    pdf.cell(200, 10, f"Ismi: {ism}", 0, 1)
    pdf.cell(200, 10, f"Familiyasi: {familiya}")
    pdf.cell(200, 10, f"Yoshi: {yosh}", 0, 1)
    pdf.cell(200, 10, f"Telefon raqami: {tel}", 0, 1)

    # Save the PDF with the user's name
    pdf.output(f"{ism}.pdf")

# Prompt user for input
ism = input("Ismimnizni kiriting: ")
familiya = input("Familiyani kiriting: ")
yosh = int(input("Tug'ilgan yilingizni kiriting: "))
tel = input("Siz bilan bog'lanish uchun telefon raqamingizni kiriting: ")

ism = ism.title()
familiya = familiya.title()
tel = int(f" +998{tel} ")
yosh = calculate_birth_year(yosh)


# Generate the PDF file
generate_pdf(ism, familiya, yosh, tel)

print(f"Sizning {ism.upper()}.pdf PDF faylingiz yaratildi!")
