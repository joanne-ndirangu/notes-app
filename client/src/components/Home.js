import React, { useEffect, useState } from 'react';

function Home() {
  const [notes, setNotes] = useState([]);
  useEffect(() => {
    fetch('http://127.0.0.1:5000/notes')
      .then((r) => {
        return r.json();
      })
      .then((data) => {
        setNotes(data);
      });
  }, []);

  return (
    <div>
      <h1>Welcome to the Notes App</h1>
      <p>This is the home page.</p>
      <div className="card-container">
        {notes.map((note) => (
          <div className="card" key={note.id}>
            <h3>{note.title}</h3>
            <p>{note.content}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Home;
