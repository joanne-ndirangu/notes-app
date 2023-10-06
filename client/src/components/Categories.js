import React, { useEffect, useState } from 'react';

function Categories() {
  const [categories, setCategories] = useState([]);
  const [notes, setNotes] = useState([]);

  // Fetch categories and notes and update state
useEffect(() => {
  fetch('http://localhost:5000/categories')
    .then((response) => response.json())
    .then((data) => setCategories(data));

  fetch('http://localhost:5000/notes')
    .then((response) => response.json())
    .then((data) => setNotes(data));
}, [])

return (
  <>
    <h1>Categories</h1>
      <div className='card-container'>
      {categories.map((category) => (
        <div className='card'>
        <div key={category.id}>{category.name}</div>
        </div>
      ))}
      </div>

    <h1>Notes</h1>
    <div className='card-container'>
      {notes.map((note) => (
        <div className='card'>
        <div key={note.id}>
          {note.title} - <strong>{note.category}</strong>
          {/* <p>{note.content}</p> */}
          {note.categories && note.categories.length > 0 && (
            <p>Categories: {note.categories.join(', ')}</p>
            )}
        </div>
        </div>
      ))}
    </div>
  </>
);

}

export default Categories