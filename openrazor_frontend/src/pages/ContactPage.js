// ContactPage.js

import React, { useEffect, useState } from 'react';
import './ContactPage.css';

const ContactPage = () => {
  const [contacts, setContacts] = useState([]);

  useEffect(() => {
    const fetchContacts = async () => {
      try {
        const response = await fetch('/api/contacts/');
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        setContacts(data);
      } catch (error) {
        console.error('Error fetching contacts:', error);
      }
    };

    fetchContacts();
  }, []);

  if (contacts.length === 0) {
    return <div className="loading-message">Loading...</div>;
  }

  return (
    <div>
      {contacts.map(contact => (
        <div key={contact.id} className="contact-wrapper">
          <h2 className="contact-header">{contact.city} Contact Information</h2>
          <p className="contact-info">Address: {contact.address}</p>
          <p className="contact-info">Phone: {contact.phone}</p>
          <p className="contact-info">Email: {contact.email}</p>
          <p className="contact-info">Working Hours: {contact.working_hours}</p>
        </div>
      ))}
    </div>
  );
};

export default ContactPage;