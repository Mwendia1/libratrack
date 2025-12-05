import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav style={styles.nav}>
      <h2>📚 LibraTrack</h2>

      <div style={styles.links}>
        <Link style={styles.link} to="/">Books</Link>
        <Link style={styles.link} to="/add">Add Book</Link>
        <Link style={styles.link} to="/members">Members</Link>
        <Link style={styles.link} to="/borrow">Borrow</Link>
      </div>
    </nav>
  );
}

const styles = {
  nav: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",  // vertical center
    padding: "15px 25px",
    background: "#222",
    color: "white",
  },
  links: {
    display: "flex",
    gap: "20px",
    // removed position: fixed
  },
  link: {
    color: "white",
    textDecoration: "none",
    fontWeight: "bold",
  },
};

export default Navbar;
