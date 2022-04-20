#Modules
from flask import (
    Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for
)
app = Blueprint('auth', __name__, url_prefix='/auth')

@app.route('/')
def index():
    """
    Retourne le contenu de la page index.html
    """
    return open("index.html").read()