import functools
from flask import (
    Blueprint, flash, g, request, redirect, url_for, render_template, session
)
from werkzeug.security import (generate_password_hash, check_password_hash)
from . import db as db_engine

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/register", methods = ("GET", "POST"))
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = db_engine.get_db()
        error =  None

        if not username:
            error = "username is required."
        elif not password:
            error = "password is required."
        
        if error is None:
            try:
                db.execute("INSERT INTO user (username, password) VALUES(?, ?)",
                       (username, generate_password_hash(password)))
                db.commit()
            except db.IntegrityError:
                error = f"{username} already exists."
            else:
                return redirect(url_for("auth.login"))
        flash(error)
    return render_template("auth/register.html")


@bp.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = db_engine.get_db()
        error = None

        user = db.execute("SELECT * from user where username = ?", (username,)).fetchone()

        if user is None:
            error = "username is invalid."
        elif not check_password_hash(user["password"], password):
            error = "password is not correct."
        
        if error is None:
            session.clear()
            session["user_id"] = user["id"]
            return redirect(url_for("index"))

        flash(error, "error")

    return render_template("auth/login.html")
    
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id", None)
    if user_id is None:
        g.user = None
    else:
        user = db_engine.get_db().execute(
            "SELECT * from user where id=?", (user_id,)
            ).fetchone()
        g.user = user

@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

def login_required(view):
    @functools.wraps(view)
    def warped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))
        return view(**kwargs)
    return warped_view
