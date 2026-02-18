import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import { Outlet } from "react-router-dom";

function MainLayout({ children }) {
  return (
    <>
      <Navbar />
      <main>
      {children ? children : <Outlet />}
      </main>
      <Footer />
    </>
  );
}

export default MainLayout;
