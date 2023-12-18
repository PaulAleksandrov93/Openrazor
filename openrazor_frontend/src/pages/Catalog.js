// Catalog.js
import React, { useEffect, useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import './Catalog.css';

const Catalog = () => {
  const [categories, setCategories] = useState([]);
  const { categoryId } = useParams();

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
    <div className="CatalogWrapper">
      <h2>Каталог товаров</h2>
      {categoryId ? (
        // Если выбрана конкретная категория, отображаем список товаров
        <ProductList categoryId={categoryId} />
      ) : (
        // Если не выбрана конкретная категория, отображаем список всех категорий
        <CategoryList categories={categories} />
      )}
    </div>
  );
};

const CategoryList = ({ categories }) => {
  return (
    <ul>
      {categories.map(category => (
        <li key={category.id} className="CategoryItem">
          <Link to={`/catalog/${category.id}`}>
            <h3>{category.name}</h3>
          </Link>
        </li>
      ))}
    </ul>
  );
};

const ProductList = ({ categoryId }) => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await fetch(`/api/products/?category=${categoryId}`);
        const data = await response.json();
        setProducts(data);
      } catch (error) {
        console.error('Ошибка при получении данных о товарах', error);
      }
    };

    fetchProducts();
  }, [categoryId]);

  return (
    <ul>
      {products.map(product => (
        <li key={product.id} className="ProductItem">
          <h3>{product.name}</h3>
          <p>{product.description}</p>
          <p>Цена: {product.price} руб.</p>
        </li>
      ))}
    </ul>
  );
};

export default Catalog;