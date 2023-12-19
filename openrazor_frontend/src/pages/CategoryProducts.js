// CategoryProducts.js
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

const CategoryProducts = () => {
  const { categoryId } = useParams();
  const [products, setProducts] = useState([]);

  useEffect(() => {
    const fetchProductsInCategory = async () => {
      try {
        const response = await fetch(`/api/categories/${categoryId}/products/`);
        const data = await response.json();
        setProducts(data);
      } catch (error) {
        console.error('Ошибка при получении данных о товарах в категории', error);
      }
    };

    fetchProductsInCategory();
  }, [categoryId]);

  return (
    <div>
      <h2>Товары в категории</h2>
      <ul>
        {products.map(product => (
          <li key={product.id}>
            <h3>{product.name}</h3>
            <p>{product.description}</p>
            <p>Цена: {product.price} руб.</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CategoryProducts;