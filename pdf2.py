from fpdf import FPDF

def create_user_profile(name, surname, phone, info):
    # Create FPDF object
    pdf = FPDF()

    # Add new page
    pdf.add_page()

    # Add title
    pdf.set_font('Arial', 'B', 20)
    pdf.cell(0, 20, 'User Profile', align='C')
    pdf.ln()

    # Add user's name
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'Name: ' + name + ' ' + surname)
    pdf.ln()

    # Add user's phone number
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'Phone: ' + phone)
    pdf.ln()

    # Add user's picture
   # pdf.set_xy(10, 80)
    #pdf.image(picture_path, w=150)

    # Add user's information
    pdf.set_font('Arial', '', 14)
    pdf.multi_cell(0, 10, 'Information about the user: ' + info)

    # Save PDF file
    pdf.output('user_profile.pdf')

    print('User profile created successfully!')

name = input('Enter your name: ')
surname = input('Enter your surname: ')
phone = input('Enter your phone number: ')
#picture_path = input('Enter the path to your picture file: ')
info = input('Enter some information about yourself: ')

create_user_profile(name, surname, phone, info)