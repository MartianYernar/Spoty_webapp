from app import app, db
from models import User, Music, Comment

with app.app_context():
    db.create_all()
