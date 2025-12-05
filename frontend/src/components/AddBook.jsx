import { useState } from "react";

function AddBook({ addBook }) {
  const [title, setTitle] = useState("");
  const [author, setAuthor] = useState("");

  function handleSubmit(e) {
    e.preventDefault();

    const newBook = { title, author };

    fetch("http://127.0.0.1:8000/books", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(newBook),
    })
      .then(res => res.json())
      .then(data => addBook(data));

    setTitle("");
    setAuthor("");
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        value={title}
        placeholder="Book title"
        onChange={e => setTitle(e.target.value)}
      />
      <input
        value={author}
        placeholder="Author"
        onChange={e => setAuthor(e.target.value)}
      />
      <button type="submit">Add</button>
    </form>
  );
}

export default AddBook;
