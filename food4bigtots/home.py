from flask import Blueprint, g, redirect, render_template, request, url_for
from food4bigtots.db import get_db, query_db, mod_db

bp = Blueprint('home', __name__)

@bp.get("/")
def home():
    return render_template("home/home.html")

@bp.get("/about")
def about():
    entries = query_db(
        "SELECT name, path, thumbnail FROM recipes"
    )
    
    return render_template("home/about.html", entries=entries)