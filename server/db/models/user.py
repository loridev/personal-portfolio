from db.database import Base
from sqlalchemy import Column, Integer, String
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