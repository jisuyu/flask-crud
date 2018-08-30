# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import *


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql:///app'
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def index():
    posts = Post.query.order_by(Post.id.desc()).all()
    # SELECT * FROM posts;
    # SELECT * FROM posts ORDER BY id DESC;
    # ASC 가 디폴트
    return render_template("index.html", posts=posts)
    
@app.route("/posts/new")
def new():
    return render_template("new.html")

@app.route("/post", methods=["POST"])
def create():
    # 사용자로부터 값을 가져와서 
    title = request.form.get('title')
    content = request.form.get('content')
    # DB에 저장
    post = Post(title=title, content=content)
    db.session.add(post)
    # INSERT INTO posts (title, content)
    # VALUES ('1번글', '1번내용');
    db.session.commit()
    return render_template("create.html", post=post)
    
@app.route("/posts/<int:id>")
def read(id):
    #DB에서 특정한 게시글을 가져와!
    post=Post.query.get(id)
    # SELECT * FROM posts WHERE id=1;
    return render_template("read.html",post=post)
  
    
@app.route("/posts/<int:id>/delete")
def delete(id):
    #DB에서 특정한 게시글을 삭제하기!
    
    post=Post.query.get(id)
    db.session.delete(post)
    db.session.commit()
    #DELETE FROM posts WHERE id=2;
    # return render_template("delete.html")
    return redirect('/')
    
@app.route("/posts/<int:id>/edit")
def edit(id):
    #DB에서 특정한 게시글을 수정하기!
    post=Post.query.get(id)
    return render_template("edit.html",post=post)

    
@app.route("/posts/<int:id>/update", methods=["POST"])
def update(id):
   
    #edit.html 에서 값 받아오기
    t = request.form.get('title')
    c = request.form.get('content')
    
    #받아온 값으로 db수정하기
    post=Post.query.get(id)
    post.title=t
    post.content=c
    db.session.commit()
    #UPDATES posts SET title ="hihi" WHERE id=2
    
    #수정됬는지 보기
    return redirect('/')
    
#post.query.filter_by(title="1").count()
#SELECT COUNT (*) FROM posts
#WHERE title='1';


#Post.query.filter_by(title="1").all()
#SELECT * FROM posts
#WHERE title = '1';

#Post.query.filter_by(title="1").first()
#SELECT * FROM posts
#WHERE title = '1' LIMIT 1;

#Post.query.filter(Post.title!="1").all()
#SELECT * FROM posts
#WHERE title != '1'

#Post.query.filter(Post.title.like("%1%")).all()
#SELECT * FROM posts
#WHERE title LIKE '%1%';

#from sqlarchemy import and_, or_
#Post.query.filter(and_(Post.title=="1", Post.content=="1"))
#SELECT * FROM posts
#WHERE title = "1" AND content="1"