from app import sqlAlchemyInstance as db
from flask import json, request, jsonify
from ..models.symbol import Symbol
from ..models.schema.symbolSchema import SymbolSchema


class ListSymbolService():

    def getSymbols(self):
        result = Symbol.query.all()
        resultList = SymbolSchema(many=True).dump(result)
        return jsonify({'message':'success', 'data':resultList}), 201