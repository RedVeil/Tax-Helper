import sqlite3
import json

def write_to_db(key,value):
    db_connection = sqlite3.connect('tax.db')
    db_cursor = db_connection.cursor()
    db_cursor.execute(f"SELECT ID FROM input_fields WHERE Input='{key}';")
    ID = db_cursor.fetchone()
    ID = int(ID[0])
    db_cursor.execute(f"UPDATE user_values SET (user_1) = '{value}' WHERE Input_ID = {ID};")
    db_connection.commit()
    db_cursor.close()


def set_up():
    input_keys = []
    titles = []
    tooltips = []
    db_connection = sqlite3.connect('tax.db')
    db_cursor = db_connection.cursor()
    db_cursor.execute(f"SELECT Input FROM input_fields") 
    input_keys_temp = db_cursor.fetchall()
    for i in input_keys_temp:
        input_keys.append(i[0])
    db_cursor.execute(f"SELECT Title FROM input_fields")
    titles_temp = db_cursor.fetchall()
    for i in titles_temp:
        titles.append(i[0])
    db_cursor.execute(f"SELECT Tooltip FROM input_fields")
    tooltips_temp = db_cursor.fetchall()
    for i in tooltips_temp:
        tooltips.append(i[0])
    db_cursor.close()
    #send to js
    
    
def load_from_db(input_key):
    db_connection = sqlite3.connect('tax.db')
    db_cursor = db_connection.cursor()
    db_cursor.execute(f"SELECT X_Location_ID FROM input_fields WHERE Input='{input_key}';")
    x_id = db_cursor.fetchone()
    db_cursor.execute(f"SELECT X_Location FROM X_Locations WHERE ID='{x_id[0]}';")
    x_location = db_cursor.fetchone() 
    db_cursor.execute(f"SELECT Y_Location_ID FROM input_fields WHERE Input='{input_key}';")
    y_id = db_cursor.fetchone()
    db_cursor.execute(f"SELECT Y_Location FROM Y_Locations WHERE ID='{y_id[0]}';")
    y_location = db_cursor.fetchone() 
    db_cursor.execute(f"SELECT ID FROM input_fields WHERE Input='{input_key}';")
    ID = db_cursor.fetchone() 
    db_cursor.close()
    return x_location, y_location, ID


def safe_data_and_retrieve_location():
    page1 = {}
    page2 = {}
    page3 = {}
    page4 = {}
    page5 = {}
    page6 = {}
    page7 = {}
    with open("test.json", "r") as f:
        json_object = json.load(f)
    for key in json_object:
        write_to_db(key, json_object[key])
        temp_locations = load_from_db(key)
        location = [temp_locations[0][0],temp_locations[1][0]]
        ID = temp_locations[2][0]
        if ID < 101:
            page1[json_object[key]] =  location
        elif ID < 201:
            page2[json_object[key]] =  location
        elif ID < 301:
            page3[json_object[key]] =  location
        elif ID < 401:
            page4[json_object[key]] =  location
        elif ID < 501:
            page5[json_object[key]] =  location
        elif ID < 601:
            page6[json_object[key]] =  location
        elif ID >= 601:
            page7[json_object[key]] =  location
    return page1,page2,page3,page4,page5,page6,page7
