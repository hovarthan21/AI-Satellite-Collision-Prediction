<p align="center">
  <img src="https://img.icons8.com/fluency/240/satellite.png" width="120" style="border-radius:50%;" />
</p>

<h1 align="center">AI Satellite Collision Prediction System</h1>

<p align="center">
  Predicting potential satellite collisions using orbital mechanics, AI optimization, and real-time space-track datasets.
</p>

---

##  Overview

The **AI Satellite Collision Prediction System** is a space analytics platform that predicts possible satellite collisions within a defined orbital window using real NORAD Two-Line Element (TLE) data.

This system propagates satellite positions for **1 hour** and detects potential close approaches within a **10 km threshold**, optimized using **KD-Tree spatial indexing** for performance efficiency.

<p align="center">
  <img src="Satellite.jpg" width="650" alt="Food Logo" />
</p>

---

##  Why This Project Was Developed

With thousands of active satellites and increasing space debris, orbital congestion is a serious risk.

This project was developed to:

- Improve space situational awareness
- Detect potential satellite conjunctions
- Demonstrate AI-driven optimization in aerospace applications
- Build a scalable collision prediction model

---

## Data Sources

This project uses real-world orbital datasets:

- **Celestrak Satellite Data**
  - https://celestrak.org/
- **NORAD Two-Line Element (TLE) Data**
  - Standard orbital format used for satellite tracking
- TLE file format for orbital propagation

These datasets provide updated orbital parameters for Earth-orbiting satellites.

---

##  How It Works

### 1️⃣ Data Collection
- Fetch TLE data from Celestrak
- Parse TLE format into orbital parameters

### 2️⃣ Orbit Propagation
- Uses:
  - `Skyfield`
  - `SGP4 (Simplified General Perturbations Model 4)`
- Predicts satellite positions over a **1-hour window**

### 3️⃣ Spatial Optimization
- Positions stored in 3D coordinate system
- **KD-Tree optimization** reduces comparison complexity
- Efficient nearest-neighbor search for collision candidates

### 4️⃣ Collision Detection Logic
- If distance between satellites ≤ **10 km**
- Flag as potential conjunction event

---

##  What Makes This Unique?

Most academic collision detection systems:
- Require large institutional infrastructure
- Are not optimized for fast spatial search
- Do not combine AI-style optimization with real-time TLE propagation

### This system is unique because:

- ✅ Uses real NORAD data
- ✅ Applies KD-Tree spatial indexing for optimization
- ✅ Lightweight & scalable
- ✅ AI-assisted filtering of conjunction candidates
- ✅ Designed for real-world deployable architecture

To our knowledge, very few independent projects combine:
- Skyfield + SGP4
- KD-Tree optimization
- Real-time TLE ingestion
- AI filtering logic
in a single streamlined system.

---

##  Technology Stack

### Backend
- Python
- Skyfield
- sgp4
- NumPy
- SciPy (KD-Tree)

### Frontend
- React.js
- Glassmorphism UI
- Modern gradient styling

### Data & Standards
- Celestrak Dataset
- NORAD TLE format

---

##  System Parameters

| Parameter | Value |
|------------|--------|
| Propagation Window | 1 Hour |
| Collision Threshold | 10 km |
| Data Source | Celestrak (NORAD TLE) |
| Optimization | KD-Tree |

---

##  Future Enhancements

- Real-time live tracking dashboard
- Machine learning collision probability model
- Debris tracking integration
- 3D orbital visualization
- Cloud deployment for large-scale monitoring

---

##  Author

###  HOVARTHAN S  
**AI & ML Enthusiast | Full Stack Developer | Data Scientist**

I developed this project to explore the intersection of **Artificial Intelligence, Orbital Mechanics, and Real-World Space Data Systems**.  
My goal is to build intelligent, scalable systems that improve **space safety and collision awareness**.

---

## Contact

**Developer:** Your Name  
📧 Email: hovarthan04@gmail.com  
🔗 LinkedIn: https://www.linkedin.com/in/hovarthan-s-06114b281/
🐙 Mobile: +91 9363793810

---

## ⭐ Support

If you find this project valuable, consider giving it a star ⭐ on GitHub.

---

<p align="center">
  <strong>Building Intelligent Systems for Safer Space.</strong>
</p>
