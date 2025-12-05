function BookCard({ book }) {
  return (
    <div style={{ padding: "10px", border: "1px solid #ccc", marginTop: "10px" }}>
      <h3>{book.title}</h3>
      <p>Author: {book.author}</p>
    </div>
  );
}

export default BookCard;
