import './App.css';
import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import Home from './components/Home';
import Notes from './components/Notes';
import AuthPage from './components/AuthPage';
import SignUp from './components/SignUp';
import Categories from './components/Categories';
import LogIn from './components/LogIn';

function App() {
  return (
    <>
    <div id='footer'>
    <Link to={'/'}>AuthPage</Link>
    <Link to={'/home'}>Home</Link>
    <Link to={'/notes'}>Notes</Link>
    <Link to={'/signup'}>SignUp</Link>
    <Link to={'/categories'}>Categories</Link>
    <Link to={'/login'}>Log In</Link>
    </div>
    <div>
    <Routes>
      <Route path="/" element={<AuthPage />}/>
      <Route path='/home' element={<Home />} />
      <Route path="/notes" element={<Notes />} />
      <Route path="/signup" element={<SignUp />} />
      <Route path="/login" element={<LogIn />}/>
      <Route path="/categories" element={<Categories />} />
    </Routes>
    </div>
    </>
  );
}

export default App;
