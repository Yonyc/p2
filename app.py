#Modules
import flask
app = flask.Flask(__name__)


@app.route('/')
def index():
    """
    Retourne le contenu de la page index.html
    """
    return flask.render_template("template.html", title_web="TEEEEEEZ")