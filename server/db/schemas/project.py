from pydantic import BaseModel
from image import Image

class ProjectBase(BaseModel):
  name: str
  description: str

class ProjectCreate(ProjectBase):
  pass

class Project(ProjectBase):
  id: int
  user_id: int
  images: list[Image] = []

  class Config:
    orm_mode: True