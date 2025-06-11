from app import db

class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titel = db.Column(db.String(100), nullable=False)
    beschrijving = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Film {self.titel}>'
