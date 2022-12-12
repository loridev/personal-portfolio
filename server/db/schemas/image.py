from pydantic import BaseModel

class ImageBase(BaseModel):
  url: str

class ImageCreate(ImageBase):
  pass

class Image(ImageBase):
  id: int
  user_id: int | None = None
  project_id: int | None = None
  job_id: int | None = None

  class Config:
    orm_mode = True