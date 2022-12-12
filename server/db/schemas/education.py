from pydantic import BaseModel
from image import Image

class EducationBase(BaseModel):
  name: str
  description: str
  begin: str
  end: str

class EducationCreate(EducationBase):
  pass

class Education(EducationBase):
  id: int
  user_id: int
  images: list[Image] = []

  class Config:
    orm_mode: True