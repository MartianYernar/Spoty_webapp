from app import db
from models import Music

music1 = Music(title='Song 1', file_path='static/music/song1.mp3')
music2 = Music(title='Song 2', file_path='static/music/song2.mp3')
db.session.add(music1)
db.session.add(music2)
db.session.commit()
