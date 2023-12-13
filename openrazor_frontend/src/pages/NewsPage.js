import React, { useState, useEffect } from 'react';
import './NewsPage.css';

const NewsPage = () => {
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
    <div className="news-block">
      <h2>Latest News</h2>
      {news.map((item) => (
        <div key={item.id} className="news-item">
          <h3>{item.title}</h3>
          {item.image && <img src={item.image} alt={item.title} />}
          <p>{item.content}</p>
          <p>
            <strong>Tags:</strong> {item.tags}
          </p>
          <p>
            <strong>Created At:</strong>{' '}
            <span className="created-at">{new Date(item.created_at).toLocaleString()}</span>
          </p>
        </div>
      ))}
    </div>
  );
};

export default NewsPage;