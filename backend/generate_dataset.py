from skyfield.api import load, EarthSatellite
import os
import numpy as np
import pandas as pd
from scipy.spatial import cKDTree


TLE_PATH = "data/active.tle"      
COLLISION_THRESHOLD_KM = 10       

ts = load.timescale()
satellites = []

with open(TLE_PATH, 'r') as f:
    lines = f.readlines()

for i in range(0, len(lines), 2):
    line1 = lines[i].strip()
    line2 = lines[i+1].strip()
    sat_number = line1[2:7]
    name = f"SAT-{sat_number}"
    satellites.append(EarthSatellite(line1, line2, name, ts))

print(f"Loaded {len(satellites)} satellites 🚀")

data = []

for sat in satellites:
    try:
        geocentric = sat.at(ts.now())
        pos = geocentric.position.km
        vel = geocentric.velocity.km_per_s

        if np.isnan(pos).any() or np.isnan(vel).any():
            continue

        elem = sat.model
        inc = np.degrees(elem.inclo)
        ecc = elem.ecco
        raan = np.degrees(elem.nodeo)
        argp = np.degrees(elem.argpo)
        mean_anomaly = np.degrees(elem.mo)
        mean_motion = elem.no_kozai * (24*60/(2*np.pi))  

        data.append({
            "name": sat.name,
            "x": pos[0], "y": pos[1], "z": pos[2],
            "vx": vel[0], "vy": vel[1], "vz": vel[2],
            "inclination": inc,
            "eccentricity": ecc,
            "RAAN": raan,
            "argument_of_perigee": argp,
            "mean_anomaly": mean_anomaly,
            "mean_motion": mean_motion
        })
    except Exception as e:
        print(f"Skipping {sat.name}: {e}")

df = pd.DataFrame(data)
print(f"Positions/velocities recorded: {len(df)} satellites")

positions = df[["x","y","z"]].values
tree = cKDTree(positions)

pairs = tree.query_pairs(r=COLLISION_THRESHOLD_KM)
labels = np.zeros(len(df), dtype=int)

for i, j in pairs:
    labels[i] = 1
    labels[j] = 1

df["collision_label"] = labels
print(f"Collisions detected: {len(pairs)}")

df.to_csv("satellite_ai_dataset_fast.csv", index=False)
print("✅ Fast dataset saved: satellite_ai_dataset_fast.csv")
