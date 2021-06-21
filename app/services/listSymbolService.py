from app import sqlAlchemyInstance as db
from flask import json, request, jsonify
from ..models.symbol import Symbol
from ..models.schema.symbolSchema import SymbolSchema


class ListSymbolService():

    def listSymbols(self):
        result = Symbol.query.all()
        resultList = SymbolSchema(many=True).dump(result)
        return jsonify({'message':'success', 'data':resultList}), 201
    
    def getSymbol(self, id):
        symbol = Symbol.query.get(id)

        if not symbol:
            return jsonify({'message':"Symbol don't exist", "data":{}}), 404

        result = SymbolSchema().dump(symbol)
        return jsonify({'message':'success', 'data':result}), 201