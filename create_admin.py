from app import app
from models import *
from werkzeug.security import generate_password_hash

user_admin = User(username="admin", email="admin@admin.com", password=generate_password_hash("admin", method='pbkdf2:sha256'))

with app.app_context():
    db.session.add(user_admin)
    db.session.commit()