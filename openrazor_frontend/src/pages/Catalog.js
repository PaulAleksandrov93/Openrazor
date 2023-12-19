import React from 'react';
import CategoriesList from '../components/CategoriesList';
import { Route, Routes } from 'react-router-dom';
import CategoryProducts from './CategoryProducts'; 
import './Catalog.css';

const Catalog = () => {
  return (
    <div className="catalog-container">
      <h2>Каталог товаров</h2>
      <Routes>
        {/* Отображаем список категорий */}
        <Route index element={<CategoriesList />} />

        {/* Отображаем товары в выбранной категории */}
        <Route path=":categoryId/*" element={<CategoryProducts />} />
      </Routes>
    </div>
  );
};

export default Catalog;