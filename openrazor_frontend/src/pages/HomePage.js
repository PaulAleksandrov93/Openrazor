import React from 'react';
import styled from 'styled-components';
import Carousel from '../components/Carousel';

const HomePageWrapper = styled.div`
  h2 {
    margin-top: 0;  // Убираем верхний отступ для заголовка
  }
`;

const HomePage = () => {
  return (
    <HomePageWrapper>
      <h2>Добро пожаловать в OpenRazor!</h2>
      <Carousel />
    </HomePageWrapper>
  );
};

export default HomePage;