import { useState } from "react";
import axios from "axios";
import { motion } from "framer-motion";

function Dashboard() {
  const [satelliteName, setSatelliteName] = useState("");
  const [altitude, setAltitude] = useState("");
  const [velocity, setVelocity] = useState("");
  const [inclination, setInclination] = useState("");
  const [result, setResult] = useState(null);

  const handlePredict = async () => {
  try {
    const response = await axios.post("http://127.0.0.1:8000/predict", {
      satellite_name: satelliteName,
      altitude: Number(altitude),
      velocity: Number(velocity),
      inclination: Number(inclination),
    });

    console.log("Response:", response.data);
    setResult(response.data);
  } catch (error) {
    console.error(error);
    alert("Prediction Failed");
  }
};


  return (
  <div className="dashboard-wrapper">
    <div className="dashboard-card">
      <h2>AI Collision Prediction Panel</h2>

      <input
  type="text"
  placeholder="Satellite Name"
  value={satelliteName}
  onChange={(e) => setSatelliteName(e.target.value)}
/>

      <input
  type="number"
  placeholder="Altitude (km)"
  value={altitude}
  onChange={(e) => setAltitude(e.target.value)}
/>

<input
  type="number"
  placeholder="Velocity (km/s)"
  value={velocity}
  onChange={(e) => setVelocity(e.target.value)}
/>

<input
  type="number"
  placeholder="Inclination (degrees)"
  value={inclination}
  onChange={(e) => setInclination(e.target.value)}
/>


      <button onClick={handlePredict}>
        Run AI Prediction
      </button>

      {result && (
  <div>
    <h3>Prediction Result</h3>
    <p><strong>Satellite:</strong> {result.satellite_name}</p>
    <p><strong>Collision Probability:</strong> {result.collision_probability}</p>
    <p><strong>Risk Level:</strong> {result.risk_level}</p>
  </div>
)}


    </div>
  </div>
  );
}

export default Dashboard;
