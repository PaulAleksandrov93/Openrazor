// ProductDetails.js
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

const ProductDetails = () => {
  const { categoryId, productId } = useParams();
  const [product, setProduct] = useState(null);

  useEffect(() => {
    const fetchProductDetails = async () => {
      try {
        const response = await fetch(`/api/categories/${categoryId}/products/${productId}/`);
        const data = await response.json();
        setProduct(data);
      } catch (error) {
        console.error('Ошибка при получении данных о товаре', error);
      }
    };

    fetchProductDetails();
  }, [categoryId, productId]);

  const handleBuyNow = () => {
    // Здесь будет логика для "Купить в один клик"
    console.log('Купить в один клик:', product);
  };

  const handleAddToCart = () => {
    // Здесь будет логика для "Добавить в корзину"
    console.log('Добавить в корзину:', product);
  };

  if (!product) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h2>{product.name}</h2>
      <p>{product.description}</p>
      <p>Цена: {product.price} руб.</p>

      {/* Кнопки "Купить в один клик" и "Добавить в корзину" */}
      <button onClick={handleBuyNow}>Купить в один клик</button>
      <button onClick={handleAddToCart}>Добавить в корзину</button>
    </div>
  );
};

export default ProductDetails;