# manage/app/createdb.py

from app import db,app
from config import Config  # Update this line

# Create the database tables
with app.app_context():
    db.create_all()
