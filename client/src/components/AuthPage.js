import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './AuthPage.css';

function AuthPage() {
  const navigate = useNavigate();
  const [isSignUp, setIsSignUp] = useState(false);

  const toggleAuthMode = () => {
    setIsSignUp((prevIsSignUp) => !prevIsSignUp);
  };

  return (
    <>
    <div className="auth-container">
    <div>
      <h1 >Welcome to the Notes App</h1>
      <div className="auth-form">
        <h2 className="auth-heading">{isSignUp ? 'Sign Up' : 'Log In'}</h2>
        {isSignUp ? <SignUpForm navigate={navigate} /> : <LogInForm navigate={navigate} />}
        <p className="auth-switch-text">
          {isSignUp ? 'Already have an account? ' : "Don't have an account? "}
          <button className="auth-switch-button" onClick={toggleAuthMode}>
            {isSignUp ? 'Log In' : 'Sign Up'}
          </button>
        </p>
      </div>
    </div>
    </div>
    </>
  );
}

function LogInForm({ navigate }) {
  const [formData, setFormData] = useState({
    username: '',
    password: '',
  });
  const [error, setError] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch("http://localhost:5000/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    })
      .then((response) => {
        if (response.ok) {
          return response.json();
        } else {
          throw new Error('Invalid username or password');
        }
      })
      .then((data) => {
        console.log(data.message);
        setError(null);
        navigate("/notes");
      })
      .catch((error) => {
        setError(error.message);
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <div className="form-group">
        <input
          type="text"
          id="username"
          name="username"
          placeholder="Username"
          value={formData.username}
          onChange={handleChange}
          required
        />
      </div>
      <div className="form-group">
        <input
          type="password"
          id="password"
          name="password"
          placeholder="Password"
          value={formData.password}
          onChange={handleChange}
          required
        />
      </div>
      <button className="auth-button" type="submit">Login</button>
      {error && <p className="auth-error">{error}</p>}
    </form>
  );
}

function SignUpForm({ navigate }) {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    fetch('http://127.0.0.1:5000/signup', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        navigate("/notes");
      })
      .catch((error) => {
        console.error('Error signing up:', error);
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <div className="form-group">
        <input
          type="text"
          id="username"
          name="username"
          placeholder="Username"
          value={formData.username}
          onChange={handleChange}
          required
        />
      </div>
      <div className="form-group">
        <input
          type="email"
          id="email"
          name="email"
          placeholder="Email"
          value={formData.email}
          onChange={handleChange}
          required
        />
      </div>
      <div className="form-group">
        <input
          type="password"
          id="password"
          name="password"
          placeholder="Password"
          value={formData.password}
          onChange={handleChange}
          required
        />
      </div>
      <button className="auth-button" type="submit">Sign Up</button>
    </form>
  );
}

export default AuthPage;
