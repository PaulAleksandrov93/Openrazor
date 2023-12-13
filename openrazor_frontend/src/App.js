import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer'; // Добавленный компонент
import HomePage from './pages/HomePage';
import NewsPage from './pages/NewsPage';
import ArticlePage from './pages/ArticlePage';
import styled from 'styled-components';

const AppWrapper = styled.div`
  font-family: 'Arial', sans-serif;
  background-color: #f5f5f5;
  color: #333;
`;

const App = () => {
  return (
    <Router>
      <AppWrapper>
        <Header />
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/news" element={<NewsPage />} />
          <Route path="/articles" element={<ArticlePage />} />
        </Routes>
        <Footer /> 
      </AppWrapper>
    </Router>
  );
};

export default App;