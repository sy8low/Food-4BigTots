from flask import Blueprint, render_template
from food4bigtots.db import query_db, Queries

bp = Blueprint('home', __name__)

@bp.get("/")
def home():
    recipes = query_db(
        Queries.get_all_recipes
    )
    
    return render_template("home/home.html", recipes=recipes)

@bp.get("/about/")
def about():
    return render_template("home/about.html")