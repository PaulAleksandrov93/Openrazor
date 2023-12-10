// NewsList.js
import React, { useState, useEffect } from 'react';
import styled from 'styled-components';

const NewsListWrapper = styled.div`
  h2 {
    margin-top: 0;
  }

  .news-item {
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;

    img {
      max-width: 100%;
      height: auto;
    }
  }
`;

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
    <NewsListWrapper>
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
            <strong>Created At:</strong> {new Date(item.created_at).toLocaleString()}
          </p>
        </div>
      ))}
    </NewsListWrapper>
  );
};

export default NewsList;