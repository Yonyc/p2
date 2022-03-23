#Modules
from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def index():
    """
    Retourne le contenu de la page index.html
    """
    return open("index.html").read()