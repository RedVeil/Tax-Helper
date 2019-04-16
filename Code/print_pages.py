from PIL import Image, ImageFont, ImageDraw
from fpdf import FPDF
from pathlib import Path
from db_connection import safe_data_and_retrieve_location
pdf = FPDF()

def __init__():
    pages = safe_data_and_retrieve_location()
    for i in range(len(pages)):
        im = Image.open(f"Steuerliche Erfassung-{i+1}.png")
        roboto = ImageFont.truetype("Roboto-Regular.ttf", size=35)
        d = ImageDraw.Draw(im)  
        text_color= (0,0,0)
        for key, value in pages[i].items():
            location = value
            text = str(key)
            d.text(location, text, font=roboto, fill=text_color)
        im.save(f"drawn_grid{i+1}.png")

__init__()