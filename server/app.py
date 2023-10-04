from flask import Flask, make_response, jsonify, request, session
from setup import app, db
from models import User, Note, Category, NoteCategory

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/signup', methods=['POST'])
def sign_up():
    if request.method == 'POST':
        userData = request.get_json()
        username = userData['username']
        password = userData['password']

        new_user = User(username=username, password_hash=password)

        db.session.add(new_user)
        db.session.commit()
        session['random_user'] = new_user.id

        return jsonify({"message": "New User created successfully"}), 201


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
            # "password": ouruser.password
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

@app.route('/notes/<int:id>', methods = ["GET", "DELETE", "POST", ""])
def getnote(id):
    ournote = Note.query.filter_by(id=id).first()

    if ournote is None:
        return jsonify({"error": "Note not found"}), 404

    if request.method == 'GET':
        noteobj = {
            "id": ournote.id,
            "title" : ournote.title,
            "category" : ournote.category,
            "content" : ournote.content,
            "created_at" : ournote.created_at,
            "updated_at" : ournote.updated_at
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
            # "delete_successful": True,
            "message": "Note deleted."
        }

        response = make_response(
            jsonify(response_body),
            200
        )

        return response

    elif request.method == 'POST':
        data = request.get_json()
        note_id = data['note_id']
        category_id = data['category_id']

        note_category.note_id = note_id
        note_category.category_id = category_id

        db.session.commit()

        note = Note.query.get(note_category.note_id)

        return make_response(
            jsonify({
                "id": note.id,
                "title" : note.title,
                "category" : note.category,
                "content" : note.content,
                "created_at" : note.created_at,
                "updated_at" : note.updated_at,
                # "categories": [category.name for category in note.category]
                }),
            200
        )


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

if __name__ == '__main__':
    app.run(port=5555)
