import './App.css';
import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import Home from './components/Home';
import Notes from './components/Notes';
import SignUp from './components/SignUp';
import Categories from './components/Categories';

function App() {
  return (
    <>
    <div>
    <Link to={'/'}>Home</Link>
    <Link to={'/notes'}>Notes</Link>
    <Link to={'/signup'}>SignUp</Link>
    <Link to={'/categories'}>Categories</Link>
    </div>
    <div>
    <Routes>
      <Route path='/' element={<Home />} />
      <Route path="/notes" element={<Notes />} />
      <Route path="/signup" element={<SignUp />} />
      <Route path="/categories" element={<Categories />} />
    </Routes>
    </div>
    </>
  );
}

export default App;
