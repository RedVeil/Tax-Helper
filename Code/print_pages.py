from PIL import Image, ImageFont, ImageDraw
from pathlib import Path
#from . import db_connector as db

coordinates_page1 = {'name': [51, 82], 'vorname': [1585, 755], 'geburtsname': [215, 855], 'ausgeuebter_beruf': [215, 955], 'geburtsdatum': [1820, 955], 'strasse': [215, 1050], 'hausnummer': [215, 1150], 'hausnummer_zusatz': [512, 1150], 'adressergaenzung': [930, 1150], 'postleitzahl': [215, 1250], 'wohnort': [572, 1250], 'identifikationsmerkmale': [572, 1450], 'reli': [2170, 1450], 'datum': [215, 1670], 'datum2': [750, 1670], 'datum3': [1285, 1670], 'datum4': [1820, 1670],
'name2': [215, 1845], 'vorname2': [1585, 1845], 'geburtsname2': [215, 1945], 'ausgeuebter_beruf2': [215, 2045], 'geburtsdatum2': [1820, 2045], 'strasse2': [215, 2145], 'hausnummer2': [215, 2245], 'hausnummer_zusatz2': [512, 2245], 'adressergaenzung12': [930, 2245], 'postleitzahl3': [215, 2345], 'wohnort6': [572, 2345], 'identifikationsmerkmale5': [572, 2445], 'reli2': [2170, 2445], 'tel_intern_vorwahl': [215, 2650], 'vorwahl_tel': [512, 2650], 'rufnummer_tel': [1050, 2650], 'e_mail': [215, 2840], 'internetadresse': [215, 2940], 'art_taetigkeit': [215, 3100]}

coordinates_page2 = {'iban_de1': [200, 325], 'iban_int1': [115, 425], 'bic1': [115, 525], 'holder1': [820, 625], 'iban_de2': [200, 835], 'iban_int2': [115, 935], 'bic2': [115, 1035], 'holder2': [820, 1135], 'iban_de3': [200, 1345], 'iban_int3': [115, 1445], 'bic3': [115, 1545], 'holder3': [820, 1645], 'steuerberater': [115, 2025], 'b_lastname': [115, 2170], 'b_firstname': [1470, 2170], 'b_strasse': [115, 2270], 'b_hausnummer': [115, 2370], 'b_hausnummer_zusatz': [400, 2370], 'b_adressergaenzung': [820, 2370], 'b_postleitzahl': [115, 2470], 'b_ort': [460, 2470], 'b_tel_int_vorwahl': [115, 2740], 'b_vorwahl_tel': [400, 2740], 'b_rufnummer_tel': [935, 2740], 'b_e_mail': [115, 2840]}
coordinates_page3 = {'e_firma': [215, 355], 'e_lastname': [215, 485], 'e_firstname': [1585, 485], 
'e_strasse': [215, 585], 'e_hausnummer': [215, 685], 'e_hausnummer_zusatz': [512, 685], 'e_adressergaenzung': [930, 685], 
'e_postleitzahl':[215, 785], 'e_city': [572, 785], 'e_tel_intern_vorwahl': [215, 1025], 'e_vorwahl_tel': [512, 1025],
'e_rufnummer_tel': [1050, 1025], 'e_e_mail': [215, 1125], 'migration_date': [1165, 1385], 
'pre_strasse': [215, 1462], 'pre_hausnummer': [215, 1560], 'pre_hausnummer_zusatz': [512, 1565], 
'pre_adressergaenzung': [930, 1565], 'pre_postleitzahl': [215, 1660], 'pre_city': [572, 1660], 
'pre_finanzamt': [630, 1905], 'pre_steuernummer': [630, 2005], 'firm_bezeichnung': [215, 2205], 
'firm_strasse': [215, 2305], 'firm_hausnummer': [215, 2405], 'firm_hausnummer_zusatz': [512, 2405], 
'firm_adressergaenzung': [930, 2405], 'firm_postleitzahl': [215, 2505], 'firm_city': [572, 2505], 
'firm_strasse2': [215, 2715], 'firm_hausnummer2': [215, 2815], 'firm_hausnummer_zusatz2': [512, 2815], 
'firm_adressergaenzung2': [930, 2815], 'firm_postleitzahl2': [215, 2910], 'firm_city2': [572, 2910], 
'firm_tel_int_vorwahl': [215, 3070], 'firm_vorwahl_tel': [512, 3070], 'firm_rufnummer_tel': [1050, 3070], 
'firm_e_mail': [215, 3170], 'firm_website': [215, 3270]}
coordinates_page4 = {}
coordinates_page5 = {}
coordinates_page6 = {}
coordinates_page7 = {}
coordinates_page8 = {}





def printer(coordinates):
    im = Image.open("Steuerliche Erfassung-3.png")
    roboto = ImageFont.truetype("Roboto-Regular.ttf", size=35)
    d = ImageDraw.Draw(im)  
    text_color= (0,0,0)
    for key, value in coordinates.items():
        location = value
        text = str(key)
        d.text(location, text, font=roboto, fill=text_color)
    im.save("drawn_grid4.png")

printer(coordinates_page3)