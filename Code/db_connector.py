import sqlite3
import template.html_formater as hf

id_names = hf.__init__()
page1_locations={}

def write_to_db(argument):
    db_connection = sqlite3.connect('tax.db')
    db_cursor = db_connection.cursor()
    db_cursor.execute(f"INSERT INTO page8 (Name) VALUES ({argument});")
    db_connection.commit()
    db_cursor.close()


def load_from_db(argument):
    db_connection = sqlite3.connect('tax.db')
    db_cursor = db_connection.cursor()
    db_cursor.execute(f"SELECT X_Location_ID FROM page1 WHERE Input='{argument}';")
    x_id = db_cursor.fetchone()
    db_cursor.execute(f"SELECT X_Location FROM X_Locations WHERE ID='{x_id[0]}';")
    x_location = db_cursor.fetchone() 
    db_cursor.execute(f"SELECT Y_Location_ID FROM page1 WHERE Input='{argument}';")
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



create_dict(id_names)



print(page1_locations)