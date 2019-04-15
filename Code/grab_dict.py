import functools
from flask import (
    Blueprint, flash, g, redirect, request, render_template, session, url_for)

bp = Blueprint("grab_dict", __name__)



@bp.route("/page2")
def start():
    return render_template("page2.html")
