from flask import render_template, request, redirect, url_for
from app import app, db
from flask import flash
from app.models.users import User
from flask_login import LoginManager, UserMixin, login_user, logout_user
from flask_bcrypt import Bcrypt

login_manager = LoginManager()
login_manager.init_app(app)

bcrypt = Bcrypt(app)

@login_manager.user_loader
def loader_user(user_id):
    return User.query.get(user_id)

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('auth.login'))


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        password = request.form.get("password")
        hashed_password = bcrypt.generate_password_hash(password)
        print('password : ', password)
        user = User(first_name=first_name, last_name=last_name, email=email, password=hashed_password)
        user_existed = User.query.filter_by(email=request.form.get("email")).first()
        if user_existed:
            flash('Ce mail est deja existant, veuillez insérer un nouveau mail.')
            return redirect("/register")
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
    else:
        return render_template("register.html")



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(email=request.form.get("email")).first()
        if not user :
            flash("Aucun utilisateur n'a été selectionné",'error')
            return redirect("/login")
        is_valid = bcrypt.check_password_hash(user.password, 'password')
        if bcrypt.check_password_hash(user.password, request.form['password']):
            login_user(user)
            #session["Authorisation"] = True
            # print(session.get("Authorisation"))
            return redirect('/  ')
        if user.password == request.form.get("password"):
            login_user(user)
            return redirect("/")
        else:
            flash('Le mot de passe saisi est incorrect.')
            return redirect("/login")
    else:
        return render_template("login.html")


@app.route("/logout")

def logout():
    logout_user()
    return redirect("/")
