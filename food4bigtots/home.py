from flask import Blueprint, g, redirect, render_template, request, url_for
from food4bigtots.db import get_db, query_db, mod_db

bp = Blueprint('home', __name__)