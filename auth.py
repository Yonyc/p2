# Importation des modules
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from db_init import get_db,init_db

# Déclaration des variables

months = {
    0: "Tous",
    1: "Janvier",
    2: "Février",
    3: "Mars",
    4: "Avril",
    5: "Mai",
    6: "Juin",
    7: "Juillet",
    8: "Août",
    9: "Septembre",
    10: "Octobre",
    11: "Novembre",
    12: "Décenbre"
}

sexes = {
    "B": "Mâle et Femelle",
    "M": "Mâle",
    "F": "Femelle"
}

bp = Blueprint('auth', __name__, url_prefix='/auth')

# Déclarations des fonctions de l'application

def renderForms():
    """
    Fonction permettant de récupérer à l'aide d'une requpête SQL toutes 
    les familles ainsi que toutes les années des velages.
    """
    year = []
    fam = []
    db = get_db()
    # Requête SQL : On récupère tous les velages
    cur =  db.execute('SELECT * FROM velages')
    
    for velage in cur.fetchall():
        ans = int(velage[3][6:])
        if ans not in year:
            year.append(ans)
    year.sort()
    # Requête SQL : On récupère toutes les familles
    cur =  db.execute('SELECT * FROM familles')

    for famille in cur.fetchall():
        fam.append(famille[1])
    fam.sort()

    return year, fam

@bp.route("/")
def index():
    """
    Fonction permettant de rendre la page d'accueil en chargeant le fichier
    index.html lorsque l'utilisateur se trouve dans auth/.
    """
    return render_template("auth/index.html")

@bp.route('/gender', methods=('GET', 'POST'))
def gender():
    """
    Fonction permettant de récupérer les données et de faire la requête SQL nous
    permettant d'afficher un graphique sur la diversité des sexes. Ceci est notre 
    première fonctionnalité supplémentaire.
    """
    db = get_db()
    # Requête SQL : On récupère tous les animaux de sexe M
    cur =  db.execute('SELECT * FROM animaux WHERE sexe = "M"')
    data = cur.fetchall()
    Male = len(data)
    # Requête SQL : On récupère tous les animaux de sexe F 
    cur =  db.execute('SELECT * FROM animaux WHERE sexe = "F"')
    data = cur.fetchall()
    Female = len(data)

    return render_template('auth/gender.html', data = data, Male = Male, Female = Female)


@bp.route('/complication', methods=('GET', 'POST'))
def complication():
    """
    Fonction permettant de récupérer les données et de faire la requête SQL nous
    permettant d'afficher un graphique des complications. Ceci est notre deuxième
    fonctionnalité supplémentaire.
    """
    list_complication = []
    list_complication_id = []
    nb_complication = []
    db = get_db()
    # Requête SQL : On récupère toutes les données de la table des complications enregistrés
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
    """
    Fonction permettant de gérer l'accès à la page où est situé l'interface
    qui permet à l'utilisateur de former des graphiques.
    """
    if request.method == 'POST':
        return redirect(url_for("auth.affich_graph",Famille = request.form.get("Famille"), Sexe = request.form.get("Sexe"),Mois = request.form.get("Mois"),Ans = request.form.get("Annee"), Graph=request.form.get("Graphique")))
    else:
        annee, fam = renderForms()
        return render_template('auth/velage.html', form=render_template('auth/form_velage.html', annee = annee, fam = fam, months=months, sexs=sexes))


@bp.route("/<Famille>/<Sexe>/<Mois>/<Ans>/<Graph>", methods=('GET', 'POST'))
def affich_graph(Famille,Sexe,Mois,Ans,Graph):
    """
    Fonction permettant à l'utilisateur d'afficher les graphiques au moyen de
    l'interface disponible sur la page 'Graphiques'.
    """
    if request.method == 'POST':
        return redirect(url_for("auth.affich_graph",Famille = request.form.get("Famille"), Sexe = request.form.get("Sexe"),Mois = request.form.get("Mois"),Ans = request.form.get("Annee"), Graph=request.form.get("Graphique")))
    else:
        annee, fam = renderForms()
        db = get_db()
        data = []
        joins = []

        def addJoin(table, car1, car2):
            """
            Fonction permettant de faire des INNER JOIN SQL, elle permet surtout
            d'éviter d'avoir de la redondance de code et de rendre plus compréhensible 
            la/les requêtes.
            """
            sql = "INNER JOIN " + table + " ON " + car1 + " = " + car2
            if sql not in joins:
                joins.append(sql)

        addJoin("animaux_velages", "velages.id", "animaux_velages.velage_id")
        addJoin("animaux", "animaux_velages.animal_id", "animaux.id")
        addJoin("familles", "animaux.famille_id", "familles.id")

        # Ici on définis les conditions que nous allons utiliser pour les requêtes,
        # ces conditions seront ajoutés après un WHERE.
        conds = []
        if Famille != "all_families":
            conds.append("familles.nom = \"" + Famille + "\"")

        if Sexe != "B":
            conds.append("animaux.sexe = \"" + Sexe + "\"")

        if Mois != "0":
            conds.append("substr(`velages`.`date`, 4, 2) = \"" + Mois.zfill(2) + "\"")

        if Ans != "all_years":
            conds.append("substr(`velages`.`date`, 7, 4) = \"" + Ans.zfill(4) + "\"")

        # Requête SQL : Enfin, on fait la requête de sélection auquel on ajoute (ou pas) un/des INNER JOIN et (ou pas) un/des WHERE comme conditions.
        req = "SELECT velages.date, animaux.sexe, familles.nom FROM velages " + (" ".join(joins) if len(joins) > 0 else "") + ((" WHERE " + " AND ".join(conds)) if len(conds) > 0 else "") + ";"
        
        err=None
        try:
            res = db.execute(req).fetchall()
            for animal in res:
                data.append([x for x in animal])
        except Exception as e:
            err="Request error: " + req  + "<br>" + str(e) + "<br>"

    return render_template('auth/afiche.html', data=data, error=err, Famille=Famille, Famille_txt=("Toutes les familles" if Famille == "all_families" else Famille), Sexe=Sexe, Sexe_txt=sexes[Sexe], Ans=Ans, Ans_txt=("Toutes les années" if Ans=="all_years" else Ans), Mois=Mois, Mois_txt=months[int(Mois)], Graph_name=Graph, form=render_template('auth/form_velage.html', annee = annee, fam = fam, months=months, sexs=sexes, graph_name=Graph))