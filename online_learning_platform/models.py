## models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    courses = relationship('Course', backref='creator')

    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = password

    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        self.courses.remove(course)


class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    creator_id = Column(Integer, ForeignKey('users.id'))
    content = relationship('Content', backref='course')

    def __init__(self, title: str, description: str, creator):
        self.title = title
        self.description = description
        self.creator = creator

    def add_content(self, content):
        self.content.append(content)

    def remove_content(self, content):
        self.content.remove(content)


class Content(Base):
    __tablename__ = 'content'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'))

    def __init__(self, title: str, body: str, course):
        self.title = title
        self.body = body
        self.course = course
