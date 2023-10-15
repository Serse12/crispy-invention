from flask import jsonify, request, g, url_for, current_app
from .. import db
from ..models import Prova
from . import api

@api.route("/prova")
def prova():

    prova = Prova(
        id=1,
        email="ciao"
        )
    
    db.session.add(prova)
    db.session.commit()

    prova2 = Prova.query.all()

    return jsonify({
        prova2
    })