// Catalog.js

import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import './Catalog.css';

const Catalog = () => {
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    // Получение данных о категориях из API
    const fetchCategories = async () => {
      try {
        const response = await fetch('/api/categories/');
        const data = await response.json();
        setCategories(data);
      } catch (error) {
        console.error('Ошибка при получении данных о категориях', error);
      }
    };

    fetchCategories();
  }, []);

  return (
    <div className="CatalogWrapper">
      <h2>Каталог товаров</h2>
      <ul>
        {categories.map(category => (
          <li key={category.id} className="CategoryItem">
            <Link to={`/catalog/${category.id}`}>
              <h3>{category.name}</h3>
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Catalog;