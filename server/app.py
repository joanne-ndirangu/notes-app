from flask import make_response, jsonify, request, session
from sqlalchemy import or_
from datetime import datetime
from setup import db, app
from models import User, Note, Category, NoteCategory

@app.route('/signup', methods=['POST'])
def sign_up():
    if request.method == 'POST':
        userData = request.get_json()
        username = userData['username']
        email = userData['email']
        password = userData['password']

        # Check if a user with the same username or email already exists
        existing_user = User.query.filter(
            or_(User.username == username, User.email == email)
        ).first()

        if existing_user:
            return jsonify({"message": "User already exists"}), 409  # HTTP 409 Conflict
        else:
            new_user = User(username=username, email=email, password_hash=password)
            db.session.add(new_user)
            db.session.commit()
            session['random_user'] = new_user.id

            return jsonify({"message": "New User created successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    user = User.query.filter_by(username=username).first()

    if user and user.validatepassword(password):
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401

@app.route('/')
def home():
    return 'Welcome'

@app.route('/users')
def getusers():

    users = []
    for user in User.query.all():
        user_dict = {
            "id": user.id,
            "email": user.email,
            "username": user.username,
            # "password": user.password
        }
        users.append(user_dict)

    response = make_response(jsonify(users), 200)
    response.headers["Content-Type"] = "application/json"

    return response

@app.route('/users/<int:id>')
def getuser(id):
    ouruser = User.query.filter_by(id=id).first()

    if ouruser is None:
        return jsonify({"error": "User not found"}), 404

    if request.method == 'GET':
        userobj = {
            "id": ouruser.id,
            "email": ouruser.email,
            "username": ouruser.username,
            "password": ouruser.password_hash
        }
        response = make_response(jsonify(userobj), 200)
        return response

@app.route('/notes')

def getnotes():
    notes = []
    for note in Note.query.all():
        note_dict = {
            "id": note.id,
            "title" : note.title,
            "category" : note.category,
            "content" : note.content,
            "created_at" : note.created_at,
            "updated_at" : note.updated_at
        }
        notes.append(note_dict)

    response = make_response(jsonify(notes), 200)
    response.headers["Content-Type"] = "application/json"

    return response

@app.route('/notes/<int:id>', methods=["GET", "DELETE", "PATCH", "POST"])
def getnote(id):
    ournote = Note.query.filter_by(id=id).first()

    if ournote is None:
        return jsonify({"error": "Note not found"}), 404

    if request.method == 'GET':
        noteobj = {
            "id": ournote.id,
            "title": ournote.title,
            "category": ournote.category,
            "content": ournote.content,
            "created_at": ournote.created_at,
            "updated_at": ournote.updated_at
        }
        response = make_response(jsonify(noteobj), 200)
        return response

    elif request.method == 'DELETE':
        note_categories = NoteCategory.query.filter_by(note_id=id).all()
        for note_category in note_categories:
            db.session.delete(note_category)

        db.session.delete(ournote)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": "Note deleted."
        }

        response = make_response(
            jsonify(response_body),
            200
        )

        return response

    elif request.method == 'PATCH':
        note_data = request.get_json()
        if 'title' in note_data:
            ournote.title = note_data['title']
        if 'category' in note_data:
            ournote.category = note_data['category']
        if 'content' in note_data:
            ournote.content = note_data['content']

        ournote.updated_at = datetime.utcnow()

        db.session.commit()

        note_dict = ournote.to_dict()

        response = make_response(
            jsonify(note_dict),
            200
        )

        return response

    elif request.method == 'POST':
        note_data = request.get_json()

        title = note_data.get("title")
        category = note_data.get("category")
        content = note_data.get("content")

        if not title or not category or not content:
            return jsonify({"error": "Incomplete data"}), 400

        ournote.title = title
        ournote.category = category
        ournote.content = content
        ournote.updated_at = datetime.utcnow()

        db.session.commit()

        note_dict = ournote.to_dict()

        response = make_response(
            jsonify(note_dict),
            200
        )

        return response

@app.route('/categories')
def getcategories():

    categories = []
    for category in Category.query.all():
        category_dict = {
            "id": category.id,
            "name" : category.name,
        }
        categories.append(category_dict)

    response = make_response(jsonify(categories), 200)
    response.headers["Content-Type"] = "application/json"

    return response

@app.route('/categories/<int:id>')
def getcategory(id):
    ourcategory = Category.query.filter_by(id=id).first()

    if ourcategory is None:
        return jsonify({"error": "User not found"}), 404

    if request.method == 'GET':
        categoryobj = {
            "id": ourcategory.id,
            "name" : ourcategory.name,
        }
        response = make_response(jsonify(categoryobj), 200)
        return response

if __name__ == '__main__':
    app.run()
