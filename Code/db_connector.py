import sqlite3
import template.html_formater as hf

#id_names = hf.__init__()
page1_locations={}

def write_to_db(argument):
    db_connection = sqlite3.connect('tax.db')
    db_cursor = db_connection.cursor()
    db_cursor.execute(f"INSERT INTO input_fields (Input) VALUES ({argument});")
    db_connection.commit()
    db_cursor.close()


def load_from_db(argument):
    db_connection = sqlite3.connect('tax.db')
    db_cursor = db_connection.cursor()
    db_cursor.execute(f"SELECT X_Location_ID FROM input_fields WHERE Input='{argument}';")
    x_id = db_cursor.fetchone()
    db_cursor.execute(f"SELECT X_Location FROM X_Locations WHERE ID='{x_id[0]}';")
    x_location = db_cursor.fetchone() 
    db_cursor.execute(f"SELECT Y_Location_ID FROM input_fields WHERE Input='{argument}';")
    y_id = db_cursor.fetchone()
    db_cursor.execute(f"SELECT Y_Location FROM Y_Locations WHERE ID='{y_id[0]}';")
    y_location = db_cursor.fetchone() 
    db_cursor.close()
    return x_location, y_location


def create_argument(id_names):
    for i in id_names:
        write_to_db(i)   

def create_dict(id_names):
    for i in id_names:
        temp_locations = load_from_db(i)
        location = [temp_locations[0][0],temp_locations[1][0]]
        page1_locations[i] = location




input_keys= [
"e_firma",
"e_lastname",
"e_firstname",
"e_strasse",
"e_hausnummer",
"e_hausnummer_zusatz",
"e_adressergaenzung",
"e_postleitzahl",
"e_city",
"e_tel_intern_vorwahl",
"e_vorwahl_tel",
"e_rufnummer_tel",
"e_e_mail",
"migration_date",
"pre_strasse",
"pre_hausnummer",
"pre_hausnummer_zusatz",
"pre_adressergaenzung",
"pre_postleitzahl",
"pre_city",
"pre_finanzamt",
"pre_steuernummer",
"firm_bezeichnung",
"firm_strasse",
"firm_hausnummer",
"firm_hausnummer_zusatz",
"firm_adressergaenzung",
"firm_postleitzahl",
"firm_city",
"firm_strasse2",
"firm_hausnummer2",
"firm_hausnummer_zusatz2",
"firm_adressergaenzung2",
"firm_postleitzahl2",
"firm_city2",
"firm_tel_int_vorwahl",
"firm_vorwahl_tel",
"firm_rufnummer_tel",
"firm_e_mail",
"firm_website",
]

create_dict(input_keys)

