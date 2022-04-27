#Modules
import flask
import os
import db_init
import auth

def create_app():
    """
    Fonction permettant de créer l'app flask.
    """
    app = flask.Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    db_init.init_app(app)

    app.register_blueprint(auth.bp)

    return app