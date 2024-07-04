"""Implements the view functions for the Home page, About page, and other non-recipe pages.

Functions:
    home    : View function for the Home page.
    about   : View function for the About page.
"""

from datetime import date
from flask import Blueprint, render_template, Response
from food4bigtots.db import query_db, Queries

bp = Blueprint('home', __name__)

@bp.get("/")
def home() -> Response:
    """View function for the Home page.

    Returns:
        The Home page.
    """
    
    recipes = query_db(
        Queries.ALL_RECIPES_DISTINCT
    )
    
    return render_template("home/home.html", recipes=recipes)


@bp.get("/about/")
def about() -> Response:
    """View function for the About page.

    Returns:
        The About page.
    """
    
    after = date.today().year - 2008
    return render_template("home/about.html", after=after)