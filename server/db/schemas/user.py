from pydantic import BaseModel
from models import project, job, education, language, skill, image

class UserBase(BaseModel):
  id: int
  bio: str
  email: str

class UserCreate(UserBase):
  password: str

class User(UserBase):
  id: int
  projects: list[project.Project] = []
  jobs: list[job.Job] = []
  educations: list[education.Education] = []
  languages: list[language.Language] = []
  skills: list[skill.Skill] = []
  images: list[image.Image] = []