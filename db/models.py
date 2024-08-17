from sqlalchemy import Column, Integer, String, \
    DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db import Base
from datetime import datetime


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    user_city = Column(String)
    password = Column(String, nullable=False)
    reg_date = Column(DateTime, default=datetime.now())


class UserPost(Base):
    __tablename__ = 'user_posts'

    id = Column(Integer, autoincrement=True, primary_key=True)
    main_text = Column(String, nullable=False)
    post_date = Column(DateTime, default=datetime.now())
    user_id = Column(Integer, ForeignKey('users.id'))

    user_fk = relationship(User, lazy="subquery")


class PostPhoto(Base):
    __tablename__ = 'photos'

    id = Column(Integer, autoincrement=True, primary_key=True)
    post_id = Column(Integer, ForeignKey('user_posts.id'))
    photo = Column(String, nullable=False)
    date = Column(DateTime, default=datetime.now())

    post_fk = relationship(UserPost, lazy='subquery')


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, autoincrement=True, primary_key=True)
    text = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('user_posts.id'))
    date = Column(DateTime, default=datetime.now())

    user_fk = relationship(User, lazy="subquery")
    post_fk = relationship(UserPost, lazy="subquery")


class Hashtag(Base):
    __tablename__ = 'hashtags'

    id = Column(Integer, autoincrement=True, primary_key=True)
    hashtag_name = Column(String, nullable=False)
    post_id = Column(Integer, ForeignKey('user_posts.id'))
    date = Column(DateTime, default=datetime.now())

    post_fk = relationship(UserPost, lazy="subquery")
