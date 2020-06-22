from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config.from_object('config')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'avalia_aqui'

mysql = MySQL(app)

from app.controllers import rotas