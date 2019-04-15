import os

from flask import Flask, render_template  

def create_app():
    # create and configure the app
    app = Flask(__name__,)
    app.config['SECRET_KEY'] = 'test'


    @app.route('/hello')
    def hello():
        return render_template("get_form.html")

    from . import grab_dict
    app.register_blueprint(grab_dict.bp)


    return app