import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="SkillSync",
    page_icon="🧠",
    layout="wide"
)

st.title("Welcome to SkillSync!")
st.subheader("Skill Match and Gap Analysis System for job seekers.")

st.divider()
st.write("Select a job role and analyze your resume skills")

base_url = "http://127.0.0.1:8000"
all_roles = requests.get(f"{base_url}/job-roles")
roles = all_roles.json()["roles"]
skills_catalog = requests.get(f"{base_url}/skills-catalog").json()["skills"]

selected_role = st.selectbox("Select job role", roles)
selected_skills = st.multiselect("Select your skills",skills_catalog)


if st.button("Analyze Skills"):
    if not selected_skills:
        st.warning("Please select at least one skill from the skills catalog.")
    else:
        requests.delete(f"{base_url}/resume/skills")    
        requests.post(f"{base_url}/resume/skills", json={"skill_req": selected_skills})
        analysis = requests.get(f"{base_url}/analysebyrole/{selected_role}").json()
        data = analysis
        
        st.divider()

        st.subheader("Skills Analysis Result🔥")
        st.subheader("Skill match percentage:")
        st.progress(data["match_percentage"]/100)
        st.metric(label="Overall Match", value=f"{data['match_percentage']}%")
        st.subheader("Matched vs Missing Skills:")
        col1, col2 = st.columns(2)
        with col1:
            st.success("Matched Skills")
            for skill in data["matched_skills"]:
                st.write("-", skill)
        with col2:
            st.error("Missing Skills")
            for skill in data["missing skills"]:
                st.write("-", skill)
        
        st.divider()
        st.subheader("Skill Gap Analysis Table")
        df = pd.DataFrame(data["skill gap table"])
        st.dataframe(df, use_container_width=True)


        