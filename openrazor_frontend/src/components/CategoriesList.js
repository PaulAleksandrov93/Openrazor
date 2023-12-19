// CategoriesList.js
import React, { useEffect, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';

const CategoriesList = () => {
  const [categories, setCategories] = useState([]);
  const navigate = useNavigate();

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

  // Обновленный путь - ссылка на категорию
  const navigateToCategoryProducts = (categoryId) => {
    navigate(`/catalog/${categoryId}`); 
  };

  return (
    <ul>
      {categories.map(category => (
        <li key={category.id} onClick={() => navigateToCategoryProducts(category.id)}>
          <Link to={`/catalog/${category.id}`}>{category.name}</Link>
        </li>
      ))}
    </ul>
  );
};

export default CategoriesList;