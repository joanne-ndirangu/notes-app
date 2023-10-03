from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    username = db.Column(db.String, unique=True)
    _password_hash = db.Column(db.String, nullable=False)

    notes = db.relationship('Note', backref='user')
    categories = db.relationship('Category', backref='user')

    serialize_rules = ('-notes.user',)

class Note(db.Model, SerializerMixin):
    __tablename__ = 'notes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    category = db.Column(db.String)
    content = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    categories = db.relationship('Category', secondary='note_categories', back_populates='notes')

    serialize_rules = ('user.notes',)


class Category(db.Model, SerializerMixin):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    notes = db.relationship('Note', secondary='note_categories', back_populates='categories')


class NoteCategory(db.Model, SerializerMixin):
    __tablename__ = 'note_categories'

    id = db.Column(db.Integer, primary_key=True)

    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    note_id = db.Column(db.Integer, db.ForeignKey('notes.id'))

    category = db.relationship('Category', back_populates=('note_categories'))
    note = db.relationship('Note', back_populates=('note_categories'))