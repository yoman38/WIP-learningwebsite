## main.py
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from models import User, Course, Content
from config import Config

app = Flask(__name__)
app.config.from_object(Config())
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

@app.route('/', methods=['GET'])
def home():
    current_user = {"is_authenticated": False}  # Replace with actual authentication logic
    return render_template('index.html', current_user=current_user)

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    user = User(username=data['username'], email=data['email'], password=hashed_password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created'}), 200

@app.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        return jsonify({'message': 'User logged in'}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/course', methods=['POST'])
def create_course():
    data = request.get_json()
    user = User.query.get(data['creator_id'])
    if user:
        course = Course(title=data['title'], description=data['description'], creator=user)
        db.session.add(course)
        db.session.commit()
        return jsonify({'message': 'Course created'}), 200
    return jsonify({'message': 'User not found'}), 404

@app.route('/content', methods=['POST'])
def create_content():
    data = request.get_json()
    course = Course.query.get(data['course_id'])
    if course:
        content = Content(title=data['title'], body=data['body'], course=course)
        db.session.add(content)
        db.session.commit()
        return jsonify({'message': 'Content created'}), 200
    return jsonify({'message': 'Course not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
