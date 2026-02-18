import { motion } from "framer-motion";

function Footer() {
  return (
    <motion.footer
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 1 }}
      style={{
        textAlign: "center",
        padding: "25px",
        marginTop: "50px",
        borderTop: "1px solid rgba(255,255,255,0.1)",
        background: "rgba(0,0,0,0.6)",
        backdropFilter: "blur(10px)"
      }}
    >
      <h3 style={{ marginBottom: "10px", color: "#00c6ff" }}>
        AI Satellite Collision Prediction
      </h3>

      <p style={{ fontSize: "14px", opacity: 0.8 }}>
        © 2026 Developed by Hovarthan S | An AI Innovator
      </p>

      <p style={{ fontSize: "13px", opacity: 0.6 }}>
        A Deep Technology for Space by Hovarthan
      </p>
    </motion.footer>
  );
}

export default Footer;
