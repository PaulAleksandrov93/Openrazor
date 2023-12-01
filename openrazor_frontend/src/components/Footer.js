import React from 'react';
import styled from 'styled-components';
import { FaFacebook, FaTwitter, FaInstagram } from 'react-icons/fa';

const FooterWrapper = styled.footer`
  background-color: #333;
  color: white;
  padding: 20px;
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap; /* Разрешает перенос на новую строку при необходимости */
`;

const Block = styled.div`
  margin: 10px;
`;

const ContactBlock = styled(Block)`
  h2 {
    font-size: 1em; /* Устанавливаем размер заголовка */
  }
`;

const AddressBlock = styled(Block)`
  h2 {
    font-size: 1em; /* Устанавливаем размер заголовка */
  }
`;

const SocialIcons = styled(Block)`
  display: flex;
  flex-direction: column;
  align-items: center;
  font-size: 1em; /* Уменьшаем размер значков до 1em */
  color: white; /* Цвет значков белый */
`;

const SocialTitle = styled.h2`
  font-size: 1.5em; /* Увеличиваем размер заголовка до 1.5em */
  margin-bottom: 10px; /* Увеличиваем расстояние между заголовком и значками */
`;

const Footer = () => {
  return (
    <FooterWrapper>
      <ContactBlock>
        <h2>Контакты</h2>
        <p>Телефон: +7 (123) 456-7890</p>
        <p>Email: info@openrazor.com</p>
      </ContactBlock>
      <AddressBlock>
        <h2>Адрес</h2>
        <p>123 Улица, Город, Страна</p>
      </AddressBlock>
      <SocialIcons>
        <SocialTitle>Социальные сети</SocialTitle>
        <a href="https://www.facebook.com/" target="_blank" rel="noopener noreferrer">
          <FaFacebook />
        </a>
        <a href="https://twitter.com/" target="_blank" rel="noopener noreferrer">
          <FaTwitter />
        </a>
        <a href="https://www.instagram.com/" target="_blank" rel="noopener noreferrer">
          <FaInstagram />
        </a>
      </SocialIcons>
    </FooterWrapper>
  );
};

export default Footer;