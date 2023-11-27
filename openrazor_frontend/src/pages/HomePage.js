import React from 'react';
import Header from '../components/Header';
import Carousel from '../components/Carousel';

const HomePage = () => {
  return (
    <div>
      <Header />
      <Carousel />
      <h2>Добро пожаловать в OpenRazor!</h2>
    </div>
  );
};

export default HomePage;