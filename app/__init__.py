from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models



"""
from app import app,db
from app.models import User, Post, Comment
import sqlalchemy as sa
app.app_context().push()
u = User(username = 'Ahmet', email='ahmet@mail.com')
>>> db.session.commit()
>>> db.session.add(u)
>>> db.session.commit()
>>> u = User(username = 'Kagan', email='kagan@mail.com')
>>> db.session.commit()
>>> query = sa.select(User)
>>> users = db.session.scalars(query).all()
>>> users
>>> u = db.session.get(User, 1)
>>> p = Post(body='my first post', author=u)
>>> db.session.add(p)
>>> db.session.commit()
>>> query=u.posts.select()
>>> posts = db.session.scalars(query).all()
>>> posts



"""