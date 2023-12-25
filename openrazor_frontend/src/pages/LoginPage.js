// LoginPage.js

import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './LoginPage.css';

const LoginPage = () => {
  const navigate = useNavigate();

  const [loginData, setLoginData] = useState({
    username: '',
    password: '',
  });

  const [registerData, setRegisterData] = useState({
    username: '',
    password: '',
    confirmPassword: '',
  });

  const handleChange = (e, formType) => {
    const formData = formType === 'login' ? loginData : registerData;
    const setFormData = formType === 'login' ? setLoginData : setRegisterData;

    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch('/api/token/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(loginData),
      });

      if (!response.ok) {
        throw new Error(`Login failed: ${response.statusText}`);
      }

      const data = await response.json();
      console.log('Login response:', data);

      // Дополнительная логика после успешного входа

      // Перенаправление на другую страницу (например, домашнюю страницу)
      navigate('/');
    } catch (error) {
      console.error('Login error:', error.message);
      // Обработка ошибок
    }
  };

  const handleRegister = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch('/api/profiles/register/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(registerData),
      });

      if (!response.ok) {
        throw new Error(`Registration failed: ${response.statusText}`);
      }

      const data = await response.json();
      console.log('Register response:', data);

      // Дополнительная логика после успешной регистрации

      // Перенаправление на другую страницу (например, страницу входа)
      navigate('/login');
    } catch (error) {
      console.error('Register error:', error.message);
      // Обработка ошибок
    }
  };

  return (
    <div className="login-container">
      <h2>Login Page</h2>
      <form onSubmit={handleLogin} className="login-form">
        <div className="form-group">
          <label htmlFor="loginUsername">Username:</label>
          <input
            type="text"
            id="loginUsername"
            name="username"
            value={loginData.username}
            onChange={(e) => handleChange(e, 'login')}
            className="input"
          />
        </div>
        <div className="form-group">
          <label htmlFor="loginPassword">Password:</label>
          <input
            type="password"
            id="loginPassword"
            name="password"
            value={loginData.password}
            onChange={(e) => handleChange(e, 'login')}
            className="input"
          />
        </div>
        <button type="submit" className="button">Login</button>
      </form>

      <div className="register-link">
        <Link to="/registration" className="link">Register</Link>
      </div>

      <div className="forgot-password-link">
        <Link to="/forgot-password" className="link">Forgot Password</Link>
      </div>

      <form onSubmit={handleRegister} className="register-form">
        <div className="form-group">
          <label htmlFor="registerUsername">Username:</label>
          <input
            type="text"
            id="registerUsername"
            name="username"
            value={registerData.username}
            onChange={(e) => handleChange(e, 'register')}
            className="input"
          />
        </div>
        <div className="form-group">
          <label htmlFor="registerPassword">Password:</label>
          <input
            type="password"
            id="registerPassword"
            name="password"
            value={registerData.password}
            onChange={(e) => handleChange(e, 'register')}
            className="input"
          />
        </div>
        <div className="form-group">
          <label htmlFor="confirmPassword">Confirm Password:</label>
          <input
            type="password"
            id="confirmPassword"
            name="confirmPassword"
            value={registerData.confirmPassword}
            onChange={(e) => handleChange(e, 'register')}
            className="input"
          />
        </div>
        <button type="submit" className="button">Register</button>
      </form>
    </div>
  );
};

export default LoginPage;