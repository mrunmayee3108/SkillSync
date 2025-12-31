from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class resumeSkills(Base):
    __tablename__ = "resume_skills"
    id = Column(Integer, primary_key = True)
    res_skill = Column(String, nullable = False)


