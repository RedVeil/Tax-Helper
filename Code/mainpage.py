import os
from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from flask import Flask, render_template, Blueprint, redirect, request

bp = Blueprint('mainpage', __name__)

@bp.route('/main', methods=("GET","POST"))
def mainpage():
    return render_template("form1.html")
