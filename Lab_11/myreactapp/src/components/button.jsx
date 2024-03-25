import React from 'react';

const MyButton = () => {
  const handleClick = () => {
    alert("Hi");
  };

  return (
    <button onClick={handleClick}>
      Click Me
    </button>
  );
}

export default MyButton;
