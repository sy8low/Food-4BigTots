from flask import Blueprint, g, redirect, render_template, request, url_for
from food4bigtots.db import get_db, query_db, mod_db
from markupsafe import escape

bp = Blueprint('recipes', __name__, url_prefix='/recipes')

@bp.get("/<name>/")
def pau(name):
    return render_template(f"recipes/{escape(name)}.html")