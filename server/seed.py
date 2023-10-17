from models import User, Note, Category, NoteCategory
from setup import app, db
from faker import Faker

fake = Faker()

with app.app_context():
    User.query.delete()
    Note.query.delete()
    Category.query.delete()
    NoteCategory.query.delete()

    # Seed users
    for _ in range(10):
        user = User(
            username=fake.user_name(),
            email=fake.email(),
            password_hash=fake.password(),
        )
        db.session.add(user)

    db.session.commit()

    print("Users successfully added to the database.")

    # Seed categories
    categories_data = [
        {"name": "Work", "user_id": 1},
        {"name": "Personal", "user_id": 2},
        {"name": "Study", "user_id": 2},
        {"name": "Shopping", "user_id": 1},
        {"name": "Health", "user_id": 2},
        {"name": "Travel", "user_id": 1},
    ]

    categories = []

    for category_data in categories_data:
        category = Category(**category_data)
        categories.append(category)

    db.session.add_all(categories)
    db.session.commit()

    print("Categories successfully added to the database.")

    # Define notes data
    notes_data = [
        {
            "title": "Morning Affirmation",
            "category": "Personal",
            "content": "I am confident and capable of achieving my goals.I love and accept myself unconditionally.I attract positive energy and good vibes into my life.I am grateful for the abundance and blessings in my life.",
            "user_id": 1,
        },
        {
        "title": "Health Checkbox List",
        "category": "Health",
        "content": "Exercise for 30 minutes \nEat a balanced diet\nDrink 8 glasses of water\nGet 7-8 hours of sleep\nMeditate for 10 minutes",
        "user_id": 1,
    },
        {
            "title": "Meeting Agenda",
            "category": "Work",
            "content": "Discuss project progress and goals.",
            "user_id": 2,
        },
        {
            "title": "Grocery List",
            "category": "Shopping",
            "content": "Buy milk, eggs, bread, and fruits.",
            "user_id": 1,
        },
        {
            "title": "Travel Plans",
            "category": "Personal",
            "content": "Book flight tickets and hotel for vacation.",
            "user_id": 3,
        },
        {
            "title": "Project Ideas",
            "category": "Work",
            "content": "Brainstorm new feature ideas for the app.",
            "user_id": 2,
        },
        {
            "title": "Prayer Note",
            "category": "Spiritual",
            "content": "Dear [Deity/God/Universe], I am grateful for the blessings in my life. Please guide me on my spiritual journey and grant me wisdom and peace.",
            "user_id": 1,
    },

    ]

    # Seed notes
    for note_data in notes_data:
        note = Note(
            title=note_data["title"],
            category=note_data["category"],
            content=note_data["content"],
            user_id=note_data["user_id"],
        )
        db.session.add(note)
        db.session.commit()

    print("Notes successfully added to the database.")

    # Seed note categories
    note_categories = []
    for note in Note.query.all():
        category_data = next(
            (category for category in categories_data if category["name"] == note.category), None
        )
        if category_data:
            note_category = NoteCategory(
                category_id=category_data["user_id"],
                note_id=note.id,
            )
            note_categories.append(note_category)

    db.session.add_all(note_categories)
    db.session.commit()

    print("Note-Category relationships successfully added to the database.")
