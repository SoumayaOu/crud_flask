from flask import Flask,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask.templating import render_template
from flask_migrate import Migrate, migrate
from werkzeug.utils import secure_filename
import os

app = Flask(__name__,static_url_path='/static')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config["UPLOAD_EXTENSIONS"] = [".jpg", ".png", ".jpeg"]
app.config["IMAGE_PATH"] = "static/images/"
app.config["ICON_PATH"] = "static/images/icons"


# Creating an SQLAlchemy instance
db = SQLAlchemy(app)



# Settings for migrations
#migrate = Migrate(app, db)

class Partenaire(db.Model):
   id = db.Column('partenaire_id', db.Integer, primary_key = True)
   code = db.Column(db.String(100))
   name = db.Column(db.String(100))
   contact = db.Column(db.String(50))
   logo = db.Column(db.String(200))
   icon = db.Column(db.String(10))
   type = db.Column(db.String(10))




   def __init__(self,code, name, contact, logo,icon,type):
      self.code = code
      self.name = name
      self.contact = contact
      self.logo = logo
      self.icon = icon
      self.type = type


def allowed_file(filename):
   return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['UPLOAD_EXTENSIONS']


@app.route('/')
def index():
   partenaire = Partenaire.query.all()
   return render_template('index.html', partenaire=partenaire)

@app.route('/add_data')
def add_data():
   types = ['Marchands', 'facteuriers', 'MTO']
   return render_template('add_partenaire.html', options=types)

@app.route('/put/<int:id>')
def put(id):
   part = Partenaire.query.get_or_404(id)
   types = ['Marchands', 'facteuriers', 'MTO']
   return render_template('update_partenaire.html', options=types,part=part)
@app.route('/delete/<int:id>')
def erase(id):

   data = Partenaire.query.get(id)
   db.session.delete(data)
   db.session.commit()
   return redirect('/')

@app.route('/update_data/<int:id>',methods=['POST','GET'])
def update_data(id):
   types = ['Marchands', 'facteuriers', 'MTO']
   part = Partenaire.query.get_or_404(id)
   if request.method =="POST":
      #part = Partenaire.query.get("id")
      part.name = request.form["name"]
      part.code = request.form["code"]
      part.contact = request.form["contact"]
      part.type = request.form["type"]
      #part.logo = request.files['logo']
      #part.icon = request.files['icon']
      if 'logo' in request.files and 'icon' in request.files:

         logo = request.files['logo']
         icon = request.files['icon']
         logo_filename = secure_filename(logo.filename)
         icon_filename = secure_filename(icon.filename)
         logo.save(os.path.join(app.config['IMAGE_PATH'], logo_filename))
         icon.save(os.path.join(app.config['IMAGE_PATH'], icon_filename))
      db.session.commit()
      return redirect(url_for('index'))
      #return render_template('index.html', options=types,partenaire=part)
   return render_template('modify_partenaire.html', partenaire=part)


# function to add profiles
@app.route('/add', methods=["POST"])
def partenaire():
   code = request.form.get("code")
   name = request.form.get("name")
   contact = request.form.get("contact")
   #logo = request.form.get("logo")
   #icon = request.form.get("icon")
   type = request.form.get("type")
   logo = request.files['logo'] if 'logo' in request.files else None
   icon = request.files['icon'] if 'icon' in request.files else None

   if type!=''  and code !='' and name != '' and contact != '' and logo is not None:
      logo_filename = secure_filename(logo.filename)

      if icon.filename =="" :
         icon_filename = secure_filename(logo.filename)
         icon.save(os.path.join(app.config['IMAGE_PATH'], icon_filename))
         logo.save(os.path.join(app.config['IMAGE_PATH'], logo_filename))
      else :
         icon_filename = secure_filename(icon.filename)
         logo.save(os.path.join(app.config['IMAGE_PATH'], logo_filename))
         icon.save(os.path.join(app.config['IMAGE_PATH'], icon_filename))

      p = Partenaire(code=code, name=name, contact=contact, logo=logo_filename, icon=icon_filename, type=type)
      db.session.add(p)
      db.session.commit()
      return redirect('/')

   else:
      return redirect('/add')


if __name__ == '__main__':


   app.run(debug=True)
