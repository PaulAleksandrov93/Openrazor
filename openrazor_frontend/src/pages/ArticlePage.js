
import React, { useState, useEffect } from 'react';
import './ArticlePage.css';

const ArticlePage = () => {
  const [articles, setArticles] = useState([]);

  useEffect(() => {
    const fetchArticles = async () => {
      try {
        const response = await fetch('/api/articles/');
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const articlesData = await response.json();
        setArticles(articlesData);
      } catch (error) {
        console.error('Error fetching articles:', error);
      }
    };

    fetchArticles();
  }, []);

  return (
    <div className="ArticlePageWrapper">
      <h2>Latest Articles</h2>
      {articles.map((item) => (
        <div key={item.id} className="article-item">
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

export default ArticlePage;