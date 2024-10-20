"""Contains the database-related logic of the app.

Classes:
    Queries: Encapsulates all database queries used by view functions.

Functions:
    get_db          : Create a Connection to the main database and save it in the global object if not done yet.
    close_db        : Close any open Connection to the main database previously saved in the global object.
    query_db        : Query the database through the Connection saved in the global object, and manage transactions.
    mod_db          : Edit the database throuth the Connection saved in the global object, and manage transactions.
    init_db         : Set up the database according to the schema.
    init_db_command : Call init_db from the command-line.
    init_app        : Register database-related functions with the app.

Adapted from:
    https://flask.palletsprojects.com/en/3.0.x/tutorial/database/
    https://flask.palletsprojects.com/en/3.0.x/patterns/sqlite3/
"""

import click
from flask import current_app, g
import sqlite3

class Queries:
    """Encapsulates all database queries used by view functions.
    
    Constants:
        ALL_RECIPES         : Retrieve the name, thumbnail, and category of every recipe. Deprecated.
                              (Ordered by id/time of insertion)
        ALL_RECIPES_DISTINCT: Retrieve the name, thumbnail, and category of every recipe.
                              (Ordered by id/time of insertion) 
        RECIPES_IN_CATEGORY : Retrieve the name, thumbnail, and category of recipes in a category.
                              (Ordered by id/time of insertion)
        ALL_CATEGORIES      : Retrieve the name of every category.
                              (Ordered alphabetically)
        RECIPE_METADATA     : Retrieve the name, date of creation, and original URL for a recipe.
                              (Only 1 result)
        CATEGORY_NAME       : Retrieve the properly capitalised name of a category.
                              (Only 1 result)
    """
    
    ALL_RECIPES = ("SELECT r.name AS name_r, r.thumbnail AS thumbnail_r, c.name AS name_c "
                   "FROM recipes AS r JOIN mapping AS m ON r.id = m.recipe_id "
                   "JOIN categories AS c ON m.category_id = c.id")
    
    # Created to allow recipes to be cross-listed under multiple categories.
    ALL_RECIPES_DISTINCT = ("SELECT * FROM "
                            "(SELECT r.name AS name_r, r.thumbnail AS thumbnail_r, c.name AS name_c, "
                            "ROW_NUMBER() OVER(PARTITION BY r.name) AS rn "
                            "FROM recipes AS r JOIN mapping AS m ON r.id = m.recipe_id "
                            "JOIN categories AS c ON m.category_id = c.id) "
                            "WHERE rn = 1")
    
    # No need to exclude cross-listed recipes (obviously).
    RECIPES_IN_CATEGORY = " ".join((ALL_RECIPES, "WHERE LOWER(c.name) = ?"))
    
    ALL_CATEGORIES = "SELECT name FROM categories ORDER BY name"
    
    # Doesn't matter which category the recipe is listed under.
    RECIPE_METADATA = ("SELECT name, date(date) AS ISO_date, original, thumbnail "
                       "FROM recipes WHERE LOWER(name) = ? LIMIT 1")
    
    CATEGORY_NAME = "SELECT name FROM categories WHERE LOWER(name) = ? LIMIT 1"
    

def get_db() -> sqlite3.Connection:
    """Create a Connection to the main database and save it in the global object if not done yet.

    Returns:
        A connection to the main database.
    """
    
    if not getattr(g, "db", None):
        g.db = sqlite3.connect(
            current_app.config["DATABASE"],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    
    return g.db


def close_db(exception: Exception) -> None:
    """Close any open Connection to the main database previously saved in the global object.

    Args:
        exception: The instance of the exception raised.
    """
    
    db = g.pop("db", None)
    if db:
        db.close()


def query_db(query: str, args: tuple=(), one: bool=False):
    """Query the database through the Connection saved in the global object, and manage transactions.

    Args:
        query           : The SQL query to be executed.
        args (optional) : The values to be substituted into qmark style placeholders. Defaults to ().
        one (optional)  : Whether a list of all matching Rows or a only single Row should be returned.
                          Defaults to False.

    Returns:
        A list of matching sqlite3.Rows if one is True; the first matching sqlite3.Row if one is False;
        or None if there are no matches.
    """
    
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()

    if not rv:
        return None
    if one:
        return rv[0]
    return rv


def mod_db(query: str, args: tuple=()):
    """Edit the database throuth the Connection saved in the global object, and manage transactions.

    Args:
        query           : The SQL query to be executed.
        args (optional) : The values to be substituted into qmark style placeholders. Defaults to ().
    """
    
    db = get_db()
    db.execute(query, args)
    db.commit()
    

def init_db() -> None:
    """Set up the database according to the schema."""
    with current_app.open_resource("schema.sql") as f:
        get_db().executescript(f.read().decode("utf8"))
        

@click.command("init-db")
def init_db_command() -> None:
    """Call init_db from the command-line."""
    init_db()
    click.echo("Initialised the database.")
    

def init_app(app) -> None:
    """Register database-related functions with the app."""
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)