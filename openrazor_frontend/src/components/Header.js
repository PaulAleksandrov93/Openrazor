// components/Header.js
import React from 'react';
import { Link } from 'react-router-dom';
import styled from 'styled-components';
import { FaUser, FaShoppingCart } from 'react-icons/fa';

const HeaderWrapper = styled.header`
  background-color: #333;
  color: white;
  padding: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
`;

const Logo = styled.h1`
  margin: 0;
`;

const Menu = styled.nav`
  display: flex;
  justify-content: space-around;
  align-items: center;
  width: 50%;
`;

const MenuItem = styled(Link)`
  color: white;
  text-decoration: none;
`;

const UserIcon = styled(FaUser)`
  font-size: 1.5em;
  margin-left: 10px;
`;

const CartWrapper = styled.div`
  display: flex;
  align-items: center;
`;

const CartIcon = styled(FaShoppingCart)`
  font-size: 1.5em;
  margin-right: 5px;
`;

const CartItemCount = styled.span`
  background-color: red;
  color: white;
  padding: 2px 5px;
  border-radius: 50%;
  margin-left: 5px;
`;

const Header = ({ cartItemCount }) => {
  return (
    <HeaderWrapper>
      <Logo>OpenRazor</Logo>
      <Menu>
        <MenuItem to="/">Главная</MenuItem>
        <MenuItem to="/news">Новости</MenuItem>
        <MenuItem to="/catalog">Каталог товаров</MenuItem>
        <MenuItem to="/articles">Статьи</MenuItem>
        <MenuItem to="/contacts">Контакты</MenuItem>
        <MenuItem to="/reviews">Отзывы и комментарии</MenuItem>
        <MenuItem to="/payment">Оплата и доставка</MenuItem>
      </Menu>
      <CartWrapper>
        <MenuItem to="/profile">
          <UserIcon />
        </MenuItem>
        <MenuItem to="/cart">
          <CartIcon />
          {cartItemCount > 0 && <CartItemCount>{cartItemCount}</CartItemCount>}
        </MenuItem>
      </CartWrapper>
    </HeaderWrapper>
  );
};

export default Header;