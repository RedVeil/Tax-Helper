import os
from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from flask import Flask, render_template, Blueprint, redirect, request

bp = Blueprint('mainpage', __name__)

@bp.route('/main', methods=("GET","POST"))
def mainpage():
    if request.method == "POST":
            return redirect("/main2")
    return render_template("form1.html")

@bp.route('/main2', methods=("GET","POST"))
def mainpage2():
    if request.method == "POST":
            return redirect("/main3")
    return render_template("form2.html")

@bp.route('/main3', methods=("GET","POST"))
def mainpage3():
    if request.method == "POST":
            return redirect("/main4")
    return render_template("form3.html")

@bp.route('/main4', methods=("GET","POST"))
def mainpage4():
    if request.method == "POST":
            return redirect("/main5")
    return render_template("form4.html")