from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///films.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_secret_key' 

db = SQLAlchemy(app)
jwt = JWTManager(app)
CORS(app)


class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(500), nullable=False)
    director = db.Column(db.String(100), nullable=False)
    film = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Float, nullable=False)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)


@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'User already exists'}), 400

    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username, password=password).first()
    if not user:
        return jsonify({'error': 'Invalid credentials'}), 401

    token = create_access_token(identity=username)
    return jsonify({'token': token})


@app.route('/recommendations', methods=['GET'])
@jwt_required()
def get_recommendations():
    genre = request.args.get('genre', 'All')

    if genre == 'All':
        films = Film.query.all()
    else:
        films = Film.query.filter_by(genre=genre).all()

    films_data = [
        {
            'description': film.description,
            'director': film.director,
            'film': film.film,
            'genre': film.genre,
            'rating': film.rating
        } for film in films
    ]

    return jsonify({'movies': films_data})

if __name__ == '__main__':
    app.run(debug=True)
