import os
from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from flask import Flask, render_template, Blueprint, redirect, request, jsonify, send_from_directory, Response, send_file
from . import print_pages

bp = Blueprint('mainpage', __name__)

@bp.route('/main', methods=("GET","POST"))
def mainpage():
    return render_template("form0.html")

@bp.route('/main1', methods=("GET","POST"))
def mainpage1():
    return render_template("form1.html")

@bp.route('/main2', methods=("GET","POST"))
def mainpage2():
    return render_template("form2.html")

@bp.route('/main3', methods=("GET","POST"))
def mainpage3():
    return render_template("form3.html")

@bp.route('/main4', methods=("GET","POST"))
def mainpage4():
    return render_template("form4.html")

@bp.route('/main5', methods=("GET","POST"))
def mainpage5():
    return render_template("form5.html")

@bp.route('/main6', methods=("GET","POST"))
def mainpage6():
    return render_template("form6.html")

@bp.route('/main7', methods=("GET","POST"))
def mainpage7():
    return render_template("form7.html")
    
@bp.route('/main8', methods=("GET","POST"))
def mainpage8():
    return render_template("form8.html")

@bp.route('/main9', methods=("GET","POST"))
def mainpage9():
    return render_template("form9.html")

@bp.route('/main10', methods=("GET","POST"))
def mainpage10():
    return render_template("form10.html")

@bp.route('/main11', methods=("GET","POST"))
def mainpage11():
    return render_template("form11.html")

@bp.route('/main12', methods=("GET","POST"))
def mainpage12():
    return render_template("form12.html")

@bp.route('/main13', methods=("GET","POST"))
def mainpage13():
    return render_template("form13.html")

@bp.route('/main14', methods=("GET","POST"))
def mainpage14():
    return render_template("form14.html")

@bp.route('/main15', methods=("GET","POST"))
def mainpage15():
    return render_template("form15.html")

@bp.route('/main16', methods=("GET","POST"))
def mainpage16():
    return render_template("form16.html")

@bp.route('/main17', methods=("GET","POST"))
def mainpage17():
    return render_template("form17.html")

@bp.route('/main18', methods=("GET","POST"))
def mainpage18():
    return render_template("form18.html")

@bp.route('/main19', methods=("GET","POST"))
def mainpage19():
    return render_template("form19.html")

@bp.route('/main20', methods=("GET","POST"))
def mainpage20():
    return render_template("form20.html")

@bp.route('/main21', methods=("GET","POST"))
def mainpage21():
    return render_template("form21.html")

@bp.route('/main22', methods=("GET","POST"))
def mainpage22():
    return render_template("form22.html")

@bp.route('/main23', methods=("GET","POST"))
def mainpage23():
    return render_template("form23.html")

@bp.route('/main24', methods=("GET","POST"))
def mainpage24():
   return render_template("form24.html")

@bp.route('/main25', methods=("GET","POST"))
def mainpage25():
       return render_template("form25.html")

@bp.route('/main26', methods=("GET","POST"))
def mainpage26():
    return render_template("form26.html")

@bp.route('/main27', methods=("GET","POST"))
def mainpage27():
    return render_template("form27.html")

@bp.route('/main28', methods=("GET","POST"))
def mainpage28():
    return render_template("form28.html")

@bp.route('/main29', methods=("GET","POST"))
def mainpage29():
    return render_template("form29.html")

@bp.route('/main30', methods=("GET","POST"))
def mainpage30():
    return render_template("form30.html")

@bp.route('/main31', methods=("GET","POST"))
def mainpage31():
    return render_template("form31.html")

@bp.route('/main32', methods=("GET","POST"))
def mainpage32():
    return render_template("form32.html")

@bp.route('/main33', methods=("GET","POST"))
def mainpage33():
    return render_template("form33.html")

@bp.route('/main34', methods=("GET","POST"))
def mainpage34():
    return render_template("form34.html")

@bp.route('/main35', methods=("GET","POST"))
def mainpage35():
    return render_template("form35.html")

@bp.route('/main36', methods=("GET","POST"))
def mainpage36():
    return render_template("form36.html")

@bp.route('/main37', methods=("GET","POST"))
def mainpage37():
    return render_template("form37.html")

@bp.route('/main38', methods=("GET","POST"))
def mainpage38():
    return render_template("form38.html")




@bp.route('/saved', methods=["GET","POST"])
def recieve_json():
    if request.method == "POST":
        data = request.form

        # short term solution
        json_dict = {}
        for i in data:
            json_dict[i] = data[i]
        json_object = json_dict
        # 

        if os.path.isfile("Steuerliche Erfassung.pdf"):
            os.remove("Steuerliche Erfassung.pdf")
        print_pages.__init__(json_object)
        path = "Steuerliche Erfassung.pdf"
        return send_file(path, as_attachment=True)
    return render_template("saved.html")