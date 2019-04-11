from bs4 import BeautifulSoup


string="""
        <input id="name" type="text" name="name" class=page1>
        <input id="vorname" type="text" name="vorname" class=page1>
        <input id="geburtsname" type="text" name="geburtsname" class=page1>
        <input id="ausgeuebter_beruf" type="text" name="ausgeuebter_beruf" class=page1>
        <input id="geburtsdatum" type="text" name="geburtsdatum" class=page1>
        <input id="strasse" type="text" name="strasse" class=page1>
        <input id="hausnummer" type="text" name="hausnummer" class=page1>
        <input id="hausnummer_zusatz" type="text" name="hausnummer_zusatz" class=page1>
        <input id="adressergaenzung" type="text" name="adressergaenzung" class=page1>
        <input id="postleitzahl" type="text" name="postleitzahl" class=page1>
        <input id="wohnort" type="text" name="wohnort" class=page1>
        <input id="identifikationsmerkmale" type="text" name="identifikationsmerkmale" class=page1>
        <input id="reli" type="text" name="reli" class=page1>

        <input id="datum" type="text" name="datum" class=page1>
        <input id="datum2" type="text" name="datum2" class=page1>
        <input id="datum3" type="text" name="datum3" class=page1>
        <input id="datum4" type="text" name="datum4" class=page1>

        <input id="name2" type="text" name="name2" class=page1>
        <input id="vorname2" type="text" name="vorname2" class=page1>
        <input id="geburtsname2" type="text" name="geburtsname2" class=page1>
        <input id="ausgeuebter_beruf2" type="text" name="ausgeuebter_beruf2" class=page1>
        <input id="geburtsdatum2" type="text" name="geburtsdatum2" class=page1>
        <input id="strasse2" type="text" name="strasse2" class=page1>
        <input id="hausnummer2" type="text" name="hausnummer2" class=page1>
        <input id="hausnummer_zusatz2" type="text" name="hausnummer_zusatz2" class=page1>
        <input id="adressergaenzung12" type="text" name="adressergaenzung12" class=page1>
        <input id="postleitzahl3" type="text" name="postleitzahl3" class=page1>
        <input id="wohnort6" type="text" name="wohnort6" class=page1>
        <input id="identifikationsmerkmale5" type="text" name="identifikationsmerkmale5" class=page1>
        <input id="reli2" type="text" name="reli2" class=page1>

        <input id="tel_intern_vorwahl" type="text" name="tel_intern_vorwahl" class=page1>
        <input id="vorwahl_tel" type="text" name="vorwahl_tel" class=page1>
        <input id="rufnummer_tel" type="text" name="rufnummer_tel" class=page1>
        <input id="e_mail" type="text" name="e_mail" class=page1>
        <input id="internetadresse" type="text" name="internetadresse" class=page1>

        <input id="art_taetigkeit" type="text" name="art_taetigkeit" class=page1>"""




def __init__():
    strings = string.split(">")
    inputs = strings[0:]
    input_names=[]
    for i in inputs:
        if len(i) != 0:
            if i[18] =="=":
                index = i.index("type")
                input_names.append(i[20:index-2])
            elif i[19]=="=":   
                index = i.index("type")
                input_names.append(i[21:index-2])
    return input_names
