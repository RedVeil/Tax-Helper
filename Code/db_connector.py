import sqlite3
import template.html_formater as hf

#id_names = hf.__init__()
page1_locations={}

def write_to_db(argument):
    db_connection = sqlite3.connect('tax.db')
    db_cursor = db_connection.cursor()
    db_cursor.execute(f"INSERT INTO page8 (Name) VALUES ({argument});")
    db_connection.commit()
    db_cursor.close()


def load_from_db(argument):
    print(argument)
    db_connection = sqlite3.connect('tax.db')
    db_cursor = db_connection.cursor()
    db_cursor.execute(f"SELECT X_Location FROM X_Locations WHERE (SELECT X_Location_ID FROM page1 WHERE Name='vorname');")
    x_locations = db_cursor.fetchone()
    #print(x_locations)
    db_cursor.execute(f"SELECT Y_Location FROM Y_Locations WHERE (SELECT Y_Location_ID FROM page1 WHERE Name='vorname');")
    y_locations = db_cursor.fetchone()
    #print(y_locations)
    db_cursor.close()
    return x_locations, y_locations


def create_argument(id_names):
    for i in id_names:
        write_to_db(i)   

def create_dict(id_names):
    for i in id_names:
        temp_locations = load_from_db(i)
        location = [temp_locations[0][0],temp_locations[1][0]]
        print(location)
        page1_locations[i] = location


id_names = ["hausnummer2","internetadresse","vorname"]

create_dict(id_names)

#print(page1_locations)
#print(id_names)
#"SELECT * FROM X_Locations WHERE ID LIKE X_Location_ID FROM {argument};"