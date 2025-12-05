import { useState } from "react";

export default function AddBook({ onBookAdded }) {
  const [form, setForm] = useState({ title: "", author: "" });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await fetch("http://127.0.0.1:8000/books/", {
        method: "POST",
        headers: { "Content-Type": "application/json", Accept: "application/json" },
        body: JSON.stringify(form),
      });

      if (!res.ok) {
        const errBody = await res.json().catch(() => ({}));
        const msg = errBody.detail || errBody || `HTTP ${res.status}`;
        throw new Error(msg);
      }

      const data = await res.json();
      alert(`Book "${data.title}" added!`);
      setForm({ title: "", author: "" });
      if (onBookAdded) onBookAdded(data);
    } catch (err) {
      console.error(err);
      alert("Error adding book. Check console for details.");
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>➕ Add New Book</h2>
      <form onSubmit={handleSubmit} style={styles.form}>
        <input
          name="title"
          placeholder="Book Title"
          value={form.title}
          onChange={handleChange}
        />
        <input
          name="author"
          placeholder="Author"
          value={form.author}
          onChange={handleChange}
        />
        <button type="submit">Add</button>
      </form>
    </div>
  );
}

const styles = {
  form: {
    display: "flex",
    flexDirection: "column",
    gap: "10px",
    width: "250px",
  },
};