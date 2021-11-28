import os
from fpdf import FPDF


def converter():
    items = []
    path = os.listdir('C:/Users/Lasha/OneDrive/სამუშაო დაფა/PY')

    for item in path:
        if ".jpeg" in item or ".jpg" in item or ".png" in item:
            items.append(item)

    pdf = FPDF()
    pdf.set_auto_page_break(0)
    for pic in items:
        pdf.add_page(orientation="p")
        pdf.image(pic, x=None, y=None, w=0, h=0, type='jpeg', link='')
    pdf.output("yourfile.pdf", "F")
