from pydantic import BaseModel

class LanguageBase(BaseModel):
  name: str
  level: str

class LanguageCreate(LanguageBase):
  pass

class Language(LanguageBase):
  id: int
  user_id: int

  class Config:
    orm_mode: True