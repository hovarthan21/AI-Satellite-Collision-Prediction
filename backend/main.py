from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from skyfield.api import load, EarthSatellite
import numpy as np
from collections import defaultdict
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "OrbitalGuard AI Backend Running"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

users = {}

class User(BaseModel):
    email: str
    password: str

@app.post("/signup")
def signup(user: User):
    if user.email in users:
        raise HTTPException(status_code=400, detail="User already exists")
    users[user.email] = user.password
    return {"message": "User created successfully"}

@app.post("/login")
def login(user: User):
    if user.email not in users or users[user.email] != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful", "token": "dummy-token"}

from pydantic import BaseModel

class PredictionInput(BaseModel):
    satellite_name: str
    altitude: float
    velocity: float
    inclination: float

@app.post("/predict")
def predict(data: PredictionInput):

    risk_score = (
        data.altitude / 2000 +
        data.velocity / 50 +
        data.inclination / 180
    )

    probability = round(min(risk_score / 3, 1), 2)

    return {
        "satellite_name": data.satellite_name,
        "collision_probability": probability,
        "risk_level": "High" if probability > 0.6 else "Low"
    }

ts = load.timescale()
tle_path = os.path.join("data", "active.tle")

@app.get("/collisions")
def check_collisions():
    satellites = []
    with open(tle_path, 'r') as file:
        lines = file.readlines()

    for i in range(0, len(lines), 2):
        line1 = lines[i].strip()
        line2 = lines[i+1].strip()
        sat_number = line1[2:7]
        name = f"SAT-{sat_number}"
        satellites.append(EarthSatellite(line1, line2, name, ts))

    t = ts.now()
    positions = []
    names = []

    for sat in satellites:
        pos = sat.at(t).position.km
        if not np.isnan(pos).any():
            positions.append(pos)
            names.append(sat.name)

    positions = np.array(positions)

    threshold = 10
    results = []

    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            dist = np.linalg.norm(positions[i] - positions[j])
            if dist < threshold:
                results.append({
                    "satellite_1": names[i],
                    "satellite_2": names[j],
                    "distance_km": round(dist, 2)
                })

    return results
