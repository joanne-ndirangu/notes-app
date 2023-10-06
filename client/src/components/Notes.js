import React, { useEffect, useState } from 'react';

function Notes() {
  const [notes, setNotes] = useState([]);
  const [editNote, setEditNote] = useState(null);
  const [editedNote, setEditedNote] = useState({ id: null, content: '' });
  const [newNote, setNewNote] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/notes')
      .then((r) => {
        return r.json();
      })
      .then((data) => {
        setNotes(data);
      });
  }, []);

  const handleEdit = (note) => {
    setEditNote(note);
  };

const handleDelete = (noteId) => {
  const confirmDeletion = window.confirm('Are you sure you want to delete this note?');

  if (confirmDeletion) {
    fetch(`http://127.0.0.1:5000/notes/${noteId}`, {
      method: 'DELETE',
    })
      .then((response) => {
        if (response.status === 204) {
          setNotes((prevNotes) => prevNotes.filter((note) => note.id !== noteId));
        } else {
          console.error('Failed to delete note:', response.statusText);
        }
      })
      .catch((error) => {
        console.error('Error deleting note:', error);
      });
  }
};

const handleSaveEdit = () => {
  // Send a PATCH request to update the note on the server
  fetch(`http://127.0.0.1:5000/notes/${editedNote.id}`, {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ content: editedNote.content }),
  })
    .then((response) => {
      if (response.status === 200) {
        setNotes((prevNotes) =>
          prevNotes.map((note) =>
            note.id === editedNote.id ? { ...note, content: editedNote.content } : note
          )
          );

          // Clear the editedNote state
          setEditedNote({ id: null, content: '' });
        } else {
          // Handle errors or display a message
          console.error('Failed to edit note:', response.statusText);
        }
      })
      .catch((error) => {
        console.error('Error editing note:', error);
      });
  };

  const handleSubmitNewNote = () => {
    // Make a POST request to add the new note to the server
    fetch('http://127.0.0.1:5000/notes', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(newNote),
    })
      .then((response) => response.json())
      .then((data) => {
        // Add the new note to the state
        setNotes([...notes, data]);

        // Clear the newNote state
        setNewNote({ title: '', content: '' });
      });
  };

  return (
    <>
      <h1>My Notes</h1>
      <div className="card-container">
        {notes.map((note) => (
          <div className="card" key={note.id}>
            <strong>{note.title}</strong> <br />
            {note.content} <br />
            <button onClick={() => handleEdit(note)}>Edit</button>
            <button onClick={() => handleDelete(note.id)}>Delete</button>
          </div>
        ))}
      </div>
      {editNote && (
        <div className="edit-form">
          <h2>Edit Note</h2>
          <input
            type="text"
            value={editNote.title}
            onChange={(e) => setEditNote({ ...editNote, title: e.target.value })}
          />
          <textarea
            value={editNote.content}
            onChange={(e) => setEditNote({ ...editNote, content: e.target.value })}
          />
          {/* <button onClick={handleCancelEdit}>Cancel</button> */}
          <button onClick={handleSaveEdit}>Save</button>
        </div>
      )}
    </>
  );
}

export default Notes;
