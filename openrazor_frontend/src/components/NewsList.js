
// NewsList.js
import React, { useState, useEffect } from 'react';
import './NewsList.css'; // Подключаем файл стилей

const NewsList = () => {
  const [news, setNews] = useState([]);

  useEffect(() => {
    const fetchNews = async () => {
      try {
        const response = await fetch('/api/news/');
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const newsData = await response.json();
        setNews(newsData);
      } catch (error) {
        console.error('Error fetching news:', error);
      }
    };

    fetchNews();
  }, []);

  return (
    <div className="NewsListWrapper">
      <h2>Новости</h2>
      {news.length > 0 && (
        <div className="news-item">
          <div className="carousel-wrapper">
            <div className="carousel-content">
              {news.map((item) => (
                <div key={item.id} className="carousel-item">
                  <h3>{item.title}</h3>
                  {item.image && <img src={item.image} alt={item.title} />}
                  <p>{item.content}</p>
                  <p>
                    <strong>Tags:</strong> {item.tags}
                  </p>
                  <p>
                    <strong>Created At:</strong> {new Date(item.created_at).toLocaleString()}
                  </p>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default NewsList;