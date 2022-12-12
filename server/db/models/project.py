from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Project(Base):
  __tablename__ = 'projects'

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, index=True)
  description = Column(String, index=True)
  user_id = Column(Integer, ForeignKey("users.id"))

  user = relationship('User', back_populates='projects')