from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask import jsonify

# configurações
app = Flask(__name__)
# caminho do arquivo de banco de dados
path = os.path.dirname(os.path.abspath(__file__)) 
arquivobd = os.path.join(path, 'construtora.db')
# sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///construtora.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)