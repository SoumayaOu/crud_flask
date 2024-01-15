from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
from flask_migrate import Migrate
migrate = Migrate(app, db)
from app.models import partenaires,users
from app.controllers import partenaire_controller,auth


