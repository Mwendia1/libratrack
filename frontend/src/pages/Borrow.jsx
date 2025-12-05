import { useEffect, useState } from "react";

function Borrow() {
  const [members, setMembers] = useState([]);
  const [books, setBooks] = useState([]);
  const [selectedMember, setSelectedMember] = useState("");
  const [selectedBook, setSelectedBook] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/members")
      .then(res => res.json())
      .then(data => setMembers(data));

    fetch("http://127.0.0.1:8000/books")
      .then(res => res.json())
      .then(data => setBooks(data));
  }, []);

  function handleBorrow(e) {
    e.preventDefault();

    if (!selectedBook || !selectedMember) return alert("Fill all fields");

    alert(
      `Member "${members.find(m => m.id == selectedMember).name}" borrowed "${books.find(b => b.key == selectedBook).title}"`
    );
  }

  return (
    <div style={{ padding: "20px" }}>
      <h2>Borrow Book</h2>

      <form onSubmit={handleBorrow}>
        <select value={selectedMember} onChange={e => setSelectedMember(e.target.value)}>
          <option value="">Select Member</option>
          {members.map(m => (
            <option key={m.id} value={m.id}>{m.name}</option>
          ))}
        </select>

        <select value={selectedBook} onChange={e => setSelectedBook(e.target.value)}>
          <option value="">Select Book</option>
          {books.map(b => (
            <option key={b.key} value={b.key}>{b.title}</option>
          ))}
        </select>

        <button type="submit">Borrow</button>
      </form>
    </div>
  );
}

export default Borrow;
