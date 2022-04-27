import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db,init_db


bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/test', methods=('GET', 'POST'))
def test():
    db = get_db()
    cur =  db.execute('SELECT * FROM animaux WHERE sexe = "M"')
    data = cur.fetchall()
    Male = len(data)
    print(Male)
    cur =  db.execute('SELECT * FROM animaux WHERE sexe = "F"')
    data = cur.fetchall()
    Female = len(data)    

    return render_template('auth/test.html', data = data, Male = Male,Female = Female)

@bp.route('/complication', methods=('GET', 'POST'))
def complication():
    list_complication = []
    list_complication_id = []
    nb_complication = []
    db = get_db()
    cur =  db.execute('SELECT * FROM complications')
    data = cur.fetchall()
    for dat in data:
        list_complication.append('"'+dat[1]+'"')
        list_complication_id.append(dat[0])
    print(list_complication)
    print(list_complication_id)
    for element in list_complication_id:
        curr = db.execute('SELECT * FROM velages_complications WHERE complication_id = "{}"'.format(element))
        nb_db = curr.fetchall()
        nb_complication.append(len(nb_db))
    return render_template('auth/complication.html',data = data,nb_complication = nb_complication,list_complication = list_complication)










