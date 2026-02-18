import { motion } from "framer-motion";

function OrbitAnimation() {
  return (
    <div
      style={{
        position: "relative",
        width: "200px",
        height: "200px",
        margin: "40px auto"
      }}
    >
      {/* Orbit Ring */}
      <motion.div
        style={{
          width: "200px",
          height: "200px",
          border: "2px solid #00c6ff",
          borderRadius: "50%",
          position: "absolute"
        }}
        animate={{ rotate: 360 }}
        transition={{ repeat: Infinity, duration: 10, ease: "linear" }}
      />

      {/* Satellite Dot */}
      <motion.div
        style={{
          width: "15px",
          height: "15px",
          background: "#00c6ff",
          borderRadius: "50%",
          position: "absolute",
          top: "0%",
          left: "50%",
          transform: "translate(-50%, -50%)",
          boxShadow: "0 0 20px #00c6ff"
        }}
        animate={{ rotate: -360 }}
        transition={{ repeat: Infinity, duration: 10, ease: "linear" }}
      />

      {/* Center Core */}
      <div
        style={{
          width: "20px",
          height: "20px",
          background: "#0072ff",
          borderRadius: "50%",
          position: "absolute",
          top: "50%",
          left: "50%",
          transform: "translate(-50%, -50%)",
          boxShadow: "0 0 30px #0072ff"
        }}
      />
    </div>
  );
}

export default OrbitAnimation;
