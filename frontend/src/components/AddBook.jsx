import { useState } from "react";
const BACKEND = "http://127.0.0.1:8000";

export default function AddBook({ onAdded }) {
  const [title, setTitle] = useState("");
  const [author, setAuthor] = useState("");
  const [year, setYear] = useState("");

  function submit(e) {
    e.preventDefault();
    const payload = {
      title,
      author,
      published_year: year ? Number(year) : null,
      copies: 1,
      likes: 0,
      rating: 0,
      rating_count: 0,
      is_favorite: false
    };
    fetch(`${BACKEND}/books`, {
      method: "POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify(payload)
    }).then(r => r.json()).then(() => {
      setTitle(""); setAuthor(""); setYear("");
      onAdded && onAdded();
    }).catch(console.error);
  }

  return (
    <form onSubmit={submit} style={{ marginBottom: 12 }}>
      <input placeholder="Title" value={title} onChange={e=>setTitle(e.target.value)} required />
      <input placeholder="Author" value={author} onChange={e=>setAuthor(e.target.value)} />
      <input placeholder="Year" value={year} onChange={e=>setYear(e.target.value)} />
      <button type="submit">Add Book</button>
    </form>
  );
}
