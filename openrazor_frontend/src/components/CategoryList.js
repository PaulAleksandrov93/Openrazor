import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

const CategoryList = () => {
  const [categories, setCategories] = useState([]);

  useEffect(() => {
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
    <div>
      <h2>Каталог товаров</h2>
      <ul>
        {categories.map(category => (
          <li key={category.id}>
            <Link to={`/catalog/${category.id}`}>{category.name}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CategoryList;