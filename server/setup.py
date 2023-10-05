import os
from flask import Flask
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
migrate = Migrate(app, db)
db.init_app(app)
bcrypt = Bcrypt(app)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'