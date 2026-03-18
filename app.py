from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List
import sqlite3

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Database setup
DATABASE = 'health_risk_predictor.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS UserHealthData (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            age INTEGER,
            gender TEXT,
            weight REAL,
            height REAL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS HealthRiskAssessment (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            risk_level TEXT,
            recommendations TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Data models
class UserHealthData(BaseModel):
    age: int
    gender: str
    weight: float
    height: float

class HealthRiskAssessment(BaseModel):
    risk_level: str
    recommendations: List[str]

# Routes
@app.get("/", response_class=HTMLResponse)
async def read_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/assess", response_class=HTMLResponse)
async def read_assess(request: Request):
    return templates.TemplateResponse("assess.html", {"request": request})

@app.get("/tips", response_class=HTMLResponse)
async def read_tips(request: Request):
    return templates.TemplateResponse("tips.html", {"request": request})

@app.get("/about", response_class=HTMLResponse)
async def read_about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.post("/api/health-risk")
async def calculate_health_risk(age: int = Form(...), gender: str = Form(...), weight: float = Form(...), height: float = Form(...)):
    # Simple mock logic for risk assessment
    bmi = weight / (height / 100) ** 2
    if bmi < 18.5:
        risk_level = "Low"
        recommendations = ["Consider gaining weight."]
    elif 18.5 <= bmi < 25:
        risk_level = "Normal"
        recommendations = ["Maintain your current lifestyle."]
    else:
        risk_level = "High"
        recommendations = ["Consider losing weight."]

    # Save to database
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO UserHealthData (age, gender, weight, height) VALUES (?, ?, ?, ?)", (age, gender, weight, height))
    cursor.execute("INSERT INTO HealthRiskAssessment (risk_level, recommendations) VALUES (?, ?)", (risk_level, ','.join(recommendations)))
    conn.commit()
    conn.close()

    return {"risk_level": risk_level, "recommendations": recommendations}

@app.get("/api/tips")
async def get_tips():
    # Simple mock tips
    tips = [
        "Stay hydrated.",
        "Exercise regularly.",
        "Eat a balanced diet.",
        "Get enough sleep."
    ]
    return {"tips": tips}
