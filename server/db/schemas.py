from pydantic import BaseModel
class ProjectBase(BaseModel):
  name: str
  description: str

class ProjectCreate(ProjectBase):
  pass

class Project(ProjectBase):
  id: int
  user_id: int

  class Config:
    orm_mode: True



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

  class Config:
    orm_mode: True



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

  class Config:
    orm_mode: True



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



class SkillBase(BaseModel):
  name: str

class SkillCreate(SkillBase):
  pass

class Skill(SkillBase):
  id: int
  user_id: int

  class Config:
    orm_mode: True



class UserBase(BaseModel):
  id: int
  bio: str
  email: str

class UserCreate(UserBase):
  password: str

class User(UserBase):
  id: int
  projects: list[Project] = []
  jobs: list[Job] = []
  educations: list[Education] = []
  languages: list[Language] = []
  skills: list[Skill] = []
