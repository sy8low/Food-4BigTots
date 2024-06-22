"""food4bigtots is the backend for Food-4BigTots, a refreshed, dynamic upgrade of the original Food-4Tots.

Note:
    The modules are:
    
    db      : Contains the database-related logic of the app.
    home    : Implements the view functions for the Home page, About page, and other non-recipe pages.
    recipes : Implements the view functions for recipes and category directories.

Functions:
    media               : Generate the path to a resource, relative to the static folder.
    handle_generic_http : Handle all non-404 HTTP exceptions registered by Werkzeug.
    handle_not_found    : Handle 404 HTTP exceptions and Jinja TemplateNotFound exceptions.
    path_format         : Convert the name of a recipe/category into the format used in its path.
    create_app          : Instantiate and configure an app.

Adapted from:
    https://flask.palletsprojects.com/en/3.0.x/tutorial/factory/
    https://flask.palletsprojects.com/en/3.0.x/errorhandling/
"""

from flask import Flask, render_template, Response
from flask_session import Session  # type: ignore
from jinja2.exceptions import TemplateNotFound
from os import path, makedirs
from werkzeug.exceptions import HTTPException


def media(filename: str, path_r: str="misc") -> str:
    """Generate the path to a resource, relative to the static folder.

    Args:
        filename            : The name of the resource without the extension name (assumed to be .jpg).
        path_r (optional)   : The folder containing the resource (usually the recipe's name).
                              Defaults to "misc".

    Returns:
        The relative path to the resource to be used in a url_for function.
    """
        
    return "".join(["media/", path_r, "/", filename, ".jpg"])
    
    
def handle_generic_http(error: HTTPException) -> Response:
    """Handle all non-404 HTTP exceptions registered by Werkzeug.

    Args:
        error: The instance of the error being handled.

    Returns:
        The error page.
    """
    return render_template("errors/error.html", error=error), error.code
    
    
def handle_not_found(error: Exception) -> Response:
    """Handle 404 HTTP exceptions and Jinja TemplateNotFound exceptions.

    Args:
        error: The instance of the error being handled.

    Returns:
        The error page.
    """
    
    return render_template("errors/404.html"), 404


def path_format(name: str) -> str:
    """Convert the name of a recipe/category into the format used in its path.

    Args:
        name: The name of a recipe/category

    Returns:
        The formatted name.
    """
    
    return name.lower().replace("-", " ")


def create_app(test_config: dict=None) -> Flask:
    """Instantiate and configure an app, and register database, blueprints, filters, and error handlers.

    Args:
        test_config (optional): Configuration values used during tests. Defaults to None.

    Returns:
        A fully-configured flask application.
    """
    
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = "dev",
        DATABASE = path.join(app.instance_path, "ffbt.db"),
        SESSION_PERMANENT = False,
        SESSION_TYPE = "filesystem"
    )
    Session(app)
    
    if test_config:
        app.config.from_mapping(test_config)
    else:
        app.config.from_pyfile("config.py", silent=True)
        
    try:
        makedirs(app.instance_path)
    except OSError:
        pass
    
    from . import db
    db.init_app(app)
    
    from . import recipes
    app.register_blueprint(recipes.bp)

    from . import home
    app.register_blueprint(home.bp)
    
    app.jinja_env.filters["media"] = media
    
    app.register_error_handler(HTTPException, handle_generic_http)
    app.register_error_handler(404, handle_not_found)
    app.register_error_handler(TemplateNotFound, handle_not_found)
    
    return app