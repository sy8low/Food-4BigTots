"""Adapted from https://flask.palletsprojects.com/en/3.0.x/tutorial/database/
and https://flask.palletsprojects.com/en/3.0.x/patterns/sqlite3/
"""

import sqlite3
import click
from flask import current_app, g

class Queries:
    get_all_recipes = ("SELECT r.name AS name_r, r.thumbnail AS thumbnail_r, c.name AS name_c "
                       "FROM recipes AS r JOIN mapping AS m ON r.id = m.recipe_id "
                       "JOIN categories AS c ON m.category_id = c.id")
    
    get_recipes_in_category = " ".join((get_all_recipes, "WHERE c.name = ?"))
    
    get_all_categories = "SELECT name FROM categories"
    
    get_recipe = ("SELECT name, date(date) AS ISO_date, original "
                  "FROM recipes WHERE LOWER(name) = ?")
    

def get_db():
    if not getattr(g, "db", None):
        g.db = sqlite3.connect(
            current_app.config["DATABASE"],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    
    return g.db


def close_db(exception):
    db = g.pop("db", None)
    if db:
        db.close()


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()

    if not rv:
        return None
    if one:
        return rv[0]
    return rv


def mod_db(query, args=()):
    db = get_db()
    db.execute(query, args)
    db.commit()
    

def init_db():
    with current_app.open_resource("schema.sql") as f:
        get_db().executescript(f.read().decode("utf8"))
        

@click.command("init-db")
def init_db_command():
    init_db()
    click.echo("Initialised the database.")
    

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)