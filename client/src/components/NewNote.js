import React, { useState, useEffect } from 'react';

function NewNote({ onNoteCreated }) {
  const [newNote, setNewNote] = useState({ title: '', content: '' });

  const handleSubmitNewNote = () => {
    fetch('http://127.0.0.1:5000/notes', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(newNote),
    })
      .then((response) => response.json())
      .then((data) => {
        setNewNote({ title: '', content: '' });
        onNoteCreated(data);
      })
      .catch((error) => {
        console.error('Error creating new note:', error);
      });
  };

  return (
    <div className="edit-container">
      <h2>Create New Note</h2>
      <input
        type="text"
        placeholder="Title"
        value={newNote.title}
        onChange={(e) => setNewNote({ ...newNote, title: e.target.value })}
      />
      <textarea
        placeholder="Content"
        value={newNote.content}
        onChange={(e) => setNewNote({ ...newNote, content: e.target.value })}
      />
      <button onClick={handleSubmitNewNote}>Save</button>
    </div>
  );
}

export default NewNote;
