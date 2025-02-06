from flask import Flask
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///' + os.getenv("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_BINDS'] = {
    'travellan': r"sqlite:///" + os.path.join(os.getenv("TRAVELLAN_DATABASE_URI"))
}

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

import routes
