from models import User, Note, Category, NoteCategory
from app import app, db

with app.app_context():
    print("🌱 Seeding users...")

    # Seed users
    users_data = [
        {"email": "user1@example.com", "username": "user1", "_password_hash": "hashed_password"},
        {"email": "user2@example.com", "username": "user2", "_password_hash": "hashed_password"},
    ]

    for user_data in users_data:
        user = User(**user_data)
        db.session.add(user)

    db.session.commit()

    print("🦸‍♀️ Seeding categories...")

    # Seed categories
    categories_data = [
        {"name": "Work", "user_id": 1},
        {"name": "Personal", "user_id": 2},
        {"name": "Study", "user_id": 2},
        {"name": "Shopping", "user_id": 1},
        {"name": "Health", "user_id": 2},
        {"name": "Travel", "user_id": 1},
    ]

    for category_data in categories_data:
        category = Category(**category_data)
        db.session.add(category)

    db.session.commit()

    print("🦸‍♀️ Seeding notes...")

    # Seed notes
    notes_data = [
        {"title": "Work Note 1", "category": "Work", "content": "Content goes here", "user_id": 1},
        {"title": "Personal Note 1", "category": "Personal", "content": "Content goes here", "user_id": 2},
    ]

    for note_data in notes_data:
        note = Note(**note_data)
        db.session.add(note)

    db.session.commit()

    print("🦸‍♀️ Seeding note categories...")

    note_categories_data = [
        {"category_id": 1, "note_id": 1},
        {"category_id": 2, "note_id": 2},
    ]

    for note_category_data in note_categories_data:
        note_category = NoteCategory(**note_category_data)
        db.session.add(note_category)

    db.session.commit()

print("🌱 Done seeding!")
