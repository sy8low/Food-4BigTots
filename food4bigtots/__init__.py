"""Adapted from https://flask.palletsprojects.com/en/3.0.x/tutorial/factory/"""

import os
from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = "dev",
        DATABASE = os.path.join(app.instance_path, "ffbt.db")
    )
    
    if test_config:
        app.config.from_mapping(test_config)
    else:
        app.config.from_pyfile("config.py", silent=True)
        
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    @app.route("/test")
    def test():
        return "Hello, world!"
    
    from . import db
    db.init_app(app)
    
    from . import recipes
    app.register_blueprint(recipes.bp)

    from . import home
    app.register_blueprint(home.bp)
    
    return app