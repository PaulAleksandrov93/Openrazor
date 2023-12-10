import React from 'react';
import styled from 'styled-components';
import Carousel from '../components/Carousel';
import NewsList from '../components/NewsList';

const HomePageWrapper = styled.div`
  h2 {
    margin-top: 0;  // Убираем верхний отступ для заголовка
  }
`;

const HomePage = () => {
  return (
    <HomePageWrapper>
      <Carousel />
      <NewsList />
    </HomePageWrapper>
  );
};

export default HomePage;