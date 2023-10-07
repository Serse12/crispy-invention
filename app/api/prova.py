from flask import jsonify, request, g, url_for, current_app
from .. import db
from . import api

@api.route("/prova")
def prova():

    return jsonify({
        'ciao':'mondo'
    })