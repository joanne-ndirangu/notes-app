import React, { useEffect, useState } from 'react';

function Categories() {
    const [categories, setCategories] = useState([]);

    useEffect(() => {
      fetch('http://127.0.0.1:5000/categories')
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          setCategories(data);
        })
        .catch((error) => {
          console.error('There was a problem with the fetch operation:', error);
        });
    }, []);

    return (
      <div>
        <h1>Categories</h1>
        <ul>
          {categories.map((category) => (
            <li key={category.id}>{category.name}</li>
          ))}
        </ul>
      </div>
    );
  }

  export default Categories;
