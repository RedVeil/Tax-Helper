from PIL import Image, ImageFont, ImageDraw
from pathlib import Path
#from . import db_connector as db

coordinates_page1 = {
'name': [215, 145], 'vorname': [215, 145], 'geburtsname': [215, 145], 'ausgeuebter_beruf': [215, 145], 
'geburtsdatum': [215, 145], 'strasse': [215, 145], 'hausnummer': [215, 145], 'hausnummer_zusatz': [215, 145],
'adressergaenzung': [215, 145], 'postleitzahl': [215, 145], 'wohnort': [215, 145], 
'identifikationsmerkmale': [215, 145], 'reli': [215, 145], 'datum2': [215, 145], 
'datum3': [215, 145], 'datum4': [215, 145], 'vorname2': [215, 145], 
'geburtsname2': [215, 145], 'ausgeuebter_beruf2': [215, 145], 
'geburtsdatum2': [215, 145], 'strasse2': [215, 145], 'hausnummer2': [215, 145],
'hausnummer_zusatz2': [215, 145], 'adressergaenzung12': [215, 145],
'postleitzahl3': [215, 145], 'wohnort6': [215, 145], 'identifikationsmerkmale5': [215, 145],
'reli2': [215, 145], 'vorwahl_tel': [215, 145], 'rufnummer_tel': [215, 145], 
'e_mail': [215, 145], 'internetadresse': [215, 145], 'art_taetigkeit': [215, 145]
}

coordinates_page2 = {}
coordinates_page3 = {}
coordinates_page4 = {}
coordinates_page5 = {}
coordinates_page6 = {}
coordinates_page7 = {}
coordinates_page8 = {}





def printer(coordinates):
    im = Image.open("Steuerliche Erfassung-1.png")
    roboto = ImageFont.truetype("Roboto-Regular.ttf", size=35)
    d = ImageDraw.Draw(im)  
    text_color= (0,0,0)
    for key, value in coordinates.items():
        location = value
        print(location)
        text = str(key)
        d.text(location, text, font=roboto, fill=text_color)
    im.save("drawn_grid3.png")

printer(coordinates_page1)