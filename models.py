from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Joke(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    level = db.Column(db.String(50), nullable=False)
    lang = db.Column(db.String(5), nullable=False)