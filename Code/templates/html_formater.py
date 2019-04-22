from bs4 import BeautifulSoup


input_list=['finanzamt', 'u_lastname', 'u_firstname', 'u_family_name', 'u_current_job', 'u_birthday', 'u_strasse', 'u_hausnummer', 'u_hausnummer_zusatz', 'u_adressergaenzung', 'u_postleitzahl', 'u_city', 'u_reli', 'u_tax_id', 'marriage_date', 'widow_date', 'divorce_date', 'seperate_date', 'p_lastname', 'p_firstname', 'p_family_name', 'p_current_job', 'p_birthday', 'p_strasse', 'p_hausnummer', 'p_hausnummer_zusatz', 'p_adressergaenzung', 'p_postleitzahl', 'p_city', 'p_tax_id', 'p_reli', 'tel_int_vorwahl', 'vorwahl_tel', 'rufnummer_tel', 'e_mail', 'website', 'art_taetigkeit', 'iban_de1', 'iban_int1', 'bic1', 'holder1', 'iban_de2', 'iban_int2', 'bic2', 'holder2', 'iban_de3', 'iban_int3', 'bic3', 'holder3', 'steuerberater', 'b_lastname', 'b_firstname', 'b_strasse', 'b_hausnummer', 'b_hausnummer_zusatz', 'b_adressergaenzung', 'b_postleitzahl', 'b_ort', 'b_tel_int_vorwahl', 'b_vorwahl_tel', 'b_rufnummer_tel', 'b_e_mail', 'e_firma', 'e_lastname', 'e_firstname', 'e_strasse', 'e_hausnummer', 'e_hausnummer_zusatz', 'e_adressergaenzung', 'e_postleitzahl', 'e_city', 'e_tel_int_vorwahl', 'e_vorwahl_tel', 'e_rufnummer_tel', 'e_e_mail', 'migration_date', 'pre_strasse', 'pre_hausnummer', 'pre_hausnummer_zusatz', 'pre_adressergaenzung', 'pre_postleitzahl', 'pre_city', 'pre_finanzamt', 'pre_steuernummer', 'firm_bezeichnung', 'firm_strasse', 'firm_hausnummer', 'firm_hausnummer_zusatz', 'firm_adressergaenzung', 'firm_postleitzahl', 'firm_city', 'firm_strasse2', 'firm_hausnummer2', 'firm_hausnummer_zusatz2', 'firm_adressergaenzung2', 'firm_postleitzahl2', 'firm_city2', 'firm_tel_int_vorwahl', 'firm_vorwahl_tel', 'firm_rufnummer_tel', 'firm_e_mail', 'firm_website', 'work_date', 'work_bezeichnung1', 'work_strasse1', 'work_hausnummer1', 'work_hausnummer_zusatz1', 'work_adressergaenzung1', 'work_postleitzahl1', 'work_city1', 'work_tel_int_vorwahl1', 'work_vorwahl_tel1', 'work_rufnummer_tel1', 'work_bezeichnung2', 'work_strasse2', 'work_hausnummer2', 'work_hausnummer_zusatz2', 'work_adressergaenzung2', 'work_postleitzahl2', 'work_city2', 'work_tel_int_vorwahl2', 'work_vorwahl_tel2', 'work_rufnummer_tel2', 'neugründungsdate', 'new_bezeichnung', 'new_lastname', 'new_firstname', 'new_strasse', 'new_hausnummer', 'new_hausnummer_zusatz', 'new_adressergaenzung', 'new_postleitzahl', 'new_city', 'new_tax_id', 'new_steuernummer', 'new_ustid', 'u_betrag1', 'p_betrag1', 'u_betrag2', 'p_betrag2', 'u_betrag3', 'p_betrag3', 'u_betrag4', 'p_betrag4', 'u_betrag5', 'p_betrag5', 'u_betrag6', 'p_betrag6', 'u_betrag7', 'p_betrag7', 'u_betrag8', 'p_betrag8', 'u_sonderausgaben1', 'p_sonderausgaben1', 'u_sonderausgaben2', 'p_sonderausgaben2', 'u_steuerabzug1', 'p_steuerabzug1', 'u_steuerabzug2', 'p_steuerabzug2', 'sonstig', 'sum1', 'sum2', 'steuerbefreiung', 'steuerbefreiung_art', 'steuersatz', 'steuersatz_art', 'durchschnittssteuer', 'durchschnittssteuer_art', 'pre_ustid', 'pre_ustid_date', 'city and date']

def create_ipunts():
    string_list = []
    for i in input_list:
        print(f"<input id='{i}' type='text' name='{i}' class='input_field'>")


def create_mainpage_routes():
    for i in range(10):
        num=i+11
        print(f"""
    @bp.route('/main{num}', methods=("GET","POST"))
    def mainpage{num}():
        return render_template("form{num}.html")""")

def __init__():
    create_mainpage_routes()  


__init__()