import PySimpleGUI as sg 
import os 
from rotate_function import rotate_pdf_pages, create_rotation_mapping

# Part 2 - The Layout
layout = [  [sg.Text("Path to your PDF file:")],     
            [sg.Input(key='-IN-' ,change_submits=True, disabled=True, size=40), sg.FileBrowse(key='-PATH-', button_text='Browse files', enable_events=True)],
            [sg.Text("Page number(s) to rotate:"), sg.Input(key='-PG-_NO-', change_submits=True, disabled=False, size=17), sg.Text("Angle:"), sg.Input(key='-ANGLE-', default_text='90', change_submits=True, disabled=False, size=3)],
            [sg.Button('Ok'), sg.Button('Cancel')]
            ]

# Part 3 - Window Defintion
window = sg.Window('Rotate PDFs', layout, margins=(2,2))      

# Display and interact with the Window
while True:  # Event Loop
    event, values = window.read()
    # print(event, values)
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == 'Ok':
        # Update the "IN" text element to be the value of "PATH" element
        pdf_file_path = os.path.abspath(values['-PATH-']) # Get path to the PDF
        dirname, fname = os.path.split(pdf_file_path)
        output_path = os.path.join(dirname, 'rotated_pdf.pdf')
        pages = [int(num) for num in values['-PG-_NO-'].split(",")] # Convert input of page no from string to list of numbers
        rotate_angle = int(values['-ANGLE-'])
        rotation_mapping = create_rotation_mapping(pages, rotate_angle) # Format a dictionary of page number: angle value pairs from the list of page numbers, default angle is 90
        rotate_pdf_pages(pdf_file_path, output_path, rotation_mapping)
        window['-IN-'].update(values['-PATH-'])
        break

window.close()