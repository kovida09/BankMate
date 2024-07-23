import React, { useState, useEffect } from 'react';
import { getAccountInformation } from '../api/service';

const AccountInformation = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    getAccountInformation()
      .then(response => setData(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      <h1>Account Information</h1>
      <ul>
        {data.map(item => (
          <li key={item.id}>{item.account_number} - {item.account_type}</li>
        ))}
      </ul>
    </div>
  );
};

export default AccountInformation;
