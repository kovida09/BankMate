import React, { useState, useEffect } from 'react';
import { getCreditCardInformation } from '../api/service';

const CreditCardInformation = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    getCreditCardInformation()
      .then(response => setData(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      <h1>Credit Card Information</h1>
      <ul>
        {data.map(item => (
          <li key={item.credit_card_id}>{item.credit_card_status} - {item.balance} - {item.credit_limit}</li>
        ))}
      </ul>
    </div>
  );
};

export default CreditCardInformation;
