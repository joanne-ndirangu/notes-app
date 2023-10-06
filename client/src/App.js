import './App.css';
import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import Notes from './components/Notes';
import AuthPage from './components/AuthPage';
import SignUp from './components/SignUp';
import Categories from './components/Categories';
// import LogIn from './components/LogIn';
import NewNote from './components/NewNote';

function App() {
  return (
    <>
    <div id='footer'>
    <Link to={'/'}>Log In</Link>
    <Link to={'/notes'}>Notes</Link>
    <Link to={'/signup'}>SignUp</Link>
    <Link to={'/categories'}>Categories</Link>
    {/* <Link to={'/'}>Log In</Link> */}
    <Link to={'/newnote'}>Create Note</Link>
    </div>
    <div>
    <Routes>
      <Route path="/" element={<AuthPage />}/>
      <Route path="/notes" element={<Notes />} />
      <Route path="/signup" element={<SignUp />} />
      {/* <Route path="/login" element={<LogIn />}/> */}
      <Route path="/categories" element={<Categories />} />
      <Route path='/newnote' element={<NewNote/> }/>
    </Routes>
    </div>
    </>
  );
}

export default App;
