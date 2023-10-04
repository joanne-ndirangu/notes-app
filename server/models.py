from sqlalchemy.ext.hybrid import hybrid_property
from setup import bcrypt, db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    username = db.Column(db.String, unique=True)
    _password_hash = db.Column(db.String, nullable=False)

    @hybrid_property
    def password_hash(self):
        return {"message":"You can't view password hashes"}

    @password_hash.setter
    def password_hash(self,password):
        our_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = our_hash.decode('utf-8')
        # return(our_hash.decode('utf-8'))

    def validatepassword(self,password):
        is_valid = bcrypt.check_password_hash(self._password_hash,password.encode('utf-8'))
        return is_valid

    notes = db.relationship('Note', backref='user')
    categories = db.relationship('Category', backref='user')


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    notes = db.relationship('Note', secondary='note_categories', back_populates='categories', viewonly=True)

class Note(db.Model):
    __tablename__ = 'notes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    category = db.Column(db.String)
    content = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    categories = db.relationship('Category', secondary='note_categories', back_populates='notes', viewonly=True)

class NoteCategory(db.Model):
    __tablename__ = 'note_categories'

    id = db.Column(db.Integer, primary_key=True)

    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    note_id = db.Column(db.Integer, db.ForeignKey('notes.id'))

    category = db.relationship('Category', backref='note_categories')
    note = db.relationship('Note', backref='note_categories')
