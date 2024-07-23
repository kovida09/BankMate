import React, { useState, useEffect } from 'react';
import { getTransactionInformation } from '../api/service';

const TransactionInformation = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    getTransactionInformation()
      .then(response => setData(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      <h1>Transaction Information</h1>
      <ul>
        {data.map(item => (
          <li key={item.transaction_id}>{item.transaction_date} - {item.transaction_amount} - {item.transaction_type}</li>
        ))}
      </ul>
    </div>
  );
};

export default TransactionInformation;
