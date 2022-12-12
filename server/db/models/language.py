from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Language(Base):
  __tablename__ = 'languages'

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, index=True)
  level = Column(String, index=True)
  user_id = Column(Integer, ForeignKey("users.id"))

  user = relationship('User', back_populates='languages')