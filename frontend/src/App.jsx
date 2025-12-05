import { BrowserRouter, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Books from "./components/Books";
import AddBook from "./components/AddBook";
import Members from "./components/Members";
import Borrow from "./components/Borrow";
//import Register from "./pages/register";  // Capitalized

export default function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path="/" element={<Books />} />
        <Route path="/add" element={<AddBook />} />
        <Route path="/members" element={<Members />} />
        <Route path="/borrow" element={<Borrow />} />
        
      </Routes>
    </BrowserRouter>
  );
}
