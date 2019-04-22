import os
from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from flask import Flask, render_template, Blueprint, redirect, request, jsonify

bp = Blueprint('mainpage', __name__)

@bp.route('/main', methods=("GET","POST"))
def mainpage():
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

@bp.route('/saved', methods=["GET","POST"])
def recieve_json():
    #data = request.get_json()
    return jsonify({"result":"Sucess!"})