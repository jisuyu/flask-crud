import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime)
    
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.created_at = datetime.datetime.now()
                             
# CREATE TABLE posts(
#     id SERIAL PRIMARY KEY,
#     title VARCHAR,
#     content TEXT,
#     created_at DATETIME
# )