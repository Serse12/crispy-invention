from flask import jsonify, request, g, url_for, current_app
from .. import db
from ..models import Prova
from . import api

@api.route("/prova")
def prova():
    prova2 = Prova.query.all()

    return jsonify({
        "result":str(prova2)
    })

@api.route("/prova/add")
def prova_add():
    prova = Prova(
        id=1,
        email="ciao"
        )
    
    db.session.add(prova)
    db.session.commit()
