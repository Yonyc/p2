# Importation des modules
import flask
import os
import db_init
import auth

def create_app():
    """
    Fonction permettant de créer et d'initialiser l'application Flask. Elle permet
    également de configurer celle-ci et d'informer la localisation du fichier
    Sqlite où seront stockées nos données.
    """
    app = flask.Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    db_init.init_app(app)

    app.register_blueprint(auth.bp)

    return app

app = create_app()

@app.route("/")
def index():
    """
    Fonction permettant d'aider l'utilisateur
    """
    return "<p>Cliquer <a href='{0}'>ICI</a> pour accéder au site web de la ferme des 3 chênes.</p>".format("/auth/velage")

# Permet de lancer l'application en exécutant simplement le fichier python 'app.py':
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)