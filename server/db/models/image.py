from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Image(Base):
  __tablename__ = 'images'

  id = Column(Integer, primary_key=True, index=True)
  url = Column(String, index=True)
  user_id = Column(Integer, ForeignKey("users.id"))
  job_id = Column(Integer, ForeignKey("jobs.id"))
  education_id = Column(Integer, ForeignKey("educations.id"))
  project_id = Column(Integer, ForeignKey("projects.id"))

  user = relationship('User', back_populates='images')
  job = relationship('Job', back_populates='images')
  education = relationship('Education', back_populates='images')
  project = relationship('Project', back_populates='images')