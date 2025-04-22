"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    # Novas atividades esportivas
    "Soccer Team": {
        "description": "Join the soccer team and compete in local tournaments",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 6:00 PM",
        "max_participants": 22,
        "participants": []
    },
    "Basketball Practice": {
        "description": "Improve your basketball skills and play friendly matches",
        "schedule": "Wednesdays, 3:00 PM - 5:00 PM",
        "max_participants": 15,
        "participants": []
    },
    # Novas atividades artísticas
    "Drama Club": {
        "description": "Explore acting and participate in school plays",
        "schedule": "Mondays and Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 20,
        "participants": []
    },
    "Painting Workshop": {
        "description": "Learn painting techniques and create your own artwork",
        "schedule": "Thursdays, 3:00 PM - 4:30 PM",
        "max_participants": 10,
        "participants": []
    },
    # Novas atividades intelectuais
    "Math Olympiad Training": {
        "description": "Prepare for math competitions with advanced problem-solving",
        "schedule": "Tuesdays, 3:30 PM - 5:00 PM",
        "max_participants": 25,
        "participants": []
    },
    "Debate Club": {
        "description": "Develop public speaking and argumentation skills",
        "schedule": "Fridays, 4:00 PM - 5:30 PM",
        "max_participants": 18,
        "participants": []
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specificy activity
    activity = activities[activity_name]

    # Validar se o aluno já está inscrito
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Already signed up for this activity")

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
