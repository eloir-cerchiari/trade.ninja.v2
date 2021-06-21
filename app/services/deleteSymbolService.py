from app import sqlAlchemyInstance as db
from flask import json, request, jsonify
from ..models.symbol import Symbol
from ..models.schema.symbolSchema import SymbolSchema


class DeleteSymbolService():
    
    def deleteSymbol(self, id):

        symbol = Symbol.query.get(id)

        if not symbol:
            return jsonify({'message':"Symbol don't exist", "data":{}}), 404

        try:
            db.session.delete(symbol)
            db.session.commit()
            data = SymbolSchema().dump(symbol)
            return jsonify({'message':'success', 'data':data}), 200
        except:
            return jsonify({'message':"Unable to delete", "data":{}}), 500