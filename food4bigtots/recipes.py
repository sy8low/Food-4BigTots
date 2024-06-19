from flask import Blueprint, g, redirect, render_template, request, url_for
from food4bigtots.db import get_db, query_db, mod_db

bp = Blueprint('recipes', __name__, url_prefix='/recipes')