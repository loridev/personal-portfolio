from .database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class User(Base):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True, index=True)
  bio = Column(String, index=True)
  email = Column(String, unique=True, index=True)
  password = Column(String)

  projects = relationship('Project', back_populates='user')
  jobs = relationship('Job', back_populates='user')
  educations = relationship('Education', back_populates='user')
  languages = relationship('Language', back_populates='user')
  skills = relationship('Skill', back_populates='user')


class Project(Base):
  __tablename__ = 'projects'

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, index=True)
  description = Column(String, index=True)
  user_id = Column(Integer, ForeignKey("users.id"))

  user = relationship('User', back_populates='projects')


class Job(Base):
  __tablename__ = 'jobs'

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, index=True)
  description = Column(String, index=True)
  begin = Column(String, index=True)
  end = Column(String, index=True)
  user_id = Column(Integer, ForeignKey("users.id"))

  user = relationship('User', back_populates='jobs')


class Education(Base):
  __tablename__ = 'educations'

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, index=True)
  description = Column(String, index=True)
  begin = Column(String, index=True)
  end = Column(String, index=True)
  user_id = Column(Integer, ForeignKey("users.id"))

  user = relationship('User', back_populates='educations')


class Language(Base):
  __tablename__ = 'languages'

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, index=True)
  level = Column(String, index=True)
  user_id = Column(Integer, ForeignKey("users.id"))

  user = relationship('User', back_populates='languages')


class Skill(Base):
  __tablename__ = 'skills'

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, index=True)
  user_id = Column(Integer, ForeignKey("users.id"))

  user = relationship('User', back_populates='skills')