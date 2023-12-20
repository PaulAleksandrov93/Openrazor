// CategoryProducts.js
import React, { useEffect, useState } from 'react';
import { Link, useParams, useNavigate } from 'react-router-dom';

const CategoryProducts = () => {
  const { categoryId } = useParams();
  const [products, setProducts] = useState([]);
  const navigate = useNavigate();

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

  const navigateToProductDetails = (productId) => {
    navigate(`/catalog/${categoryId}/${productId}`);
  };

  return (
    <div>
      <h2>Товары в категории</h2>
      <ul>
        {products.map(product => (
          <li key={product.id} onClick={() => navigateToProductDetails(product.id)}>
            <Link to={`/catalog/${categoryId}/${product.id}`}>{product.name}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CategoryProducts;