import React from 'react';

const Book = ({ book }) => {
  return (
    <div>
      <h3>{book.volumeInfo.title}</h3>
      <p>Author(s): {book.volumeInfo.authors.join(', ')}</p>
      <p>Publisher: {book.volumeInfo.publisher}</p>
    </div>
  );
};

export default Book;
