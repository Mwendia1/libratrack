import { useEffect, useState } from "react";
const BACKEND = "http://127.0.0.1:8000";

export default function Borrow() {
  const [members, setMembers] = useState([]);
  const [books, setBooks] = useState([]);
  const [memberId, setMemberId] = useState("");
  const [bookId, setBookId] = useState("");

  useEffect(() => {
    fetch(`${BACKEND}/members`).then(r => r.json()).then(setMembers).catch(console.error);
    fetch(`${BACKEND}/books`).then(r => r.json()).then(setBooks).catch(console.error);
  }, []);

  function handleBorrow(e) {
    e.preventDefault();
    if (!memberId || !bookId) return alert("Choose member and book");
    fetch(`${BACKEND}/borrow`, {
      method: "POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify({ member_id: Number(memberId), book_id: Number(bookId) })
    })
      .then(r => {
        if (!r.ok) return r.json().then(j => Promise.reject(j));
        return r.json();
      })
      .then(() => alert("Borrow recorded"))
      .catch(err => alert(err.detail || JSON.stringify(err)));
  }

  return (
    <div style={{ padding: 20 }}>
      <h2>Borrow</h2>
      <form onSubmit={handleBorrow}>
        <div>
          <select value={memberId} onChange={e => setMemberId(e.target.value)}>
            <option value="">Select member</option>
            {members.map(m => <option key={m.id} value={m.id}>{m.name}</option>)}
          </select>
        </div>
        <div>
          <select value={bookId} onChange={e => setBookId(e.target.value)}>
            <option value="">Select book</option>
            {books.map(b => <option key={b.id} value={b.id}>{b.title} ({b.copies})</option>)}
          </select>
        </div>
        <button type="submit">Borrow</button>
      </form>
    </div>
  );
}
