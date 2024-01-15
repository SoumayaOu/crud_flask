from flask_login import UserMixin
from datetime import datetime
from flask import current_app as app
from app import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.Text, nullable=False)
    first_name = db.Column(db.Text, nullable=False)
    email = db.Column(db.VARCHAR(255), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    date_joined = db.Column(db.Date, default=datetime.utcnow)