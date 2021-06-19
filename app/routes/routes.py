
from app import app
from ..models.symbol import Symbol

from flask import Flask, jsonify
from ..services.createSymbolService import CreateSymbolService

@app.route('/',methods=['GET'])
def root():
    return jsonify({'message':'vai vendo!'})
@app.route('/symbol', methods=['POST'])
def postSymbol():
    create = CreateSymbolService()
    return create.postSymbol()