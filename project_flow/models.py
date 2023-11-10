from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    """
    Represents a user in the system.
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)

    projects = relationship('Project', back_populates='user')

class Project(Base):
    """
    Represents a project in the system.
    """
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    project_name = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='projects')
    tasks = relationship('Task', back_populates='project')

class Task(Base):
    """
    Represents a task in the system.
    """
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    task_name = Column(String)
    description = Column(String)
    deadline = Column(Date)
    project_id = Column(Integer, ForeignKey('projects.id'))

    project = relationship('Project', back_populates='tasks')