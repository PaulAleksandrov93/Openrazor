// Catalog.js
import React from 'react';
import CategoriesList from '../components/CategoriesList';
import { Route, Routes } from 'react-router-dom';
import CategoryProducts from './CategoryProducts'; 
import ProductDetails from './ProductDetails';
import './Catalog.css';

const Catalog = () => {
  return (
    <div className="catalog-container">
      <h2>Каталог товаров</h2>
      <Routes>
        {/* Отображаем список категорий */}
        <Route path="/" element={<CategoriesList />} />

        {/* Отображаем товары в выбранной категории */}
        <Route path=":categoryId/*" element={<CategoryProducts />} />

        {/* Добавляем роут для ProductDetails */}
        <Route path=":categoryId/:productId" element={<ProductDetails />} />
      </Routes>
    </div>
  );
};

export default Catalog;