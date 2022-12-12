from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Job(Base):
  __tablename__ = 'jobs'

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, index=True)
  description = Column(String, index=True)
  begin = Column(String, index=True)
  end = Column(String, index=True)
  user_id = Column(Integer, ForeignKey("users.id"))

  user = relationship('User', back_populates='jobs')