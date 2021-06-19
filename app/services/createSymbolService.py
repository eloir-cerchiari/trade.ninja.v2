from app import sqlAlchemyInstance as db
from flask import json, request, jsonify
from ..models.symbol import Symbol, SymbolSchema


class CreateSymbolService():
    def postSymbol(self):
        symbol = Symbol("POSI3F","BMFBOVESPA", "BRAZIL","4h")
        db.session.add(symbol)
        db.session.commit()
        result = SymbolSchema().dump(symbol)
        return jsonify({'message':'success', 'data':result}), 201