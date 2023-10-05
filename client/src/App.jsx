import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(0)
  const [users, setUsers] = useState([])

  useEffect(() => {
    fetch('/api/users')
      .then((response) => response.json())
      .then((data) => {
        setUsers(data);
      })
    }, []);

  return (
    <>
      <h1>Notes App</h1>
      <h2>List of Users:</h2>
      <ul>
        {users.map((user) => (
          <li key={user.id}>
            Name:{user.username}
            </li>
        ))}
      </ul>
    </>
  )
}

export default App
