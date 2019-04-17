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
    if request.method == "POST":
        return redirect("/main4")
    return render_template("form3.html")

@bp.route('/saved', methods=["GET","POST"])
def recieve_json():
    #data = request.get_json()
    return jsonify({"result":"Sucess!"})