from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_BINDS'] = {
    'message': 'sqlite:///message.db',
    'news': 'sqlite:///news.db',
    'urgent': 'sqlite:///urgent.db'
}
db = SQLAlchemy(app)







