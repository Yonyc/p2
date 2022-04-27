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

@bp.route('/velage', methods=('GET', 'POST'))
def velage():

    if request.method == 'POST':
        print('clicked')
        print(request.form.get("Famille"))
        print(request.form.get("Sexe"))
        print(request.form.get("Année"))
        print(request.form.get("Mois"))
        Famille = request.form.get("Famille")
        Sexe = request.form.get("Sexe")
        Année = request.form.get("Année")
        Mois  = request.form.get("Mois")
        return redirect(url_for("auth.affich_graph",Famille = Famille,Sexe = Sexe,Mois = Mois, Ans = Année))
    else:
        année = []
        fam = []
        db = get_db()
        cur =  db.execute('SELECT * FROM velages')
        for velage in cur.fetchall():
            ans = int(velage[3][6:])
            if ans not in année:
                année.append(ans)
        année.sort()
        cur =  db.execute('SELECT * FROM familles')
        for famille in cur.fetchall():
            fam.append(famille[1])
        fam.sort()
        return render_template('auth/velage.html', année = année, fam = fam)