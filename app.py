#Modules
import flask
from . import db
from . import auth

def create_app():
    """
    Fonction permettant de créer l'app flask.
    """
    app = flask.Flask(__name__, instance_relative_config=True)

    db.init_app(app)

    app.register_blueprint(auth.bp)

    return app