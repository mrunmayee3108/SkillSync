# 🧠 SkillSync — Skill Match & Gap Analysis Platform

<p align="left">
  <img src="https://cdn.simpleicons.org/python" height="48" />
  <img src="https://cdn.simpleicons.org/fastapi" height="48" />
  <img src="https://cdn.simpleicons.org/sqlite" height="48" />
  <img src="https://cdn.simpleicons.org/streamlit" height="48" />
  <img src="https://cdn.simpleicons.org/pandas" height="48" />
</p>

**Python · FastAPI · SQLite · Streamlit · Pandas**


## 📘 Project Overview

**SkillSync** is a full-stack **Skill Match & Gap Analysis system** designed for job seekers.

Users select a **job role** and their **resume skills**, and the application analyzes how well their skills match industry expectations.

The system:
- Calculates **skill match percentage**
- Identifies **matched and missing skills**
- Displays a **skill gap analysis table**
- Uses **FastAPI** for backend APIs and **Streamlit** for frontend UI


## 🌐 Live Application

- **Frontend (Streamlit App):**  
  👉 https://skillsync-frontend-mrunmayee.streamlit.app/

- **Backend (FastAPI API):**  
  👉 https://skillsync-gwqj.onrender.com

## 📸 Demo Screenshots
<img width="1919" height="1021" alt="image" src="https://github.com/user-attachments/assets/12b49d37-4cfe-4518-b081-eff1fa1ec16c" />
<img width="1919" height="1011" alt="image" src="https://github.com/user-attachments/assets/f6944776-4e73-4ea3-84c2-00931c0074e8" />
<img width="1919" height="1015" alt="image" src="https://github.com/user-attachments/assets/bb1bde5a-121b-48b5-9398-e31797d9baf9" />


## ✨ Features

- Dropdown selection for job roles
- Multi-select resume skills (avoids typing errors)
- Skill match percentage indicator
- Matched vs Missing skills breakdown
- Skill gap analysis table
- Fully deployed and shareable


## 📁 Project Structure

```

SkillSync/
│
├── frontend/
│   ├── app.py                 # Streamlit frontend
│   └── requirements.txt       # Frontend dependencies
│
├── database.py                # Database configuration
├── models.py                  # SQLAlchemy models
├── schemas.py                 # Pydantic schemas
├── skill_lib.py               # Job role → skills mapping
├── main.py                    # FastAPI backend
├── requirements.txt           # Backend dependencies
│
└── README.md                  # Project documentation

```

> Note: Virtual environments, `__pycache__`, and local database files are excluded from the repository.


## ⚙️ How It Works

1. User selects a **job role**
2. User selects their **resume skills**
3. Frontend sends skills to the backend
4. Backend compares resume skills with required role skills
5. Results returned:
   - Match percentage
   - Matched skills
   - Missing skills
   - Skill gap analysis table


## 🛠️ Tech Stack

### Backend
- FastAPI
- SQLAlchemy
- SQLite
- Pandas

### Frontend
- Streamlit
- Requests
- Pandas


## 🚀 Run Locally

### 1️⃣ Clone the Repository
```

git clone https://github.com/mrunmayee3108/SkillSync.git
cd SkillSync

```

### 2️⃣ Start Backend (FastAPI)
```

pip install -r requirements.txt
uvicorn main:app --reload

```

Backend runs at:
```

http://127.0.0.1:8000

```

### 3️⃣ Start Frontend (Streamlit)
```

pip install -r frontend/requirements.txt
streamlit run frontend/app.py

```


## 🧠 Future Enhancements

- User authentication
- Resume PDF parsing
- Skill recommendations
- NLP-based skill extraction
- User-specific dashboards


## 📄 License

MIT License


## ⭐ Support

If you like this project, please consider giving it a ⭐ on GitHub!

~ Mrunmayee Sachin Potdar

