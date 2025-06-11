from flask import Flask, render_template
from models import db, Film
import os

app = Flask(__name__)

# Configureer de database via omgevingsvariabele
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    films = Film.query.all()
    return render_template('index.html', films=films)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
