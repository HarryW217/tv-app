from app import db
from flask_login import UserMixin
from app import login

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

#### User Model ####

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(70), index=True, unique=True)
    password = db.Column(db.String(120))
    
    def get_id(self):
        return (self.id)
    
#### Show Model ####

class Show(db.Model):
    show_id = db.Column(db.Integer, primary_key=True)
    show_name = db.Column(db.String(70), index=True, unique=True)
    show_genre = db.Column(db.String(70))
    episodes = db.relationship('Episode', backref='episodes', lazy=True)
    
#### Episodes Model ####

class Episode(db.Model):
    episode_id = db.Column(db.Integer, primary_key=True)
    episode_name = db.Column(db.String(70), index=True, unique=True)
    episode_date = db.Column(db.Date)
    show_id = id.Column(db.Integer, db.ForeignKey('show.show_id'), nullable=False)
    