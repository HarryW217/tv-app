from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy()
DB_NAME = 'database.db'

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)


# Starting the Login
login = LoginManager(app)

from app import routes, models

if __name__ == '__main__':
    app.run(debug=True)