import BookCard from "./BookCard";

export default function BookList({ books, remote=false, onSave, onLike, onToggleFavorite, onRate, savedBooks=[] }) {
  return (
    <div>
      {books && books.length ? books.map((b, i) =>
        <BookCard
          key={b.key ?? b.id ?? i}
          book={b}
          remote={remote}
          onSave={onSave}
          onLike={onLike}
          onToggleFavorite={onToggleFavorite}
          onRate={onRate}
          savedBooks={savedBooks}
        />
      ) : <p>No books found.</p>}
    </div>
  );
}
