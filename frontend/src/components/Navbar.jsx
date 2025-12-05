import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav style={{ display: "flex", gap: "20px", padding: "10px", background: "#eee" }}>
      <Link to="/">Home</Link>
      <Link to="/books">Books</Link>
      <Link to="/members">Members</Link>
      <Link to="/borrow">Borrow</Link>
      <Link to="/register">Register</Link>
    </nav>
  );
}

export default Navbar;
