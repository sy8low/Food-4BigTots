"""Adapted from https://flask.palletsprojects.com/en/3.0.x/tutorial/factory/"""

import os
from flask import Flask, render_template, json
from flask_session import Session  # type: ignore
from jinja2.exceptions import TemplateNotFound
from werkzeug.exceptions import HTTPException

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = "dev",
        DATABASE = os.path.join(app.instance_path, "ffbt.db"),
        SESSION_PERMANENT = False,
        SESSION_TYPE = "filesystem"
    )
    Session(app)
    
    if test_config:
        app.config.from_mapping(test_config)
    else:
        app.config.from_pyfile("config.py", silent=True)
        
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    from . import db
    db.init_app(app)
    
    from . import recipes
    app.register_blueprint(recipes.bp)

    from . import home
    app.register_blueprint(home.bp)
    
    @app.template_filter("media")
    def media(filename, path_r="misc"):
        return "".join(["media/", path_r, "/", filename, ".jpg"])
    
    
    @app.errorhandler(HTTPException)
    def handle_generic_http(error):
        return render_template("errors/error.html", error=error), error.code
    
    
    @app.errorhandler(404)
    @app.errorhandler(TemplateNotFound)
    def handle_not_found(error):
        return render_template("errors/404.html"), 404
    
    return app