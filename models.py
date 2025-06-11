from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titel = db.Column(db.String(100), nullable=False)
    beschrijving = db.Column(db.Text, nullable=True)
