from PIL import Image, ImageFont, ImageDraw
from fpdf import FPDF
from pathlib import Path
from db_connection import safe_data_and_retrieve_location
pdf = FPDF()

def __init__():
    pages = safe_data_and_retrieve_location()
    im_list = []
    for i in range(len(pages)):
        im = Image.open(f"Steuerliche Erfassung-{i+1}.jpg")
        roboto = ImageFont.truetype("Roboto-Regular.ttf", size=35)
        d = ImageDraw.Draw(im)  
        text_color= (0,0,0)
        for key, value in pages[i].items():
            location = value
            text = str(key)
            d.text(location, text, font=roboto, fill=text_color)
        im_list.append(im)
    
        #im.save(f"testimg{i+1}.jpg", quality=50)

    #make_pdf()

def make_pdf():
    filepath = "drawn_grid2.png"
    newfilename = "test2.pdf"

    im = Image.open(filepath)
    im = im.convert("RGB")
    im.save("test2.jpg", quality=100)
    im1 = Image.open("test.jpg")
    im2 = Image.open("/test2.jpg")
    im_list = [im1,im2]

    pdf1_filename = "tester.pdf"
    im1.save(pdf1_filename, "PDF" ,resolution=100.0, save_all=True, append_images=im_list)

#make_pdf()
__init__()