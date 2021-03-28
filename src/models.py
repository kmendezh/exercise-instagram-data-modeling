import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class Link(Base):
   __tablename__ = 'Post_and_Post_Media_Relationship'
   post_id = Column(Integer, ForeignKey('post.id'), primary_key = True)
   post_media_id = Column(Integer, ForeignKey('post_media.id'), primary_key = True)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key = True)
    comment_Text = Column(String(250), ForeignKey('comments.id'))
    author_id = Column(Integer, ForeignKey('user.id'))
    likes = Column(Integer)

    # Post -> Comments: One to Many relationship
    comments = relationship("Comments")

    # Post ID -> Post Media ID: Many to many relationship
    post_media_id = relationship('Post_Media', secondary = 'Post_and_Post_Media_Relationship')

class Post_Media(Base):
    __tablename__ = "post_media"
    id = Column(Integer, primary_key = True)
    media_Type = Column(String(20))
    url = Column(String(100), nullable = False)
    # Post Media ID -> Post ID: Many to many relationship
    post_id = relationship('Post', secondary = 'Post_and_Post_Media_Relationship')

class Comments(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    user_Name = Column(String(20), nullable = False)
    profile_Description = Column(String(100))
    pswd = Column(String(20), nullable = False)
    email = Column(String(30), nullable = False)

    #User ID -> post: One to Many relationship
    post = relationship(Post)

    #User ID -> comments: One to Many relationship
    comments = relationship(Comments)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')