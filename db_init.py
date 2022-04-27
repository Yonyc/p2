# Importation des modules

import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext

# Définition des fonctions

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
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
    Initialise la base de données.
    """
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)