import React from "react";

function About() {
  return (
    <div style={styles.page}>
      <div style={styles.box}>
        <h1 style={styles.heading}>
          About the AI Collision Prediction System
        </h1>

        <p style={styles.text}>
          The AI Collision Prediction System is an intelligent web-based
          platform developed to estimate and analyze the probability of
          potential satellite collisions using key orbital parameters such as
          altitude, velocity, and inclination.
        </p>

        <p style={styles.text}>
          With the increasing number of satellites in Earth’s orbit,
          especially in Low Earth Orbit (LEO), orbital congestion and
          collision risks have become major global concerns.
        </p>

        <p style={styles.text}>
          This system demonstrates how artificial intelligence and predictive
          analytics can be applied to aerospace safety. By processing
          orbital inputs, the application calculates a collision probability
          score and classifies the associated risk level.
        </p>

        <p style={styles.text}>
          The platform integrates a React-based frontend with a FastAPI
          backend, providing a structured, efficient, and responsive
          predictive environment for educational and research purposes.
        </p>

        <p style={styles.text}>
          Overall, the project promotes proactive monitoring, responsible
          space operations, and improved decision-making in satellite
          mission planning.
        </p>
      </div>
    </div>
  );
}

const styles = {
  page: {
    display: "flex",
    justifyContent: "center",
    padding: "60px 20px",
    backgroundColor: "#f9f9f9",
    minHeight: "100vh"
  },
  box: {
    maxWidth: "900px",
    backgroundColor: "#ffffff",
    padding: "40px",
    borderRadius: "15px",
    border: "2px solid #ff4d88",
    boxShadow: "0 0 25px rgba(255, 77, 136, 0.5)",
    fontFamily: "Times New Roman, serif",
    lineHeight: "1.9",
    color: "#000000",
    textAlign: "justify"
  },
  heading: {
    textAlign: "center",
    marginBottom: "25px",
    color: "#b30059"
  },
  text: {
    marginBottom: "18px",
    fontSize: "16px",
    color: "#000000" 
  }
};

export default About;
