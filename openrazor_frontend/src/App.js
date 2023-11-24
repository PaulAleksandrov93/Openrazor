import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/Header';
import HomePage from './pages/HomePage';
import styled from 'styled-components';

const AppWrapper = styled.div`
  font-family: 'Arial', sans-serif;
  background-color: #f5f5f5;
  color: #333;
  padding: 20px;
`;

const App = () => {
  return (
    <Router>
      <AppWrapper>
        <Header />
        <Routes>
          <Route path="/" element={<HomePage />} />
          {/* Добавьте другие роуты для других страниц */}
        </Routes>
      </AppWrapper>
    </Router>
  );
};

export default App;