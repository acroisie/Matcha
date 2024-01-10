from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from flask_cors import CORS
from dotenv import load_dotenv
from models.user import User
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['MONGO_URI'] = os.getenv('MONGODB_HOST')

mongo = PyMongo(app)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    user = User(
        username=data['username'],
        email=data['email'],
        password=data['password'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        gender=data['gender'],
        sexual_preferences=data['sexual_preferences'],
        bio=data['bio'],
        interests=data['interests'],
        profile_pictures=data['profile_pictures'],
        fame_rating=data['fame_rating'],
        location=data['location']
    )
    mongo.db.users.insert_one(user.to_json())
    return jsonify({"message": "Registration succeeded"}), 201