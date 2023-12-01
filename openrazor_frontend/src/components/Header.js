import React from 'react';
import { Link } from 'react-router-dom';
import styled from 'styled-components';
import { useSpring, animated } from 'react-spring';
import { FaUser, FaShoppingCart } from 'react-icons/fa';

const HeaderWrapper = styled.header`
  background-color: rgba(51, 51, 51, 0.8);
  color: white;
  padding: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: fixed;
  width: 100%;
  top: 0;
  z-index: 1000;
  margin-bottom: 20px; /* Добавим нижний отступ, чтобы устранить наезд на Carousel */
`;

const Logo = styled.h1`
  margin: 0;
  font-family: 'YourDesiredFont', sans-serif;
`;

const Menu = styled.nav`
  display: flex;
  justify-content: space-around;
  align-items: center;
  width: 50%;
`;

const AnimatedLink = animated(Link);
const AnimatedUserIcon = animated(FaUser);
const AnimatedCartIcon = animated(FaShoppingCart);

const AnimatedMenuItem = styled(AnimatedLink)`
  color: white;
  text-decoration: none;
  position: relative;
  overflow: hidden;

  &:before {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 2px;
    background-color: white;
    transform-origin: 100% 50%;
    transform: scaleX(0);
    transition: transform 0.3s ease-out;
  }

  &:hover {
    &:before {
      transform: scaleX(1);
    }
  }
`;

const UserIcon = styled(AnimatedUserIcon)`
  font-size: 1.2em;
  margin-left: -5px;
`;

const CartWrapper = styled.div`
  display: flex;
  align-items: center;
  margin-left: auto;
  margin-right: 40px;
`;

const CartIcon = styled(AnimatedCartIcon)`
  font-size: 1.2em;
  margin-right: -5px;
`;

const CartItemCount = styled.span`
  background-color: red;
  color: white;
  padding: 2px 5px;
  border-radius: 50%;
  margin-left: 3px;
`;

const Header = ({ cartItemCount }) => {
  const menuItemProps = useSpring({
    opacity: 1,
    from: { opacity: 0 },
  });

  const userIconProps = useSpring({
    transform: 'translateX(0)',
    from: { transform: 'translateX(-20px)' },
  });

  const cartIconProps = useSpring({
    transform: 'translateX(0)',
    from: { transform: 'translateX(20px)' },
  });

  return (
    <HeaderWrapper>
      <Logo>OpenRazor</Logo>
      <Menu>
        <AnimatedMenuItem to="/" style={menuItemProps}>
          Главная
        </AnimatedMenuItem>
        <AnimatedMenuItem to="/news" style={menuItemProps}>
          Новости
        </AnimatedMenuItem>
        <AnimatedMenuItem to="/catalog" style={menuItemProps}>
          Каталог товаров
        </AnimatedMenuItem>
        <AnimatedMenuItem to="/articles" style={menuItemProps}>
          Статьи
        </AnimatedMenuItem>
        <AnimatedMenuItem to="/contacts" style={menuItemProps}>
          Контакты
        </AnimatedMenuItem>
        <AnimatedMenuItem to="/reviews" style={menuItemProps}>
          Отзывы и комментарии
        </AnimatedMenuItem>
        <AnimatedMenuItem to="/payment" style={menuItemProps}>
          Оплата и доставка
        </AnimatedMenuItem>
      </Menu>
      <CartWrapper>
        <AnimatedMenuItem to="/profile" style={menuItemProps}>
          <UserIcon style={userIconProps} />
        </AnimatedMenuItem>
        <AnimatedMenuItem to="/cart" style={menuItemProps}>
          <CartIcon style={cartIconProps} />
          {cartItemCount > 0 && <CartItemCount>{cartItemCount}</CartItemCount>}
        </AnimatedMenuItem>
      </CartWrapper>
    </HeaderWrapper>
  );
};

export default Header;