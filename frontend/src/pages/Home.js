import { motion } from "framer-motion";
import { Link } from "react-router-dom";
import "./Home.css";

function Home() {
  return (
    <div className="space-container">
      <motion.div
        initial={{ opacity: 0, y: 50 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 1 }}
        className="glass-card"
        style={{ textAlign: "center" }}
      >
        <h1>🛰 AI Satellite Collision Prediction</h1>

        <p style={{ marginTop: "20px", lineHeight: "1.8" }}>
          A Deep Technology for Space by Hovarthan.
          <br />
          This intelligent AI system predicts potential satellite collisions
          using advanced deep learning models.
        </p>

        <div style={{ marginTop: "30px" }}>
          <Link to="/login">
            <button className="launch-btn">
              🚀 Launch System
              <span className="rocket-icon"> 🚀</span>
            </button>
          </Link>
        </div>

      </motion.div>
    </div>
  );
}

export default Home;
