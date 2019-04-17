import os
from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from flask import Flask, render_template, redirect, request

def create_app():
    # create and configure the app
    app = Flask(__name__,)
    app.config['SECRET_KEY'] = 'test'


    @app.route('/', methods=("GET","POST"))    
    def hello():
        return render_template("index.html")

    from . import mainpage
    app.register_blueprint(mainpage.bp)

    return app