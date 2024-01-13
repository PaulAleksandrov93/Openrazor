// Footer.js

import React from 'react';
import './Footer.css';
import { FaFacebook, FaTwitter, FaInstagram } from 'react-icons/fa';

const Footer = () => {
  return (
    <div className="footer-wrapper">
      <div className="contact-block">
        <h2>Контакты</h2>
        <p>Телефон: +7 (123) 456-7890</p>
        <p>Email: info@openrazor.com</p>
      </div>
      <div className="address-block">
        <h2>Адрес</h2>
        <p>123 Улица, Город, Страна</p>
      </div>
      <div className="social-block">
        <h2 className="social-title">Социальные сети</h2>
        <div className="social-icons">
          <a className="social-link" href="https://www.facebook.com/" target="_blank" rel="noopener noreferrer">
            <FaFacebook />
          </a>
          <a className="social-link" href="https://twitter.com/" target="_blank" rel="noopener noreferrer">
            <FaTwitter />
          </a>
          <a className="social-link" href="https://www.instagram.com/" target="_blank" rel="noopener noreferrer">
            <FaInstagram />
          </a>
        </div>
      </div>
    </div>
  );
};

export default Footer;