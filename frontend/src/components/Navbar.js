import { Link, useNavigate } from "react-router-dom";
import { useContext } from "react";
import { AuthContext } from "../context/AuthContext";

function Navbar() {
  const { user, logout } = useContext(AuthContext);
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate("/login");
  };

  
  const navBtnStyle = {
    textDecoration: "none",
    padding: "8px 18px",
    borderRadius: "25px",
    border: "2px solid #ff4d88",
    color: "#ff4d88",
    fontWeight: "bold",
    fontFamily: "Times New Roman, serif",
    background: "transparent",
    cursor: "pointer",
    transition: "all 0.3s ease",
  };

  return (
    <nav
      style={{
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        padding: "20px 40px",
        background: "rgba(0,0,0,0.7)",
        backdropFilter: "blur(12px)",
        borderBottom: "1px solid rgba(255,255,255,0.1)",
      }}
    >
      <h2 style={{ color: "#00c6ff" }}>
        🛰 AI Satellite Collision Prediction
      </h2>

      <div style={{ display: "flex", gap: "15px" }}>
        <Link to="/" style={navBtnStyle}>Home</Link>
        <Link to="/about" style={navBtnStyle}>About</Link>

        {user ? (
          <>
            <Link to="/dashboard" style={navBtnStyle}>Dashboard</Link>
            <button onClick={handleLogout} style={navBtnStyle}>
              Logout
            </button>
          </>
        ) : (
          <>
            <Link to="/login" style={navBtnStyle}>Login</Link>
            <Link to="/signup" style={navBtnStyle}>Signup</Link>
          </>
        )}
      </div>
    </nav>
  );
}

export default Navbar;
