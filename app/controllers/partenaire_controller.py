from flask import render_template, request, redirect, url_for
from app import app, db
from flask import flash
from app.models.partenaires import Partenaire
import os
from PIL import Image


app.config.from_object('config')


#VARIABLES
types = ['Marchands', 'Facturiers', 'MTO']
path = app.config['IMAGE_PATH']
sizes = [16, 24, 32, 64]


#ROUTES
@app.route('/')
def index():
   partenaire = Partenaire.query.all()
   return render_template('index.html', partenaire=partenaire)

@app.route('/add_data')
def add_data():
   return render_template('add_partenaire.html', options=types)

@app.route('/add', methods=["POST"])
def partenaire():
   code = request.form.get("code")
   name = request.form.get("name")
   contact = request.form.get("contact")
   type = request.form.get("type")
   logo = request.files['logo']
   icon = request.files['icon']

   logo_filename = type + '_' + code + '_logo.png'
   icon_filename = type + '_' + code + '_icon.png'

   if not allowed_file(logo) or (icon and not allowed_file(icon)):
      return redirect('/add_data')
   if not image_size_allowed(logo) or (icon and not image_size_allowed(icon)):
      return redirect('/add_data')

   logo.save(path + logo_filename)
   logo.filename = logo_filename

   if not icon:
      icon = Image.open(path + logo_filename)
   icon.save(path + icon_filename)
   icon.filename = icon_filename

   p = Partenaire(code=code, name=name, contact=contact, logo=logo_filename, icon=icon_filename, type=type)
   db.session.add(p)
   db.session.commit()
   image_processing(p.code, p.type, p.logo, p.icon)
   return redirect('/')

@app.route('/put/<int:id>')
def put(id):
   p = Partenaire.query.get(id)
   return render_template('update_partenaire.html', options=types, part=p)

@app.route('/update_data/<int:id>', methods=['POST'])
def update_partenaire(id):
   p = Partenaire.query.get(id)
   p.name = request.form["name"]
   p.contact = request.form["contact"]

   icon_filename = p.type + '_' + p.code + '_icon.png'
   logo_filename = p.type + '_' + p.code + '_logo.png'

   logo = request.files['logo']
   icon = request.files['icon']

   if (logo and not image_size_allowed(logo)) or (icon and not image_size_allowed(icon)):
      return redirect(request.referrer)
   if logo:
      logo.save(path + logo_filename)
   if icon:
      icon.save(path+icon_filename)

   image_processing(p.code, p.type, p.logo, p.icon)
   db.session.commit()
   return redirect(url_for('index'))


@app.route('/delete/<int:id>')
def delete(id):
   p = Partenaire.query.get(id)
   images = os.listdir(path)
   for im in images:
      if im.__contains__(p.type) and im.__contains__(p.code):
         os.remove(path+im)
   db.session.delete(p)
   db.session.commit()
   return redirect('/')





#FUNCTIONS
def allowed_file(logo):
   if '.' in logo.filename and logo.filename.rsplit('.', 1)[1].lower() in app.config['UPLOAD_EXTENSIONS']:
      return True
   else :
      flash('Veuillez insérer une image avec une extension .png. ', 'error')
      return False

def image_size_allowed(image):
   width, height = Image.open(image).size
   image.seek(0)
   if height >= 100 and width >= 100:
      return True
   else :
      flash("Veuiller insérer une image de taille supérieure ou égale à 100x100 ", "error")
      return False

def image_processing(code, type, logo, icon):
   logo = Image.open(path + logo)
   icon = Image.open(path + icon)
   for i in sizes:
      logo_name = type + '_' + code + '_logo_' + str(i) + '.png'
      icon_name = type + '_' + code + '_icon_' + str(i) + '.png'
      miniature_generator(logo, (i, i), logo_name)
      miniature_generator(icon, (i, i), icon_name)

def miniature_generator(image, size, new_name):
   image.thumbnail(size)
   img_w, img_h = image.size

   background = Image.new('RGBA', size=size, color=(0, 0, 0, 0))
   bg_w, bg_h = background.size
   x_position = (bg_w - img_w) // 2
   y_position = (bg_h - img_h) // 2

   background.paste(image, (x_position, y_position))
   background.save(path + new_name)

