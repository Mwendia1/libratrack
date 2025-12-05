import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav style={{ display: "flex", gap: 12, padding: 12, background: "#fff" }}>
      <Link to="/">Home</Link>
      <Link to="/books">Books</Link>
      <Link to="/members">Members</Link>
      <Link to="/borrow">Borrow</Link>
      <Link to="/register">Register</Link>
    </nav>
  );
}
