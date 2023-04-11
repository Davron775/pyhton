# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 21:07:14 2023

@author: DAVRON
"""
from datetime import datetime

def calculate_birth_year(age):
    current_year = datetime.now().year
    birth_year = current_year - age
    return birth_year

from fpdf import FPDF

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
yosh = input(f"Tug'ilgan yilingizni kiriting: ")
tel = input("Siz bilan bog'lanish uchun telefon raqamingizni kiriting: ")

ism = ism.title()
familiya = familiya.title()
tel = f"+998{tel.title()}"
yosh = calculate_birth_year(yosh)


# Generate the PDF file
generate_pdf(ism, familiya, yosh, tel)

print(f"Sizning {ism.upper()}.pdf PDF faylingiz yaratildi!")