from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)

@bp.route("/test")
def request_data():
    """
    By default `GET` method is allowed in route if not specified.
    """
    return {
        "Key": 34
    }

@bp.route("/user/<name>")
def url_with_variable(name = None):
    """
    variable parts of the user are kept in an angle braket pair.
    Varibles are passed as keyword arguments to the view function.
    """
    return f"Welcome {name}"

@bp.route("/student/<int:roll>")
def url_with_variable_caonverter(roll = None):
    """
    variables can have converter (string, int, float, uuid, path, any)
    """
    even_or_odd = "even" if roll %2 == 0 else "odd"
    return f"Your roll is {even_or_odd}"

@bp.route("/query")
def url_with_query_str():
    name = request.args.get("name")
    return f"Welcome {name}"

@bp.route("/json")
def data_in_json():
    data = request.get_json()
    return data