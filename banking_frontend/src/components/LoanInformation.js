import React, { useState, useEffect } from 'react';
import { getLoanInformation } from '../api/service';

const LoanInformation = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    getLoanInformation()
      .then(response => setData(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      <h1>Loan Information</h1>
      <ul>
        {data.map(item => (
          <li key={item.loan_id}>{item.loan_type} - {item.loan_amount} - {item.loan_status}</li>
        ))}
      </ul>
    </div>
  );
};

export default LoanInformation;
