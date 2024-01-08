from app import db
from sqlalchemy import Index


class Partenaire(db.Model):
   id = db.Column('partenaire_id', db.Integer, primary_key = True)
   code = db.Column(db.String(100),nullable=True)
   name = db.Column(db.String(100),nullable=True)
   contact = db.Column(db.String(50),nullable=True)
   logo = db.Column(db.String(200),nullable=True)
   icon = db.Column(db.String(10),nullable=True)
   type = db.Column(db.String(10),nullable=True)

   __table_args__ = (db.UniqueConstraint('code', 'type',name='unique_code_type',),)


   def __init__(self,code, name, contact, logo,icon,type):
      self.code = code
      self.name = name
      self.contact = contact
      self.logo = logo
      self.icon = icon
      self.type = type