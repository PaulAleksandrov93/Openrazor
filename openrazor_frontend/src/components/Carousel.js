import React from 'react';
import Slider from 'react-slick';
import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';
import styled from 'styled-components';

const CarouselWrapper = styled.div`
  width: 100%;
  margin-top: 20px;
`;

const CarouselImage = styled.img`
  width: 100%;
`;

const Carousel = () => {
  const settings = {
    dots: true,
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1,
  };

  return (
    <CarouselWrapper>
      <Slider {...settings}>
        <div>
          <CarouselImage src={require('../assets/image_1.png').default} alt="Image 1" />
        </div>
        <div>
          <CarouselImage src={require('../assets/image_2.png').default} alt="Image 2" />
        </div>
      </Slider>
    </CarouselWrapper>
  );
};

export default Carousel;