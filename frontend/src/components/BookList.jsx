import BookCard from "./BookCard";

function BookList({ books }) {
  return (
    <div>
      {books.map(book => (
        <BookCard key={book.key} book={book} />
      ))}
    </div>
  );
}

export default BookList;
