from fastapi import FastAPI, Depends
from database import Base, SessionLocal, engine
from sqlalchemy.orm import Session
from models import resumeSkills
from schemas import bulkskillCreate
from skill_lib import JOB_SKILL_LIBRARY
import pandas as pd
from typing import List

Base.metadata.create_all(bind = engine)
app = FastAPI(title = "Skill Match API")

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "Hello, Welcome to SKillSync!"}

@app.post("/resume/skills")
def add_resume_skill(skill: bulkskillCreate, db: Session = Depends(get_db)):
    for skill_name in skill.skill_req:
        rs = resumeSkills(res_skill = skill_name)
        db.add(rs)
    db.commit()
    return {"message": f"Added {len(skill.skill_req)} skills"}

@app.get("/resume/skills") 
def get_all_skills(db: Session = Depends(get_db)):
    skills = db.query(resumeSkills).all()
    return {"skills": [s.res_skill for s in skills]}

@app.get("/job-roles")  
def get_available_roles():
    return {
        "roles": list(JOB_SKILL_LIBRARY.keys())
    }

@app.get("/skills-catalog")
def get_skills_catalog():
    skills = set()
    for role_skills in JOB_SKILL_LIBRARY.values():
        skills.update(role_skills)

    return {"skills": sorted(skills)}

@app.delete("/resume/skills")
def del_all_skills(db: Session = Depends(get_db)):
    count = db.query(resumeSkills).count()
    db.query(resumeSkills).delete()
    db.commit()
    return {"message": f"Deleted {count} skills"}

# analysis:
@app.get("/analysebyrole/{role_name}")
def analyse_by_role(role_name: str, db: Session = Depends(get_db)):
    role_name = role_name.lower()
    
    if role_name not in JOB_SKILL_LIBRARY: 
        return {
            "error": "Job role not found!", 
            "available_roles": list(JOB_SKILL_LIBRARY.keys())
        }
    
    required_skills = set(JOB_SKILL_LIBRARY[role_name])
    resume_skills = db.query(resumeSkills).all()

    resume_set = {rs.res_skill.lower() for rs in resume_skills}

    matched = list(required_skills & resume_set)
    missing = list(required_skills - resume_set)

    match_percentage = round(len(matched)/len(required_skills)*100, 2) if required_skills else 0

    df = pd.DataFrame({
        "Skill": matched + missing,
        "Status": ["matched"]*len(matched) + ["missing"]*len(missing)
    })

    return{
        "job_role": role_name, 
        "match_percentage": match_percentage, 
        "matched_skills": matched, 
        "missing skills": missing, 
        "skill gap table": df.to_dict() 
    }
