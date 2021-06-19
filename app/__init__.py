from flask import Flask, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
#cria versões da base de dados, no readme vou colocar as informações a respeito
from flask_migrate import Migrate
# import sqlalchemy

app = Flask(__name__)
app.config.from_object('config')

#cria a conexao ao banco
sqlAlchemyInstance = SQLAlchemy(app)
marshmallowInstance = Marshmallow(app) 


Migrate(app, sqlAlchemyInstance)

#carrega as rotas
from .models import symbol
from .routes import routes