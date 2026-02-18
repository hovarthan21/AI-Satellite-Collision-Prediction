import torch
import numpy as np
import joblib
from train_collision_model import CollisionMLP  

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = CollisionMLP(input_dim=12).to(device)
model.load_state_dict(torch.load("collision_mlp_model.pt", map_location=device))
model.eval()

scaler = joblib.load("feature_scaler.pkl")

def predict_collision(sat_features):
    """
    sat_features: dict with keys
      x, y, z, vx, vy, vz, inclination, eccentricity,
      RAAN, argument_of_perigee, mean_anomaly, mean_motion
    """
    
    X = np.array([[sat_features[key] for key in [
        'x','y','z','vx','vy','vz','inclination','eccentricity',
        'RAAN','argument_of_perigee','mean_anomaly','mean_motion']]])
    
    
    X_scaled = scaler.transform(X)
    X_tensor = torch.tensor(X_scaled, dtype=torch.float32).to(device)
    
    with torch.no_grad():
        prob = model(X_tensor).item()
    
    return prob
