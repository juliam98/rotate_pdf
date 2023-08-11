import PyPDF2

def rotate_pdf_pages(input_path, output_path, rotation_mapping):
    with open(input_path, 'rb') as file:
        pdf = PyPDF2.PdfReader(file)
        writer = PyPDF2.PdfWriter()

        for page_num in range(len(pdf.pages)):
            page = pdf.pages[page_num]

            if page_num + 1 in rotation_mapping:
                rotation_angle = rotation_mapping[page_num + 1]
                page.rotate(rotation_angle)

            writer.add_page(page)

        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

# format pages to be rotated from a list into a dictionary
def create_rotation_mapping(pages, angle=90):
    rotation_mapping = {}
    for page in pages:
        rotation_mapping[page] = angle
    return rotation_mapping