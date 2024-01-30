from flask import render_template, url_for, redirect
from app import app, db
from flask_login import login_user, logout_user, current_user, login_required, LoginManager
from app.models import *

#### LOGIN ####
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

#### LOGIN / LOGOUT ####

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

