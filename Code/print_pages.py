from PIL import Image, ImageFont, ImageDraw
from pathlib import Path
#from . import db_connector as db

coordinates_page1 = {'name': [215, 755], 'vorname': [1585, 755], 'geburtsname': [215, 855], 'ausgeuebter_beruf': [215, 955], 'geburtsdatum': [1820, 955], 'strasse': [215, 1050], 'hausnummer': [215, 1150], 'hausnummer_zusatz': [512, 1150], 'adressergaenzung': [930, 1150], 'postleitzahl': [215, 1250], 'wohnort': [572, 1250], 'identifikationsmerkmale': [572, 1450], 'reli': [2170, 1450], 'datum': [215, 1670], 'datum2': [750, 1670], 'datum3': [1285, 1670], 'datum4': [1820, 1670],
'name2': [215, 1845], 'vorname2': [1585, 1845], 'geburtsname2': [215, 1945], 'ausgeuebter_beruf2': [215, 2045], 'geburtsdatum2': [1820, 2045], 'strasse2': [215, 2145], 'hausnummer2': [215, 2245], 'hausnummer_zusatz2': [512, 2245], 'adressergaenzung12': [930, 2245], 'postleitzahl3': [215, 2345], 'wohnort6': [572, 2345], 'identifikationsmerkmale5': [572, 2445], 'reli2': [2170, 2445], 'tel_intern_vorwahl': [215, 2650], 'vorwahl_tel': [512, 2650], 'rufnummer_tel': [1050, 2650], 'e_mail': [215, 2840], 'internetadresse': [215, 2940], 'art_taetigkeit': [215, 3100]}

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
    im.save("drawn_grid7.png")

printer(coordinates_page1)