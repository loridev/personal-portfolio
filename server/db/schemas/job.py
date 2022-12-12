from pydantic import BaseModel
from image import Image

class JobBase(BaseModel):
  name: str
  description: str
  begin: str
  end: str

class JobCreate(JobBase):
  pass

class Job(JobBase):
  id: int
  user_id: int
  images: list[Image] = []

  class Config:
    orm_mode: True