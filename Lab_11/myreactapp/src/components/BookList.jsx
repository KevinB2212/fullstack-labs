import React, { useState, useEffect } from 'react';
import Book from './Book';

const BookList = () => {
  const [books, setBooks] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    fetchBooks();
  }, []);

  const fetchBooks = async () => {
    try {
      const response = await fetch(`https://www.googleapis.com/books/v1/volumes?q=computerscience`);
      const data = await response.json();
      setBooks(data.items);
      setIsLoading(false);
    } catch (error) {
      console.error('Error fetching books:', error);
      setIsLoading(false);
    }
  };

  if (isLoading) {
    return <p>Loading...</p>;
  }

  return (
    <div>
      <h2>Book List</h2>
      {books.map(book => (
        <Book key={book.id} book={book} />
      ))}
    </div>
  );
};

export default BookList;
