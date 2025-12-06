import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="bg-blue-600 text-white shadow-lg">
      <div className="container mx-auto px-4">
        <div className="flex justify-between items-center py-4">
          <Link to="/" className="text-2xl font-bold">LibraTrack</Link>
          <div className="space-x-4">
            <Link to="/" className="hover:text-blue-200 transition">Home</Link>
            <Link to="/books" className="hover:text-blue-200 transition">Books</Link>
            <Link to="/members" className="hover:text-blue-200 transition">Members</Link>
            <Link to="/borrow" className="hover:text-blue-200 transition">Borrow</Link>
            <Link to="/register" className="hover:text-blue-200 transition">Register</Link>
          </div>
        </div>
      </div>
    </nav>
  );
}