import React, { useEffect, useState } from 'react';

function Notes() {
  const [notes, setNotes] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/notes')
      .then((r) => {
        return r.json();
      }).then((data) => {setNotes(data);
      })
  }, []);

  return (
    <div>
      <h1>My Notes</h1>
      <ul>
        {notes.map((note) => (
          <li key={note.id}>
            <strong>Title:</strong> {note.title}<br />
            <strong>Category:</strong> {note.category}<br />
            <strong>Content:</strong> {note.content}<br />
            <strong>Created At:</strong> {note.created_at}<br />
            <strong>Updated At:</strong> {note.updated_at}<br />
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Notes;
