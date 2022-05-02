# Importation des modules

import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext

# Définition des fonctions
def get_db():
    """
    Fonction permettant de récupérer de la base de données en SQLite. On établit sa connexion.
    """
    print(current_app.config['DATABASE'])
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    """
    Fonction permettant de fermer la connexion avec la base de données.
    """
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    """
    Initialisation de la base de données, on récupère les fichiers du
    dossier 'db' pour les charger.
    """
    db = get_db()

    with current_app.open_resource('./db/db_schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
    with current_app.open_resource('./db/insert_animaux.sql') as f:
        db.executescript(f.read().decode('utf8'))
    with current_app.open_resource('./db/insert_animaux_types.sql') as f:
        db.executescript(f.read().decode('utf8'))
    with current_app.open_resource('./db/insert_familles.sql') as f:
        db.executescript(f.read().decode('utf8'))
    with current_app.open_resource('./db/insert_types.sql') as f:
        db.executescript(f.read().decode('utf8'))
    with current_app.open_resource('./db/insert_velages.sql') as f:
        db.executescript(f.read().decode('utf8'))
    with current_app.open_resource('./db/insert_animaux_velages.sql') as f:
        db.executescript(f.read().decode('utf8'))
    with current_app.open_resource('./db/insert_complications.sql') as f:
        db.executescript(f.read().decode('utf8'))
    with current_app.open_resource('./db/insert_velages_complications.sql') as f:
        db.executescript(f.read().decode('utf8'))

    db.commit()

@click.command('init-db')
@with_appcontext

def init_db_command():
    """
    Fonction permettant de confirmer l'initialisation à la base de données,
    on appelle la fonction init_db()
    """
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    """
    Fonction permettant d'initialiser l'application.
    """
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)