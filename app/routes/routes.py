
from app import app
from ..models.symbol import Symbol

from flask import Flask, jsonify
from ..services.createSymbolService import CreateSymbolService
from ..services.listSymbolService import ListSymbolService
from ..services.deleteSymbolService import DeleteSymbolService

@app.route('/',methods=['GET'])
def root():
    return jsonify({'message':'vai vendo!'})

@app.route('/symbol', methods=['POST'])
def postSymbol():
    create = CreateSymbolService()
    return create.postSymbol()

@app.route('/symbol', methods=['GET'])
def listSymbol():
    list = ListSymbolService()
    return list.listSymbols()

@app.route('/symbol/<id>', methods=['GET'])
def getSymbol(id):
    list = ListSymbolService()
    return list.getSymbol(id)

@app.route('/symbol/<id>', methods=['DELETE'])
def deleteSymbol(id):
    deleteSymbolService = DeleteSymbolService()
    return deleteSymbolService.deleteSymbol(id)