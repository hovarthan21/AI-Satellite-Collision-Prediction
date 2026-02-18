import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import axios from "axios";
import { motion } from "framer-motion";

function Signup() {
  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSignup = async () => {
    try {
      await axios.post("http://127.0.0.1:8000/signup", {
        email,
        password,
      });

      alert("Account Created Successfully 🚀");
      navigate("/login");
    } catch (err) {
      alert("Signup Failed");
    }
  };

  return (
    <div className="auth-wrapper">
      <motion.div
        className="auth-card"
        initial={{ opacity: 0, y: 40 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6 }}
      >
        <h2>Create AI Access</h2>

        <input
          type="email"
          placeholder="Email Address"
          onChange={(e) => setEmail(e.target.value)}
        />

        <input
          type="password"
          placeholder="Create Password"
          onChange={(e) => setPassword(e.target.value)}
        />

        <button onClick={handleSignup}>Activate System</button>

        <p>
          Already registered? <Link to="/login">Login here</Link>
        </p>
      </motion.div>
    </div>
  );
}

export default Signup;
