from flask import render_template, url_for, redirect, flash
from app import app, db
from flask_login import login_user, logout_user, current_user, login_required, LoginManager
from app.models import *
from app.forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    
    # get form data
    form_username = form.username.data
    form_password = form.password.data
    
    if form.validate_on_submit():
        user = User.query.filter_by(user_name=form_username).first()
        password = user.password
        if user is None or password != form_password:
            flash('Invalid username or password')
            return redirect(url_for('login'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

