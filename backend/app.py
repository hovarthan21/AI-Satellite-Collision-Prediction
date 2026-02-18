
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import main 
import ai_predictor

app = FastAPI(
    title="AI Satellite Collision Prediction",
    description="A Deep technology for the Space by Hovarthan",
    version="1.0"
)
@app.get("/")
def home():
    return {"message": "AI Satellite Collision Prediction API is running 🚀"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SatelliteFeatures(BaseModel):
    x: float
    y: float
    z: float
    vx: float
    vy: float
    vz: float
    inclination: float
    eccentricity: float
    RAAN: float
    argument_of_perigee: float
    mean_anomaly: float
    mean_motion: float

@app.get("/collisions")
def get_collisions():
    return main.check_collisions()  
@app.post("/predict")
def predict_collision(sat_features: SatelliteFeatures):
    features_dict = sat_features.dict()
    prob = ai_predictor.predict_collision(features_dict)
    return {"collision_probability": prob}
