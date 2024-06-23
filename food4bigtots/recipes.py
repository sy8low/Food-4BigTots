"""Implements the view functions for recipes and category directories.

Functions:
    load_categories : Load the list of all recipe categories into a cookie if not done yet.
    recipe          : View function for recipe pages.
    category        : View function for category directories.
"""

from datetime import datetime
from flask import Blueprint, session, render_template, Response
from food4bigtots import name_format
from food4bigtots.db import query_db, Queries
from markupsafe import escape
from re import sub

bp = Blueprint('recipes', __name__, url_prefix='/recipes')

@bp.before_app_request
def load_categories() -> None:
    """Load the list of all recipe categories into a cookie if not done yet."""
    if not getattr(session, "categories", None):
        session.categories = query_db(
            Queries.ALL_CATEGORIES
        )


@bp.get("/<cat>/<path>/")
def recipe(cat: str, path: str) -> Response:
    """View function for recipe pages.
    
    Args:
        cat : The name of the recipe's category.
        path: The name of the recipe.

    Returns:
        The recipe page.
    """
    
    name_r = name_format(path)
    
    info = query_db(
        Queries.RECIPE_METADATA,
        (name_r,), True
    )
    
    name, ISO_date, original = info["name"], info["ISO_date"], info["original"]

    date = datetime.strptime(ISO_date, "%Y-%m-%d")
    # Remove leading zeroes.
    date = sub(r"\b0", r"", date.strftime("%d %B %Y"))
    
    return render_template(f"recipes/{escape(cat)}/{escape(path)}.html",
                           name=name, ISO_date=ISO_date,
                           date=date, original=original)


@bp.get("/<cat>/")
def category(cat: str) -> Response:
    """View function for category directories.

    Args:
        cat: The name of the recipe category.
        
    Returns:
        The category directory.
    """
    
    name_c = name_format(cat)
    recipes = query_db(
        Queries.RECIPES_IN_CATEGORY,
        (name_c,)
    )
    
    full_name_c = query_db(
        Queries.CATEGORY_NAME,
        (name_c,), True
    )["name"]
    
    return render_template(f"recipes/category.html", name=full_name_c, recipes=recipes)