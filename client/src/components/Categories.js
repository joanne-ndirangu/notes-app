import React, { useEffect, useState } from 'react';

function Categories() {
  const [categories, setCategories] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState(null);
  const [notes, setNotes] = useState([]);

  useEffect(() => {
    // Fetch the list of categories from your API and set it in the 'categories' state.
    fetch('http://127.0.0.1:5000/categories')
      .then((response) => response.json())
      .then((data) => setCategories(data))
      .catch((error) => console.error('Error fetching categories:', error));
  }, []);

  useEffect(() => {
      fetch(`http://127.0.0.1:5000/notes{category.id}`)
        .then((response) => response.json())
        .then((data) => setNotes(data))
        .catch((error) => console.error('Error fetching notes:', error));
    }, [])

  const handleCategoryClick = (category) => {
    setSelectedCategory(category);
  };

  return (
    <>
    <div>
      <h1>Categories</h1>
      <div className="card-container"></div>
        {categories.map((category) => (
          <div className="card" key={category.id}>
            <button onClick={() => handleCategoryClick(category)}>
              {category.name}
            </button>
          </div>
        ))}

      {selectedCategory && (
        <div>
          <h2>Notes in {selectedCategory.name}</h2>
          <ul>
            {notes.map((note) => (
              <li key={note.id}>{note.title}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
    </>
  );
}

export default Categories;
