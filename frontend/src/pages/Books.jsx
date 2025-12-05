import { useEffect, useState } from "react";
import BookList from "../components/BookList";
import AddBook from "../components/AddBook";

function Books() {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    fetch("https://openlibrary.org/search.json?q=the+hobbit")
      .then(res => res.json())
      .then(data => setBooks(data));
  }, []);

  function addBook(newBook) {
    setBooks([...books, newBook]);
  }

  return (
    <div style={{ padding: "20px" }}>
      <h2>Books</h2>
      <AddBook addBook={addBook} />
      <BookList books={books} />
    </div>
  );
}

export default Books;
