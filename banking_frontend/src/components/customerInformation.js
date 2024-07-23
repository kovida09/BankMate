import React, { useState, useEffect } from 'react';
import { getCustomerInformation } from '../api/service';

const CustomerInformation = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    getCustomerInformation()
      .then(response => setData(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      <h1>Customer Information</h1>
      <ul>
        {data.map(item => (
          <li key={item.customer_id}>{item.name} - {item.gender}</li>
        ))}
      </ul>
    </div>
  );
};

export default CustomerInformation;
