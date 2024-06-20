from datetime import datetime
from flask import Blueprint, session, render_template
from food4bigtots.db import query_db, Queries
from markupsafe import escape
from re import sub

bp = Blueprint('recipes', __name__, url_prefix='/recipes')

@bp.before_app_request
def load_categories():
    if not getattr(session, "categories", None):
        session.categories = query_db(
            Queries.get_categories
        )


@bp.get("/<cat>/<path>/")
def recipe(cat, path):
    name_r = path.lower().replace("-", " ")
    
    info = query_db(
        Queries.get_recipe,
        (name_r,), True
    )
    
    name, ISO_date, original = info["name"], info["ISO_date"], info["original"]

    date = datetime.strptime(ISO_date, "%Y-%m-%d")
    # Remove leading zeroes.
    date = sub(r"\b0", r"", date.strftime("%d %B %Y"))
    
    return render_template(f"recipes/{escape(path)}.html",
                           name=name, ISO_date=ISO_date,
                           date=date, original=original)


@bp.get("/<cat>/")
def category(cat):
    name_c = cat.title().replace("-", " ")
    recipes = query_db(
        Queries.get_recipes_in_category,
        (name_c,)
    )
    return render_template(f"category.html", name=name_c, recipes=recipes)