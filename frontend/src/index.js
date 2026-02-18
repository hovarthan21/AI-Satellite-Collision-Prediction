import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "./styles/global.css";


const link = document.createElement("link");
link.href =
  "https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;800&display=swap";
link.rel = "stylesheet";
document.head.appendChild(link);

const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
