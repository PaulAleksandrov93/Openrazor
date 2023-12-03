import React from 'react';
import Slider from 'react-slick';
import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';
import styled from 'styled-components';

const CarouselWrapper = styled.div`
  width: 100%;
  margin-top: 0px;
  position: relative; /* Добавляем позиционирование для стрелок */
`;

const CarouselImage = styled.img`
  width: 100%;
  height: auto;
`;

const CustomArrow = styled.div`
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background-color: rgba(0, 0, 0, 0.5);
  color: white;
  font-size: 24px;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  border-radius: 50%;
  z-index: 1;
  user-select: none; /* Запрещаем выделение текста */

  &:hover {
    background-color: rgba(0, 0, 0, 0.8);
  }

  &.prev {
    left: 10px; /* Отступ слева для левой стрелки */
  }

  &.next {
    right: 10px; /* Отступ справа для правой стрелки */
  }
`;

const NextArrow = ({ onClick }) => <CustomArrow className="next" onClick={onClick}>{'>'}</CustomArrow>;
const PrevArrow = ({ onClick }) => <CustomArrow className="prev" onClick={onClick}>{'<'}</CustomArrow>;

const Carousel = () => {
  const settings = {
    dots: true,
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1,
    centerMode: true,
    centerPadding: 0,
    arrows: true,
    nextArrow: <NextArrow />,
    prevArrow: <PrevArrow />,
  };

  return (
    <CarouselWrapper>
      <Slider {...settings}>
        <div>
          <CarouselImage src="image_1.jpg" alt="Image 1" />
        </div>
        <div>
          <CarouselImage src="image_2.jpeg" alt="Image 2" />
        </div>
      </Slider>
    </CarouselWrapper>
  );
};

export default Carousel;